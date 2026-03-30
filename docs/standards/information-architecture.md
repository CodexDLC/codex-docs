# Information Architecture Standard

## Ecosystem hub IA

The hub must provide:

- Home
- Libraries catalog
- Updates
- Developers

The hub may additionally expose internal standards, templates, ADR, and migration backlog, but those are contributor-facing references and must not dominate the public landing experience.

## Library IA

Every library docs site must expose this top-level model:

- `Home`
- `Guide (EN)`
- `Руководство (RU)`
- `API Reference`
- `Changelog`
- optional `Roadmap`

`Home` is not part of `Guide (EN)` or `Руководство (RU)`. It is a separate top-level route.

## Required page taxonomy

At minimum, every library must have:

- a canonical top-level home landing page;
- at least one getting-started or overview path;
- both EN and RU guide roots when the repository claims bilingual support;
- architecture or conceptual guide pages;
- source-driven API reference;
- changelog;
- migration guides when breaking changes affect usage.

## Home versus guides

The `Home` page is the language-neutral public entrypoint for the library. It must:

- sit outside both language guide trees;
- link into EN and RU guide entrypoints instead of duplicating them;
- explain package role, quick-start intent, and primary navigation choices;
- behave as a landing page, not as a normal guide article.

The EN and RU guides are content trees. They are not allowed to own the home route.

## Ownership boundary

The hub owns ecosystem IA. Library repositories own library IA inside the standard frame.
