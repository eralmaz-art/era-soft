#!/bin/sh

set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
source_file="$repo_root/macos/era-soft-launcher.c"
app_bundle="$repo_root/macos/ERA SOFT.app"
executable="$app_bundle/Contents/MacOS/era-soft-launcher"
launcher_script="$app_bundle/Contents/Resources/era-soft-launcher.sh"

clang -Wall -Wextra -Werror -O2 "$source_file" -o "$executable"
chmod +x "$executable" "$launcher_script"
touch "$app_bundle"

echo "Built ERA SOFT macOS application: $app_bundle"
