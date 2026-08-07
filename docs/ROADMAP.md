# Master Roadmap

The roadmap is outcome-based. A phase exits only when its evidence is accepted;
code volume is not an exit criterion.

## Phase 0 — Foundation (current)

- establish the ERA SOFT custom application repository;
- adopt supported Frappe/ERPNext version boundaries;
- document product, architecture, contribution, and upgrade rules;
- create repeatable local setup and repository checks.

Exit evidence: clean install of `era_soft` next to ERPNext on a disposable site,
passing repository checks, and an accepted architecture decision.

## Phase 1 — ERPNext study and fit-gap

Study real workflows in Selling, Buying, Accounts, Manufacturing, Projects,
Stock, CRM, and HR. Build scenario fixtures, not only feature inventories.

Exit evidence: approved capability map with `configure`, `extend`, `build`, or
`defer` decisions and named process owners.

## Phase 2 — Existing ERA software audit

Inventory the existing frontend, backend, database, authentication, reports,
integrations, and live data. Map every capability and field to an ERPNext or ERA
SOFT destination. No migration design proceeds without data profiling.

Exit evidence: repository/system access, module comparison, data-quality report,
and migration disposition for every source table.

## Phase 3 — ERP foundation

Configure companies, roles, permissions, parties, items, warehouses, bank and
cash accounts, chart of accounts, cost centers, and projects. Avoid domain code.

Exit evidence: approved role matrix and end-to-end standard purchase, sale,
stock, payment, and project-cost scenarios.

## Phase 4 — ERA Concrete

Deliver in vertical slices: order-to-dispatch, batch traceability, mixer/driver
assignment, delivery-to-invoice, cost, then operational reports and KPIs.

Exit evidence: one plant can execute a full day from confirmed orders through
reconciled deliveries and management reporting without shadow spreadsheets.

## Phase 5 — ERA Construction

Deliver budget versions, requests and commitments, site warehouses and material
consumption, contracts, actual cost, budget variance, and project cash flow.

Exit evidence: a pilot project reports approved budget, commitments, actuals,
forecast, and warehouse balances from authoritative records.

## Phase 6 — Management finance

Deliver cash/bank, receivable/payable, cash-flow, profitability, and management
reports on top of ERPNext ledgers. Tax accounting is explicitly deferred.

Exit evidence: management closes an agreed reporting period and reconciles every
headline number to source transactions.

## Phase 7 — Executive dashboard

Expose cash, bank, receivables, payables, today's sales, concrete volume, project
health, leading counterparties, profit, and cash forecast with drill-through.

Exit evidence: each KPI has an owner, formula, freshness target, permission rule,
and reconciliation test; all priority KPIs are reachable within two actions.

## Phase 8 — AI

Add OCR, document understanding and generation, assistant interactions, voice,
analytics, and forecasting only after source data, permissions, and evaluation
sets are production-ready.

Exit evidence: each use case has measured quality, human review, audit history,
and a failure path that cannot silently post financial or stock transactions.
