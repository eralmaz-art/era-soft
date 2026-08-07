# Data visualization

## Purpose

A chart is used only when shape, trend, distribution, or comparison is faster to
understand visually than in a number or compact table. Charts are evidence for a
decision, not decoration.

## Approved baseline patterns

| Question | Pattern |
|---|---|
| Budget vs committed vs actual | aligned bullet or horizontal bars with exact values |
| Cash movement over time | line with period, currency, and directly labeled current value |
| Project progress over time | one line against approved plan, with variance annotation |
| Cost composition | sorted horizontal bars; avoid pie charts with many categories |
| Delivery or payment timing | timeline or time-bucketed bars |
| Status distribution | table or bar before colored tiles |

## Rules

- State title, period, currency/unit, data freshness, and scope.
- Start zero-based when bar length communicates magnitude.
- Use consistent scales for comparisons.
- Limit persistent series to four unless the decision requires more.
- Directly label important values; do not force legend lookup for one or two
  series.
- Use Deep Green for the selected or primary series, graphite/neutrals for
  context, and semantic colors only for actual business state.
- Pair color with labels, shape, or line style.
- Provide the underlying table or accessible summary.
- Tooltips add exact detail but never contain the only available value.
- No 3D, gauge speedometers, decorative gradients, animated counters, or
  unexplained red/green comparisons.

## Financial integrity

- A financial chart identifies source records and reconciliation status.
- Multi-currency totals state the translation date and rate source.
- Forecast, commitment, accounting actual, and paid amount remain separate
  series and are never visually merged under “расходы”.
- Missing or stale data is shown as unavailable, not as zero.
- Restatements preserve the reporting cut-off and explain changed values.

## Accessibility and export

Charts support keyboard inspection where interactive, have a concise text
summary, preserve meaning without color, and remain legible at 200% zoom. PDF
and print exports include labels, period, units, and source timestamp.
