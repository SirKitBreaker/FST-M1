#!/usr/bin/env python3
"""Scan a repo for missing activity files based on README activity checklist.

Usage: python scan_missing_activities.py [repo_path] [output_csv]

If no repo_path is provided, the current working directory is used.
"""
import argparse
import csv
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

def get_git_email(repo_path: Path) -> str:
    # local, then global, then last commit
    def run(cmd):
        try:
            return subprocess.check_output(cmd, cwd=repo_path, shell=True, text=True).strip()
        except Exception:
            return ""

    local = run("git config --local user.email")
    if local:
        return local
    global_e = run("git config --global user.email")
    if global_e:
        return global_e
    last = run("git log -1 --pretty=format:'%ae'")
    return last or ""


def parse_readme(readme_path: Path):
    text = readme_path.read_text(encoding="utf-8")
    sections = []  # list of (title, expected_count)

    # find headings like ### Java
    heading_iter = list(re.finditer(r"^###\s+(.*)$", text, flags=re.MULTILINE))
    for m in heading_iter:
        title = m.group(1).strip()
        start = m.end()
        # find the next markdown table after this heading (header + separator + data rows)
        table_match = re.search(r"\n(\|[^\n]*\n\|\s*-+[^\n]*\n(?:\|[^\n]*\n)*)", text[start:])
        if not table_match:
            continue
        table = table_match.group(1)
        # split lines, ignore header and separator
        lines = [ln.strip() for ln in table.strip().splitlines() if ln.strip()]
        if len(lines) < 3:
            expected = 0
        else:
            # data rows are lines after the separator (first two lines are header + separator)
            data_rows = lines[2:]
            expected = len(data_rows)
        sections.append((title, expected))
    return sections


def candidate_paths_for_title(title: str) -> list:
    # common mappings
    title_norm = title.lower()
    candidates = []
    if "project" in title_norm:
        base = title.split()[0]
        candidates.append(f"{base}/Project")
        candidates.append(f"{base}/project")
    else:
        candidates.append(f"{title}/Activities")
        candidates.append(f"{title}/activities")
        candidates.append(f"{title}/Project")
        candidates.append(f"{title}/project")

    # special cases
    special = {
        "api testing (readyapi)": ["API/Activities", "API/Project"],
        "api testing project": ["API/Project"],
        "api testing": ["API/Activities"],
        "selenium project": ["Selenium/Project"],
        "selenium": ["Selenium/Activities"],
        "restassured": ["RestAssured/Activities"],
        "restassured project": ["RestAssured/Project"],
        "appium": ["Appium/Activities"],
        "appium project": ["Appium/Project"],
        "git": ["Git/Activities"],
        "selenium project": ["Selenium/Project"],
        "api testing (readyapi)": ["API/Activities"],
        "api testing project": ["API/Project"],
        "api testing (readyapi)": ["API/Activities"],
    }
    if title_norm in special:
        candidates = special[title_norm] + candidates

    # also try simple folder equal to title
    candidates.append(title)

    return candidates


def count_existing_files(repo_path: Path, candidates: list) -> int:
    for cand in candidates:
        p = repo_path / cand
        if p.exists() and p.is_dir():
            # count user files excluding .gitkeep and hidden
            valid_files = []
            for f in p.iterdir():
                if not f.is_file():
                    continue
                if f.name.startswith('.') or f.name == '.gitkeep':
                    continue
                try:
                    # treat zero-byte files as empty
                    if f.stat().st_size == 0:
                        continue
                    # treat files with only whitespace as empty
                    content = f.read_text(encoding='utf-8', errors='ignore').strip()
                    if not content:
                        continue
                except Exception:
                    # if we can't read the file, count it only if size > 0
                    try:
                        if f.stat().st_size == 0:
                            continue
                    except Exception:
                        # conservative: count file
                        pass
                valid_files.append(f)
            return len(valid_files)
    return 0


def write_csv(output_path: Path, email: str, results: dict):
    # header: email, then sections
    headers = ["email"] + list(results.keys())
    with output_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(headers)
        row = [email] + [str(results[k]) for k in results.keys()]
        writer.writerow(row)


def is_git_url(s: str) -> bool:
    s = s.strip()
    return s.startswith("git@") or s.startswith("http://") or s.startswith("https://") or s.endswith('.git') or 'github.com' in s


def sanitize_repo_name(repo_identifier: str) -> str:
    # return a short name for naming outputs
    # try to parse owner/repo from URL
    repo_identifier = repo_identifier.rstrip('/')
    if repo_identifier.endswith('.git'):
        repo_identifier = repo_identifier[:-4]
    parts = repo_identifier.replace('\\', '/').split('/')
    if len(parts) >= 2 and (parts[-2] and parts[-1]):
        return f"{parts[-2]}_{parts[-1]}"
    return parts[-1]


def scan_one(repo_identifier: str, out_path: Path):
    # repo_identifier can be a local path or a git URL
    use_tmp = False
    workdir = None
    if Path(repo_identifier).exists():
        workdir = Path(repo_identifier)
    elif is_git_url(repo_identifier):
        tmp = Path(tempfile.mkdtemp(prefix='scanrepo_'))
        try:
            subprocess.check_call(f"git clone --depth 1 {repo_identifier} {tmp}", shell=True)
        except subprocess.CalledProcessError:
            shutil.rmtree(tmp, ignore_errors=True)
            print(f"Failed to clone {repo_identifier}")
            return 1
        use_tmp = True
        workdir = tmp
    else:
        print(f"Repo path not found and not a recognized git URL: {repo_identifier}")
        return 2

    try:
        readme = workdir / "README.md"
        if not readme.exists():
            print(f"README.md not found in {repo_identifier}")
            return 3

        email = get_git_email(workdir)
        sections = parse_readme(readme)
        results = {}
        for title, expected in sections:
            candidates = candidate_paths_for_title(title)
            existing = count_existing_files(workdir, candidates)
            missing = max(0, expected - existing)
            col = title.replace(" ", "_").replace("(", "").replace(")", "")
            results[col] = missing

        if out_path:
            write_csv(out_path, email, results)
            print(f"Wrote {out_path} (owner_email={email})")
            return 0
        # if no out_path provided, return results for aggregation
        return (email, results)
    finally:
        if use_tmp and workdir and workdir.exists():
            shutil.rmtree(workdir, ignore_errors=True)


def main(argv=None):
    p = argparse.ArgumentParser(description="Scan one or more repos for missing activity files based on README checklist")
    p.add_argument('repos', nargs='*', help='Local repo paths or git URLs to scan')
    p.add_argument('-l', '--list-file', help='Text file with one repo URL/path per line')
    p.add_argument('-o', '--output-dir', help='Directory to write per-repo CSV outputs (default: current directory)')
    p.add_argument('--single-output', help='If set, write a single CSV for the first repo (keeps legacy behavior)')
    p.add_argument('--aggregate', help='Write a single aggregated CSV with results for all repos')
    args = p.parse_args(argv[1:] if argv else None)

    repo_list = []
    if args.list_file:
        lf = Path(args.list_file)
        if not lf.exists():
            print(f"List file not found: {lf}")
            return 2
        for ln in lf.read_text(encoding='utf-8').splitlines():
            ln = ln.strip()
            if not ln or ln.startswith('#'):
                continue
            repo_list.append(ln)

    if args.repos:
        repo_list.extend(args.repos)

    if not repo_list:
        # default to current repo (legacy)
        repo_list = [str(Path.cwd())]

    out_dir = Path(args.output_dir) if args.output_dir else Path.cwd()
    out_dir.mkdir(parents=True, exist_ok=True)

    # If user provided --single-output and only one repo, behave like before
    if args.single_output and len(repo_list) >= 1:
        repo = repo_list[0]
        out_path = Path(args.single_output)
        return scan_one(repo, out_path)

    # Aggregate mode: collect results and write a single consolidated CSV
    if args.aggregate:
        aggregated = []
        all_cols = set()
        for repo in repo_list:
            name = sanitize_repo_name(repo)
            ret = scan_one(repo, None)
            if isinstance(ret, int):
                print(f"Scan failed for {repo} (code={ret})")
                continue
            email, results = ret
            aggregated.append({"repo": name, "email": email, "results": results})
            all_cols.update(results.keys())

        cols = sorted(all_cols)
        agg_out = Path(args.aggregate)
        with agg_out.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.writer(fh)
            header = ["repo", "email"] + cols
            writer.writerow(header)
            for item in aggregated:
                row = [item["repo"], item["email"]]
                res = item["results"]
                for c in cols:
                    # empty string when section not present, else missing count
                    row.append(str(res.get(c, "")))
                writer.writerow(row)
        print(f"Wrote aggregated CSV: {agg_out}")
        return 0

    # Default: per-repo CSV outputs
    exit_codes = []
    for repo in repo_list:
        name = sanitize_repo_name(repo)
        out_name = out_dir / f"missing_activities_{name}.csv"
        code = scan_one(repo, out_name)
        exit_codes.append(code)

    # return non-zero if any failed
    return 0 if all(c == 0 for c in exit_codes) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
