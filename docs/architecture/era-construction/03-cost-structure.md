# Project and Cost Structure

## Recommended hierarchy

Use independent dimensions for independent business questions. Do not encode
the full structure into names or repeat work categories below every block.

```text
ERPNext Project
  EcoCity Ayni

ERPNext Cost Center tree (physical cost object)
  Construction Projects - ERA
    EcoCity Ayni - ERA
      Block A - ERA
      Block B - ERA

ERA Work Category tree (activity axis / Accounting Dimension)
  Civil Works
    Foundation
    Frame
    Masonry
  Envelope
    Facade
  Engineering
  Finishing

ERPNext Account tree (cost category / posting axis)
  Construction Cost / CWIP
    Materials
    Subcontractors
    Direct Labor
    Equipment
    Design and Permits
    Site Overheads
```

The example `Block A → Foundation` is therefore an intersection, not a nested
master-data duplication:

```text
Project = EcoCity Ayni
Cost Center = Block A - ERA
Work Category = Foundation
Account = Construction Materials / CWIP
Item = Rebar 16 mm
Supplier = Supplier X
```

## Dimension assignment

| Analysis requirement | Representation | Why |
| --- | --- | --- |
| Project | built-in `Project` | Standard field exists on procurement, stock, accounting and GL rows. |
| Construction site | Project metadata + site Warehouse | One site per Project is the MVP assumption. |
| Building / block | leaf or group `Cost Center` | Hierarchical financial cost object with GL/report support. |
| Floor | optional child Cost Center | Use only when ERA will approve/post/budget at this grain. |
| Work category | `ERA Work Category` Accounting Dimension | Independent reusable hierarchy across all blocks/projects. |
| Cost category | posting `Account` | Keeps management view reconciled with the chart of accounts. |
| Supplier / contractor | source `Supplier` | Derived from PO/PI/payment, not copied into GL classification. |
| Material / service | source `Item` | Carries quantity, UOM, stock behavior and purchase history. |
| Date | transaction/posting date | Use posting date for ledgers; retain request/order/due dates for operational views. |
| Payment status | Purchase Invoice outstanding + Payment Ledger | A changing state, not a master/dimension. |

## Transaction grain

Direct construction rows should carry the following fields where supported:

1. Company.
2. Project.
3. block Cost Center.
4. ERA Work Category.
5. expense/CWIP Account.
6. Item and quantity/UOM when meaningful.
7. approved construction Budget Line reference for traceability.

Project, block and work category should be recorded on **item rows**, not only
document headers. A document may legitimately contain different work packages,
but this creates the paid-allocation limitation described below. For the first
pilot, ERA should prefer one Project per Purchase Invoice and Payment Entry.

## Cost recognition policy

Management project cost and accounting expense are related but not identical.
The following source precedence is proposed:

| Event | Management actual cost? | Proposed amount/date | Explanation |
| --- | --- | --- | --- |
| Material Request | No | N/A | It is demand, not a commitment or cost. |
| Submitted Purchase Order | No; it is commitment | base net ordered amount / order date | No stock or GL posting occurs. |
| Purchase Receipt of stock item | No consumption cost | received stock valuation / receipt date shown separately | Material is delivered and owned but remains inventory. |
| Material Transfer to site | No | transfer valuation shown in stock movement reports | Location changes; economic consumption does not. |
| Material Issue from site | **Yes** | stock value difference / posting date | This is the authoritative stocked-material consumption event. |
| Accepted non-stock service | Operational delivery only | accepted PO value / receipt date shown separately | Useful for delivery/progress; actual cost is recognized on PI unless a separate approved accrual policy is adopted. |
| Submitted Purchase Invoice for service/direct non-stock item | **Yes** | base net line amount / posting date | Creates payable and expense/CWIP posting. |
| Purchase Invoice for stock item already received | No second material actual | invoice variance only where policy requires | Counting the invoice and later issue would double count the material. |
| Payment Entry | No new actual; **paid cost** | allocated paid amount / payment date | Settles liability or creates advance; it is a cash measure. |
| Timesheet | Conditional | submitted costing amount / work date | Can represent direct labor before payroll integration if business approves. |
| Payroll | Deferred | not defined | Requires separate HRMS fit-gap and allocation policy. |
| Journal Entry / adjustment | Conditional | dimensioned debit-credit / posting date | Include only approved project-cost account types and explicit adjustment purposes. |

Returns and cancellations reverse the originating amount. All reports must use
submitted, non-cancelled documents and base/company currency for aggregation,
while retaining transaction currency for drill-down.

## Capitalized construction cost

A developer may capitalize construction cost to a balance-sheet CWIP or
inventory account instead of posting it immediately to P&L expense. This is a
business/accounting-policy decision, not a software detail.

The proposed cost projection accepts either approved direct-expense or approved
CWIP accounts. This is one reason standard ERPNext Budget cannot be the detailed
construction budget: its controller rejects non-P&L accounts. The report must
show the account and cost-recognition source so that management actual can be
reconciled to GL without labeling every amount an accounting expense.

## Project–block integrity

Cost Center is company-scoped but does not natively prove that a block belongs
to the selected Project. ERA should later add a small custom link on Cost Center
to Project and server-side validation on controlled transaction rows:

- selected block must be a non-group descendant of the Project's Cost Center;
- selected site warehouse must belong to the same company and Project;
- direct construction accounts require Project, block and Work Category;
- overhead accounts may use the Project-level Cost Center and an approved
  overhead Work Category;
- transfers do not become cost solely because Project is present.

These rules are extension validations in `era_soft`, not ERPNext overrides.

## Floor policy

Floor is intentionally conditional:

- use a Cost Center leaf for a floor only if budget lines, approvals and source
  transactions will consistently carry floor;
- use Project Tasks for scheduling/progress detail that has no independent cost
  attribution;
- do not create a Floor DocType merely for display;
- if future spatial/BIM requirements exceed Cost Center semantics, design a
  separate operational Location model and keep accounting dimensions stable.

## Supplier and material analysis limits

Supplier analysis is exact for ordered, received and invoiced procurement
because those records retain Supplier. It is not automatically exact for actual
consumption after fungible material from several suppliers is pooled in one
warehouse. Moving-average/FIFO valuation provides cost, but an ordinary Stock
Entry issue does not preserve a simple originating-supplier field.

ERA must choose one of these policies before promising “actual consumed cost by
supplier”:

1. report procurement cost by Supplier and consumed cost by Item separately
   (recommended MVP);
2. segregate batches/warehouses by supplier where operationally justified;
3. implement explicit provenance allocation later.

## Paid-cost allocation

Payment Entry allocates to invoice references, not to individual Purchase
Invoice rows. Proposed MVP reporting allocates invoice payment proportionally to
eligible base net line amounts:

```text
invoice paid amount = invoice grand total - current outstanding amount
line paid amount = invoice paid amount * eligible line base net amount
                   / total eligible line base net amount
```

Taxes, retention, advances, returns and multi-currency differences can make this
only a management allocation. Exact project paid cost therefore requires one of:

- one Project per Purchase Invoice (recommended pilot policy);
- a reviewed tax/allocation formula with reconciliation difference shown;
- a future explicit payment allocation by project/budget line.

Paid cost never replaces Accounts Payable or GL balances.

## Reconciliation controls

Every ERA report must provide drill-through and a reconciliation footer:

- procurement totals to Purchase Order Analysis;
- delivery quantities/values to Purchase Receipt and Stock Ledger;
- inventory balances to Stock Balance;
- invoice/outstanding totals to Purchase Register and Accounts Payable;
- paid totals to Payment Ledger and bank/cash GL;
- accounting actuals to General Ledger by Project, Cost Center, Work Category
  and Account;
- management-only adjustments and timing differences shown separately.
