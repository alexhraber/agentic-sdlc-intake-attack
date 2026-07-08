#!/usr/bin/env bash
set -euo pipefail

# WARNING: Static inspection only. This script hashes files and never executes them.
# Do not use it as approval to open, extract, import, build, chmod, or run artifacts.

if [ "$#" -lt 1 ]; then
  echo "usage: $0 <file> [file ...]" >&2
  exit 2
fi

for path in "$@"; do
  if [ ! -f "$path" ]; then
    echo "not a regular file: $path" >&2
    exit 1
  fi
  echo "== $path =="
  sha256sum "$path"
  if command -v md5sum >/dev/null 2>&1; then
    md5sum "$path"
  fi
  if command -v file >/dev/null 2>&1; then
    file "$path"
  fi
done
