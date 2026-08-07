# Local Development

## Supported baseline

ERA SOFT targets Frappe and ERPNext `version-16`. Do not develop against
`develop`; it is the bleeding-edge upstream branch. The v16 toolchain currently
requires Python 3.14, Node.js 24, Yarn, Redis/Valkey, MariaDB 11.8, and Bench.

The Frappe project recommends its Docker devcontainer workflow for local custom
app development. A native Bench install is also possible on macOS or supported
Linux distributions. The disposable ERPNext `pwd.yml` demo is not a development
environment and cannot serve as the migration path to production.

## Preflight

From the ERA SOFT repository:

```bash
python3 scripts/preflight.py
```

The script reports missing required commands without installing or changing the
workstation.

## Native Bench outline

Install the exact prerequisites from the official Frappe v16 installation guide,
then create the bench beside (not inside) this repository:

```bash
bench init --frappe-branch version-16 frappe-bench
cd frappe-bench
bench get-app --branch version-16 erpnext https://github.com/frappe/erpnext.git
bench get-app era_soft https://github.com/eralmaz-art/era-soft.git
bench new-site era.localhost
bench --site era.localhost install-app erpnext
bench --site era.localhost install-app era_soft
bench --site era.localhost list-apps
bench start
```

Use local-only credentials and never commit `site_config.json`. Add
`era.localhost` to local name resolution if the operating system does not resolve
`*.localhost` automatically.

## Verification

In another terminal, from the bench directory:

```bash
bench --site era.localhost migrate
bench --site era.localhost run-tests --app era_soft
```

Expected installed apps include `frappe`, `erpnext`, and `era_soft`.

## Isolated native stack

When Docker virtualization is unavailable, ERA SOFT can use a workspace-local
toolchain and native processes. The prepared Codex workspace keeps the toolchain,
bench, and runtime as siblings of this repository:

```text
work/
├── era-soft/
├── frappe-bench/
├── runtime/
└── toolchain/
```

After the toolchain and site are initialized, manage the services from this
repository:

```bash
scripts/local_stack.sh start
scripts/local_stack.sh status
scripts/local_stack.sh stop
```

The default development URL is `http://era.localhost:8003`. The local test user
is `Administrator`; credentials are chosen during `bench new-site` and must never
be reused outside a disposable development environment.

The prepared disposable database uses `admin` as its local root password. Set
`ERA_DB_ROOT_PASSWORD` when the site was initialized with another password. The
database and Redis listeners remain bound to the local machine.

## Version upgrades

Pin both upstream applications to `version-16`; do not pin production to
`develop`. Test updates first in an upgrade branch and disposable database copy:

```bash
bench update --reset
bench --site era.localhost migrate
bench --site era.localhost run-tests --app era_soft
```

Review upstream release notes and schema changes before promoting the same
versions to staging. Production instructions will be documented separately after
hosting, backup, restore, observability, and rollback decisions are approved.
