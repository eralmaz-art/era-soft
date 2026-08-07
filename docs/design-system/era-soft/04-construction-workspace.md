# Construction Workspace UX

Status: **Concept for approval; no implementation authorized**

## Decision

The Construction Workspace makes the selected object—not the ERP module—the
stable working context. For **EcoCity Ayni**, a project manager should understand
progress, budget exposure, commitments, deliveries, payments, and current risks
without mentally joining records across separate modules.

## Object shell

```text
Строительство / EcoCity Ayni
EcoCity Ayni · В работе · Руководитель · Updated time

Обзор | Бюджет | Закупки | Договоры | Материалы
Подрядчики | Оплаты | Документы | Фото | Аналитика
```

The object name, status, company, and responsibility remain visible as users move
between sections. Global navigation stays available but visually secondary.

## Overview information hierarchy

1. **Decision strip:** physical progress, approved budget position, and current
   amount requiring payment or approval.
2. **Exceptions:** budget, schedule, supply, quality, contract, and payment risks.
3. **Work structure:** blocks and major work categories with progress and
   blocking state.
4. **Near-term operations:** upcoming deliveries, procurement decisions, and
   payment dates.
5. **Recent evidence:** documents and dated site photos.

The overview does not duplicate every tab. It shows only information that
changes a project decision and links to the responsible section.

## Local sections

| Section | Primary decision | Authoritative source direction |
|---|---|---|
| Обзор | What requires attention now? | reconciled summaries and source links |
| Бюджет | Where are commitments/actuals/forecast outside plan? | approved ERA budget versions plus ERPNext transactions |
| Закупки | What must be sourced, approved, received, or escalated? | Material Request, RFQ, Purchase Order, Purchase Receipt |
| Договоры | Which terms, limits, obligations, or dates require action? | ERPNext Contract plus approved ERA extensions |
| Материалы | What is on site, in transit, reserved, or consumed? | Warehouse and Stock Entry ledger records |
| Подрядчики | Who is responsible, contracted, accepted, or overdue? | Supplier/Contractor profile and contracts |
| Оплаты | What is invoiced, proposed, paid, advanced, or payable? | Purchase Invoice, Payment Entry, ledger and allocations |
| Документы | Which evidence supports the object? | attached source documents with metadata |
| Фото | What dated visual evidence exists by block/work? | approved attachment/photo metadata model |
| Аналитика | What trend or variance changes a decision? | reconciled reports with definitions |

## Budget view contract

The visible management row follows the approved architecture:

```text
Уточненный бюджет
- Принятые обязательства
- Фактическая себестоимость
- Оплаченная себестоимость
= Остаток / потребность / прогноз / отклонение
```

Actual and paid are distinct views of the same authoritative transactions, not
separate editable cost ledgers. Users can analyze by object, block, type of work,
cost category, supplier/contractor, material, date, and payment state.

## Procurement inside an object

The interface keeps one business flow visible:

```text
Потребность -> Заявка -> Согласование -> Заказ -> Приемка
-> Счет поставщика -> Оплата -> Себестоимость объекта
```

Materials and services share the decision structure but use appropriate
acceptance evidence. A service is never shown as “delivered to warehouse”.

## Context and navigation rules

- Object context is carried in links and filters; it is never inferred only from
  the last visited page.
- A create action opened within an object pre-fills the object but still shows it
  before submission.
- Cross-object lists clearly show the object column.
- Returning from a record restores the previous object tab and filter state.
- Roles see the same object language but different actions and protected values.
- Generic ERPNext pages remain available for administration and deep inspection,
  not as the default project-manager journey.

## First approved screen sequence

The smallest implementation candidate after Phase 3 approval is:

1. object overview shell with read-only reconciled summary;
2. budget view with source drill-through;
3. object-scoped procurement list and create path;
4. delivery, invoice, and payment state on one traceable purchase chain.

No screen in this sequence is ready for implementation until its data contract,
permissions, states, and detailed mockup pass the review gate.
