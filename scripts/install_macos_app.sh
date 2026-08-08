#!/bin/sh

set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
source_app="$repo_root/macos/ERA SOFT.app"
desktop_dir=${ERA_DESKTOP_DIR:-"$HOME/Desktop"}
desktop_app="$desktop_dir/ERA SOFT.app"

if [ ! -d "$source_app" ]; then
	echo "ERA SOFT application bundle does not exist: $source_app" >&2
	exit 1
fi

if [ ! -d "$desktop_dir" ]; then
	echo "Desktop directory does not exist: $desktop_dir" >&2
	exit 1
fi

if [ -e "$desktop_app" ] || [ -L "$desktop_app" ]; then
	echo "ERA SOFT is already installed: $desktop_app"
	exit 0
fi

ln -s "$source_app" "$desktop_app"
echo "Installed ERA SOFT application: $desktop_app"
