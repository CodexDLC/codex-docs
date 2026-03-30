# Version Policy

## Standard policy

The docs platform itself is versioned as a governed standard.

- Initial baseline: `Docs Standard v1.0`
- Minor increments: clarifications and non-breaking additions
- Major increments: contract changes that require migration work in library repositories

## Library docs policy

Library documentation uses `latest + major lines`.

Examples:

- `/latest/`
- `/1.x/`
- `/2.x/`

The UI should not expose full patch-level noise as the primary version selection model.

## Release rules

- Documentation-only normalization may ship as a patch release
- A breaking documentation line change must ship with migration guidance
- Previous supported major lines remain accessible for the support window

## Canonical behavior

- `latest` points to the most recent supported stable line
- Major-line pages remain stable and predictable
- Migration guides are required when a new major line changes user paths or concepts
