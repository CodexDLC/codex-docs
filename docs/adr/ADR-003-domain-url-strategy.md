# ADR-003: Domain And URL Strategy

## Status

Accepted

## Decision

Use a business-rooted brand domain for the main site and a docs-focused domain or subdomain for the documentation platform.

Target shape:

- business site on the main brand domain
- docs on a dedicated docs domain or subdomain
- path-based library routing within docs where aggregation is centralized

## Rationale

- separates business and documentation concerns cleanly
- supports a future branded experience beyond GitHub Pages
- allows one ecosystem entrypoint while preserving library-specific paths

## Consequences

- transitional GitHub Pages URLs may remain for a time
- redirects must be planned during migration
- final hosting strategy should preserve stable library/version URLs
