# Construction Budget Model

## Required management semantics

ERA needs to distinguish these measures:

| Measure | Definition |
| --- | --- |
| Initial Budget | Amount in the first approved baseline version. Immutable after approval. |
| Revised Budget | Amount in the latest approved version; supersedes the prior current version without deleting history. |
| Requested | Approved but not fully ordered Material Request balance. Informational, not a legal commitment. |
| Total Committed | Value of active submitted Purchase Order lines. |
| Open Committed | Portion of an active PO obligation not yet recognized in the selected actual-cost source. Used to avoid double counting in forecast. |
| Actual Cost | Recognized management project cost under the source policy in `03-cost-structure.md`. |
| Invoiced | Submitted Purchase Invoice amount, separately visible even when it is not the material-consumption actual. |
| Paid Cost | Cash allocated from Payment Ledger/advances to project cost under an explicit allocation policy. |
| Forecast to Complete (ETC) | Approved estimate of future cost not represented by Actual or Open Commitment. Optional manual input after MVP. |
| Forecast at Completion (EAC) | `Actual + Open Committed + ETC`. MVP system forecast may use `ETC = 0`. |
| Remaining to Commit | `Current Budget - Actual - Open Committed`, before manual ETC. |
| Variance | `Current Budget - EAC`; positive is under budget. |
| Variance % | `Variance / Current Budget × 100`; blank when Current Budget is zero. |

The requested management view should display at least:

```text
Initial Budget | Current Budget | Requested | Total/Open Committed
Delivered | Invoiced | Actual | Paid | Remaining | Forecast | Variance | Variance %
```

Showing Delivered and Invoiced prevents the single word “Actual” from hiding
important operational timing differences.

## Standard ERPNext Budget fit-gap

ERPNext v16 Budget is valuable and should not be discarded. Source inspection
confirmed that it provides:

- Project, Cost Center or a configured Accounting Dimension as `budget_against`;
- one Account and amount per Budget record;
- fiscal/date range and monthly/quarterly/half-yearly/yearly distribution;
- revision by cancelling and copying with `revision_of`;
- Warn/Stop rules for Material Request, Purchase Order, actual GL expense and
  cumulative MR + PO + GL;
- aggregation over Cost Center tree descendants;
- a Budget Variance report based on GL debit minus credit.

It is not the detailed ERA construction budget because:

1. one record chooses one dimension; it cannot hold Project + Block + Work
   Category simultaneously;
2. the Account must be a P&L account, while ERA construction cost may be CWIP or
   another balance-sheet account;
3. it has no Item, quantity, UOM, rate, contract package or line identity;
4. its “actual” is GL expense, not the material-consumption/service recognition
   model proposed for ERA;
5. it does not expose delivered, invoiced, paid, ETC or the required EAC view;
6. revision cancels/replaces individual Budget records, not one approved
   multi-line construction package.

## Proposed custom DocTypes

Only two transactional schema objects are proposed.

### `ERA Construction Budget`

A submittable version header:

| Field | Purpose |
| --- | --- |
| company | Required ERPNext Company. |
| project | Required ERPNext Project; one Project per budget. |
| budget_version | Monotonic project version number. |
| budget_type | `Initial` or `Revision`. |
| revision_of | Link to prior approved ERA Construction Budget. |
| effective_date | Date from which this approved version is current. |
| status | Workflow state: Draft, Pending Approval, Approved, Superseded, Rejected, Cancelled. |
| currency | Company currency in MVP; transaction currencies remain on procurement docs. |
| change_reason | Mandatory for revisions. |
| approved_by / approved_on | Audit fields set by workflow/action, not manually trusted. |
| total_budget | Read-only sum of lines. |
| lines | Child table of `ERA Construction Budget Line`. |

Submission/approval makes lines immutable. A revision copies the current
approved version, preserves stable line keys where possible, records deltas and
supersedes the previous version only after the new version is approved.

### `ERA Construction Budget Line`

| Field | Purpose |
| --- | --- |
| line_key | Stable identifier across revisions for variance/change history. |
| block_cost_center | Required block/floor cost object. |
| work_category | Required `ERA Work Category`. |
| cost_account | Required approved direct-cost/CWIP Account. |
| item | Optional ERPNext Item; required where quantity/material control needs it. |
| description | Controlled description for non-item packages. |
| quantity / uom / rate | Optional planning quantities and price. |
| amount | `quantity × rate` when quantitative, otherwise an approved lump sum. |
| notes | Scope/exclusion note, not a substitute for category fields. |

Forecast-to-complete should not be added to the budget line in the first
vertical slice. It is a later forecast/version concern and must not silently
rewrite an approved budget.

## Version rules

1. There is exactly one approved Initial Budget per Project.
2. There is at most one current approved version per Project/effective date.
3. Draft revisions do not affect procurement control or reports.
4. Approval of a revision marks the preceding current version Superseded; it
   never deletes or edits it.
5. Current Budget comes from the latest approved effective version.
6. Initial Budget always comes from version 1, enabling scope-growth reporting.
7. Submitted procurement remains linked to the Budget Line/version approved at
   the time; reporting also rolls that stable line key into the current view.
8. Cancellation after downstream use requires an explicit correction process,
   not direct deletion.

## Commitment formulas

The report should expose both total and open commitment.

```text
total committed = sum(active submitted PO item base net amounts)

open committed = sum(max(PO line committed amount
                         - recognized amount matched to that line, 0))
```

For non-stock services, recognized amount can be matched Purchase Invoice base
net amount (or accepted service amount if ERA formally adopts accrual at
acceptance). For stocked materials, invoice matching does not prove consumption.
The MVP should therefore show:

- ordered material commitment;
- received material value;
- consumed material actual;
- unreceived order balance;
- site stock value;

rather than force them into one misleading number. The exact material
`open committed` presentation is a review decision.

## Actual and paid formulas

Actual follows the source matrix in `03-cost-structure.md`:

```text
actual = service/direct PI actual
       + valued Material Issue consumption
       + approved labor source
       + eligible dimensioned adjustments
       - returns/reversals
```

It excludes Purchase Orders, warehouse transfers, unconsumed stock receipts and
cash payment itself.

Paid is derived separately:

```text
paid = reconciled Payment Ledger allocations
     + applicable supplier advances
     - reversed/refunded payments
```

Paid must never exceed the report's explicitly allocated payable/cost amount
without displaying an “unallocated advance” bucket. Exact dimension allocation
for multi-project invoices is an open policy decision.

## Forecast

MVP system forecast:

```text
System EAC = Actual + Open Committed
Remaining = Current Budget - System EAC
Variance = Current Budget - System EAC
```

Later controlled forecast:

```text
EAC = Actual + Open Committed + approved ETC
```

ETC should be a dated, approved forecast snapshot with author and explanation,
not an editable number on a dashboard. It is explicitly deferred from the first
vertical slice.

## Standard Budget control envelope

After an ERA budget version is approved, ERA may create or reconcile coarse
standard Budget records for control:

- Budget Against = Project **or** block Cost Center, selected by business policy;
- Account = controlled P&L construction account only;
- Amount = approved aggregation from ERA lines;
- Applicable on MR, PO, actual and cumulative expense;
- action initially `Warn` during pilot, then selected `Stop` rules after
  reconciliation is proven.

No standard Budget should be generated for CWIP/balance-sheet accounts because
ERPNext rejects them. The ERA detailed budget must continue to control those
lines through approval validation and reporting.

## Budget validation at procurement time

Proposed MVP checks when submitting an MR or PO:

1. referenced ERA Budget is approved and current for the Project;
2. Budget Line belongs to the same Project, block, Work Category, Account and
   optional Item as the transaction row;
3. requested/ordered amount is evaluated against current approved budget and
   existing demand/commitment/actual;
4. over-budget behavior follows workflow role and threshold: Warn, require
   exception approval, or Stop;
5. approved exception records a reason and approver; it does not alter budget;
6. standard ERPNext budget validation remains enabled where applicable.

The validation must aggregate company-currency base amounts and respect
cancellations, amendments and closed orders.

## Report grain and drill-down

Default grain:

```text
Project > Block > Work Category > Cost Account > optional Item/Budget Line
```

Filters include Project, block, work category, account, supplier, item, date
range and payment status. Supplier/payment filters are derived from source
transactions rather than stored on Budget Line.

Each measure drills to its authoritative documents. The report must show
unmapped transactions in an explicit “Unbudgeted / Missing Dimension” section;
silently dropping them is forbidden.
