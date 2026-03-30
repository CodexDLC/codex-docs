# ADR-004: Library Ownership Stays In Package Repositories

## Status

Accepted

## Decision

Per-library technical content remains in each package repository. `codex-docs` owns standards, hub pages, templates, and migration governance.

## Rationale

- package teams remain close to their technical content
- source-driven docs stay near code and release workflows
- governance stays centralized without turning into content duplication

## Consequences

- the standard must be explicit and enforceable
- README/PyPI drift must be managed through process and templates
- the hub must link rather than duplicate library API and guide content
