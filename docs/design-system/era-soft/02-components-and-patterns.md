# Components and interaction patterns

## Component contract

Every component defines anatomy, variants, states, keyboard behavior, responsive
behavior, Russian wording, and its source-data relationship. A locally styled
copy is not a new component; it is design-system debt.

## Buttons and actions

### Hierarchy

| Variant | Use | Limit |
|---|---|---|
| Primary | the safest expected next action | one per action group |
| Secondary | valid alternative or supporting action | two before overflow |
| Ghost | low-emphasis navigation or utility | use with visible label |
| Destructive | irreversible or materially harmful action | confirmation required |
| Icon-only | universal utility such as close | must have accessible name |

The Russian label **Создать** is consistent everywhere. Add the entity only when
the context is ambiguous: **Создать заявку**. Use verbs, not nouns. Disable an
action only when the reason is shown nearby; otherwise hide actions the role can
never perform.

States: default, hover, focus-visible, pressed, loading, disabled, success, and
error. Loading preserves button width and prevents duplicate submission.

## Navigation

- The global shell contains: Главная, Строительство, Закупки, Финансы, Проекты,
  Поставщики, Сотрудники, Отчеты, Настройки.
- **Строительство** is the primary operational workspace.
- Within an object, the persistent local navigation is: Обзор, Бюджет, Закупки,
  Договоры, Материалы, Подрядчики, Оплаты, Документы, Фото, Аналитика.
- The selected object remains visible when a user moves between its sections.
- Breadcrumbs explain hierarchy; they do not duplicate the main navigation.
- Framework modules and infrequent setup are accessible to permitted roles but
  are not promoted into daily navigation.

## Tables

Tables are the primary high-density operational view.

Required anatomy: view title, item count, search when justified, active filters,
primary action, column headers, rows, selection/action state, pagination, and
empty/error/loading states.

Rules:

- use a quiet surface, horizontal separators, and no vertical gridlines;
- keep the identifying field leftmost and row actions at the end;
- right-align numbers, money, quantities, and percentages;
- sort explicitly and show the active direction;
- place status text near the entity name or deadline, not in a distant legend;
- use sticky headers for long lists and preserve horizontal context;
- do not truncate the only identifying value without an accessible full value;
- bulk selection appears only when a reviewed bulk action exists;
- saved views belong to roles and tasks, not to arbitrary technical filters.

Density modes are **Comfortable** and **Compact**. Comfortable is the product
default; Compact is available for procurement, finance, and stock roles after
the content survives usability review.

## Cards

Cards group one coherent summary or action. A card is not the default container
for every piece of content.

- One card answers one question.
- The title names the business concept; the value includes unit and period.
- A KPI card exposes source freshness and drill-through.
- No more than three peer KPI cards lead a page unless the design review shows
  that the user's decision genuinely requires more.
- Avoid nested cards and decorative shadows.

The project card pattern contains object name, accountable manager, progress,
one financial or schedule exception, and the next relevant action. It does not
duplicate the entire project report.

## Forms

Forms follow the user's decision sequence, not DocType field order.

1. Context and relationship: company, object, supplier/contractor.
2. Business facts: dates, lines, quantities, prices, budget relationship.
3. Consequences: totals, warehouse, payment terms, accounting effect.
4. Supporting detail: attachments, comments, audit metadata.

Rules:

- show only required daily fields initially;
- use one label above each field and persistent units;
- explain why a field is required when business meaning is not obvious;
- validate near the field and summarize blocking errors at submission;
- preserve user input after recoverable failures;
- place accounting and developer fields in a reviewed advanced section;
- use autocomplete for large masters, not unbounded select lists;
- autosave only where users understand draft semantics.

## Filters and search

- Search finds an entity by its human identifier, counterparty, or approved
  reference—not by internal fieldname.
- Common filters are visible. Advanced filters open progressively.
- Active filters appear as removable chips and the result count updates clearly.
- **Сбросить** restores the role's approved default view, not an unknowable blank
  state.
- Date filters show explicit periods and timezone. Financial views always state
  company and currency.

## Statuses

Each business status has one Russian label, semantic meaning, allowed next
actions, and source-of-truth field. Status badges use text plus restrained color.

Recommended status families:

- neutral: Черновик, Запланировано;
- active: На согласовании, В работе, В пути;
- positive: Утверждено, Принято, Оплачено, Завершено;
- attention: Требует внимания, Частично, Срок сегодня;
- critical: Просрочено, Заблокировано, Отклонено, Отменено.

Do not calculate a visual status from client-side guesses when ERPNext or ERA
business logic owns the authoritative state.

## Notifications and messages

| Pattern | Use |
|---|---|
| Inline message | field or section-specific guidance and validation |
| Toast | confirmation of a completed reversible action |
| Notification center | asynchronous events that can wait |
| Risk item | owner/project exception requiring a decision |
| Blocking dialog | permission, conflict, or irreversible consequence |

Success toasts disappear automatically and do not contain critical information.
Errors remain until resolved or dismissed. Notifications state what happened,
which record is affected, and the next safe action.

## Modals and drawers

- Use a modal for confirmation or one short focused decision.
- Use a side drawer for inspecting related detail without losing list context.
- Use a full page for multi-step forms, complex line items, reconciliation, or
  work that needs a stable URL.
- Destructive confirmation names the record and consequence. Requiring a typed
  name is reserved for unusually high-risk actions.

## Empty, loading, error, and permission states

- Empty: explain whether no records exist or filters excluded them; offer one
  valid next action.
- Loading: preserve layout with restrained skeletons; do not show false zeroes.
- Error: preserve context, explain recoverability, and provide a retry or support
  path with a reference ID.
- Permission denied: do not expose protected values; state which role or owner
  can grant access.
- Stale data: show last refresh and avoid presenting an old value as current.
