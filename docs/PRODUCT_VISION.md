# Product Vision

## North star

> Создание единой модульной операционной платформы для ERA Group.

ERA SOFT is not a construction ERP. It is the modular operating platform for
ERA Group. ERA Construction is its first application; Concrete, Education,
Finance, HR, Procurement, CRM, Documents, AI Assistant, and future products can
join as independent applications without redesigning Construction or each
other.

The platform should feel like one ERA product across ERA companies and future
businesses even though Frappe and ERPNext provide the current technical
foundation. Shared identity, permissions, files, audit, notifications, search,
reports, dashboards, localization, and interface patterns belong to the
platform. Business logic remains inside the application that owns the outcome.

The product is not framed internally as “ERP development.” The operating system
ambition sets the quality bar for decisions, interaction speed, trust,
architecture, language, and visual consistency.

## Product promise

An authorized owner or manager can understand cash, obligations, sales,
production, and project health without reconciling disconnected spreadsheets or
waiting for a manually assembled report.

## Experience principles

- ERA language and business processes, not framework terminology.
- Every screen must help a named user make a named decision faster.
- One authoritative record for every material business event.
- Desktop-first, responsive, fast, and visually quiet.
- Graphite typography, Deep Green accents, calm light surfaces, strict hierarchy,
  and generous whitespace create one recognizable ERA product.
- No unnecessary actions; the next operational step is obvious.
- Any owner KPI is reachable within two interactions.
- Operational entries create financial and project consequences automatically.
- Exceptions demand attention; normal work stays calm.
- UX brief, mockup, and approval precede user-facing implementation.

## Product surface

```text
ERA SOFT
├── Construction — first application
├── Concrete
├── Education
├── Finance
├── Procurement
├── HR
├── CRM
├── Documents
├── AI Assistant
└── Future applications
```

Applications are peers. They depend on ERA SOFT Platform services and never on
one another. The governing boundary is defined in
[ERA SOFT Platform Architecture](platform/ERA_SOFT_PLATFORM.md).

The five-to-ten-year choices, product boundaries, feature admission standard,
and vertical-slice strategy are defined in
[ERA SOFT Product Strategy](PRODUCT_STRATEGY.md).

## Initial users

- owner / executive;
- concrete plant dispatcher and operator;
- construction project manager and site storekeeper;
- procurement manager;
- management accountant / cashier;
- sales and receivables manager;
- system administrator.

Each role receives a task-oriented workspace. Direct access to generic ERPNext
workspaces remains available to administrators during implementation, but is not
the target daily experience.

## Success measures

Baselines must be measured before targets are fixed. The first useful measures
are:

- time from concrete order confirmation to dispatch;
- percentage of deliveries with complete order, batch, mixer, driver, and site
  traceability;
- time to produce a current receivables and cash position;
- percentage of project purchases linked to budget and cost center;
- variance between planned and actual material cost;
- executive dashboard data freshness;
- number of operational spreadsheets retired.

## Out of scope for the first release

- tax accounting and statutory localization;
- replacing proven ERPNext accounting, buying, selling, stock, HR, or project
  models;
- AI automation before source data and permissions are reliable;
- independent mobile apps;
- customer-facing portals unless a validated workflow requires one.
