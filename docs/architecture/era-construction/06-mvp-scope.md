# ERA Construction MVP Scope

## MVP outcome

One pilot Project can execute and reconcile this vertical slice without a
shadow budget spreadsheet:

```text
Project
  -> approved versioned Budget
  -> approved Purchase Request
  -> Purchase Order
  -> material/service delivery
  -> Purchase Invoice
  -> Payment
  -> Budget vs Actual and procurement/payment drill-down
```

The MVP proves source-of-truth, dimensions, workflow and reconciliation. It is
not the complete construction product.

## In scope

### Standard ERPNext configuration

- one pilot Company and fiscal/calendar/currency policy;
- one Project with Project user access;
- Cost Center hierarchy down to block (floor only if approved);
- direct-cost/CWIP Account hierarchy;
- Supplier/Supplier Group governance, including contractor classification;
- material and non-stock service Items with controlled UOM;
- central/site Warehouse hierarchy;
- bank/cash/payable/stock-clearing accounts and Modes of Payment;
- standard MR → RFQ/SQ optional → PO → Receipt → PI → Payment mappings;
- Material Transfer and Material Issue;
- ERPNext Budget control envelopes where eligible;
- role permissions, User Permissions and request/order workflows.

### Minimal ERA-owned schema

Only these custom DocTypes are proposed for the first implementation review:

1. `ERA Work Category` — small tree master used as Accounting Dimension.
2. `ERA Construction Budget` — approved version header.
3. `ERA Construction Budget Line` — child rows at construction cost grain.

No other custom transaction DocType is in the MVP. Standard DocTypes receive
only reviewed fixtures/custom fields such as Budget Line, contract/project links
and site defaults.

### Reports

1. **ERA Budget vs Actual**
   - Initial and Current Budget;
   - Requested, Total/Open Committed, Delivered, Invoiced;
   - Actual, Paid, Remaining, System Forecast and Variance;
   - Project > Block > Work Category > Account > Item/Budget Line drill-down;
   - explicit Unbudgeted/Missing Dimension bucket;
   - reconciliation footer.
2. **ERA Procurement and Payment Control**
   - request/order/receipt/invoice/payment chain;
   - supplier, due date, advance, outstanding and payment status;
   - links to standard source documents.
3. Standard ERPNext reports remain available for AP, GL, Stock Balance, Stock
   Ledger, Purchase Analysis and accounting Cash Flow.

### Material scenario

The pilot must demonstrate:

1. approved rebar budget line for Block A/Foundation;
2. Material Request from that line;
3. mapped PO and supplier selection evidence;
4. Purchase Receipt into Block A/site warehouse;
5. optional central-to-site transfer if central receipt is used;
6. Material Issue to Block A/Foundation;
7. mapped Purchase Invoice and supplier payable;
8. partial/full Payment Entry;
9. correct ordered/delivered/stock/consumed/invoiced/paid amounts without double
   counting.

### Service scenario

The pilot must also demonstrate:

1. non-stock subcontract service budget line;
2. request and mapped PO;
3. optional Contract registry/link;
4. authorized acceptance using a non-stock Purchase Receipt;
5. mapped PI and Payment Entry;
6. commitment, actual, payable and paid cost at the same dimensions.

## Out of scope

- complete contract BOQ, variation, retention, claims and progress certificates;
- bid-scoring portal or supplier portal redesign;
- custom Project Cost or cash ledger;
- payroll and labor allocation from HRMS;
- equipment utilization and depreciation allocation;
- floor/BIM/spatial model unless approved as essential for the pilot;
- manual approved ETC/forecast snapshots;
- executive dashboard or large custom workspace;
- mobile/offline site application;
- production data migration;
- tax/localization redesign;
- ERA Concrete features;
- Frappe or ERPNext core changes.

## Proposed implementation increments after architecture approval

### Increment 1 — configuration proof

- configure pilot masters, dimensions and roles;
- prove standard material and service chains manually;
- record accounting/stock postings and reconciliation evidence;
- confirm decisions on CWIP, service acceptance, paid allocation and floors.

Exit: approved scenario ledger showing expected standard consequences.

### Increment 2 — budget schema and fixtures

- implement the three approved ERA DocTypes;
- add minimal custom fields as fixtures;
- add dimension-integrity and approved-budget-line validations;
- add workflows with tests.

Exit: initial/revised budget and controlled MR/PO submission pass automated
permission, workflow and migration tests.

### Increment 3 — vertical material report

- implement Budget vs Actual for the material scenario;
- implement procurement/payment drill-down;
- reconcile to Stock, AP, Payment and GL reports.

Exit: no unexplained difference in the material pilot.

### Increment 4 — vertical service report

- add non-stock acceptance and service actual rules;
- test advance, partial invoice and partial payment;
- reconcile multi-currency/tax treatment selected for the pilot.

Exit: the service pilot meets the same control and audit criteria.

### Increment 5 — controlled pilot

- load only approved sample/pilot masters;
- train named users on standard forms;
- run one reporting period in test/staging;
- collect gaps before any broad UI or module expansion.

## Acceptance criteria

The MVP is usable only when all of these are true:

- a user cannot submit an unapproved or dimensionally inconsistent request/order;
- every direct cost drills to an ERPNext source document;
- every budget change preserves initial and revision history;
- ordered, delivered, invoiced, actual and paid are independently explainable;
- stocked material becomes actual only on approved consumption, not delivery;
- AP and paid totals reconcile to ERPNext ledgers with documented allocations;
- missing dimensions appear as errors/unmapped lines, never as silent omissions;
- cancellation, amendment, return and partial payment scenarios are tested;
- permissions prevent requester self-approval and unauthorized financial posting;
- migration and app-boundary tests remain green;
- no ERPNext/Frappe source file is modified.

## Architecture review gate

Before Increment 1, ERA business owners must approve at minimum questions Q01,
Q03, Q05, Q06, Q08, Q10, Q12 and Q15 in
[07-open-questions.md](07-open-questions.md). This document authorizes no major
implementation by itself.
