#!/usr/bin/env bash
set -euo pipefail

# WARNING: Static inspection only. This script lists archive metadata and never extracts
# or executes contained files.

if [ "$#" -ne 1 ]; then
  echo "usage: $0 <archive>" >&2
  exit 2
fi

archive="$1"

if [ ! -f "$archive" ]; then
  echo "not a regular file: $archive" >&2
  exit 1
fi

echo "== file type =="
if command -v file >/dev/null 2>&1; then
  file "$archive"
else
  echo "file command not available"
fi

echo "== archive listing =="
if command -v zipinfo >/dev/null 2>&1; then
  zipinfo "$archive"
elif command -v unzip >/dev/null 2>&1; then
  unzip -l "$archive"
elif command -v 7z >/dev/null 2>&1; then
  7z l "$archive"
else
  echo "no supported archive listing tool found: install zipinfo, unzip, or 7z" >&2
  exit 1
fi
