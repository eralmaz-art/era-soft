# ERA SOFT Design Principles

Status: **Product constitution**  
Applies to: every user-facing workspace, dashboard, report, form, and workflow

## Product ambition

> Создание лучшей строительной операционной системы в Кыргызстане.

ERA SOFT is not an ERP catalogue with a new logo. It is the daily operating
product through which ERA Group understands the business, makes decisions, and
executes construction work. Frappe and ERPNext remain the upgrade-safe engine;
their module structure does not define the user experience.

## Rules

1. **One screen, one primary decision.** The screen brief names the user,
   context, and decision it accelerates. Content that does not improve that
   decision is removed or disclosed later.
2. **Frequent work in three navigational actions.** A trained user reaches a
   frequent task from their role home in no more than three navigational
   actions. Safety review, confirmation, and legally required steps are not
   removed to satisfy this target.
3. **Seven to nine primary destinations.** The global navigation shows no more
   than seven to nine role-relevant destinations. Administration and rare setup
   remain reachable but never compete with daily work.
4. **Progressive disclosure: 10 → 5 → 2 → 1.** Start with a small set of
   business areas, reveal the relevant subgroup, narrow to the records requiring
   attention, and end at one concrete decision. Do not expose the full ERP tree
   at the first level.
5. **Decision data first.** By default, show only the information required to
   understand status, consequence, and next action. Source records, accounting
   detail, history, and technical metadata open on demand.
6. **Color carries meaning only.** Color communicates selection, status, risk,
   or attention. It is never decoration. Every colored state also has a Russian
   label or icon so meaning never depends on color alone.
7. **Normal work stays calm.** Exceptions receive emphasis; healthy operation
   does not become a field of green badges, congratulatory cards, or animation.
8. **One interaction grammar.** Create, approve, filter, search, sort, inspect,
   confirm, and return behave consistently across every domain. All tables use
   the same filtering, search, sorting, density, selection, and empty-state
   patterns.
9. **Object before module.** A construction user works inside an object and
   moves between budget, procurement, contracts, materials, payments, and
   documents without losing project context.
10. **Every number is trustworthy.** A management value identifies company,
    period, currency or unit, definition, freshness, permissions, and source
    records. A KPI without a reconciled data contract is not implemented.
11. **Russian is the product language.** User-facing terminology follows the
    approved glossary. Framework identifiers remain internal. Kyrgyz is the
    next product language; English remains available to developers.
12. **UX approval precedes code.** Every new page passes decision brief,
    workflow and source map, low-fidelity states, reviewable mockup, and product
    approval before implementation. Material post-approval changes return to
    review.

## Product lifecycle

Every ERA SOFT product follows the mandatory sequence defined in
`PRODUCT_DEVELOPMENT_PROCESS.md`:

```text
IDEA → BUSINESS MODEL → UX → UI → DATA MODEL → IMPLEMENTATION
```

Construction is the first product governed by this sequence. It is not treated
as an ERP module or a list of framework entities.

## Thirty-second test

The role owner should understand within thirty seconds:

- what changed;
- what is healthy;
- what requires attention;
- what requires a decision now;
- what action is safe;
- which records prove it.

If the screen cannot pass this test, adding more data is not the solution.

## Screen acceptance questions

1. What single decision is faster because this screen exists?
2. Can the primary user reach the frequent task in three navigational actions?
3. Can any menu item, KPI, card, chart, status, or field be removed?
4. Does the screen reveal detail progressively rather than expose the ERP tree?
5. Is each color meaningful and paired with a label?
6. Can every management number be reconciled to authoritative records?
7. Does the user keep company, project, and process context?
8. Have normal, empty, loading, stale, error, offline, and permission states
   been designed?
9. Has the product owner approved the named mockup version?
