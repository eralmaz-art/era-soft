# Master Roadmap

The roadmap is outcome-based. A phase exits only when its evidence is accepted;
code volume is not an exit criterion.

All products follow the mandatory gates in
`docs/PRODUCT_DEVELOPMENT_PROCESS.md`. No release may skip Business Model, UX,
UI, Data Model, or Implementation approval. Every application also passes the
Platform Boundary review defined in
`docs/platform/ERA_SOFT_PLATFORM.md`.

## Release map

| Release | Outcome | Status |
|---|---|---|
| `v0.1-architecture-approved` | upgrade-safe repository and construction architecture | complete |
| `v0.2-visual-baseline` | branded local product shell and curated navigation | complete |
| `v0.3-product-foundation` | Russian product language, design constitution, dashboard UX v2, and product-development gates | current stable foundation |
| `v0.4-platform-foundation` | locked platform/application boundary and shared-service architecture | architecture locked; governance approval pending |
| `v0.5-construction-business-model` | approved Construction Product Spec, rules, decisions, modules, and pilot boundary | draft complete; approval pending |
| `v0.6-construction-ux` | validated information architecture and flows for the first vertical scenario | planned |
| `v0.7-construction-ui` | approved ERA Design System compositions and complete UI states | planned |
| `v0.8-construction-data-model` | approved ERPNext fit-gap, authoritative model, permissions, and data contracts | blocked by UX and UI |
| `v0.9-construction-mvp` | implemented and reconciled first Construction vertical scenario | blocked by Data Model |
| `v1.0-production-pilot` | accepted real-project pilot with operations, controls, support, and rollback | blocked by MVP |

## Phase 0 — Foundation (completed)

- establish the ERA SOFT custom application repository;
- adopt supported Frappe/ERPNext version boundaries;
- document product, architecture, contribution, and upgrade rules;
- create repeatable local setup and repository checks.

Exit evidence: clean install of `era_soft` next to ERPNext on a disposable site,
passing repository checks, and an accepted architecture decision.

## Phase 1 — ERPNext study and fit-gap (construction scope completed)

Inspect real workflows and source behavior before choosing configuration,
extension or custom development. The construction-scope inspection covers
Projects, Buying, Stock, Accounts, Assets, Contract and Employee; other domains
retain their own fit-gap gate.

Exit evidence: source-backed capability map with `reuse`, `extend`, `custom`, or
`defer` decisions.

## Phase 2 — ERA Construction architecture (completed)

Inspect and model the real Projects, Buying, Stock, Accounts, Assets, Contract
and Employee capabilities required for ERA Construction. Approve the project and
cost hierarchy, construction budget semantics, procurement/payment workflow,
MVP boundary, risks and open business decisions before implementation.

Exit evidence: approved ERA Construction architecture pack with `reuse`,
`extend`, `custom`, or `defer` decisions, resolved P0 questions and named process
owners.

## Phase 2.1 — Visual and Russian baseline (completed)

Establish upgrade-safe ERA branding, curated navigation, macOS launch, Russian
as the primary user language, and one authoritative Russian business glossary.
No business behavior is introduced.

Exit evidence: verified local site, tagged visual baseline, complete ERA
Workspace translation, reviewed daily ERPNext screens, and reversible extension
configuration without upstream source changes.

## Phase 3 — ERA SOFT product foundation (completed)

Define the visual foundations, reusable component behavior, product navigation,
data-visualization rules, Owner Dashboard experience, Construction Workspace
experience, product-development lifecycle, and UX-before-code governance gate.
Validate concepts before changing the production Frappe interface.

Exit evidence: approved design tokens and component rules, approved Owner
Dashboard v2, Finance, Project, and Procurement direction, and a screen-review
gate applied to the first product backlog.

## v0.4 — Platform Foundation (architecture locked; approval pending)

Establish ERA SOFT as a modular operating platform and Construction as its first
independent application. Define Core Platform Services, application dependency
rules, shared UI and business-service boundaries, and the governance required to
add future applications without architectural redesign.

Exit evidence: approved `docs/platform/ERA_SOFT_PLATFORM.md`, named Platform
Product and Architecture Owners, resolved P0 platform decisions, and a confirmed
rule that applications depend on platform contracts rather than one another.
No Data Model or implementation is authorized by this gate.

The architecture boundary is locked by ADR 0003. This prevents architectural
drift but does not close the document's unresolved P0 governance decisions or
create the `v0.4-platform-foundation` tag automatically.

## v0.5 — Construction Business Model (current next gate)

Describe how the best construction business should work before selecting ERP
entities. Approve the purpose, users, goals, end-to-end process, screen map,
navigation, KPIs, permissions, reports, boundaries, and open decisions in
`docs/modules/construction/PRODUCT_SPEC.md`.

Exit evidence: approved Construction Product Spec and business process, with
named product and process owners, an approved application module map, confirmed
first vertical scenario and pilot, plus a passed Platform Boundary review. UX,
UI, Data Model, and implementation remain blocked until this evidence is
recorded.

## v0.6 — Construction UX

Validate how each role completes the first scenario without navigating an ERP
catalogue or maintaining a shadow spreadsheet:

```text
Need
  → approval
  → supplier order
  → material delivery or service acceptance
  → supplier invoice
  → payment
```

Define information architecture, role entry points, decision briefs, flows,
normal and exception states, Russian terminology, and reviewable mockups. Keep
the approved Platform and Construction boundaries unchanged.

Exit evidence: named users can walk through the full scenario and every material
decision, state, handoff, source, correction, and not-authorized outcome is
represented in the approved UX.

## v0.7 — Construction UI

Apply the ERA SOFT Design System to the approved UX. Complete desktop,
responsive, accessibility, Russian long-text, loading, empty, stale, error,
permission, confirmation, and destructive states without changing business
meaning.

Exit evidence: Product Owner, primary users, and Design System Owner approve the
complete visual scenario and component use.

## v0.8 — Construction Data Model

Only after UX and UI approval, inspect the actual supported ERPNext behavior and
define `reuse`, `extend`, `custom`, or `defer` for the first vertical scenario.
Approve authoritative records, relationships, permissions, audit boundaries,
KPI/report contracts, migration impact, and reconciliation tests.

Any existing ERA software and live-data audit required for the scenario occurs
inside this gate before migration design. Configuration of ERP foundations is
planned only after the approved model establishes responsibility and sequence.

Exit evidence: approved fit-gap and Data Model package with no duplicate
business truth, no direct application dependency, no ERPNext core modification,
and explicit acceptance tests for every management consequence.

## v0.9 — Construction MVP

Implement only the approved vertical scenario. Budget and project context are
required controls; contracts, forecasting, labor, tender scoring, advanced
document management, and unrelated reporting remain outside scope unless an
approved scenario decision requires them.

Exit evidence: the full Need → Approval → Supplier Order → Delivery or Service
Acceptance → Supplier Invoice → Payment chain works on a test object, preserves
authority and evidence, reconciles to source facts, and passes automated,
permission, migration, visual, and rollback checks.

## v1.0 — Production Pilot

Run the approved scenario with named users on one real construction project.
Measure adoption, decision time, exceptions, reconciliation, support load, and
remaining spreadsheet dependence. Operate backup, recovery, monitoring,
security, release, rollback, and support procedures.

Exit evidence: Product Owner and process owners accept the pilot; the scenario
can be operated through a normal working cycle without a shadow operational
ledger; every headline result traces to authoritative sources; production
operations and rollback have been rehearsed.

## After v1.0 — Application portfolio expansion

Construction expands through additional complete scenarios only after pilot
evidence. Concrete, Education, Finance, HR, Procurement, CRM, Documents, and AI
Assistant remain independent future applications and enter the roadmap only
through their own Business Model → UX → UI → Data Model → Implementation gates.
