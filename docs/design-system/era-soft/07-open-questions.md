# Open questions before implementation

## P0 — blocks design-system approval

1. Which exact ERA/EcoCity brand files are authoritative for graphite, Deep
   Green, warm surfaces, logo clear space, and icon usage? The repository only
   contains the temporary visual-baseline assets.
2. Is Inter the approved product font, and is there a licensed corporate font
   with complete Russian and future Kyrgyz coverage?
3. Who has final design approval, and who owns ongoing design-system changes?
4. What is the supported daily desktop baseline: 1280, 1440, or another managed
   resolution? Is tablet entry required, or only responsive viewing?
5. Which density is preferred by procurement and finance users after one day of
   realistic data entry: Comfortable or Compact?
6. Which Owner Dashboard concepts are approved as the first hierarchy: cash,
   projects, today, risks? Which should be removed before data contracts are
   written?
7. Is the construction-object local navigation complete and correctly ordered?

## P0 — blocks Owner Dashboard implementation

1. Define **Доступные денежные средства**: included accounts, restricted funds,
   pending bank entries, companies, currencies, and update latency.
2. Define project progress: physical quantities, weighted tasks, certified work,
   earned value, or another method.
3. Define what makes a budget variance, supplier delay, contract, or payment an
   owner-level risk and how severity is ranked.
4. Define the owner approval boundary and whether approval can occur directly
   from the dashboard.
5. Define consolidated currency translation and reporting cut-off.

## P0 — blocks Construction Workspace implementation

1. Confirm the canonical object hierarchy and whether block/floor/work category
   are all visible in the first overview.
2. Approve the definitions of initial budget, revised budget, commitment, actual,
   paid, forecast, remaining, and variance from the architecture pack.
3. Identify the authoritative schedule and physical-progress sources for the
   first pilot.
4. Decide required object-photo metadata, retention, permissions, and storage.
5. Approve which contract and service-acceptance gaps require ERA extensions.

## P1 — resolve during detailed screen design

- keyboard shortcuts and command palette scope;
- saved-view ownership and sharing;
- exact table column defaults per role;
- notification channels and escalation timing;
- audit-history presentation for non-accountants;
- offline and degraded-network expectations for construction sites;
- print/PDF layouts and signing requirements;
- future Kyrgyz string expansion and typography verification;
- dark-theme demand and separate approval timing.

## Review record

| Decision | Owner | Status | Evidence/version |
|---|---|---|---|
| Palette and typography | Product owner | Open | Phase 3 draft |
| Owner Dashboard hierarchy | Product owner | Open | Phase 3 concept |
| Construction object shell | Construction process owner | Open | Phase 3 concept |
| Screen review gate | Product + Engineering | Open | ADR 0002 |
