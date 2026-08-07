# Master Roadmap

The roadmap is outcome-based. A phase exits only when its evidence is accepted;
code volume is not an exit criterion.

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

## Phase 3 — ERA SOFT design system (current)

Define the visual foundations, reusable component behavior, product navigation,
data-visualization rules, Owner Dashboard experience, Construction Workspace
experience, and the UX-before-code governance gate. Validate concepts before
changing the production Frappe interface.

Exit evidence: approved design tokens and component rules, approved Owner
Dashboard and construction-object mockups, resolved P0 design questions, and a
screen-review gate applied to the first implementation backlog.

## Phase 4 — Existing ERA software audit

Inventory the existing frontend, backend, database, authentication, reports,
integrations, and live data. Map every capability and field to an ERPNext or ERA
SOFT destination. No migration design proceeds without data profiling.

Exit evidence: repository/system access, module comparison, data-quality report,
and migration disposition for every source table.

## Phase 5 — ERP foundation

Configure companies, roles, permissions, parties, items, warehouses, bank and
cash accounts, chart of accounts, cost centers, and projects. Avoid domain code.

Exit evidence: approved role matrix and end-to-end standard purchase, sale,
stock, payment, and project-cost scenarios.

## Phase 6 — ERA Construction implementation

Deliver the approved vertical slice: Project, budget version, purchase request,
purchase order, material/service acceptance, invoice, payment and reconciled
Budget vs Actual. Expand to contracts, forecasting and labor only after the
pilot evidence is accepted.

Exit evidence: a pilot project reports approved budget, commitments, delivered
and consumed material, actual, paid, forecast and warehouse balances from
authoritative records without a shadow cost ledger.

## Phase 7 — ERA Concrete

Deliver in vertical slices after the ERA Construction priority: order-to-dispatch,
batch traceability, mixer/driver assignment, delivery-to-invoice, cost, then
operational reports and KPIs.

Exit evidence: one plant can execute a full day from confirmed orders through
reconciled deliveries and management reporting without shadow spreadsheets.

## Phase 8 — Management finance

Deliver cash/bank, receivable/payable, cash-flow, profitability, and management
reports on top of ERPNext ledgers. Tax accounting is explicitly deferred.

Exit evidence: management closes an agreed reporting period and reconciles every
headline number to source transactions.

## Phase 9 — Executive dashboard

Expose cash, bank, receivables, payables, today's sales, concrete volume, project
health, leading counterparties, profit, and cash forecast with drill-through.

Exit evidence: each KPI has an owner, formula, freshness target, permission rule,
and reconciliation test; all priority KPIs are reachable within two actions.

## Phase 10 — AI

Add OCR, document understanding and generation, assistant interactions, voice,
analytics, and forecasting only after source data, permissions, and evaluation
sets are production-ready.

Exit evidence: each use case has measured quality, human review, audit history,
and a failure path that cannot silently post financial or stock transactions.
