#!/bin/sh

set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
source_launcher="$repo_root/macos/ERA SOFT.command"
desktop_dir=${ERA_DESKTOP_DIR:-"$HOME/Desktop"}
desktop_launcher="$desktop_dir/ERA SOFT.command"

if [ -e "$desktop_launcher" ] || [ -L "$desktop_launcher" ]; then
	echo "Launcher already exists: $desktop_launcher" >&2
	exit 1
fi

if [ ! -d "$desktop_dir" ]; then
	echo "Desktop directory does not exist: $desktop_dir" >&2
	exit 1
fi

ln -s "$source_launcher" "$desktop_launcher"
echo "Installed ERA SOFT launcher: $desktop_launcher"
