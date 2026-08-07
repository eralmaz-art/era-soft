# Architecture

## System context

```text
Users
  │
  ▼
ERA SOFT product experience
app shell, navigation, Design System, localization
  │
  ▼
ERA SOFT applications
Construction, Concrete, Education, Finance, HR, Procurement,
CRM, Documents, AI Assistant, future applications
  │
  ▼
ERA SOFT Platform services
identity, companies, permissions, workflow, notifications, files,
search, audit, reports, dashboards, AI, API, settings
  │
  ▼
Supported foundations
ERPNext standard capabilities + Frappe Framework
  │
  ▼
MariaDB + Redis/Valkey + file storage
```

ERA SOFT Platform is the product architecture above the current technical
foundation. Construction is its first application, not the platform itself.
Applications are peers and communicate only through governed platform
contracts. The complete platform boundary is defined in
[`platform/ERA_SOFT_PLATFORM.md`](platform/ERA_SOFT_PLATFORM.md).

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

### ERA SOFT Platform

Owns the shared product shell and contracts for identity, company context,
permissions, workflow, notifications, files, search, audit, reports, dashboards,
AI, API, settings, localization, and the Design System. It supplies reusable
mechanisms but does not own application business rules.

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

The proposed construction domain model, ERPNext fit-gap, cost dimensions,
budget semantics, procurement flow and review questions are recorded in
[`architecture/era-construction/`](architecture/era-construction/01-domain-model.md).
That proposal is an architecture review pack, not authorization for major
implementation.

ERA Construction must not depend on ERA Concrete, Finance, Procurement,
Documents, HR, or any other ERA application. Any future cross-application
handoff uses a platform contract and preserves the authoritative business owner.

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

ERA applications depend on platform contracts, never on one another. Platform
services do not depend on application business logic. Cross-application cycles,
private-state access, and duplicated shared facts are prohibited.

An application's reuse of standard ERPNext capabilities requires its own fit-gap
review and supported extension boundary; it does not grant ownership of
ERPNext core or permission to modify it.

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
