# Screen review gate

No user-facing screen or material change enters implementation without an
approved brief and mockup.

## Required sequence

```text
1. Decision brief
2. Workflow and source-data map
3. Low-fidelity states
4. Reviewable UX mockup
5. Product/process approval
6. Engineering fit-gap and estimate
7. Implementation through supported extension points
8. Visual, accessibility, permission, and reconciliation verification
```

## Screen brief template

Copy this template into the feature specification:

```markdown
# Screen: <Russian user-facing name>

- Primary user/role:
- Context (company/object/process step):
- Decision accelerated:
- Current workaround and measured time:
- Authoritative source records:
- Primary action:
- Secondary actions:
- Required information:
- Explicitly excluded information:
- Permissions and sensitive values:
- Normal, empty, loading, stale, error, offline, and permission states:
- Destructive consequences and confirmation:
- Drill-through and audit trail:
- Russian terminology references:
- Reused design-system patterns:
- Success measure:
- Product owner:
- Process owner:
- Approval date and mockup version:
```

## Definition of ready for implementation

- the decision sentence is specific and accepted by the primary user;
- ERPNext reuse/extend/custom disposition is documented;
- all values have source, period, company, currency/unit, and freshness semantics;
- roles, permissions, approvals, and destructive consequences are known;
- happy path and exception states are visible in the mockup;
- Russian wording follows the terminology standard;
- the design uses existing components or declares a reviewed system change;
- the product owner and process owner approve a named mockup version;
- acceptance scenarios and reconciliation evidence are written.

Missing information blocks implementation. It does not block further discovery
or prototyping.

## Definition of done for a screen

- the implemented hierarchy matches the approved mockup or records an approved
  deviation;
- keyboard operation, focus, zoom, contrast, and screen-reader labels pass the
  agreed accessibility check;
- 1280 px and 1440 px desktop layouts pass visual review; narrower supported
  layouts reflow without losing decisions or actions;
- Russian text, long names, large values, empty data, stale data, and error states
  are verified;
- role and company boundaries are tested server-side;
- management numbers reconcile to source transactions;
- performance meets the agreed page budget on representative data;
- visual regression evidence and process-owner acceptance are attached.

## Design review checklist

1. Can the primary decision be found within 10 seconds?
2. Is there exactly one visually primary action per action group?
3. Can any nonessential field, card, chart, color, or line be removed?
4. Does the user remain inside their company/object/process context?
5. Are normal operations calm and exceptions specific?
6. Is every KPI defined and drillable?
7. Are accounting consequences visible before commitment?
8. Are words taken from the Russian terminology standard?
9. Are all states and permissions designed?
10. Does the result look and behave like ERA SOFT rather than a generic ERP?

## Governance

- Product owner approves information hierarchy and visual direction.
- Process owner approves workflow, terminology, exceptions, and consequences.
- Engineering approves feasibility, upstream safety, source integrity, and
  performance.
- A design-system owner accepts or rejects new component patterns.
- Approval is versioned. Material post-approval change returns to the relevant
  review step.
