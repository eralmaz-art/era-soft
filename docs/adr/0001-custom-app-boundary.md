# ADR 0001: Keep ERA SOFT as a separate Frappe application

- Status: Accepted
- Date: 2026-08-07

## Context

ERA Group needs construction and ready-mix concrete capabilities on top of a
general ERP. ERPNext already provides users, permissions, parties, accounting,
buying, selling, stock, projects, manufacturing primitives, reports, and APIs.
Maintaining a fork would couple ERA releases to core patches and make upstream
upgrades expensive.

## Decision

ERA SOFT is a separately installed Frappe application. ERPNext and Frappe remain
upstream dependencies on matching supported major versions. Standard ERPNext
documents stay authoritative. ERA-specific records link to them and extend
behavior through documented Frappe hooks.

Core modifications and copied ERPNext source are prohibited. An override is
allowed only when configuration, composition, events, and an upstream proposal
cannot solve a validated requirement; it requires its own ADR and regression
tests.

## Consequences

- upstream updates remain feasible and are tested as dependency upgrades;
- ERA domain code has a clear owner and deployment unit;
- duplicate master and transaction models must be actively rejected;
- some UX work is required to present one ERA-branded surface across underlying
  ERPNext modules;
- API and hook compatibility becomes an explicit contract test responsibility.
