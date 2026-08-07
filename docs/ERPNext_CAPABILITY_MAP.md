# Initial ERPNext Capability Map

This is a hypothesis register, not a completed audit. Decisions must be verified
against ERA's real workflows and a running ERPNext v16 site.

| Capability | Existing ERA software | ERPNext baseline | Initial decision |
| --- | --- | --- | --- |
| Users, roles, permissions | Not available for audit | Frappe users and role permissions | Configure |
| Customers and suppliers | Not available for audit | Customer, Supplier, contacts, addresses | Configure |
| Sales orders | Not available for audit | Quotation and Sales Order | Configure, then validate concrete fields |
| Purchasing | Not available for audit | Material Request, RFQ, Supplier Quotation, Purchase Order | Configure |
| Inventory | Not available for audit | Items, warehouses, Stock Entry/Ledger | Configure |
| Accounting | Not available for audit | GL, invoices, payments, receivables/payables | Configure |
| Projects and costing | Not available for audit | Project, Task, Timesheet, Cost Center | Extend after construction fit-gap |
| Manufacturing | Not available for audit | BOM, Work Order, Job Card, Stock Entry | Evaluate for batch consumption; do not assume fit |
| HR and payroll | Not available for audit | Separate Frappe HR/HRMS application in current ecosystem | Defer and assess dependency |
| Concrete grade | Not available for audit | Item attributes may cover only the sellable product | Extend or build after domain workshop |
| Mix design and versioning | Not available for audit | BOM may cover material formula but needs process validation | Extend or build after pilot modeling |
| Batch/plant production | Not available for audit | Manufacturing gives production transactions, not plant telemetry | Build ERA event layer if gap is confirmed |
| Dispatch planning | Not available for audit | Delivery Note covers delivery execution, not plant dispatch board | Build ERA planning layer if gap is confirmed |
| Mixers and drivers | Not available for audit | Asset/Vehicle/Employee may provide masters | Extend; avoid duplicate masters |
| Construction budgets | Not available for audit | Project estimated cost is not a full versioned control budget | Extend or build after fit-gap |
| Site warehouses | Not available for audit | Warehouse tree and project links/custom dimensions | Configure first |
| Budget vs actual | Not available for audit | Budgets, GL dimensions, project reports | Extend reporting after accounting design |
| Executive KPIs | Not available for audit | Workspaces, dashboards, reports, Insights ecosystem | Extend with reconciled ERA projections |

## Audit blockers

The referenced `era-soft` repository was empty at project initialization and no
existing ERA application, schema, exports, screenshots, or process documents
were supplied. Phase 2 therefore cannot be completed yet.

Minimum evidence required:

- source repository or application export;
- database schema and anonymized representative data;
- list of active reports and their consumers;
- role/user matrix;
- integrations and scheduled jobs;
- three representative workflows each for concrete and construction;
- known data-quality and reconciliation issues.
