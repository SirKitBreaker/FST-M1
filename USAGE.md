Usage: Scanner and Wrapper Scripts
===============================

Overview
--------
This repository includes tools to scan repositories for missing activity files based on the README activity checklist.

Files provided
- `scan_missing_activities.py` — Python scanner. Scans a repository (local path or git URL) and writes CSV(s) showing missing activity files per README sections.
- `run_remote_scan.sh` — POSIX shell wrapper to shallow-clone a repo, run the scanner, and clean up.
- `run_remote_scan.bat` — Windows batch wrapper equivalent.

Prerequisites
- `git` installed and on PATH
- `python3` (3.8+) installed and on PATH
- For remote private repos: appropriate SSH keys or credentials configured for `git clone` (or use HTTPS with credentials)

Quick examples
--------------

Scan current local repo (legacy behavior):
```
python3 scan_missing_activities.py
```

Scan a specific local repo path and write a single CSV output:
```
python3 scan_missing_activities.py /path/to/repo --single-output /tmp/out.csv
```

Scan multiple repos (local or git URLs) and produce per-repo CSVs in an output directory:
```
python3 scan_missing_activities.py git@github.com:owner/repo1.git /path/to/local/repo2 -o /tmp/results
```

Scan from a text file with one repo per line and produce an aggregated CSV:
```
python3 scan_missing_activities.py -l repos.txt --aggregate /tmp/agg.csv
```

`repos.txt` example:
```
# comment lines start with #
git@github.com:owner/repo1.git
https://github.com/owner/repo2
/home/user/local-repo
```

Wrapper usage
-------------
The wrappers are convenience scripts that shallow-clone remote repos and run the scanner.

POSIX (Linux / macOS):
```
./run_remote_scan.sh git@github.com:owner/repo.git /tmp/out.csv
```

You can also forward scanner flags directly to the Python script (no clone):
```
./run_remote_scan.sh -l repos.txt --aggregate /tmp/agg.csv
```

Windows (CMD/PowerShell):
```
run_remote_scan.bat https://github.com/owner/repo.git C:\tmp\out.csv
```
Or forward flags:
```
run_remote_scan.bat -l repos.txt --aggregate C:\tmp\agg.csv
```

Behavior notes
--------------
- The Python scanner parses `README.md` headings (###) and the table rows that follow to determine the expected number of activities per section.
- When counting existing activity files the scanner:
  - ignores `.gitkeep` and hidden files
  - treats zero-byte files or files that contain only whitespace as "missing"
- For git URLs the script performs a shallow clone (`git clone --depth 1`) into a temporary directory and removes it after scanning.
- The `--aggregate` option writes one consolidated CSV where columns are `repo,email,<section columns...>`.

CSV outputs
-----------
- Per-repo CSVs: default filename `missing_activities_<owner>_<repo>.csv` (or user-specified with `--single-output`).
- Aggregated CSV: user-specified path via `--aggregate`.

Security and credentials
------------------------
- For private repositories ensure `git clone` works from the machine running the script (SSH keys or HTTPS credentials). The script does not store credentials.
- If you run scanning across many repos, run from a secure environment and monitor rate limits if using GitHub API alternatives.

Troubleshooting
---------------
- "README.md not found" — ensure the target repo root has a README.md in Markdown format.
- Clone failures — verify repo URL and access rights (SSH keys, token).
- Python errors — ensure `python3` is available and you are using a supported version.