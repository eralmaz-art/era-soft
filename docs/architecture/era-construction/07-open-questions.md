# Open Questions and Required Business Decisions

Priorities:

- **P0** blocks schema, accounting or the first vertical slice;
- **P1** must be resolved before pilot acceptance;
- **P2** may be deferred without corrupting the MVP design.

| ID | Priority | Decision required | Recommended starting position | Why it matters / owner |
| --- | --- | --- | --- | --- |
| Q01 | P0 | What is a Project versus Site, and can one Project contain multiple independent sites? | One Project = one controlled construction site for MVP. | Determines whether Project extensions are enough or a Site DocType is necessary. Owner: Construction Director. |
| Q02 | P1 | Must cost be posted by floor, or only by block? | Block mandatory; floor deferred unless existing approvals/reports truly use it. | Determines Cost Center depth and transaction burden. Owner: Project Controls. |
| Q03 | P0 | Are construction costs expensed, capitalized to CWIP/inventory, or split by type/stage? | Define approved account mapping before configuration; reports support both but show them separately. | Drives PI/Stock Entry postings and proves why standard Budget may not apply. Owner: CFO/Chief Accountant. |
| Q04 | P1 | Should Project-level and Block-level Cost Centers both accept direct postings? | Direct cost at leaf Block; Project-level node for approved common overhead only. | Prevents ambiguous aggregation and duplicate cost. Owner: Finance + Project Controls. |
| Q05 | P0 | What is the controlled Work Category hierarchy and who owns changes? | Approve a compact tree (Foundation, Frame, Masonry, Facade, Engineering, Finishing) before transactions. | It becomes a database-wide Accounting Dimension. Owner: Construction Director. |
| Q06 | P0 | Does management Cost Category equal the Account hierarchy? | Use Account in MVP; add a separate category only after a documented cross-account gap. | Avoids duplicate taxonomy and determines budget-line grain. Owner: CFO. |
| Q07 | P1 | How are initial/revised budgets approved and when does a revision become effective? | Immutable submitted versions; one current approved version; mandatory reason and approval. | Determines lifecycle, permissions and historical reporting. Owner: Budget Committee. |
| Q08 | P0 | What does “Committed” mean for materials: total PO, unreceived PO, uninvoiced PO, or unconsumed ordered value? | Display total commitment plus separate unreceived/uninvoiced/site-stock/open measures; do not collapse initially. | Prevents misleading EAC and double counting. Owner: CFO + Procurement + Project Controls. |
| Q09 | P1 | Is service cost actual at engineer acceptance, at PI posting, or accrued at period end? | PI posting for MVP; service receipt is operational acceptance. Enable provisional accounting only if accounting policy requires accrual. | Changes actual date and GL reconciliation. Owner: Chief Accountant. |
| Q10 | P0 | Is one Purchase Invoice allowed to contain several Projects/blocks/work categories? | One Project per PI during pilot; multiple blocks/work categories allowed with proportional paid allocation disclosed. | ERPNext payments allocate by invoice, not item row. Owner: Finance Manager. |
| Q11 | P1 | How are tax, retention, exchange differences and discounts allocated to project paid/actual cost? | Base net lines for cost; taxes/FX/retention in explicit separate buckets until policy approved. | Required for exact paid-cost and GL reconciliation. Owner: Chief Accountant. |
| Q12 | P0 | Are supplier advances made against PO, unallocated to Supplier, or both? Which separate advance account setting applies? | Prefer PO-referenced Payment Entry; show unallocated advances separately and never as actual cost. | Determines Advance Payment Ledger behavior and cash forecast. Owner: Treasury/Finance. |
| Q13 | P1 | What supplier-selection thresholds and sole-source exceptions apply? | Standard RFQ/Supplier Quotation above threshold; mandatory reason/attachment/approval for exception. | Determines workflow states and audit evidence. Owner: Procurement Director. |
| Q14 | P1 | Is non-stock Purchase Receipt acceptable as the service acceptance certificate? | Pilot it for simple quantity/milestone services. | Avoids a custom acceptance DocType, but may not cover certified BOQ/retention. Owner: Construction + Legal + Accounting. |
| Q15 | P0 | Which approval thresholds and roles apply to MR, PO, PI exceptions and Payment? | Separate requester, project approval, procurement, finance and high-value director roles; no self-approval. | Required for workflows and permission tests. Owner: CEO/CFO/Construction Director. |
| Q16 | P1 | What receipt tolerance, overbilling tolerance, quality/rejection and return rules apply? | Start with strict match and explicit manager exception; use rejected warehouse where relevant. | Affects PO/PR/PI controls and stock accuracy. Owner: Procurement + Warehouse. |
| Q17 | P1 | Is site stock received centrally then transferred, or received directly at site? | Model the actual operating route; count neither receipt nor transfer as consumption. | Determines warehouses, document volume and responsibility. Owner: Warehouse Manager. |
| Q18 | P1 | Must consumed material actual be analyzed by originating Supplier? | Not in MVP; procurement by Supplier and consumption by Item are separate views. | Ordinary pooled stock does not preserve simple supplier provenance. Owner: Project Controls. |
| Q19 | P2 | Is manual Forecast to Complete required in the first pilot? | Defer; use system EAC = Actual + Open Commitment first. | Manual forecast requires its own dated approval/version model. Owner: Project Controls. |
| Q20 | P1 | What is the cash-requirement horizon and date source? | Monthly horizon using PI due schedule first, then uninvoiced PO schedule, then budget remaining. | Determines cash forecast precedence and granularity. Owner: Treasury. |
| Q21 | P2 | Which contract capabilities are required now: registry only, BOQ, retention, variation, progress certificate, claim? | Registry/link only in MVP; architect advanced contract management separately. | Prevents overloading generic Contract or prematurely building a large module. Owner: Legal + Construction. |
| Q22 | P2 | Will direct labor use Timesheets before HRMS? | Defer labor actual or pilot Timesheet only after costing-rate/privacy approval. | Payroll is not installed and must not be reinvented. Owner: HR + Finance. |
| Q23 | P2 | Should Frappe HRMS be installed and evaluated for payroll in Phase 2/3? | Separate version-16 compatibility/localization fit-gap after procurement MVP. | Adds an application dependency, permissions and payroll accounting. Owner: HR + CTO. |
| Q24 | P1 | Which users may see supplier prices, payroll, bank accounts and cross-project reports? | Role plus Project/Company User Permissions; Auditor read-only; least privilege. | Standard roles alone may expose broader records than intended. Owner: Security/System Owner. |
| Q25 | P1 | What base currency and multi-currency policy applies to budgets and commitments? | Budget in Company currency; retain document currency and use posting conversion rate with explicit FX variance. | Required for stable comparisons and payment allocation. Owner: CFO. |
| Q26 | P1 | What historical source data exists and what is the cutover policy? | No migration in architecture phase; later profile budgets, open POs, stock, invoices, advances and balances separately. | Prevents unreconciled opening commitments/costs. Owner: Data Owner + Finance. |

## Review record template

Record each resolved decision in the pull request or an ADR when it changes a
durable technical boundary:

```text
Question:
Decision:
Effective date:
Owner/approver:
Example transaction:
Accounting/report consequence:
Exception rule:
```

Answers must include at least one representative material and service example.
Names such as “actual”, “commitment” or “site” are not considered resolved until
their source documents, dates and formulas are explicit.
