#!/usr/bin/env sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
CHROMIUM=${CHROMIUM:-chromium}
"$CHROMIUM" --headless --no-sandbox --disable-dev-shm-usage --hide-scrollbars \
  --force-device-scale-factor=1 --window-size=1200,630 \
  --screenshot="$ROOT/site/assets/og-card.png" \
  "file://$ROOT/scripts/social-card.html"
