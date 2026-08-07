# Visual foundations

Status: **Proposed tokens for review**

Exact logo assets and an authoritative external brand-token file were not
present in the repository during this phase. The palette below preserves the
existing ERA graphite and warm paper values, replaces the temporary amber accent
with the requested Deep Green direction, and must be confirmed against the ERA
and EcoCity brand source before production CSS changes.

## Color system

### Core palette

| Token | Proposed value | Role |
|---|---:|---|
| `era.graphite.900` | `#172733` | primary text, navigation, high-emphasis neutral |
| `era.graphite.700` | `#34444D` | secondary headings and icons |
| `era.graphite.500` | `#64727A` | supporting text and metadata |
| `era.green.700` | `#0E5A43` | Deep Green brand accent and selected state |
| `era.green.600` | `#147052` | hover/interactive emphasis |
| `era.green.100` | `#E6F1EC` | selected rows, subtle positive context |
| `era.paper.100` | `#F7F3EB` | warm brand surface, used sparingly |
| `era.canvas` | `#F5F7F6` | application background |
| `era.surface` | `#FFFFFF` | primary working surface |
| `era.border` | `#DDE4E0` | quiet dividers and control boundaries |

Deep Green is an action and identity accent, not a decorative fill. Graphite is
the primary reading color. Large areas remain neutral so that operational data
and exceptions retain meaning.

### Semantic colors

| Meaning | Proposed token | Required use |
|---|---:|---|
| success / completed | `#2F6B52` | text/icon plus explicit status label |
| warning / attention | `#946417` | deadlines or recoverable business risk |
| danger / blocked | `#A3443D` | failure, overdue critical item, destructive action |
| information | `#35637A` | neutral system information |

Color must never carry meaning alone. Every state pairs color with a Russian
label and, where space permits, a Lucide-style icon. Brand green does not mean
“successful” by itself; action selection and business status remain distinct.

### Contrast and themes

- Body text and controls target WCAG 2.2 AA contrast.
- Critical values and small labels target at least 4.5:1 against their surface.
- Focus indicators remain visible at 3:1 against adjacent colors.
- Phase 3 approves the light product theme first. A dark theme is not inferred by
  inverting colors; it requires a separate reviewed token mapping.
- Printing and PDF exports use a separate high-contrast mapping and never depend
  on surface color.

## Typography

Inter is the proposed product typeface because it supports Cyrillic, tabular
figures, long-form operational reading, and the existing Frappe stack. System
fallbacks are `-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, and `sans-serif`.
An alternative corporate font requires Cyrillic proofing and a confirmed web
license before approval.

| Style | Size / line height | Weight | Use |
|---|---:|---:|---|
| Display | `32 / 40` | 500 | owner greeting or one page-defining number |
| Heading 1 | `24 / 32` | 500 | page or object name |
| Heading 2 | `20 / 28` | 500 | major section |
| Heading 3 | `16 / 24` | 500 | subsection or table group |
| Body | `14 / 20` | 400 | default product text |
| Label | `13 / 18` | 500 | fields, table headers, controls |
| Caption | `12 / 16` | 400 | timestamps, source, metadata |

Rules:

- use only weights 400 and 500 in the product interface;
- use sentence case in Russian; do not write navigation or headings in all caps;
- align money and quantities to the right and enable tabular figures;
- keep currency with the value and use thin non-breaking spaces for grouping;
- do not use display type for multiple competing metrics.

## Spacing and layout

The base unit is 4 px. Approved spacing steps are 4, 8, 12, 16, 24, 32, 48,
and 64 px. Components use 8–16 px internally; page sections use 24–48 px. A new
intermediate value requires a design-system change, not a local exception.

- Desktop design baseline: 1440 px viewport, with verification at 1280 px.
- Content width follows the task: tables may use the available workspace;
  reading and forms use a narrower measure.
- Forms use at most two columns and collapse to one when labels or values become
  difficult to scan.
- Whitespace creates hierarchy; avoid extra borders, tinted panels, and shadows
  as substitutes for spacing.

## Shape, elevation, and motion

| Token | Value | Use |
|---|---:|---|
| `radius.control` | 8 px | inputs, buttons, filters |
| `radius.card` | 12 px | bounded summaries and panels |
| `radius.modal` | 16 px | dialogs and focused overlays |
| `border.default` | 1 px | structural boundaries |

Cards have no shadow by default. Popovers and modals may use one subtle elevation
token. Motion is functional, lasts about 120–200 ms, and respects reduced-motion
preferences. No looping animation, parallax, glass effects, gradients, or
decorative blur is part of the baseline.

## Icons and imagery

- Use one outline icon family with 1.5–2 px optical stroke; Lucide is the proposed
  implementation source.
- Standard icon sizes are 16 px in controls, 20 px in navigation, and 24 px only
  for an empty state or major section.
- Icons supplement visible labels for important actions; they do not replace
  unfamiliar business words.
- Project photos are content, not decoration. Always show date, object, author,
  and document relationship when known.
- The ERA logo has clear space and approved light/dark variants; it is never used
  as a repeated background or watermark in daily screens.
