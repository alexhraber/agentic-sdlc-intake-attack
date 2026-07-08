#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

secret_pattern='sk-''ant-|nv''api-|gh''o_|gh''p_|github_''pat_|BEGIN OPENSSH PRIVATE ''KEY|BEGIN PGP PRIVATE ''KEY|refresh''Token|access''Token|SECRET_ACCESS_''KEY|PRIVATE ''KEY|seed ''phrase|mnemo''nic|xox''b-|xox''p-|aws_secret_access_''key'
secret_hits="$(
  grep -RInE "$secret_pattern" . \
    --exclude-dir=.git \
    --exclude-dir=.venv \
    --exclude='check-public-safety.sh' \
    --exclude='build-public-notebooks.py' \
    --exclude='sanitize-notebooks.py' \
    --exclude='*.ipynb' \
    || true
)"
if [[ -n "$secret_hits" ]]; then
  echo "Unexpected secret-pattern hits:"
  printf '%s\n' "$secret_hits"
  exit 1
fi

danger_pattern='e''val\(|new Func''tion|child_''process|ex''ec\(|sp''awn\(|/home/''arx'
danger_hits="$(
  grep -RInE "$danger_pattern" scripts tools analysis fixtures \
    --exclude='*.md' \
    --exclude='*.html' \
    --exclude='check-public-safety.sh' \
    --exclude='build-public-notebooks.py' \
    || true
)"
if [[ -n "$danger_hits" ]]; then
  echo "Unexpected executable-code safety hits:"
  printf '%s\n' "$danger_hits"
  exit 1
fi

python3 scripts/sanitize-notebooks.py notebooks
echo "Public safety checks passed."
