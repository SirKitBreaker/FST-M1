#!/usr/bin/env bash
set -euo pipefail
# run_remote_scan.sh - clone a remote repo shallowly, run the scanner, copy CSV out, and clean up
# Usage: ./run_remote_scan.sh <git-repo-url> [output_csv]

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <git-repo-url> [output_csv]"
  exit 2
fi


REPO_URL="$1"

# If first arg is an option (starts with -) or is an existing file, forward all args to the scanner
if [[ "$REPO_URL" == -* || -f "$REPO_URL" ]]; then
  SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  SCANNER="$SCRIPT_DIR/scan_missing_activities.py"
  if [ ! -f "$SCANNER" ]; then
    echo "Scanner not found at $SCANNER"
    exit 3
  fi
  python3 "$SCANNER" "$@"
  exit $?
fi

OUT="${2:-./missing_activities_$(basename "$REPO_URL" .git).csv}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCANNER="$SCRIPT_DIR/scan_missing_activities.py"

if [ ! -f "$SCANNER" ]; then
  echo "Scanner not found at $SCANNER"
  exit 3
fi

command -v git >/dev/null 2>&1 || { echo "git not installed"; exit 3; }
command -v python3 >/dev/null 2>&1 || { echo "python3 not installed"; exit 3; }

TMP_DIR="$(mktemp -d)"
cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

echo "Cloning $REPO_URL (shallow) into $TMP_DIR..."
git clone --depth 1 "$REPO_URL" "$TMP_DIR"

echo "Running scanner..."
python3 "$SCANNER" --single-output "$OUT" "$TMP_DIR"

echo "Result written to: $OUT"
exit 0
