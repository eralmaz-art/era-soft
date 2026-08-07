# ERA SOFT Product Development Process

Status: **Approved governance baseline**  
Applies from: **v0.3-product-foundation**

## Operating principle

ERA SOFT does not begin with the question “Which DocTypes should we create?”
The first question is:

> Как должен работать лучший бизнес-процесс и какое решение должен принять
> пользователь?

Frappe and ERPNext are evaluated only after the business model, user experience,
and interface intent are understood. Configuration, extension, and custom code
remain implementation choices rather than product requirements.

## Platform foundation prerequisite

ERA SOFT is a modular platform, and every business product is an independent
application on that platform. Before an application passes its Business Model
gate, it must declare:

- the business capabilities and outcomes it owns;
- the Core Platform Services it uses;
- any shared business facts and their authoritative owner;
- every proposed cross-application handoff;
- how it remains usable when another optional application is absent.

A Platform Boundary review is mandatory at every product gate. A direct
dependency on another ERA application, duplicated platform capability, or
application business logic placed in the platform blocks approval. The platform
boundary is governed by
[ERA_SOFT_PLATFORM.md](platform/ERA_SOFT_PLATFORM.md).

## Feature admission rule

No feature enters an approved backlog, UX flow, UI composition, Data Model, or
implementation scope until it identifies:

- the named user and operating context;
- the concrete business decision or observable outcome it supports;
- the trigger, frequency, required facts, and evidence;
- the accountable business owner and consequence;
- the application and module that own it;
- normal, exception, and not-authorized outcomes;
- how success will be observed;
- why an existing process, ERPNext capability, or platform service is
  insufficient.

A field, button, document, dashboard, report, or notification is a possible
solution, not a product requirement. The full admission standard and statement
template are defined in [PRODUCT_STRATEGY.md](PRODUCT_STRATEGY.md).

## Mandatory sequence

```text
IDEA
  ↓
BUSINESS MODEL
  ↓
UX
  ↓
UI
  ↓
DATA MODEL
  ↓
IMPLEMENTATION
```

**IDEA** is the intake state. The five stages after it are mandatory approval
gates. A product may return to an earlier gate; it may never skip one.

## Gate 1 — Business model

### Question

How should the business operate when responsibilities, decisions, evidence, and
exceptions are made explicit—without reference to ERP screens?

### Required evidence

- purpose, users, jobs, business goals, and boundaries;
- current and target process from trigger to outcome;
- roles, decision rights, approvals, evidence, and exception paths;
- business vocabulary and authoritative owners;
- measurable problems and success criteria;
- initial product specification.

### Prohibited

- selecting DocTypes because their names resemble business concepts;
- designing around current ERPNext navigation;
- implementation estimates presented as product requirements.

## Gate 2 — UX

### Question

What information and interaction help each user make the next decision faster?

### Required evidence

- information architecture and progressive-disclosure path;
- screen inventory and role navigation;
- decision brief for every screen;
- normal, empty, loading, stale, error, offline, and permission states;
- low-fidelity flows and reviewable interactive mockups;
- validated Russian wording.

### Prohibited

- coding a screen before its named mockup is approved;
- exposing the ERP module tree as the product navigation;
- adding information without a decision it supports.

## Gate 3 — UI

### Question

How does the approved UX become a consistent, accessible ERA SOFT interface?

### Required evidence

- approved design-system components and tokens;
- desktop and responsive compositions;
- typography, spacing, status, icon, table, chart, form, and motion treatment;
- contrast, keyboard, zoom, long-text, and Russian-language review;
- visual approval against the named UX version.

### Prohibited

- one-off component styling without a design-system decision;
- decorative color, unexplained charts, and generic widget dashboards;
- changing information hierarchy during visual polish without returning to UX.

## Gate 4 — Data model

### Question

Which authoritative records, relationships, permissions, and calculations can
support the approved product without a shadow business ledger?

### Required evidence

- ERPNext reuse / extend / custom / defer disposition;
- entity and relationship model;
- company, project, currency, unit, date, and status semantics;
- permission matrix and audit boundaries;
- KPI and report data contracts with reconciliation tests;
- migration and backward-compatibility impact;
- architecture decision record for every material custom model.

### Prohibited

- creating a custom DocType before reuse and extension are evaluated;
- client-side financial or permission authority;
- storing the same business fact in competing records.

## Gate 5 — Implementation

### Question

What is the smallest upgrade-safe vertical slice that proves the approved
business outcome?

### Required evidence

- versioned acceptance scenarios and implementation scope;
- supported extension points only; no ERPNext or Frappe core changes;
- automated tests for permissions, calculations, reconciliation, and upgrades;
- visual verification against the approved mockup;
- operational documentation, rollback, and release evidence;
- product- and process-owner acceptance.

### Prohibited

- implementing the entire product in one release;
- speculative functionality outside the approved product specification;
- declaring completion without source reconciliation and role testing.

## Required product specification

Every ERA SOFT product maintains a versioned `PRODUCT_SPEC.md` containing at
minimum:

- Platform Relationship and owned business boundary;
- application module map and feature ownership;
- Purpose;
- Users;
- Business Goals;
- Business Process;
- Main Screens;
- Navigation;
- KPIs and data contracts;
- Permissions;
- Reports;
- Future Scope;
- Out of Scope;
- Open Decisions;
- Approval Record.

The specification may be refined during Business Model, UX, and UI stages. No
Data Model or Implementation work begins until the corresponding sections and
approval record are complete.

## Product ownership

| Decision | Required owner |
|---|---|
| Product purpose, goals, priority | Product owner |
| Business process, exceptions, terminology | Process owner |
| UX hierarchy and interaction | Product owner and primary user |
| UI system and accessibility | Design-system owner |
| Data integrity, ERPNext fit, permissions | Engineering owner |
| Release acceptance | Product owner and process owner |

An approval is versioned, dated, and scoped. Silence, an implementation commit,
or a passed technical test does not substitute for product approval.
