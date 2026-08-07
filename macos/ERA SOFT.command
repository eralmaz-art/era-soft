#!/bin/sh

set -eu

launcher_path=$0
while [ -L "$launcher_path" ]; do
	launcher_dir=$(CDPATH= cd -- "$(dirname -- "$launcher_path")" && pwd)
	launcher_target=$(readlink "$launcher_path")
	case "$launcher_target" in
		/*) launcher_path=$launcher_target ;;
		*) launcher_path="$launcher_dir/$launcher_target" ;;
	esac
done

launcher_dir=$(CDPATH= cd -- "$(dirname -- "$launcher_path")" && pwd)
repo_root=$(dirname "$launcher_dir")
stack_script="$repo_root/scripts/local_stack.sh"
era_url=${ERA_URL:-http://era.localhost:8003}

if ! "$stack_script" start; then
	osascript -e 'display alert "ERA SOFT could not start" message "Open Terminal and run scripts/local_stack.sh start to see diagnostic output." as critical'
	exit 1
fi

if open "$era_url" 2>/dev/null; then
	exit 0
fi

# Some macOS profiles have no default HTTP handler. Prefer Chrome when it is
# installed, while keeping the normal default-browser behavior first.
if [ -d "/Applications/Google Chrome.app" ] && \
	open -a "/Applications/Google Chrome.app" "$era_url" 2>/dev/null; then
	exit 0
fi

osascript -e "display alert \"ERA SOFT is running\" message \"Open $era_url in a browser.\""
exit 1
