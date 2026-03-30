# ADR-001: Hybrid Hub Docs Platform Model

## Status

Accepted

## Decision

Use a hybrid hub model: one ecosystem docs hub plus independently owned per-library documentation.

## Rationale

- Gives the ecosystem one canonical entrypoint
- Preserves content ownership in package repositories
- Avoids duplicating guides and API reference in a central monolith
- Scales better than a purely repo-first model

## Consequences

- The hub must define a strong standard
- Library repos must conform to a shared shell and IA contract
- Cross-links and metadata become first-class governance artifacts
