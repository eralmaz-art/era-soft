# ADR 0002: Design before user-facing implementation

- Status: Accepted
- Date: 2026-08-07
- Decision owners: ERA product owner and ERA SOFT engineering

## Context

ERA SOFT uses Frappe and ERPNext as its transactional engine, but its daily
experience must not inherit the density, terminology, or navigation model of a
generic ERP. If each module independently adapts upstream screens, the product
will quickly accumulate inconsistent buttons, tables, forms, dashboards, and
project views. Those inconsistencies are expensive to remove after users and
workflows depend on them.

## Decision

Every new user-facing screen or material change to an existing daily screen
must pass this sequence:

```text
decision brief -> low-fidelity flow -> UX mockup -> product approval
-> implementation -> visual/accessibility verification
```

Implementation is not authorized by an approved domain model alone. The review
must identify the user, the decision being accelerated, the authoritative data,
the primary action, the exception states, and the design-system patterns being
reused.

The ERA SOFT design system is the default contract. A new visual or interaction
pattern requires a documented reason and design-system review before it enters a
feature branch. ERPNext core remains unchanged; approved experiences are built
through supported configuration, custom-app assets, Workspaces, Page/Report
extensions, and additive ERA-owned code only where the fit-gap decision permits.

## Consequences

- Phase 3 design approval precedes Construction module implementation.
- A raw ERPNext form or list is an implementation surface, not automatically the
  accepted daily experience.
- Designers and process owners review exceptions, empty states, permissions, and
  destructive actions before engineering estimates are considered final.
- Delivery may start more slowly, but later modules reuse a stable vocabulary and
  component language.
- Production CSS and business code are unchanged until the corresponding mockup
  is approved.
