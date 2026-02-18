#!/usr/bin/env bash
set -euo pipefail

echo "Building single-file executable with pyinstaller..."
if ! command -v pyinstaller >/dev/null 2>&1; then
  echo "pyinstaller not found. Install with: pip install pyinstaller"
  exit 1
fi

# Example: create a one-file executable (may require tuning on Windows/macOS)
pyinstaller --onefile --name space-invaders -c -F -n space-invaders -i '' -y \
  --add-data "invaders/assets:invaders/assets" \
  -p . -m invaders

echo "Done. Check the dist/ directory for the executable."
