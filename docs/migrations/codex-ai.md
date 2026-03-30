# codex-ai Migration Guide

## Status

`planned`

## Target standard

`Docs Standard v1.0`

## Current state

The site explains the package well, but the home page still behaves more like a repository README than a canonical docs landing page.

## Must-have changes

- Replace the current `Home` with the standard landing structure defined in `Home Landing Standard`
- Keep `Home` as a top-level route outside both language guide trees
- Declare `site_url` in `mkdocs.yml` to match the publishing standard
- Add stronger ecosystem-role and related-library blocks
- Align README and PyPI to the docs-first contract
- Keep API reference structure but normalize entry labels if needed

## Optional improvements

- Add migration guidance conventions before the next breaking provider or routing line
- Add clearer language on support boundaries and extras

## Release plan

- Release type: `documentation-only`
- Recommended bump: patch
