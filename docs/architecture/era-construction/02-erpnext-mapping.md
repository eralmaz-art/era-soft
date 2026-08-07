# ERPNext Reuse / Extend / Custom Matrix

- **REUSE**: configure and use the standard entity without a parallel model.
- **EXTEND**: keep the standard entity authoritative; add fixtures, custom
  fields, workflow, validation or an ERA report.
- **CUSTOM**: add an ERA-owned DocType because the standard semantic/grain is
  insufficient.
- **DEFER**: no implementation decision is safe with the present evidence.

“Extend” never means editing ERPNext source. All extensions live in `era_soft`
and use supported Frappe fixtures/hooks.

## Mapping matrix

| ERA Construction entity | ERPNext entity | Decision | Reasoning | Risks / limitations |
| --- | --- | --- | --- | --- |
| Company | `Company` | REUSE | Owns currency, fiscal defaults, default bank/cash/payable/stock accounts and company-scoped permissions. | Legal-entity and inter-company design must be confirmed before masters are loaded. |
| Construction Project | `Project` | EXTEND | Already supplies company, dates, status, project users, Cost Center link and links from purchase/accounting/stock rows. Add only construction type, site metadata, manager and defaults. | Standard `total_purchase_cost` sums submitted Purchase Invoice items and is not the approved ERA actual-cost formula. |
| Construction Site | `Project` + `Address`/`Location` + site `Warehouse` | EXTEND | In the MVP one physical site belongs to one Project. Store site address/location and link the default site warehouse instead of duplicating Project. | If one Project can have several independently controlled sites, a dedicated Site master may become necessary. |
| Building / Block | `Cost Center` tree node | EXTEND | Hierarchical, company-scoped, present on transaction and GL rows and aggregatable in reports. Add a Project association and enforce membership. | Cost Center is a financial cost object, not a BIM/spatial model. Do not put blocks here unless costs are actually posted by block. |
| Floor | child `Cost Center` node, conditional | REUSE / DEFER | Use a leaf only when ERA budgets and posts costs by floor. Otherwise omit from MVP. | Mandatory floor capture creates high master/transaction volume and false precision. |
| Work Category | Accounting Dimension backed by `ERA Work Category` | CUSTOM | Work category is an axis independent of block. A tree master registered as Accounting Dimension propagates to supported MR/PO/receipt/invoice/stock/GL rows. | Creating/renaming a dimension changes Custom Fields across many DocTypes; migration and regression tests are required. |
| Cost Category | `Account` hierarchy | REUSE | The account already drives posting, budget control and reconciliation. Use controlled direct-cost/CWIP groups as the initial management category. | Statutory account and management category may diverge; a separate category is justified only after that gap is demonstrated. |
| Budget | `Budget` plus `ERA Construction Budget` | CUSTOM | Standard Budget is useful as a control envelope, but its grain is one dimension × one P&L account and cannot express the construction matrix, quantities/rates or an approved package. | Two layers must reconcile; avoid pretending the generated/control Budget is the detailed baseline. |
| Budget Line | child `ERA Construction Budget Line` | CUSTOM | Holds block, work category, account, optional item, quantity, UOM, rate and amount within one versioned budget. | Line identity and revision matching must be stable; uncontrolled free-text lines will break reporting. |
| Supplier | `Supplier`, `Supplier Group`, Address, Contact | REUSE | Standard party is integrated with orders, invoices, payments, taxes, accounts and bank details. | Duplicate tax IDs/names and company-specific payable accounts require master-data governance. |
| Contractor | `Supplier` classified by Supplier Group/type | EXTEND | A contractor is a supplier of services. Add a controlled contractor classification/capabilities only if Supplier Group is insufficient. | Creating a second Contractor party would split payable history and must be prohibited. |
| Contract | generic `Contract` linked from `Purchase Order` | EXTEND | Supports Supplier party, dates, status, terms, fulfilment checklist and a linked Purchase Order/Purchase Invoice. Add Project, contract type/value, retention/advance fields and `era_contract` on PO. | One generic Contract link is insufficient for many POs, BOQ, variations, progress certificates, retention and claims. Those are outside MVP. |
| Purchase Request | `Material Request` type `Purchase` | EXTEND | Standard submitted request carries required date, item, quantity, warehouse, Project, Cost Center, expense account and row links into PO. Add ERA workflow and budget-line/work-category context. | Standard Purchase User permissions allow submission/cancellation; workflow/roles must narrow this. Rate is indicative, not a supplier commitment. |
| Supplier Selection | `Request for Quotation` + `Supplier Quotation` | REUSE | Standard flow records invited suppliers, offers and link to PO; PO item retains Supplier Quotation reference. | Formal bid scoring and conflict-of-interest declarations are not standard. Manual selection needs a mandatory rationale/attachment policy. |
| Purchase Order | `Purchase Order` and item rows | EXTEND | Tracks supplier, schedule, items/services, Project, Cost Center, warehouses, payment schedule, received/billed percentages and source request/quotation. Submission validates budget and authorization. | PO creates no GL entry. Contract linkage, work category, approved budget line and approval workflow must be added/configured. |
| Material | stock `Item` | REUSE | Standard item supplies UOM, item group, stock flag, supplier parts, valuation and warehouse transactions. | Naming/UOM duplicates and overly generic items destroy quantity and cost analysis. |
| Material Delivery | `Purchase Receipt` | REUSE | Updates received quantity, Stock Ledger and PO status; under perpetual inventory may post Stock/Stock Received But Not Billed GL entries. | A receipt is not consumption. Quality inspection, rejected warehouse and returns policy must be configured. |
| Warehouse | `Warehouse` tree | REUSE | Company-scoped hierarchy, stock account linkage and standard stock reports already exist. | Warehouse is an inventory location, not the project/cost hierarchy. Never use it as the only project dimension. |
| Site Warehouse | child `Warehouse` | EXTEND | Configure one site group and optional block stores; add Project/Cost Center defaults for controlled entry. | Transactions do not automatically inherit correct project dimensions merely because a warehouse is selected; validation/defaulting is needed. |
| Material Transfer | `Stock Entry` purpose `Material Transfer` | REUSE | Moves quantity and valuation between central and site warehouses with Stock Ledger traceability. | A transfer is neither expense nor project consumption; reports must not count it as actual cost. |
| Material Consumption | `Stock Entry` purpose `Material Issue` | EXTEND | Stock issue creates the consumption event and valuation; row already supports Project, Cost Center and accounting dimensions. Add purpose-specific workflow/defaults. | Supplier provenance is normally lost for fungible stock after pooling. Incorrect expense/CWIP accounts will misstate actuals. |
| Service Purchase | non-stock `Item` through MR/PO/receipt/PI | EXTEND | Standard item-based purchasing supports service quantities, rates, project dimensions and order/invoice matching. A non-stock Purchase Receipt can be used as acceptance when policy requires it. | Construction progress certification, retention and variation orders are not covered by simple quantity receipt. |
| Service Confirmation | `Purchase Receipt` for non-stock service item | EXTEND | Updates PO received progress without creating stock for a non-stock item and preserves standard document links. | Semantics must be proven in a pilot; provisional accounting settings can create GL consequences for non-stock receipts. |
| Purchase Invoice | `Purchase Invoice` and item rows | EXTEND | Authoritative supplier liability with due date, outstanding amount, PO/receipt references, Project, Cost Center, account and payment schedule. | `update_stock` must be controlled to avoid duplicating a prior receipt. Multi-project invoices complicate paid-cost allocation. |
| Advance Payment | `Payment Entry` referencing `Purchase Order`; Advance Payment Ledger | REUSE | ERPNext supports PO advances, unallocated supplier payments and later invoice reconciliation. | Project/block allocation may exist only on PO/payment header, not at final invoice-line grain. Advance policy and separate advance account setting affect reporting. |
| Payment | `Payment Entry` | REUSE | Posts GL, settles invoice references through Payment Ledger and supports Pay/Receive/Internal Transfer, modes and references. | A payment can allocate several invoices and a single invoice can contain several project lines; exact paid cost by line is not inherently stored. |
| Bank Account | `Bank Account` + GL `Account` type Bank | REUSE | Standard bank master links actual bank details to the posting account and bank reconciliation. | Access to account numbers and reconciliation must be role-restricted. |
| Cash Account | GL `Account` type Cash + `Mode of Payment` | REUSE | Payment Entry can post cash disbursement using standard accounts and controls. | Cash-holder/cashbox accountability may need additional operational policy, but not a second cash ledger. |
| Accounts Payable | Purchase Invoice + Payment Ledger + standard AP reports | REUSE | ERPNext Accounts Payable and summary reports calculate supplier outstanding/aging from authoritative ledgers. | Standard AP is supplier/company-centric; ERA needs a project-filtered management view and allocation rules. |
| Employee | `Employee` | REUSE | Standard employee identity, company, department, designation and basic bank details are present. | Sensitive HR permissions and employee-to-project assignments require design. |
| Payroll | separate Frappe HRMS (not installed) | DEFER | No Payroll Entry, Salary Slip or Salary Structure source is installed in the verified bench. A source-level fit-gap cannot be completed now. | Do not build payroll in ERA SOFT. HRMS version compatibility, localization and accounting-dimension propagation need a separate decision. |
| Asset / equipment | `Asset` linked to Item, Location and Cost Center | REUSE | Appropriate for owned equipment and depreciation, with standard accounting effects. | Asset is not a block/site model. Equipment usage cost allocation is outside the first slice. |
| Project Cost | ERA Script Report over PI/Stock Entry/Timesheet/GL | EXTEND | Cost is a projection of authoritative events, not a new voucher. The source depends on material versus service recognition. | Double counting is likely unless source precedence and cancellations/returns are specified and tested. |
| Committed Cost | ERA report over submitted PO item balances | EXTEND | PO is the approved commercial commitment. Show total and open commitment separately. | ERPNext `amount - billed_amt` is invoice-oriented and may not equal unconsumed material commitment. Formula must be agreed. |
| Paid Cost | ERA report over Payment Ledger allocated to invoices/advances | EXTEND | Payment Entry/Payment Ledger are authoritative for cash settlement. | Exact allocation to Project/Block/Work Category is ambiguous for multi-dimensional invoices and advances. |
| Budget vs Actual | ERA Script Report combining budget lines and ERPNext transactions | EXTEND | Required view needs baseline/current budget, open commitments, management actual, paid, remaining, forecast and variance at construction grain. | Must reconcile to standard GL/stock/AP reports while explaining timing differences. |
| Cash Flow | standard `Cash Flow` report / GL | REUSE | Standard report is authoritative for posted historical cash movements. | It is accounting-statement oriented and not a project cash forecast. |
| Project Cash Requirement | ERA report over PI due dates, PO schedules and remaining budget | EXTEND | A layered forecast can show unpaid invoices, uninvoiced PO schedules and approved uncommitted budget without a second ledger. | Double counting across invoice/PO/budget layers and treatment of advances/taxes require explicit formulas. |

## Standard workflow and accounting consequences

| Submitted document | Operational consequence | Stock consequence | Accounting consequence |
| --- | --- | --- | --- |
| Material Request (Purchase) | Approved need; updates requested/ordered progress | None | None; can be included in ERPNext budget control. |
| Purchase Order | Supplier commitment; updates source request and received/billed status | May reserve/subcontract stock depending on flow | No GL; included in budget commitment control and advance eligibility. |
| Purchase Receipt, stock item | Records accepted delivery and updates PO received quantity | Stock Ledger entry at valuation | With perpetual inventory, typically debit stock and credit Stock Received But Not Billed, plus taxes/valuation entries. |
| Purchase Receipt, non-stock service | Can record accepted service quantity and update PO | No stock quantity | May create provisional expense/service-received-not-billed entries when company setting is enabled. |
| Purchase Invoice | Creates supplier invoice, due/outstanding and billed progress | Only if `update_stock=1` | Supplier payable plus expense/CWIP/stock-reconciliation/tax entries; Payment Ledger outstanding. |
| Stock Entry — Material Transfer | Moves material between stores | Source and target Stock Ledger entries | Inventory-account movement where applicable; not project consumption. |
| Stock Entry — Material Issue | Records consumed/issued material | Reduces site stock at valuation | Credit stock and debit selected expense/CWIP/difference account with project dimensions. |
| Payment Entry — supplier payment | Allocates cash to PI or PO advance | None | Bank/cash versus payable/advance GL entries; Payment and Advance Payment ledgers updated. |

## Permission observations and proposed response

| Standard area | Observed standard capability | ERA response |
| --- | --- | --- |
| Project | Projects User can create/write; Project Users can be granted record access | Configure project-level User Permissions and separate view/edit roles. |
| Material Request | Purchase/Stock roles can create, submit, cancel and amend | Add workflow states and remove direct submit from requester roles. |
| Purchase Order | Purchase User and Manager can submit/cancel; authorization-by-amount exists | Require procurement preparation plus Project Manager/Finance approval based on value and budget status. |
| Purchase Receipt / Stock Entry | Stock/Purchase roles can submit/cancel | Separate site receiver from Stock Manager; cancellation requires controlled role/reason. |
| Purchase Invoice / Payment Entry | Accounts roles can submit/cancel | Finance owns posting; project/procurement receive read-only drill-down. |
| Contract | Purchase Manager can submit/cancel | Use a contract owner and legal/management approval workflow if contract extensions enter MVP. |

## Rejected duplications

The MVP must not introduce custom equivalents of `Supplier`, `Contractor`,
`Item`, `Warehouse`, `Purchase Request`, `Purchase Order`, `Purchase Invoice`,
`Payment`, `Accounts Payable`, `Project Cost voucher` or `Cash Ledger`. Custom
fields and reports may present ERA terminology while the standard record remains
authoritative.
