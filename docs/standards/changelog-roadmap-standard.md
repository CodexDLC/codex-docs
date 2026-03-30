# Changelog and Roadmap Standard

## Distinction

Changelog and roadmap serve different functions and must not be merged into one page.

- `Changelog`: release history and user-impacting change log
- `Roadmap`: forward-looking direction and planned work

## Library-level requirements

- Every library must have a changelog
- Roadmap is optional, but if present it must follow the same naming and placement model
- Documentation-only releases must be marked explicitly

## Ecosystem-level requirements

- The hub owns one ecosystem roadmap
- The hub may own a governance changelog or highlights feed
- The hub does not duplicate full library changelogs

## Migration requirement

When a changelog entry corresponds to a breaking documentation change, add or update a migration guide and cross-link it from the landing page and changelog.
