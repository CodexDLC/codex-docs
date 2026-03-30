# API Reference Standard

## Baseline

API reference remains source-driven through `mkdocstrings`.

## Required rules

- API reference is English-only
- Public API and internal modules must be separated clearly
- Navigation labels should be consistent across libraries
- Generated pages must not replace conceptual guide pages

## Required entrypoints

- `Overview`
- `Public API`
- `Internal Modules` when relevant

## Constraints

- The hub does not aggregate all API pages into one monolith
- The hub links to each library API section instead
- Libraries must mark unstable or internal areas clearly
