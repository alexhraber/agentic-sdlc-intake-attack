#!/usr/bin/env bash
set -euo pipefail

# WARNING: Static inspection only. This script extracts printable strings and never
# executes, imports, builds, chmods, or runs the supplied file.

if [ "$#" -lt 1 ] || [ "$#" -gt 2 ]; then
  echo "usage: $0 <file> [min-length]" >&2
  exit 2
fi

path="$1"
min_length="${2:-8}"

if [ ! -f "$path" ]; then
  echo "not a regular file: $path" >&2
  exit 1
fi

if ! command -v strings >/dev/null 2>&1; then
  echo "strings command not available" >&2
  exit 1
fi

strings -a -n "$min_length" "$path"
