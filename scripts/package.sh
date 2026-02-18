#!/usr/bin/env bash
set -euo pipefail

echo "Building single-file executable with pyinstaller..."
if ! command -v pyinstaller >/dev/null 2>&1; then
  echo "pyinstaller not found. Install with: pip install pyinstaller"
  exit 1
fi

# Example: create a one-file executable (may require tuning on Windows/macOS)
# Add data from invaders/assets into the packaged executable. On Windows the
# --add-data syntax is different; this script assumes Linux/macOS style.
pyinstaller --onefile --name space-invaders \
  --add-data "invaders/assets:invaders/assets" \
  invaders/__main__.py

echo "Done. Check the dist/ directory for the executable."
