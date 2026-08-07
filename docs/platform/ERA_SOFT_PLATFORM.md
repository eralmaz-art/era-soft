# ERA SOFT Platform Architecture

Status: **Draft — architecture baseline locked; governance approval pending**<br>
Architecture baseline: **LOCKED for application design**<br>
Scope: **Product and application architecture**<br>
Data Model: **not authorized**<br>
Implementation: **not authorized**

## Mission

ERA SOFT exists to give ERA Group one trusted, calm, and coherent way to run its
businesses. It connects people, decisions, evidence, and operating facts across
companies without forcing teams to reconcile disconnected spreadsheets or work
through the vocabulary and navigation of a generic ERP.

ERA SOFT is not a construction ERP. It is a modular business operating platform.
ERA Construction is the first application delivered on that platform.

## Vision

Within ten years, ERA SOFT is the shared operating platform for ERA Group and
its future businesses. A person signs in once, works within the companies and
responsibilities they are authorized to see, moves between focused applications,
and retains one consistent language, interaction model, evidence trail, and
source of truth.

Construction, concrete production, education, finance, people operations,
procurement, customer relationships, documents, and AI assistance appear as
independent applications within one ERA product. New applications can be added
without redesigning existing applications or duplicating identity, permissions,
files, audit, search, notifications, reports, dashboards, or interface patterns.

The platform helps people understand what changed, why it matters, which
decision is required, and what consequence follows. Technology remains in the
background; the visible product speaks ERA's language and supports daily work.

## Platform Goals

1. Provide one recognizable ERA SOFT experience across every application.
2. Let applications evolve independently without direct application-to-
   application dependencies.
3. Develop cross-cutting capabilities once and make them available through
   stable platform contracts.
4. Preserve one authoritative source for shared business facts and reject
   application-specific duplicates.
5. Make identity, access, decisions, evidence, and audit consistent across the
   product portfolio.
6. Allow a new application to be introduced without redesigning existing ones.
7. Keep business rules inside the application that owns the business outcome.
8. Preserve upgrade safety by extending supported foundations without modifying
   Frappe or ERPNext core.
9. Support Russian as the primary product language, Kyrgyz as the next business
   language, and English for development and technical administration.
10. Create a governed foundation for safe reporting, integrations, and future AI
    assistance.

## Platform Principles

1. **Platform first, applications focused.** Cross-cutting product capabilities
   belong to the platform; business outcomes remain inside focused applications.
2. **Applications are peers.** Construction, Concrete, Education, Finance, HR,
   Procurement, CRM, Documents, and AI Assistant never form a dependency chain.
3. **No direct application dependency.** An application does not import,
   manipulate, or depend on another application's private behavior or business
   records.
4. **Communication through platform contracts.** Cross-application requests,
   references, events, and status exchange use governed platform services and
   remain understandable to the user.
5. **One fact, one authority.** A shared business fact has one designated owner;
   applications reference or consume it instead of copying it into competing
   records.
6. **Business logic stays with its owner.** The platform supplies mechanisms but
   does not absorb construction, concrete, education, finance, HR, or CRM policy.
7. **Shared does not mean generic by assumption.** A capability moves into the
   platform only when its contract is stable, domain-neutral, and genuinely
   useful across applications.
8. **One experience system.** Every application uses the ERA SOFT Design System,
   localization standards, navigation shell, accessibility baseline, and common
   interaction patterns.
9. **Traceability across boundaries.** A cross-application decision preserves
   its origin, responsible owner, evidence, authority, status, and consequence.
10. **Optional applications remain optional.** Removing or delaying one
    application must not make an unrelated application unusable.
11. **Platform contracts are versioned.** Applications can evolve at different
    speeds without silently breaking shared behavior.
12. **Configuration and supported extension before custom infrastructure.** The
    platform reuses proven Frappe and ERPNext capabilities when they satisfy the
    approved contract and never modifies upstream core.

## Platform Model

```text
                         ERA SOFT

  Product Experience
  App shell · navigation · company context · search · notifications
  Design System · localization · accessibility · settings

  Applications
  Construction · Concrete · Education · Finance · HR · Procurement
  CRM · Documents · AI Assistant · future applications

  Core Platform Services
  Identity · users · companies · permissions · workflow · files
  audit · reports · dashboards · search · notifications · output · AI · API

  Supported Foundations
  Frappe Framework · ERPNext · approved external services
```

Dependency direction is downward. Core Platform Services never depend on an ERA
business application. Applications depend on platform contracts, not on each
other. Supported foundations remain replaceable or upgradeable behind reviewed
boundaries; their internal terminology does not define the visible product.

## Core Platform Services

The platform owns the reusable mechanism and its product-wide contract. Each
application owns the business meaning, policy, and trigger that it supplies to
that mechanism.

| Core service | Platform responsibility | Application responsibility |
|---|---|---|
| Authentication | Secure sign-in, session, recovery, and approved identity-provider behavior | State which users may enter the application; never implement a separate sign-in system |
| Users | One user identity, profile, language, availability, and application membership | Define business roles and responsibilities without duplicating user identity |
| Companies | One company context, permitted-company selection, and shared company identity | Define application-specific company policy and required business scope |
| Permissions | Common authorization enforcement, scope primitives, segregation support, and access-denied behavior | Define business visibility, decision rights, and restricted information |
| Workflow | Reusable decision routing, assignment, conditions, escalation, delegation, and decision history | Define the business decision, required inputs, authority, outcomes, and consequences |
| Notifications | Common inbox, delivery channels, preferences, urgency, acknowledgement, and delivery history | Define which business event requires attention, who owns it, and when it escalates |
| Reports | Common presentation, filtering, export, scheduling, freshness, source navigation, and access control | Define report meaning, business owner, audience, inputs, reconciliation, and decision supported |
| Dashboard | Common composition, context, refresh, status, drill-through, and responsive behavior | Define KPI meaning, hierarchy, thresholds, narrative, and business action |
| Search | Permission-aware global and in-application discovery with consistent result behavior | Define searchable business concepts, labels, ranking intent, and destination |
| Audit | Consistent actor, time, origin, change, decision, and access history | Define which business events and evidence are material and how corrections affect meaning |
| AI | Permission-aware assistance, source attribution, human-control policy, safety boundaries, and usage audit | Define validated use cases, responsible human decision, acceptable inputs, and prohibited actions |
| Files | Secure storage, versioning, access, preview, retention mechanism, and attachment behavior | Define required evidence, document purpose, business context, validity, and acceptance |
| Output and printing | Consistent print, PDF, export, branding, localization, access, and output history | Define the business content, approved template meaning, recipient, and required evidence |
| API | Authenticated, observable, versioned, and resilient integration boundary | Define domain meaning, allowed operations, source ownership, and business reconciliation |
| Settings | Layered product, company, application, role, and user configuration with safe defaults | Define application-owned settings and the business consequence of each option |
| Localization | Language selection, translation delivery, formatting, and terminology-governance mechanism | Supply approved domain vocabulary and validate meaning in each supported language |
| Design System | Shared tokens, components, interaction patterns, accessibility, and review gate | Compose domain experiences without forking shared components or changing approved UX silently |

These services are product responsibilities, not authorization to create new
technical services. At a future Data Model and implementation gate, ERA must
first determine which responsibilities are already satisfied by Frappe,
ERPNext, configuration, or supported extension points.

## Product Decomposition Model

ERA SOFT uses four product levels:

```text
ERA SOFT Platform
  ↓
Application
  ↓
Module
  ↓
Feature
  ↓
Named business decision
```

| Level | Purpose | Owns | Must not become |
|---|---|---|---|
| Platform | Provide stable capabilities shared across independent applications | Cross-cutting contracts, product shell, common services, Design System, platform governance | A container for one application's business logic |
| Application | Deliver a bounded business operating outcome for named users | Product mission, business rules, application navigation, decisions, KPI meanings, modules, roadmap | A technical menu group or dependency of another application |
| Module | Keep one coherent capability area inside an application understandable and governable | Related users, decisions, vocabulary, business boundary, feature set, module owner | A second application, generic platform service, or arbitrary folder of screens |
| Feature | Help one named user achieve an observable outcome or make a named decision | Trigger, user value, required context, behavior, consequence, and success evidence | A field, button, document, or technical task without product value |

Example:

```text
ERA SOFT Platform
  → ERA Construction
    → Procurement Control
      → Purchase Need
        → Approve, return, defer, or reject the need
```

### Module rules

- Every module belongs to exactly one application and has one accountable
  product or process owner.
- A module is a logical product boundary, not a decision to create a package,
  database, DocType group, workspace, or deployment unit.
- A module groups decisions that share users, vocabulary, operating context, and
  business outcome; visual proximity alone is insufficient.
- Modules inside an application may collaborate only through application-owned
  contracts and must not manipulate one another's private behavior.
- Cyclic module dependencies and duplicated business facts are prohibited.
- A module does not call another ERA application. Cross-application work still
  uses platform contracts.
- A capability used by two modules does not automatically belong to the
  platform; it must pass the Capability Placement Test.
- Module boundaries are reviewed before UX and again before Data Model, because
  screen grouping and record grouping are not assumed to be identical.

### Feature admission rule

No feature enters approved product scope until it identifies:

- the named user and operating context;
- the concrete business decision or outcome it supports;
- the trigger and frequency of that need;
- the minimum facts and evidence required;
- the responsible business owner and consequence;
- the application and module that own it;
- how success will be observed;
- normal, exception, and not-authorized outcomes.

“Add a comment field” is not an admissible feature. “Let the approver understand
and preserve why a purchase need was rejected” is an admissible product outcome
that may later lead to an approved UX and implementation choice.

## Application Architecture

### Definition of an ERA SOFT application

An application is a bounded business product with:

- a mission, users, owner, and measurable business outcomes;
- an explicit business boundary and vocabulary;
- business rules and decisions owned by named process roles;
- task-oriented navigation and screens governed by the ERA Design System;
- application-owned KPI and report meanings;
- declared use of platform services;
- an independent product lifecycle, roadmap, approval record, and release scope;
- no requirement that an unrelated ERA application be installed or active.

An application is not merely a menu group, technical package, ERPNext module, or
collection of records.

This is a logical product boundary. It does not decide whether applications use
separate repositories, Frappe packages, sites, databases, or deployments; those
are future architecture and implementation decisions.

### Application dependency rules

- An application may use Core Platform Services through their approved
  contracts.
- An application may consume authoritative ERPNext capabilities only as
  approved foundations within the platform boundary and after its own fit-gap
  review. This does not create a dependency on another ERA application.
- An application must not read or write another application's private state.
- An application must not call another application's internal functions or
  reproduce its business rules.
- A cross-application reference must preserve the authoritative owner and must
  remain valid when the supplying application is temporarily unavailable.
- A cross-application process must expose its handoff, status, responsible
  party, and failure or reconciliation state.
- The platform must not require every application to share one release date.
- Cyclic application dependencies are prohibited.

### Planned application portfolio

| Application | Product responsibility | Explicitly not Core Platform responsibility |
|---|---|---|
| ERA Construction | Project planning and control, budgets, construction needs, site supply, work acceptance, project cash and cost decisions | Generic identity, file storage, notification delivery, audit engine, or UI component library |
| ERA Concrete | Concrete demand, mix and production control, dispatch, delivery traceability, and concrete operating performance | Authentication, cross-product search, shared files, or Construction project logic |
| ERA Education | Education operations, learners, programs, academic delivery, and institution decisions | Generic users, permissions, dashboards, or notifications |
| Finance | Group financial control, cash, obligations, receivables, planning, and management-finance decisions | Authentication, company selector, generic reports engine, or Construction cost policy |
| HR | People operations, employment, attendance, development, and workforce decisions | User authentication identity or generic authorization engine |
| Procurement | Cross-company sourcing, supplier performance, commercial policy, and procurement portfolio control | Construction-specific need, work, budget, or site-acceptance logic |
| CRM | Customer relationships, opportunities, commercial pipeline, and account decisions | Generic identity, notification, search, or API mechanisms |
| Documents | Governed document lifecycles, classification, review, retention policy, and enterprise document work | Low-level file storage or application-specific evidence meaning |
| AI Assistant | A coherent user experience for governed assistance across authorized business contexts | The AI engine's security, permissions, source attribution, or audit mechanism |

This portfolio is directional, not implementation scope. Each application must
pass the approved product-development gates before its Data Model or
implementation begins.

## Shared UI Components

The following product-wide patterns are designed and maintained once:

- application shell, application switcher, company context, user menu, and
  primary navigation frame;
- global command and search experience;
- notification and assigned-decision inbox;
- page titles, breadcrumbs, tabs, contextual navigation, and primary actions;
- tables, filtering, search, sorting, saved views, pagination, and bulk-action
  safety;
- forms, field groups, validation, help, unsaved state, and destructive-action
  confirmation;
- status, risk, exception, freshness, missing-data, and permission-denied states;
- cards, KPI presentation, charts, comparisons, trends, and source drill-through;
- decision panels showing purpose, required evidence, reason, consequence, and
  approval conditions;
- files, evidence, comments, activity history, and responsible-person patterns;
- loading, empty, error, stale, offline, access-denied, and partial-data states;
- Russian-first typography, terminology, date, number, currency, and long-text
  behavior;
- keyboard, focus, contrast, zoom, responsive, and accessibility behavior.

Applications compose these components around their own decisions. A component
must not contain Construction, Concrete, Finance, HR, or other domain policy.
Application-specific compositions may become shared only after the platform
owner confirms a stable cross-application need.

## Shared Business Services

Shared business services express reusable cross-application responsibilities.
They do not own domain outcomes.

| Shared service | Reusable responsibility | Boundary |
|---|---|---|
| Organization context | Carry authorized company, business unit, role, and working context consistently | Applications decide which business facts require that context |
| Decision and approval service | Route a defined decision to authorized people and preserve outcome, conditions, and delegation | Applications define the decision contract and consequence |
| Work and escalation service | Assign accountable follow-up, due dates, escalation, acknowledgement, and resolution | Applications define what work exists and why it matters |
| Evidence service | Attach, classify, secure, version, and retrieve evidence in its originating context | Applications define what evidence proves a business event |
| Activity and comments service | Provide accountable collaboration and history around a business context | Comments cannot replace required approval or evidence |
| Notification service | Deliver meaningful attention requests across channels and applications | Applications own trigger, recipient intent, urgency, and resolution |
| Search and discovery service | Find authorized business contexts across applications without exposing private internals | Applications own searchable meaning and destination |
| Reporting and dashboard service | Present governed measures with scope, freshness, access, and source navigation | Applications own KPI semantics, inputs, thresholds, and reconciliation |
| Document output service | Produce consistent printable, PDF, and exported business output with access and version context | Applications own content meaning, template approval, and recipient purpose |
| Integration service | Exchange versioned requests, references, events, and acknowledgements with traceability | Applications own the business contract and failure consequence |
| AI assistance service | Ground assistance in authorized sources and preserve human accountability | AI cannot approve, pay, post, or change business truth autonomously |
| Reference governance | Designate an authoritative owner for shared vocabulary and business identities | It does not automatically turn every reused master into platform logic |

Concrete records, relationships, schemas, events, and APIs are deliberately not
defined here. They belong to future product and Data Model decisions.

## Cross-Application Interaction

Cross-application work follows a platform-mediated handoff:

```text
Originating application
  → approved platform contract
  → receiving application or approved external provider
  → acknowledged status and consequence
  → originating application
```

For example, ERA Construction may identify and approve a concrete need. If ERA
Concrete later fulfils that need, the applications exchange the authorized
request, reference, and fulfilment status through a platform integration
contract. Construction does not depend on Concrete's internal production model,
and Concrete does not depend on Construction's internal budget model. If ERA
Concrete is absent, Construction can still complete its procurement outcome
through an approved external supply path.

The same rule applies to future Finance, HR, Procurement, Documents, Education,
CRM, and AI Assistant interactions.

## Capability Placement Test

Before placing a new capability in the platform, the product and architecture
owners must answer:

1. Is the capability domain-neutral, or does it contain one application's
   business policy?
2. Do at least two independent applications need the same stable behavior?
3. Can the platform contract be explained without using one application's
   private concepts?
4. Is there one clear authoritative owner and compatibility policy?
5. Would platform ownership reduce duplication without forcing applications
   into the same lifecycle?
6. Does Frappe or ERPNext already provide the required capability through a
   supported, upgrade-safe extension point?

If the first five answers are not clearly favorable, the capability remains in
the owning application. If the sixth answer is yes, ERA configures or extends
the proven foundation instead of recreating it.

## ERA Construction Boundary Review

The Phase 3.1 Construction specification remains the authority for construction
business behavior. This review moves only cross-cutting mechanisms to the
platform boundary.

| Concept found around ERA Construction | Platform responsibility | Construction responsibility retained |
|---|---|---|
| User and login | Identity, authentication, profile, language, and application membership | Construction role, project responsibility, and decision authority |
| Company selector and scope | Shared company identity and authorized working context | Construction rules within the selected company and object |
| Permissions | Enforcement, scope primitives, segregation support, and access-denied behavior | Who may see, request, accept, approve, pay, or close in Construction |
| Workflow | Reusable routing, assignment, delegation, escalation, and decision history | Purchase, budget, acceptance, payment, exception, and closeout decisions |
| Notifications and tasks | Inbox, channels, delivery, preferences, acknowledgement, and escalation mechanism | The event, urgency, recipient intent, owner, and resolution condition |
| Files, documents, and photos | Storage, versioning, access, preview, retention mechanism, and common UI | Which evidence is required for a project fact or decision and what it proves |
| Audit and activity | Common actor, time, origin, change, access, and decision history | Which Construction events are material and how correction changes meaning |
| Dashboard and report engines | Composition, rendering, filtering, freshness, export, access, and drill-through patterns | Construction KPI definitions, inputs, thresholds, reports, and decisions |
| Search | Permission-aware discovery and consistent result behavior | Construction concepts, labels, relevance, and destinations |
| Design System and localization | Shared visual, interaction, accessibility, and language foundation | Construction information hierarchy and approved domain terminology |
| API and integrations | Secure, versioned, observable exchange and reconciliation mechanism | Construction business meaning and allowed cross-boundary outcomes |
| AI engine | Permission, source, safety, human-control, and audit contract | Future validated Construction assistance use cases |
| Settings | Product, company, application, role, and user configuration layers | Meaning and consequence of Construction-owned settings |

The following remain entirely within ERA Construction because they are domain
behavior, not platform mechanisms:

- construction object lifecycle and project context;
- initial and revised project budgets;
- construction need and procurement decisions;
- supplier or contractor selection in construction context;
- commercial commitment and construction contract policy;
- material receipt, site custody, movement, consumption, and discrepancy;
- measured service and subcontracted-work acceptance;
- project obligation, payment priority, advance, retention, and dispute meaning;
- committed, actual, paid, forecast, progress, variance, and project-risk
  semantics;
- construction roles, reports, business rules, decision model, and closeout.

Supplier, customer, employee, item, and other potentially shared business
identities are not automatically declared Core Platform Services by this
document. Their authoritative ownership and reuse boundary must be decided at a
future business and Data Model gate; duplication remains prohibited.

## Platform Governance

- The Platform has a named Product Owner and Architecture Owner.
- Every Core Platform Service has one accountable owner and a versioned contract.
- Every application declares the platform services it uses and the business
  capabilities it owns.
- A new application passes the standard IDEA → BUSINESS MODEL → UX → UI → DATA
  MODEL → IMPLEMENTATION sequence plus a Platform Boundary review.
- A proposed cross-application dependency blocks approval until it is removed or
  replaced by a governed platform contract.
- Shared-component changes are reviewed against all consuming applications and
  the Design System.
- Platform releases publish compatibility expectations; applications are not
  forced into one feature release cadence.
- Security, access, audit, localization, accessibility, and upgrade compatibility
  are product-wide release gates.
- Upstream Frappe or ERPNext core modifications remain prohibited.

## Architecture Freeze and Change Control

The Platform architecture boundary is now **LOCKED for application design**.
Construction work proceeds within this baseline; the platform is not reopened
merely because an application finds a local design inconvenient.

Locked does not mean that unresolved P0 governance choices are approved. It
means the dependency direction, platform/application separation, shared-service
boundary, and no-direct-application-dependency rule are the governing baseline
until a separately approved change replaces them.

The following require a Platform Change Proposal and a separate Architecture
Decision Record:

- adding, removing, or materially changing a Core Platform Service;
- moving business logic between an application and the platform;
- allowing any direct application-to-application dependency;
- changing the authoritative owner of a shared business fact;
- introducing a breaking platform contract or incompatible application rule;
- changing the supported-foundation or upstream-core boundary;
- changing the Platform → Application → Module → Feature hierarchy.

A Platform Change Proposal must state:

1. The business problem and named decision that cannot be supported safely by
   the current boundary.
2. Evidence that the need is cross-application, stable, and not merely local
   convenience.
3. Alternatives considered, including keeping the capability in its owning
   application.
4. Applications, users, contracts, security, audit, UX, and releases affected.
5. Compatibility, transition, rollback, and ownership consequences.
6. Product Owner and Architecture Owner approval.

Typographical corrections, links, examples, and clarifications that do not
change ownership, dependency direction, contract meaning, or approval criteria
may be updated through normal documentation review.

This freeze is recorded by
[ADR 0003](../adr/0003-lock-platform-application-boundary.md).

## Open Decisions

### P0 — required before Platform Foundation approval

1. Confirm the Platform Product Owner and Architecture Owner.
2. Confirm which responsibilities are ERA platform contracts versus direct reuse
   of supported Frappe and ERPNext capabilities.
3. Confirm authoritative ownership for shared company, counterparty, item,
   employee, currency, unit, location, and other cross-application identities.
4. Confirm whether Finance, Procurement, HR, and Documents begin as independent
   applications, platform-backed surfaces over ERPNext, or later product
   extractions; no current application may depend on that choice.
5. Confirm the platform contract and compatibility governance for cross-
   application references, requests, events, and status.
6. Confirm application activation, company availability, and role-membership
   policy.
7. Confirm product-wide decision delegation, escalation, and segregation policy.
8. Confirm audit, evidence retention, privacy, and sensitive-data policy.
9. Confirm Russian/Kyrgyz/English terminology ownership and translation approval.
10. Confirm AI governance, prohibited actions, human accountability, and source
    requirements before any AI capability is enabled.

### P1 — required before the second application

1. Define the minimum application declaration and Platform Boundary review.
2. Define versioning and compatibility expectations for platform contracts.
3. Validate the shared application shell and app-switching experience with at
   least Construction and one independent future application concept.
4. Define product-wide search, notification, and assigned-decision information
   architecture.
5. Confirm the first real cross-application use case and its failure behavior.

## Approval Criteria

Platform Foundation may be recommended for approval only when:

- Platform and application ownership is named;
- P0 decisions are resolved and recorded;
- Construction is confirmed as an application, not the platform itself;
- the Platform → Application → Module → Feature hierarchy is accepted;
- no planned application directly depends on another application;
- Core Platform Services and application business responsibilities have clear
  non-overlapping ownership;
- the product-development process includes a Platform Boundary review;
- the architecture remains upgrade-safe and contains no Frappe or ERPNext core
  modification.

This document does not authorize a Data Model, DocType, workflow, API, service,
screen, integration, migration, or implementation.
