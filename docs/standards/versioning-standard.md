# Versioning Standard

## Chosen model

The standard model is `latest + major lines`.

Examples:

- `/latest/`
- `/0.x/`
- `/1.x/`
- `/2.x/`

## Why this model

- simpler user-facing navigation;
- stable URLs for supported lines;
- avoids exposing every patch release as a first-class decision;
- aligns with long-lived documentation rather than package archives.

## Required behaviors

- `latest` must always exist
- Supported major lines must remain accessible
- Breaking lines require migration guidance
- UI version labels must be named consistently across all sites

## Transition rule

Repositories that still use a non-standard version or URL model must track migration work in `codex-docs`.
