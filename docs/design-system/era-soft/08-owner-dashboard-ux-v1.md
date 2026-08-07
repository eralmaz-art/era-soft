# Owner Dashboard — UX mockup v1

Status: **Superseded by dashboard suite UX v2; retained for decision history**  
Screen: **Главная**  
Primary user: owner / chief executive  
Mockup version: **1.0**  
Data: **illustrative only**

## Decision brief

- **Decision accelerated:** understand within ten seconds whether cash is
  sufficient and which project, payment, delivery, or contract needs the
  owner's decision first.
- **Context:** one company or consolidated ERA Group scope, current business
  day, Russian interface.
- **Primary action:** open the highest-materiality risk and its source records.
- **Secondary actions:** open a project overview or a filtered queue for today.
- **Explicit exclusions:** accounting document creation, inline approval,
  decorative charts, unexplained KPIs, forecasts without approved formulas,
  and autonomous narrative.

## Proposed information hierarchy

```text
Global navigation
└── Главная
    ├── Greeting, company scope, freshness
    ├── Available cash
    │   ├── Due today
    │   └── Seven-day cash requirement
    ├── Projects
    │   └── Progress plus one named exception
    ├── Today
    │   ├── Approvals
    │   ├── Payments
    │   ├── Purchases
    │   └── Deliveries
    └── Risks ordered by materiality and deadline
```

The initial viewport must show available cash, all project rows, today's queue,
and at least the beginning of the ranked risk list without competing KPI cards.

## Interaction contract

- Company scope is selected in the header and remembered per user.
- Every monetary value states currency, period, and refresh time.
- A cash value opens its reconciled account composition; it does not open a
  generic accounting module.
- A project row opens that object's **Обзор** and preserves the selected company
  scope on return.
- Today's counts open exact filtered source lists.
- The leading risk is the only visually primary action in the risks section.
- High-impact approval is never completed directly from this dashboard.

## Responsive behavior

- At 1280–1440 px the content uses a calm two-column reading rhythm after the
  cash summary.
- Below 900 px the navigation collapses and all decision sections stack.
- At 320–767 px cash remains first, project rows retain names and percentages,
  and supporting metadata moves below rather than truncating the decision.
- No horizontal scrolling is permitted.

## Required states

| State | Behavior |
|---|---|
| Normal | Current values, quiet operations, ranked exceptions |
| Loading | Preserve layout; never display temporary zero values |
| Empty | Explain that no source records match the company/period |
| Stale | Show last successful update and one **Обновить данные** action |
| Error | Keep last known values visibly stale and provide reference ID |
| Permission denied | Hide protected amounts and name the role that can grant access |
| Partial source coverage | Identify missing accounts/projects beside freshness |

## Data contracts blocking implementation

1. Definition of **Доступные денежные средства**, including restricted funds,
   pending bank transactions, cash accounts, currency, and consolidation.
2. Definition of **К оплате сегодня** and treatment of overdue invoices,
   advances, proposed payments, and unposted documents.
3. Approved seven-day cash-requirement horizon and source documents.
4. Physical project-progress method and responsible data owner.
5. Budget variance threshold and whether committed, actual, forecast, or paid
   cost drives the exception.
6. Risk materiality, urgency, deduplication, ownership, and dismissal rules.
7. Exact ERPNext reports/DocTypes behind every drill-through.

## Approval record

- Product owner: **pending**
- Process owner: **pending**
- Information hierarchy: **pending**
- Visual direction: **pending**
- KPI definitions: **blocked by business decisions above**
- Implementation authorization: **not granted**

## Supersession

Product review kept the decision order—cash, projects, today, risks—but rejected
the widget-dashboard treatment. The replacement is documented in
`09-dashboard-suite-ux-v2.md` and uses a company-control-center model, four
leading financial values, larger project cards, explicit risk semantics, and
progressive disclosure.
