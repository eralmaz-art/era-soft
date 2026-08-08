#!/bin/sh

set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
workspace_root=$(dirname "$repo_root")
toolchain_root=${ERA_TOOLCHAIN_ROOT:-"$workspace_root/toolchain"}
bench_root=${ERA_BENCH_ROOT:-"$workspace_root/frappe-bench"}
runtime_root=${ERA_RUNTIME_ROOT:-"$workspace_root/runtime"}
site_name=${ERA_SITE_NAME:-"era.localhost"}
web_port=${ERA_WEB_PORT:-8003}
db_port=${ERA_DB_PORT:-3307}
db_root_password=${ERA_DB_ROOT_PASSWORD:-admin}

export PATH="$toolchain_root/redis/bin:$toolchain_root/bin:$toolchain_root/node/node_modules/.bin:$PATH"
export ERA_MARIADB_CONNECTOR_PREFIX="$toolchain_root/bottles/mariadb-connector-c"

mariadb_pid=/private/tmp/era-mariadb.pid
mariadb_socket=/private/tmp/era-mariadb.sock
web_pid="$bench_root/config/pids/era_web.pid"

is_running() {
	[ -f "$1" ] && kill -0 "$(sed -n '1p' "$1")" 2>/dev/null
}

mariadb_running() {
	mariadb --no-defaults \
		--host=127.0.0.1 \
		--port="$db_port" \
		--user=root \
		--password="$db_root_password" \
		--execute='SELECT 1' >/dev/null 2>&1
}

redis_running() {
	redis-cli -p "$1" ping 2>/dev/null | grep -q '^PONG$'
}

web_running() {
	command -v curl >/dev/null 2>&1 &&
		curl -fsS -H "Host: $site_name" \
			"http://127.0.0.1:$web_port/api/method/ping" >/dev/null 2>&1
}

web_process_running() {
	if command -v lsof >/dev/null 2>&1; then
		lsof -tiTCP:"$web_port" -sTCP:LISTEN >/dev/null 2>&1
	else
		is_running "$web_pid"
	fi
}

wait_until_running() {
	label=$1
	shift
	attempt=0
	while [ "$attempt" -lt 30 ]; do
		if "$@"; then
			return 0
		fi
		attempt=$((attempt + 1))
		sleep 1
	done
	echo "$label did not become ready within 30 seconds" >&2
	return 1
}

wait_until_stopped() {
	label=$1
	shift
	attempt=0
	while [ "$attempt" -lt 30 ]; do
		if ! "$@"; then
			return 0
		fi
		attempt=$((attempt + 1))
		sleep 1
	done
	echo "$label did not stop within 30 seconds" >&2
	return 1
}

stop_web_process() {
	if ! web_process_running; then
		echo "web server is not running"
		return 0
	fi

	if command -v lsof >/dev/null 2>&1; then
		for process_id in $(lsof -tiTCP:"$web_port" -sTCP:LISTEN); do
			kill "$process_id"
		done
	elif is_running "$web_pid"; then
		kill "$(sed -n '1p' "$web_pid")"
	fi
	wait_until_stopped "web server" web_process_running
	echo "Stopped web server"
}

require_file() {
	if [ ! -e "$1" ]; then
		echo "Missing required local runtime file: $1" >&2
		exit 1
	fi
}

start_stack() {
	require_file "$toolchain_root/bottles/mariadb@11.8/bin/mariadbd"
	require_file "$toolchain_root/redis/bin/redis-server"
	require_file "$bench_root/sites/$site_name/site_config.json"
	mkdir -p "$bench_root/config/pids" "$runtime_root/mariadb-run"

	if ! mariadb_running; then
		nohup "$toolchain_root/bottles/mariadb@11.8/bin/mariadbd" \
			--no-defaults \
			--basedir="$toolchain_root/bottles/mariadb@11.8" \
			--datadir="$runtime_root/mariadb-data" \
			--plugin-dir="$toolchain_root/bottles/mariadb@11.8/lib/plugin" \
			--socket="$mariadb_socket" \
			--pid-file="$mariadb_pid" \
			--log-error="$runtime_root/mariadb-run/mariadb.log" \
			--port="$db_port" \
			--bind-address=127.0.0.1 \
			--skip-name-resolve \
			--character-set-server=utf8mb4 \
			--collation-server=utf8mb4_unicode_ci >/dev/null 2>&1 &
	fi
	wait_until_running "MariaDB" mariadb_running

	if ! redis_running 13003; then
		(cd "$bench_root" && redis-server config/redis_cache.conf --daemonize yes)
	fi
	if ! redis_running 11003; then
		(cd "$bench_root" && redis-server config/redis_queue.conf --daemonize yes)
	fi
	wait_until_running "Redis cache" redis_running 13003
	wait_until_running "Redis queue" redis_running 11003

	if web_process_running && ! web_running; then
		stop_web_process
	fi
	if ! web_process_running; then
		(cd "$bench_root" && nohup bench serve --port "$web_port" --noreload > logs/era-web.log 2>&1 & echo $! > "$web_pid")
	fi
	wait_until_running "Frappe web" web_running

	echo "ERA SOFT local stack started: http://$site_name:$web_port"
}

stop_process() {
	pid_file=$1
	label=$2
	if is_running "$pid_file"; then
		kill "$(sed -n '1p' "$pid_file")"
		echo "Stopped $label"
	else
		echo "$label is not running"
	fi
}

stop_stack() {
	stop_web_process
	if redis_running 11003; then
		redis-cli -p 11003 shutdown
		wait_until_stopped "Redis queue" redis_running 11003
		echo "Stopped Redis queue"
	else
		echo "Redis queue is not running"
	fi
	if redis_running 13003; then
		redis-cli -p 13003 shutdown
		wait_until_stopped "Redis cache" redis_running 13003
		echo "Stopped Redis cache"
	else
		echo "Redis cache is not running"
	fi
	if mariadb_running; then
		mariadb --no-defaults \
			--host=127.0.0.1 \
			--port="$db_port" \
			--user=root \
			--password="$db_root_password" \
			--execute=SHUTDOWN >/dev/null 2>&1
		wait_until_stopped "MariaDB" mariadb_running
		echo "Stopped MariaDB"
	else
		echo "MariaDB is not running"
	fi
}

status_stack() {
	if mariadb_running; then echo "[running] MariaDB 11.8"; else echo "[stopped] MariaDB 11.8"; fi
	if redis_running 13003; then echo "[running] Redis cache"; else echo "[stopped] Redis cache"; fi
	if redis_running 11003; then echo "[running] Redis queue"; else echo "[stopped] Redis queue"; fi
	if web_running; then echo "[running] Frappe web"; else echo "[stopped] Frappe web"; fi
}

case "${1:-status}" in
	start) start_stack ;;
	stop) stop_stack ;;
	restart)
		stop_stack
		start_stack
		;;
	status) status_stack ;;
	*)
		echo "Usage: $0 {start|stop|restart|status}" >&2
		exit 2
		;;
esac
