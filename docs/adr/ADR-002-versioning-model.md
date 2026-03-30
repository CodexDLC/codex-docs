# ADR-002: Latest Plus Major Lines Versioning

## Status

Accepted

## Decision

Use `latest + major lines` as the user-facing documentation version model.

## Rationale

- Keeps the version selector understandable
- Supports stable documentation URLs
- Avoids overwhelming users with full semver history
- Works well with long-lived support lines

## Consequences

- Repositories must align their version labels
- Breaking lines must ship with migration guidance
- Legacy version layouts need tracked migration work
