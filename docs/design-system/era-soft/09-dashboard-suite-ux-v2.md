# ERA SOFT dashboard suite — UX v2

Status: **Product hierarchy and visual direction approved; not approved for implementation**  
Version: **2.0**  
Data: **illustrative only**  
Implementation: **explicitly excluded**

## Product model

These screens are company control surfaces, not collections of ERP widgets.
They share one information rhythm:

```text
Context and freshness
→ four decision-critical numbers
→ domain state
→ today's actions
→ ranked exceptions
→ authoritative source record
```

Progressive disclosure follows the product rule **10 → 5 → 2 → 1**. Global
navigation reveals a domain, the domain reveals a small group, the group reveals
the relevant queue, and the queue ends at one concrete record or decision.

## Shared shell

- Russian greeting, date, time, company scope, and data freshness.
- Seven to nine role-relevant global destinations; rare setup is secondary.
- Graphite reading hierarchy, Deep Green selection, quiet surfaces, and semantic
  risk color only.
- No unexplained KPI, decorative chart, or direct high-impact approval.
- Every count and amount drills into the exact records behind it.

## 1. Owner Dashboard — Главная v2

**Primary decision:** is the company financially safe today, and what requires
the owner's decision first?

### First view

1. Four large unframed values: **Денежные средства**, **Дебиторская
   задолженность**, **Кредиторская задолженность**, **Свободный денежный поток**.
2. Large project cards containing physical progress, budget, actual, variance,
   next payment, and one named risk.
3. Collapsed **Сегодня** groups: payments, deliveries, contracts, and tasks.
4. Risks grouped by explicit semantic state: **Нет проблем**, **Требует
   внимания**, **Решить сегодня**.

Today's groups reveal records only after selection. The first render does not
show the records and the group counts simultaneously.

### Blocking decisions

- available cash and free-cash-flow formulas;
- receivable/payable posting and overdue semantics;
- consolidated currency policy;
- project physical-progress method;
- project variance and risk thresholds.

## 2. Finance Dashboard — Финансы v1

**Primary decision:** which liquidity or payment action protects the company
over the selected horizon?

### First view

1. Available cash, expected receipts, approved payments, and projected closing
   balance.
2. One cash movement view across the approved horizon.
3. Receivables and payables summarized by due state, not by accounting module.
4. A ranked payment queue with source, consequence, and safe next action.

Selecting a financial measure reveals its composition; selecting a due-state
reveals counterparties; selecting a counterparty reveals invoices and payments.

### Blocking decisions

- bank/cash accounts included in liquidity;
- payment proposal and approval semantics;
- treatment of advances, credits, unallocated payments, and draft documents;
- forecast horizon and confidence policy;
- access to salaries, owners, and restricted accounts.

## 3. Project Dashboard — Объект v1

**Primary decision:** what threatens the selected object's cost, schedule, or
work continuity, and which action removes the constraint?

### First view

1. Object identity, accountable manager, physical progress, and freshness.
2. Budget, committed cost, actual cost, forecast, and named variance.
3. Current construction stages with one selected stage detail.
4. Today's site events and the highest-materiality constraint.
5. Local navigation: **Обзор**, **Бюджет**, **Закупки**, **Материалы**,
   **Оплаты**, **Ещё**. Secondary sections open inside **Ещё**.

Selecting a stage reveals its budget, actual, completion, contractor, and next
constraint. The user never leaves the object context.

### Blocking decisions

- block/stage hierarchy and progress ownership;
- management-cost recognition rules;
- committed, actual, paid, and forecast cost definitions;
- schedule baseline and variance threshold;
- stage-to-budget and stage-to-procurement relationships.

## 4. Procurement Dashboard — Закупки v1

**Primary decision:** which request, order, delivery, invoice, or payment is
blocking project work or creating avoidable cash exposure?

### First view

1. Requests awaiting decision, ordered amount, due deliveries, and supplier
   exposure.
2. One lifecycle: **Заявки → Заказы → Поставки → Счета → Оплаты**.
3. Selected stage detail with the few records requiring action.
4. Supplier and project exceptions ranked by work impact and deadline.

Selecting a lifecycle stage reveals its subgroups; selecting a subgroup reveals
the source records. Materials and services share the lifecycle but retain
different confirmation evidence.

### Blocking decisions

- purchase-request terminology and approval levels;
- material versus service confirmation rules;
- committed-cost event and cancellation/revision behavior;
- delivery-delay and supplier-exposure definitions;
- contract requirement thresholds and advance allocation.

## States required before implementation

Each screen must show normal, loading, empty, stale, partial-data, error,
offline, and permission-denied states. High-impact decisions must also show the
source evidence, consequence, attachments, and audit trail before confirmation.

## Approval record

| Area | Product hierarchy | Visual direction | KPI/data contracts | Implementation |
|---|---|---|---|---|
| Owner | approved 2026-08-08 | approved 2026-08-08 | blocked | not authorized |
| Finance | approved 2026-08-08 | approved 2026-08-08 | blocked | not authorized |
| Project | approved 2026-08-08 | approved 2026-08-08 | blocked | not authorized |
| Procurement | approved 2026-08-08 | approved 2026-08-08 | blocked | not authorized |

Approval accepts this iteration as the product-foundation direction. It does
not approve illustrative values, KPI formulas, data sources, permissions, or
implementation. Each dashboard must pass its product and data gates before it
can enter code.
