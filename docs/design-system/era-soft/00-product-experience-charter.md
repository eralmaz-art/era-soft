# Product experience charter

## Product ambition

ERA SOFT must feel like a focused, high-trust operating product for ERA Group,
not a reskinned generic ERP. The desired character is calm, precise, modern,
European, and materially useful during an eight-to-ten-hour workday.

The interface is successful when a user understands what changed, what needs a
decision, and what action is safe without interpreting ERP internals.

## North-star question

Every screen must answer:

> Which decision does this screen help this user make faster?

If the team cannot answer in one sentence, the screen is not ready to design. If
the screen contains information that does not improve that decision, simplify
or remove it.

## Seven principles

1. **Decision before data.** Lead with the decision, exception, or next action;
   make supporting records available on demand.
2. **Project before module.** In construction, users work inside an object and
   move between budget, procurement, materials, contractors, payments, and
   documents without losing context.
3. **Calm by default.** Normal operations stay visually quiet. Color and
   interruption are reserved for selection, risk, failure, and time-sensitive
   exceptions.
4. **One primary action.** Each page region has one obvious next action. Equal
   visual weight must not be given to competing actions.
5. **Progressive disclosure.** Daily fields and decisions are visible first;
   accounting detail, audit data, and rare settings remain reachable but do not
   dominate.
6. **Trust through traceability.** Every management number exposes its period,
   freshness, definition, and drill-through to authoritative records.
7. **Consistent ERA language.** Russian terminology follows the approved
   glossary; framework identifiers remain internal.

## Product personality

| ERA SOFT is | ERA SOFT is not |
|---|---|
| precise and composed | decorative or theatrical |
| spacious but information-rich | empty for the sake of minimalism |
| direct and human | informal, playful, or vague |
| contextual to a role and object | a catalogue of ERP modules |
| transparent about status and source | a dashboard of unexplained numbers |

## Interaction priorities

1. Resolve risk or approval.
2. Continue the current operational flow.
3. Understand performance and variance.
4. Inspect source records and history.
5. Configure the system.

Navigation, keyboard order, page hierarchy, and action emphasis must follow this
priority unless a role-specific workflow documents a different order.

## Experience targets

- A returning user identifies today's highest-priority action within 10 seconds.
- An owner reaches the source records behind a KPI within two interactions.
- A project manager changes between Budget, Procurement, Materials, Contractors,
  and Payments without leaving the selected construction object.
- A frequent create or approval action is reachable without horizontal scrolling
  at the agreed desktop baseline.
- Normal, empty, loading, permission-denied, offline, validation-error, and
  destructive states are designed before implementation.

These are initial product hypotheses. Instrumentation and baselines must be
agreed before numeric delivery targets become contractual.
