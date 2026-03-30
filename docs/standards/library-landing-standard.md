# Library Landing Standard

## Purpose

A library landing page is the canonical long-form entrypoint for a package. It is not a raw README dump.

This standard applies to the top-level `Home` route of a library docs site unless an approved ADR says otherwise.

## Required sections

Every library landing page must include:

1. Package definition in one line
2. Role in the Codex ecosystem
3. Install block
4. Quick start block
5. Recommended entry paths
6. Module or subsystem map
7. API reference entrypoint
8. Changelog and migration links
9. Related libraries block
10. Explicit links into EN and RU guides when the site is bilingual

## Recommended section order

1. Title and one-line definition
2. Value proposition and ecosystem role
3. Install
4. Quick start
5. Choose your path
6. Runtime or module map
7. Language/reference split
8. Changelog and migration
9. Related libraries

## Route contract

- The landing page route must be the top-level `Home` item in navigation
- The landing page must not be nested under `Guide (EN)` or `Руководство (RU)`
- The landing page may be implemented with a template override instead of plain markdown when the design requires a landing-style hero
- The landing page must degrade gracefully when CSS or JavaScript enhancements are absent

## Language contract

- The landing page itself is language-neutral
- EN and RU content trees must have their own guide roots
- Buttons and entry links on the landing page must route users into the correct language trees deliberately
- A bilingual library must not expose only one language in the shell while still claiming the standard is complete

## Style rules

- Product-facing prose must be concise and explicit
- No repo-specific color or tone drift without approval
- Avoid emoji-led design unless justified by a standard exception
- Landing pages must explain how the package fits into the ecosystem, not just what modules exist

## Implementation guidance for agents

When an agent is updating a library repository, it must treat the landing page as a shell-level feature, not as an ordinary guide article. The safe implementation order is:

1. verify `mkdocs.yml` top-level nav
2. verify EN and RU guide roots
3. implement or update the top-level `Home`
4. wire landing buttons into guide and API entrypoints
5. validate that the home route does not inherit the wrong sidebar context

## Source of truth

The library landing page in docs is the canonical source for package narrative. README and PyPI derive from it.
