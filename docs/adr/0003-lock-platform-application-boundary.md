# ADR 0003: Lock the Platform and application boundary

- Status: Accepted
- Date: 2026-08-08
- Scope: Product architecture baseline

## Context

ERA SOFT has been elevated from a construction-centered system to a modular
business operating platform. Construction is the first application; Concrete,
Education, Finance, HR, Procurement, CRM, Documents, AI Assistant, and future
applications are intended to remain independent peers.

Without a freeze, application teams could gradually move local business logic
into the platform, introduce direct application dependencies, duplicate shared
capabilities, or reopen foundational decisions for convenience. That would turn
the platform into an ungoverned monolith.

At the same time, the platform document still contains P0 ownership and policy
questions. An architecture lock must not be misrepresented as approval of those
unresolved governance decisions.

## Decision

The architecture baseline in `docs/platform/ERA_SOFT_PLATFORM.md` is locked for
application design.

The governing hierarchy is:

```text
Platform → Applications → Modules → Features → Business decisions
```

The following rules are frozen:

- applications are independent peers;
- applications depend on platform contracts, never directly on one another;
- platform services provide reusable mechanisms and do not own application
  business logic;
- modules remain bounded capability areas inside one application;
- every feature must support a named business decision or observable outcome;
- shared facts have one authoritative owner;
- Frappe and ERPNext core remain unmodified.

Any material change to these rules, the platform/application ownership boundary,
Core Platform Services, shared-fact authority, or contract compatibility requires
a separate Platform Change Proposal and ADR approved by the Platform Product
Owner and Architecture Owner.

Normal documentation corrections and clarifications may proceed without a new
ADR only when they do not alter ownership, dependency, contract meaning, or
approval criteria.

Construction remains at the Business Model gate. Platform governance P0
decisions remain open; this ADR does not approve them and does not authorize UX,
UI, Data Model, DocTypes, workflows, services, or implementation.

## Consequences

- product teams have a stable boundary within which to design applications;
- Construction cannot justify changing the platform solely for local
  convenience;
- future applications cannot form a dependency chain;
- platform growth requires explicit cross-application evidence and ownership;
- module and feature boundaries become required product-design decisions;
- unresolved Platform Foundation governance remains visible and must still be
  approved before the foundation is formally complete;
- architectural change becomes deliberate, reviewable, and reversible rather
  than incremental drift.
