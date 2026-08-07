# ERA Construction Business Model Finalization Review

Review date: **2026-08-08**<br>
Reviewed document: **PRODUCT_SPEC.md**<br>
Review scope: **Product and business model only**

## Executive Finding

The existing product specification was already strong: it defined a coherent
project-centered purpose, end-to-end construction process, product boundary,
screen inventory, progressive navigation, permissions intent, reports, future
scope, exclusions, and product gates. It did not require a rewrite.

The finalization added only capabilities that were objectively missing for a
multi-year product specification:

- a five-year product Vision;
- permanent Product Principles for future product decisions;
- a role-by-role test of the promise to operate without shadow spreadsheets;
- explicit business ownership, decisions, and inputs for every proposed KPI;
- constitutional Business Rules independent of future software mechanisms;
- a Decision Model that defines inputs, authority, outcomes, and consequences;
- a precise assessment of project-centric navigation without changing approved
  UX;
- closeout and exception-governance decisions that were absent from the P0
  approval list.

The specification package is now suitable as a long-term product-management
foundation. The business model itself is **not yet ready for approval** because
its named owners and material P0 policy decisions remain unresolved.

## Section-by-Section Review

| Section | Modification | Why it improves the product | Priority |
|---|---|---|---|
| Document status and gate | Preserved as Draft; no authority was invented. | Product quality includes truthful governance. Raising the status while owners and P0 rules are unresolved would weaken trust in every later gate. | Critical |
| Purpose | Preserved. | It already distinguishes a project operating product from an ERP module catalogue and states the decision outcome clearly; editing it would be cosmetic. | — |
| Vision | Added a five-year, technology-independent outcome. | Future teams need a durable test for scope and trade-offs. The Vision prevents local features from recreating spreadsheet silos or document-first ERP navigation. | Recommended |
| Product Principles | Added nine permanent principles. | Principles make future product choices consistent when the specification cannot predict every screen or process. Each principle constrains a known product risk: duplication, untraceable metrics, ambiguous stages, silent history changes, alert overload, avoidable complexity, or technology-led design. | Recommended |
| Product promise | Preserved. | It already expresses the user outcome in testable business questions and includes source traceability. Rephrasing would add no product value. | — |
| Users | Preserved the role inventory and added daily-work readiness for the six requested roles. | A user list does not prove the product can replace spreadsheets. The readiness test exposes the exact missing operating routines and policies that must be validated before implementation. | Critical |
| Business Goals | Preserved. | The goals already cover operating truth, project context, cost control, blockers, evidence, authority, spreadsheet reduction, and Russian-first experience. | — |
| Business Process | Preserved. | The end-to-end process and separate material/service paths are complete enough for the current gate. Stable constitutional rules were extracted into a companion document rather than duplicating or rewriting the approved flow. | — |
| Product Scope | Preserved. | The first boundary and vertical slice remain disciplined and aligned with the approved product sequence. Expanding scope would contradict the milestone. | — |
| Main Screens | Preserved. | These are approved UX inputs. This iteration did not authorize new screens or layout changes. | — |
| Navigation | Added a project-centricity assessment and behavioral requirements; menu labels and hierarchy were not changed. | The current menu is project-centric inside an object but must also support portfolio queues. Persisting object context and distinguishing cross-project work prevents functional navigation from pulling site roles back into an ERP-style catalogue. | Recommended |
| KPIs | Replaced placeholder definition prompts with a Business Owner, Decision Supported, and Required Inputs for every KPI; no formulas were added. | A KPI without an owner and decision can become decorative or disputed. Inputs expose the business facts and policy decisions required before any data contract or implementation is designed. | Critical |
| Permissions | Preserved. | The section already establishes scope, sensitivity, server-enforced authority, and segregation without prematurely designing permissions. | — |
| Reports | Preserved. | Each listed report already states the decision it supports. Prioritization should follow pilot validation, not speculative additions in this review. | — |
| Future Scope | Preserved. | It protects long-term intent without expanding the first product boundary. | — |
| Out of Scope | Preserved. | These exclusions are essential controls against premature UI, automation, migration, and broad implementation. | — |
| Open Decisions | Added project-closeout criteria, emergency and policy exception governance, and role validation. | A construction operating model cannot be complete if it cannot govern abnormal action or determine when an object is truly closed. Role validation is necessary to test the no-spreadsheet promise. | Critical |
| Future Data Model Gate | Preserved. | It explicitly prevents this product iteration from authorizing records, permissions, queries, workflows, or migration. | — |
| Approval Record | Expanded the Business Model evidence list; status remains Draft. | Approval should apply to the complete product constitution, not one file in isolation. | Recommended |

No text was changed solely for style. Existing content was retained wherever it
already served the product decision.

## Findings

### Critical

1. **Named ownership is unresolved.** The Product Owner and process owners are
   still pending. Without them, KPI ownership, exceptions, reconciliations, and
   process decisions cannot be governed or approved.

2. **Core cost-control meanings remain unresolved.** ERA must approve what
   creates or reverses commitment, when material and service value becomes
   management cost, how progress is accepted, and how advances and retentions
   are closed. These choices materially change operational decisions even before
   any Data Model is considered.

3. **Authority is unresolved.** Budget, purchase, contract, invoice, advance,
   payment, exception, and closeout limits—plus independent review—must have
   named accountable authorities. A decision model without approved authority
   cannot govern daily work.

4. **Acceptance evidence is unresolved.** Material receipt, material quality,
   service measurement, technical acceptance, discrepancy, and correction need
   agreed evidence and accountable roles. Otherwise project cost and supplier
   obligation cannot be trusted.

5. **The product has not been validated on a real pilot.** The selected pilot
   must exercise at least the first vertical slice and applicable exception
   decisions. Without this, the claim that primary roles can stop maintaining
   shadow spreadsheets is unproven.

6. **Project closeout and emergency exception policy require approval.** These
   are now specified as decisions and rules, but their owners, thresholds, and
   acceptable residual risks are still open.

### Recommended

1. **Approve the three-document business constitution as one package.** Review
   `PRODUCT_SPEC.md`, `BUSINESS_RULES.md`, and `DECISION_MODEL.md` together.
   This prevents a process owner from approving a screen promise without also
   accepting its rules and decision consequences.

2. **Run role validation with named representatives.** For Owner, Construction
   Director, Project Manager, Procurement Manager, Finance Manager, and Site
   Engineer, walk through one normal day and one exception day. Confirm exact
   inputs, handoffs, decision timing, and any remaining spreadsheet.

3. **Confirm KPI ownership before calculation design.** Each proposed business
   owner must accept responsibility for meaning, freshness, source completeness,
   and exception resolution. Only then should a future data contract define a
   calculation.

4. **Validate project-context behavior during future UX review.** Project and
   site roles should start in an assigned or recent object, retain that context,
   and see cross-project actions clearly marked. This preserves the approved
   navigation while protecting the project-first principle.

5. **Approve normal and exception decisions together.** Emergency purchase,
   partial acceptance, disputed invoice, advance, budget exception, and residual
   closeout must not be deferred until implementation; they define the operating
   model's safety.

### Optional

1. **Record baseline operating measurements before the pilot.** Approval time,
   procurement lead time, delivery reliability, payment cycle, reconciliation
   effort, and spreadsheet usage would allow later product benefits to be
   measured. The specification already defers quantitative targets until these
   baselines exist.

2. **Prioritize reports after role validation.** The current report inventory is
   sufficient for this gate. Later ranking by decision frequency and business
   risk can keep the first release focused.

3. **Maintain a decision log for approved P0 answers.** A short record of who
   decided, why, effective date, and affected rules will make later changes less
   ambiguous. This is governance documentation, not a Data Model.

## Navigation Conclusion

The approved navigation is genuinely project-centric for users working inside
an object. The product-level layer is intentionally portfolio- and
function-oriented for cross-project roles. No redesign is recommended.

The only recommended strengthening is behavioral: preserve selected-object
context, default project/site roles into their object, inherit the object in
contextual actions, and label cross-project queues. This does not alter the
approved screen structure or menu.

## Role Readiness Conclusion

None of the six reviewed roles can yet be guaranteed to perform all daily work
without spreadsheets. The missing items are not primarily more screens; they
are unapproved operating definitions, authority, evidence, control cadence, and
handoff rules. The exact gaps are recorded in the `Users` section of
`PRODUCT_SPEC.md` and must be validated against a real pilot.

## KPI Conclusion

Every candidate KPI now has:

- one accountable business owner;
- a named decision it supports;
- the minimum required business inputs.

No formula, query, record type, accounting behavior, or implementation contract
was introduced. KPI calculation remains blocked until its business meaning and
data contract are approved.

## Status Recommendation

Do **not** change the status from **Draft** to **Business Model Approved** yet.

The documents have reached production-quality specification structure, but the
business model is not approved while the P0 decisions remain open. A valid
status change requires:

1. confirmed Product Owner and named process owners;
2. approved answers to all P0 decisions in `PRODUCT_SPEC.md`;
3. owner acceptance of applicable rules in `BUSINESS_RULES.md`;
4. confirmed authority and policy for the decisions in `DECISION_MODEL.md`;
5. validation against the named pilot and six primary roles;
6. a recorded approval by the required product and process owners.

Once those conditions are met, the package can be recommended for **Business
Model Approved** without rewriting the product specification.

## Scope Confirmation

This review adds documentation only. It does not create or authorize a Data
Model, DocType, workflow, screen, formula, permission implementation, ERPNext
change, migration, or business functionality.
