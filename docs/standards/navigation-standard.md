# Navigation Standard

## Top-level navigation

Every library site must use the same top-level sections:

- `Home`
- `Guide (EN)`
- `Руководство (RU)`
- `API Reference`
- `Changelog`
- optional `Roadmap`

`Home` must point to the dedicated top-level landing page. It must not be implemented as the overview page of `Guide (EN)` or `Руководство (RU)`.

## Label rules

- Use one canonical label form across all repositories
- Do not alternate between `Guide (RU)` and `Руководство (RU)` without a standard-level decision
- Do not invent repo-specific top-level sections unless the standard is updated
- If the site is bilingual, both `Guide (EN)` and `Руководство (RU)` must exist together
- If bilingual parity is incomplete, the gap must be documented in the migration file instead of silently collapsing navigation

## Ordering

The standard order is fixed:

1. Home
2. Guide (EN)
3. Руководство (RU)
4. API Reference
5. Changelog
6. Roadmap if present

## Sidebar behavior

- The home landing page must not render the EN or RU guide sidebar as its primary navigation context
- The home landing page may hide sidebars entirely if implemented as a landing page override
- Guide pages must render the sidebar for their own language tree
- The home landing page may link to EN and RU guide roots, but may not pretend to belong to either tree
