# ERA SOFT

ERA SOFT is ERA Group's operating system for ready-mix concrete, construction,
management accounting, procurement, HR, executive reporting, and future AI
workflows.

It is a custom Frappe application installed alongside ERPNext. ERPNext remains
an upstream dependency and is never vendored or modified in this repository.

## Current status

This repository contains the approved architecture foundation and the first
upgrade-safe visual baseline:

- a valid `era_soft` Frappe application skeleton;
- explicit ERPNext extension boundaries;
- product, architecture, roadmap, and decision records;
- ERA SOFT branding, curated navigation, and a macOS launcher;
- a local environment preflight check;
- lightweight repository quality checks.

No business DocTypes have been created yet. That is intentional: the first
implementation must follow a fit-gap review against ERPNext.

## Target platform

| Component | Target |
| --- | --- |
| Frappe Framework | `version-16` |
| ERPNext | `version-16` |
| ERA SOFT | `main` for releases, `develop` for integration |
| Python | 3.14 |
| Database | MariaDB 11.8 |
| Node.js | 24 |

See [Local development](docs/LOCAL_DEVELOPMENT.md) before installing anything.

The prepared isolated workspace can be checked with:

```bash
scripts/local_stack.sh status
```

## Repository map

```text
era_soft/             Frappe application package
docs/                 Product and engineering decisions
scripts/preflight.py  Local dependency check
tests/                 Checks that run without a live Frappe site
```

## Non-negotiable rule

Before adding a DocType, report, workflow, or service, record the answer to:

> Does ERPNext already solve this business problem?

Configure ERPNext when the answer is yes. Extend it through ERA SOFT when the
answer is partial. Add ERA-owned code only when the answer is no.

## Documentation

- [Product vision](docs/PRODUCT_VISION.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Master roadmap](docs/ROADMAP.md)
- [Initial capability map](docs/ERPNext_CAPABILITY_MAP.md)
- [Local development](docs/LOCAL_DEVELOPMENT.md)
- [Visual baseline operations](docs/VISUAL_BASELINE.md)
- [Russian terminology standard](docs/localization/russian-terminology.md)
- [Contributing](CONTRIBUTING.md)
