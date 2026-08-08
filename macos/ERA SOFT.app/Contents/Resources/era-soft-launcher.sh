#!/bin/sh

set -u

launcher_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_root=$(CDPATH= cd -- "$launcher_dir/../../../.." && pwd)
stack_script="$repo_root/scripts/local_stack.sh"
era_url=${ERA_URL:-http://era.localhost:8003}
log_dir="$HOME/Library/Logs"
log_file="$log_dir/ERA SOFT Launcher.log"

mkdir -p "$log_dir"

{
	printf '\n[%s] Starting ERA SOFT\n' "$(date '+%Y-%m-%d %H:%M:%S')"

	if [ ! -x "$stack_script" ]; then
		printf 'Launcher cannot find %s\n' "$stack_script"
		osascript -e 'display alert "ERA SOFT не найдена" message "Не найден сценарий запуска. Проверьте папку проекта ERA SOFT." as critical'
		exit 1
	fi

	if ! "$stack_script" start; then
		printf 'ERA SOFT stack failed to start.\n'
		osascript -e 'display alert "ERA SOFT не запустилась" message "Диагностика сохранена в ~/Library/Logs/ERA SOFT Launcher.log" as critical'
		exit 1
	fi

	chrome_executable="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
	if [ -x "$chrome_executable" ]; then
		nohup "$chrome_executable" --app="$era_url" >/dev/null 2>&1 &
		printf 'Opened %s as an ERA SOFT application window\n' "$era_url"
		exit 0
	fi

	if open "$era_url"; then
		printf 'Opened %s in the default browser\n' "$era_url"
		exit 0
	fi

	printf 'Could not open %s\n' "$era_url"
	osascript -e 'display alert "ERA SOFT работает" message "Откройте http://era.localhost:8003 в браузере."'
	exit 1
} >>"$log_file" 2>&1
