# Owner Dashboard UX

Status: **Concept for approval; figures are illustrative**

## Decision

The Owner Dashboard helps the owner answer, in this order:

1. How much usable cash is available now?
2. Which projects, payments, supplies, or contracts need attention today?
3. Is any object materially outside budget or schedule?
4. What source records explain the number or risk?

It is not a general analytics catalogue and does not replace finance or project
reports.

## Information hierarchy

```text
ERA SOFT / greeting / freshness
├── Cash position and near-term requirement
├── Projects: progress plus one meaningful exception
├── Today: approvals, payments, purchases, and deliveries
└── Risks: ranked exceptions with owner and next action
```

### Header

- Greeting: **Добрый день, Алмаз.**
- Scope: selected company or consolidated ERA Group.
- Freshness: last successful update and source coverage.
- One global action only when needed, such as **Обновить данные** after a stale
  or failed refresh.

### Cash

The leading number is **Доступные денежные средства**, not an unexplained
“Cash”. Its definition must identify included bank/cash accounts, restricted
funds, pending transactions, company scope, currency, and refresh time.

Supporting context may show **К оплате сегодня** and a short-horizon cash need,
but the page does not show every balance as an equal KPI.

### Projects

Each row shows:

- object name and responsible manager;
- approved physical progress method;
- budget state: within limit or named variance;
- schedule or supply exception when one exists;
- direct transition into the object's **Обзор**.

Progress percentages are not accepted until the measurement source is defined:
task-weighted, work-volume, certified completion, cost-earned, or another agreed
method.

### Today

Today's queue groups actionable items, not documents by technical type:

- approvals awaiting the owner;
- payments due or proposed;
- purchase decisions;
- deliveries affecting today's work.

Every count opens a filtered authoritative list. A zero count is quiet and does
not become a celebratory card.

### Risks

Risks are ordered by materiality and time sensitivity. A risk line contains:

- plain-language issue;
- object or counterparty;
- financial/time exposure where known;
- accountable owner;
- deadline and next safe action;
- drill-through to source evidence.

Examples in the concept—overdue supplier, budget overrun, contract requiring
payment—are placeholders, not final risk logic.

## Interaction model

- Clicking a project opens the object overview and preserves owner context in the
  back path.
- Clicking a number opens the exact filtered records used to calculate it.
- Approvals can be reviewed from the dashboard, but high-impact approval still
  shows source, consequence, attachments, and audit trail before confirmation.
- The dashboard remembers company scope per user, not globally.
- Keyboard order follows visual importance: cash, risks, today's decisions,
  projects, supporting navigation.

## Data contract required before implementation

For every KPI or risk: Russian name, decision owner, formula, source DocTypes,
company and currency rules, posting-date semantics, update frequency, permission
rule, drill-through route, reconciliation test, and failure/stale behavior.

## Explicit exclusions for the first version

- decorative charts without a decision;
- leaderboards or vanity metrics;
- AI-generated narrative without cited source records;
- consolidated multi-currency totals without an approved translation policy;
- inline editing of accounting transactions;
- live operational animation.
