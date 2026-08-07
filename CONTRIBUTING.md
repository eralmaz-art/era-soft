# Contributing

## Workflow

1. Branch from `develop` using `feature/<scope>`, `fix/<scope>`, or
   `chore/<scope>`.
2. Keep each change focused and independently reviewable.
3. Update the capability map or add an ADR when a change creates a new ERPNext
   dependency, override, integration boundary, or irreversible data model.
4. Run the repository checks and relevant Frappe tests.
5. Open a pull request into `develop`. Promote tested releases from `develop`
   to `main`.

## Extension policy

Preferred mechanisms, in order:

1. ERPNext configuration, roles, permissions, workflows, and reports;
2. ERA-owned DocTypes linked to ERPNext master or transaction records;
3. additive Frappe hooks and event handlers;
4. class or method overrides only with an ADR and regression tests;
5. upstream ERPNext core changes only as a separately reviewed last resort.

Do not copy ERPNext source into this repository. Do not monkey-patch at import
time. Do not store secrets, site configuration, database dumps, or generated
bench files here.

## Definition of done

- the ERPNext fit-gap decision is documented;
- the screen brief names its user, decision, primary action, source data, and
  success measure;
- user-facing work has an approved UX mockup and reuses documented ERA SOFT
  patterns;
- permissions and company boundaries are tested;
- validation exists on the server, not only in JavaScript;
- migrations are repeatable and backward-safe;
- user-facing labels are translatable;
- the feature has an owner-visible outcome or a documented operational need;
- relevant tests and documentation are updated.

User-facing implementation must pass the UX review gate in
`docs/design-system/era-soft/06-screen-review-gate.md`. A Frappe or ERPNext page
that technically exposes the required records is not automatically an accepted
ERA SOFT experience.

## Local checks

```bash
python3 scripts/preflight.py
python3 -m compileall -q era_soft scripts tests
python3 -m unittest discover -s tests -v
```

Run full Frappe tests from the bench directory once the app is installed:

```bash
bench --site era.localhost run-tests --app era_soft
```
