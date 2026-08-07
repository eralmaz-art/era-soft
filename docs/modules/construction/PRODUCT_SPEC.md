# ERA Construction Product Specification

Status: **Draft — Business Model gate**<br>
Product: **ERA Construction**<br>
Target release: **v0.4-construction-product-spec**<br>
Product owner: **pending confirmation**<br>
Process owners: **pending confirmation**<br>
Data Model: **not authorized**<br>
Implementation: **not authorized**

## Purpose

ERA Construction is the operating product through which ERA Group plans,
executes, finances, and controls construction projects. It must let each role
understand the state of an object, make the next safe decision, and trace that
decision from the original need through budget, procurement, delivery, work,
invoice, payment, and final project cost.

The product is not an ERP module catalogue. It is organized around the
construction object and the business decisions required to keep work moving
within approved cost, schedule, quality, and cash constraints.

## Vision

Within five years, ERA Construction is the project operating application for
ERA Group's construction portfolio within ERA SOFT Platform. Every object is
managed through one shared, project-centered view from intent and budget through
procurement, execution, cash control, and closeout.

Field teams, project leadership, procurement, and finance work from the same
business facts instead of maintaining parallel spreadsheets. Management trusts
the product as the source of truth because every important number, risk, and
decision can be traced to its origin and accountable owner.

ERA Construction does more than record completed activity. It reveals the next
decision, its context, and its likely consequence early enough to protect work,
budget, schedule, quality, and cash. The product grows across companies and
objects without losing a common operating language or becoming harder to use.

## Product Principles

1. **Project before document.** People enter through the construction object
   and the decision they need to make, not through a catalogue of record types.
2. **One business fact, one authoritative home.** The same need, obligation,
   acceptance, cost, or payment is not maintained in parallel operational
   ledgers or spreadsheets.
3. **Every important number is traceable.** A manager can move from a KPI or
   exception to its source facts, evidence, responsible person, and decision
   history.
4. **The user understands why.** Requests, approvals, exceptions, and warnings
   explain the business reason and consequence, not only the current status.
5. **Distinct business stages remain distinct.** Need, approval, order,
   delivery, acceptance, invoice, payment, and management cost are related but
   never treated as interchangeable facts.
6. **History is preserved.** Approved baselines and decisions are corrected by
   explicit revision, reversal, or exception; they are never silently replaced.
7. **Attention goes to exceptions.** The normal path stays quiet while risks,
   blockers, missing evidence, and overdue decisions become visible early.
8. **Simple before clever.** The product uses the smallest understandable
   process that protects authority, evidence, and control; complexity must
   justify the decision it improves.
9. **Business behavior precedes software mechanism.** Product decisions are
   defined in business language before screens, records, automation, or
   implementation choices are authorized.

The permanent operating rules and decision contracts that apply to this
specification are maintained in [BUSINESS_RULES.md](BUSINESS_RULES.md) and
[DECISION_MODEL.md](DECISION_MODEL.md).

## Platform Relationship

ERA Construction is the first application on
[ERA SOFT Platform](../../platform/ERA_SOFT_PLATFORM.md). It owns construction
business behavior and depends only on approved platform contracts. Supported
ERPNext capabilities may fulfil those contracts after a future fit-gap and
Platform Boundary review. Construction must not depend on ERA Concrete,
Finance, Procurement, Documents, HR, Education, CRM, AI Assistant, or any other
ERA application.

The platform owns reusable mechanisms for identity, users, company context,
permission enforcement, workflow routing, notifications, files, search, audit,
reports, dashboards, AI, API, settings, localization, and the Design System.
Construction owns the project-specific meaning, business rules, decision
authority, evidence requirements, KPI semantics, report purpose, and
consequences supplied to those mechanisms.

In particular:

- platform identity is not duplicated as a Construction user model;
- platform workflow executes approved Construction decision contracts but does
  not define construction approval policy;
- platform files store and protect evidence while Construction defines what the
  evidence proves;
- platform report and dashboard engines present Construction measures while
  Construction owns their business definitions and reconciliation;
- platform audit preserves common history while Construction identifies the
  material business events and correction consequences;
- future cross-application work uses platform-mediated handoffs and remains
  functional when an optional application is absent.

## Product promise

A responsible manager can answer, without reconciling separate spreadsheets:

- what is planned and approved for each object;
- what is needed, requested, ordered, delivered, accepted, invoiced, and paid;
- what work is complete and what is blocked;
- what has been committed against the budget;
- what management cost has actually been incurred;
- what remains payable and which advances are unresolved;
- what is likely to exceed budget, schedule, or available cash;
- which source records prove every material number.

## Users

| User | Primary job in ERA Construction | Decisions supported |
|---|---|---|
| Owner / Executive | Control company and project health | cash priority, material risk, project exception, escalation |
| Construction Director | Coordinate the portfolio of objects | resource priority, schedule constraint, contractor escalation |
| Project Manager | Deliver one object within approved constraints | next work, procurement priority, budget response, acceptance |
| Site Engineer / Foreman | Organize daily work and confirm need | quantities, work readiness, material need, completion evidence |
| Cost Controller / Estimator | Maintain the management budget | budget version, coding, commitment, forecast, variance |
| Procurement Manager | Convert approved need into supply | sourcing, supplier selection, order, delivery escalation |
| Contract Manager | Control commercial terms and evidence | contract requirement, limits, validity, obligation, amendment |
| Site Storekeeper | Control materials at the object | receipt, transfer, issue, return, balance, discrepancy |
| Finance Manager / Accountant | Validate obligations and project cost | invoice evidence, payable, allocation, reconciliation |
| Treasurer / Cashier | Execute approved payments | payment priority, account, date, advance allocation |
| Auditor / Controller | Verify traceability and authority | source evidence, approval history, exceptions, reconciliation |
| System Administrator | Maintain access and reference configuration | role access, company scope, safe setup; no business approval |

One person may hold several roles in the first release. Permissions and approval
authority are assigned to roles and company/project scope, not inferred from a
job title alone. User identity, authentication, language, and application
membership belong to the platform; this specification defines only Construction
roles, scope, responsibility, and business authority.

### Daily-work readiness by primary role

The product promise is not yet sufficient to eliminate spreadsheets for the
following roles. These are business-model gaps to close before implementation,
not requests for additional approved screens.

| Role | Can daily work be performed without spreadsheets? | Exact missing business capability |
|---|---|---|
| Owner | Not yet | Approved portfolio definitions for cash, forecast, risk, and project health; risk thresholds; and accountable drill-through from each exception to a decision owner. |
| Construction Director | Not yet | A defined portfolio control cadence for schedule constraints, resource conflicts, cross-project priorities, escalation, and resolution ownership. |
| Project Manager | Not yet | A complete daily control loop covering plan, need, delivery, accepted work, budget response, forecast update, blockers, and handoff responsibility inside one object context. |
| Procurement Manager | Not yet | Approved sourcing thresholds, supplier-comparison evidence, sole-source and emergency exceptions, promised-date ownership, and escalation rules for material and service supply. |
| Finance Manager | Not yet | Approved evidence and allocation rules for invoices, advances, retentions, project cash requirements, payment priority, disputes, and reconciliation cut-off. |
| Site Engineer | Not yet | A defined field routine for daily work readiness, need quantities, received discrepancies, material consumption, measured completion, acceptance evidence, and correction responsibility. |

Business Model validation must demonstrate that each role can complete its
normal daily control cycle without a private spreadsheet. Temporary analysis
exports do not count as a parallel source of truth, but permanent shadow ledgers
do.

## Business Goals

1. Establish one authoritative operating view for every construction object.
2. Link every material purchase, service, invoice, payment, and management cost
   to an approved project context and cost purpose.
3. Show budget, commitments, actual management cost, paid cost, forecast, and
   variance without maintaining a competing shadow ledger.
4. Make project-blocking needs, deliveries, contracts, and payments visible
   before they stop work.
5. Separate material and service evidence while preserving one procurement and
   payment-control lifecycle.
6. Make responsibilities, approval limits, deadlines, and source evidence
   explicit.
7. Reduce manual spreadsheet reconciliation and duplicate data entry.
8. Provide a Russian-first, project-centered experience usable throughout the
   working day.

Quantitative targets will be set only after baseline measurements exist for
approval time, procurement lead time, delivery reliability, payment cycle,
budget reconciliation, and spreadsheet usage.

## Business Process

### End-to-end target process

```text
Project intent
  ↓
Project approval and responsible team
  ↓
Initial budget
  ↓
Approved baseline / revised budget
  ↓
Need identified at the object
  ↓
Budget and authority check
  ↓
Need approval
  ↓
Supplier / contractor selection
  ↓
Purchase order and contract when required
  ↓
Material delivery or service/work confirmation
  ↓
Warehouse receipt, transfer, issue, return, or accepted work
  ↓
Supplier invoice and obligation validation
  ↓
Payment proposal and approval
  ↓
Bank or cash payment
  ↓
Project management cost and payable reconciliation
  ↓
Budget, forecast, cash, and risk control
```

### Process rules

- A need begins with a business purpose, project context, responsible person,
  required date, and supporting quantity or scope.
- A budget check informs the decision but never silently replaces approval.
- Material and service purchases share commercial control but use different
  fulfillment evidence.
- Delivery does not equal invoice; invoice does not equal payment; payment does
  not by itself prove delivery or accepted work.
- Supplier advances remain visible until allocated to delivery, work, invoice,
  refund, or an approved exception.
- Management project cost and accounting expense are related but not assumed to
  be identical.
- Every revision preserves the approved baseline and decision history.
- Cancellations, returns, credit notes, rejected work, and payment reversals
  unwind their management consequences through explicit traceable events.

### Material path

```text
Need → approval → sourcing → order → delivery → site warehouse
→ issue / transfer / return → consumption evidence → invoice → payment
```

Required evidence includes item, quantity, unit, object, destination, delivery
date, receiver, discrepancy, and subsequent movement.

### Service and subcontractor path

```text
Scope → approval → sourcing → order / contract → work execution
→ measured or certified acceptance → invoice → payment
```

Required evidence includes scope, object and work category, period, quantity or
milestone, acceptance authority, attachments, retained amounts where applicable,
and contract relationship.

## Product Scope

### First product boundary

- construction objects and accountable teams;
- project cost structure and approved budget versions;
- needs and purchase requests;
- materials and service/subcontract procurement;
- suppliers, contractors, orders, and contract references;
- delivery and work/service acceptance;
- site warehouses and material movement;
- supplier invoices, advances, payment status, and payables;
- management project cost, commitments, paid cost, forecast, and variance;
- role-specific queues, risks, and reconciled reports;
- document attachments and decision history.

### First vertical slice candidate

```text
Project
→ approved budget
→ purchase request
→ purchase order
→ material delivery
→ supplier invoice
→ payment
→ budget vs actual reconciliation
```

The slice is a product hypothesis. It enters Data Model only after this
specification, its business process, and corresponding UX are approved.

## Main Screens

Screen names describe user decisions rather than technical records. Inventory
is provisional until the UX gate.

| Screen | Primary decision |
|---|---|
| Construction Overview | Which object or cross-project constraint needs attention first? |
| Projects | Which object should I enter, and why? |
| Project Overview | What threatens this object's cost, schedule, or work continuity? |
| Budget | What is approved, committed, actual, paid, forecast, and outside limit? |
| Needs | Which requested need is justified, timely, and within authority? |
| Procurement | Which sourcing, order, or commercial decision keeps work moving? |
| Deliveries | What is due, late, partial, rejected, or blocking the site? |
| Materials | What is available, reserved, issued, consumed, returned, or missing? |
| Work and Services | What work is planned, complete, measured, accepted, or disputed? |
| Contractors and Contracts | Which obligation, limit, expiry, or evidence requires action? |
| Payments | What should be paid, from which account, and with what consequence? |
| Documents | Which evidence belongs to the object, process, or decision? |
| Reports | Which reconciled view supports control, review, or audit? |

No screen is authorized for implementation until its decision brief, state set,
source map, and mockup are approved.

Documents, photos, dashboards, and reports use shared platform services and UI
components. Their project context, evidence meaning, KPI definition, and
decision purpose remain owned by Construction.

## Navigation

### Project-centricity assessment

The approved navigation is project-centric once an object is selected and does
not require redesign. The product-level destinations remain necessary for roles
that manage cross-project queues, including procurement, finance, and portfolio
leadership.

To preserve project-centric behavior, project and site roles should start in
their assigned or most recent object; the selected object must persist across
relevant destinations; contextual actions must inherit that object; and any
cross-project queue or action must be clearly identified as such. These are
navigation behavior requirements, not changes to the approved menu or UX.

### Construction product level

The first level contains no more than seven primary destinations:

```text
Обзор
Объекты
Бюджеты
Закупки
Поставки
Финансы
Отчеты
```

Rare setup, master data, contracts, documents, and administration remain
available through context or **Ещё**, according to role.

### Inside a project

```text
Обзор
Бюджет
Закупки
Материалы
Работы
Оплаты
Ещё
```

**Ещё** may reveal contracts, contractors, documents, photos, analytics, and
project settings. The selected company and object remain visible throughout.

### Progressive disclosure

```text
Construction area
→ project or business queue
→ subgroup requiring attention
→ source records
→ one decision
```

Frequent work should be reachable in no more than three navigational actions,
without removing required safety review or confirmation.

## KPIs

This is a candidate metric inventory, not an approved calculation catalogue.
The table assigns business accountability and the minimum business inputs for
each metric. It deliberately does not define formulas. Every metric still
requires an approved data contract before Data Model or implementation.

| KPI | Business owner | Decision supported | Required inputs |
|---|---|---|---|
| Physical progress | Project Manager | Is the object advancing as expected, and where is recovery action required? | approved progress method; work scope and weights; accepted progress evidence; reporting cut-off; accountable update |
| Initial budget | Cost Controller / Estimator | What cost baseline did leadership originally authorize? | approved baseline; scope boundary; cost classification; currency; approval date and authority |
| Revised budget | Cost Controller / Estimator | What cost limit is currently authorized, and what changed? | initial baseline; approved revisions; change reasons; effective dates; approval authority |
| Committed cost | Cost Controller / Estimator | What future cost has been commercially committed, and where is budget capacity constrained? | approved commercial obligations; amendments; cancellations; project and cost context; effective dates |
| Actual management cost | Finance Manager / Accountant | What value has been consumed or accepted for the object? | accepted material consumption; accepted service or work; returns and corrections; project and cost context; reporting cut-off |
| Paid cost | Finance Manager / Accountant | How much object-related cash has left controlled accounts, and where was it allocated? | completed payments; reversals; allocations; company and project context; payment date |
| Forecast at completion | Project Manager | Is the object expected to finish within the current authorized budget? | current approved budget; actual and committed position; remaining scope; current estimates; assumptions; confidence and update date |
| Budget variance | Cost Controller / Estimator | Which part of the object requires corrective action or an authorized revision? | approved comparison baseline; current actual, commitment, and forecast facts; project cost structure; decision thresholds |
| Payables | Finance Manager / Accountant | What remains owed, disputed, retained, or due, and when? | validated obligations; due terms; payments and allocations; advances; retentions; disputes; reporting date |
| Unresolved advances | Finance Manager / Accountant | Which advance cash lacks completion evidence, allocation, or recovery action? | advance approvals and payments; supporting evidence; allocations; refunds; responsible owner; due and ageing dates |
| Delivery reliability | Procurement Manager | Which supplier or supply risk threatens planned work? | promised dates and quantities; accepted, partial, rejected, and outstanding delivery facts; required-on-site dates; supplier responsibility |
| Site material balance | Site Storekeeper | Is required material available, located, and accounted for at the object? | accepted receipts; transfers; reservations; issues; consumption; returns; discrepancies; cut-off and responsible custodian |
| Cash requirement | Finance Manager | What cash is required to maintain approved work over the selected horizon? | approved work priorities; due and expected obligations; planned advances; available cash; payment constraints; horizon and scenarios |
| Approval ageing | Construction Director | Which internal decision delay is blocking execution and who must act? | request and decision timestamps; current decision owner; due rule; pause reason; escalation threshold; final outcome |

## Permissions

The platform owns identity and permission-enforcement mechanisms. ERA
Construction owns the following business access, visibility, authority, and
segregation requirements.

### Principles

- Access is constrained by company, project, role, and document state.
- Financial amounts, salaries, owner transactions, bank accounts, and restricted
  contracts receive explicit permission rules.
- Approval authority is server-enforced and versioned; visibility does not imply
  authority.
- A user cannot approve their own request where segregation of duties requires
  independent review.
- High-impact decisions show source evidence and consequence before
  confirmation.
- Audit history is append-only from the user's perspective.

### Draft permission responsibilities

| Role | Typical view scope | Typical action scope |
|---|---|---|
| Owner / Executive | all permitted companies and projects | executive decisions within approved limits |
| Construction Director | construction portfolio | prioritize, escalate, approve assigned levels |
| Project Manager | assigned projects | request, coordinate, accept assigned work, forecast |
| Site Engineer / Foreman | assigned object and work areas | create need, confirm progress and field evidence |
| Cost Controller | assigned project budgets and costs | classify, revise proposal, reconcile, forecast |
| Procurement Manager | approved needs and commercial records | source, recommend, order within authority |
| Contract Manager | permitted counterparties and contracts | prepare, verify, amend within authority |
| Storekeeper | assigned warehouses and movements | receive, transfer, issue, return, record discrepancy |
| Finance Manager / Accountant | financial and source evidence in scope | validate invoice, allocate, reconcile |
| Treasurer / Cashier | approved payment queue and permitted accounts | prepare and execute authorized payment |
| Auditor / Controller | read-only evidence and history | review, comment, report exception |
| Administrator | system configuration without business authority | maintain access and reference configuration |

Exact limits, substitutions, temporary delegation, and segregation rules are P0
business decisions.

## Reports

### Decision reports

- Portfolio Project Health;
- Project Budget vs Committed vs Actual vs Paid vs Forecast;
- Budget Variance by project, block, work category, and cost category;
- Procurement Lifecycle by project and required date;
- Ordered vs Delivered vs Invoiced vs Paid;
- Overdue and At-Risk Deliveries;
- Site Inventory and Material Movement;
- Material Consumption by project and work category;
- Contractor Work Accepted vs Invoiced vs Paid;
- Supplier and Contractor Advances;
- Project Payables and Payment Calendar;
- Project Cash Requirement;
- Approval Ageing and Bottlenecks;
- Source Reconciliation and Exception Report.

Reports are not authorized until their decision owner, formula, filters,
permissions, freshness, drill-through, and reconciliation evidence are approved.
Rendering, filtering, export, scheduling, access enforcement, and source
navigation are platform-service responsibilities; report meaning and
reconciliation remain Construction responsibilities.

## Future Scope

- detailed work scheduling and earned-value methods;
- tender comparison and supplier performance scoring;
- equipment, machinery, fuel, and maintenance control;
- labor attendance, piecework, payroll allocation, and productivity;
- quality inspections, defects, warranty, and handover;
- safety incidents and compliance;
- BIM, drawing, revision, and document-control integrations;
- mobile/offline site workflows after a validated field-use case;
- customer/developer sales and unit handover;
- Construction AI assistance only through the governed platform AI service and
  only after permissions and source evidence are reliable.

Future scope does not enter UX, Data Model, or implementation merely because it
is listed here.

## Out of Scope

- modifying Frappe or ERPNext core;
- replacing proven accounting, buying, stock, project, or HR engines without an
  approved fit-gap decision;
- tax and statutory accounting localization in the Construction MVP;
- a complete BIM, CAD, scheduling, document-management, or payroll system;
- decorative executive analytics without decision and reconciliation contracts;
- autonomous approvals, payments, accounting postings, or stock movements;
- production-data migration before source audit and migration approval;
- building all Construction capabilities in one release;
- custom UI or DocTypes before the corresponding product gates are approved.

## Open Decisions

### P0 — blocks Business Model approval

1. Confirm product owner and named process owners.
2. Confirm the target project lifecycle from project intent to closeout.
3. Confirm the project hierarchy: project, site, building/block, floor, work
   category, and cost category.
4. Confirm initial and revised budget approval authority.
5. Confirm what event creates, changes, and cancels committed cost.
6. Confirm management actual-cost recognition for materials and services.
7. Confirm the physical-progress method and accountable updater.
8. Confirm material and service acceptance evidence.
9. Confirm purchase, contract, invoice, and payment approval limits.
10. Confirm supplier advance, retention, and unresolved-balance rules.
11. Confirm role segregation and company/project visibility.
12. Confirm the smallest real pilot project and responsible operational team.
13. Confirm project closeout criteria and authority for accepted residual
    obligations, stock, advances, claims, and missing evidence.
14. Confirm emergency purchase, budget-exception, and policy-exception rules,
    including who may authorize them and how they are later resolved.

### P1 — required before UX approval

1. Rank the daily decisions for each primary user.
2. Confirm Construction and project-level navigation.
3. Confirm required normal and exception states for each screen.
4. Confirm Russian names for need, acceptance, work stage, advance, retention,
   commitment, forecast, and variance.
5. Confirm the maximum useful density for site, procurement, and finance roles.
6. Validate the daily-work readiness gaps with named representatives of the six
   primary roles before approving screen briefs.

## Future Data Model Gate

Only after Business Model, UX, and UI approval will engineering map this product
to ERPNext reuse, extension, or custom records. The existing construction
architecture pack is input to that future decision; it does not override this
product specification.

The future mapping must also pass the Platform Boundary review: it may reuse
Core Platform Services but must not duplicate them or introduce a dependency on
another ERA application.

No DocType, relationship, permission implementation, report query, workflow, or
migration is authorized by this draft.

## Approval Record

| Gate | Status | Required approvers | Evidence |
|---|---|---|---|
| Idea | accepted: Construction is first ERA SOFT product | Product owner | product strategy direction |
| Business Model | draft | Product owner and named process owners | this specification, business rules, decision model, and review report |
| UX | not started | Product owner and primary users | screen inventory, flows, states, mockups |
| UI | not started | Product and design-system owners | approved compositions and components |
| Data Model | blocked | Engineering and process owners | fit-gap, entity model, permissions, data contracts |
| Implementation | blocked | Product and process owners | approved vertical slice and acceptance scenarios |
