# Architecture

## System context

```text
Users
  │
  ▼
ERA workspaces, forms, reports, dashboards
  │
  ├── ERA SOFT custom domains
  │     Concrete, Construction, Executive projections
  │
  └── ERPNext standard domains
        Selling, Buying, Stock, Manufacturing, Projects, Accounts, HR
          │
          ▼
     Frappe Framework
     auth, permissions, workflow, ORM, jobs, API, audit
          │
          ▼
     MariaDB + Redis/Valkey + file storage
```

## Ownership boundaries

ERPNext owns standard parties, items, warehouses, sales and purchase documents,
stock ledger, general ledger, projects, employees, permissions primitives, and
their standard reports.

ERA SOFT owns concrete-specific master data and events, construction control
extensions not represented by ERPNext, executive read models, ERA roles and
workspaces, integration adapters, and ERA-specific validation.

References across the boundary use links to standard ERPNext documents. ERA
SOFT does not duplicate Customer, Supplier, Item, Project, Warehouse, Sales
Order, Delivery Note, Purchase Order, Payment Entry, Stock Entry, or GL Entry.

## Extension decision ladder

For each requirement:

1. Configure standard ERPNext.
2. Add Custom Fields / Property Setters only when they are portable as fixtures
   and have clear ownership.
3. Add an ERA DocType that links to ERPNext records.
4. Subscribe through documented Frappe hooks.
5. Override a class or whitelisted method only with an ADR and regression tests.
6. Propose an upstream change if the need is generic.

## Domain boundaries

### ERA Concrete

Owns concrete grade specifications, mix-design versions, batching/production
events, dispatch planning, mixer and driver assignment, delivery traceability,
and concrete cost projections. It reuses ERPNext parties, items, orders,
inventory movements, invoices, payments, and ledgers.

### ERA Construction

Owns project budget versions, commitments, construction contracts, site control
events, and project cost projections that are missing from standard ERPNext. It
reuses ERPNext Projects, Cost Centers, Warehouses, procurement, stock, and
accounting documents.

### ERA Finance

Adds management views and controls. It does not create a parallel ledger. Cash,
bank, receivables, payables, and journal truth remain in ERPNext Accounts.

### Executive Dashboard

Contains read-only KPI queries and cached projections. A dashboard may navigate
to source records but never becomes a transaction system or a second source of
truth.

## Data rules

- Every operational record is company-scoped.
- Submitted business events are immutable; corrections use cancellation and
  amendment or explicit reversal.
- Master-data identity is not inferred from display labels.
- Currency, units of measure, posting date/time, and timezone are explicit.
- Server-side permission checks apply to every API and report.
- Integrations are idempotent and preserve the external reference.
- Dashboard calculations are reproducible from authoritative documents.

## Dependency policy

ERA SOFT supports one ERPNext major version at a time. Both Frappe and ERPNext
are bounded to major version 16 in `pyproject.toml`. Upgrades are performed in a
dedicated branch with migration rehearsal and contract tests; `develop` is not a
supported production target.

## Environments

- local: developer bench and disposable site data;
- test: automated checks and migration validation;
- staging: production-like integrations and anonymized/sample data;
- production: controlled releases from `main`, backups, monitoring, and audited
  access.

Production topology and hosting remain open decisions. Local development is not
promoted into production.
