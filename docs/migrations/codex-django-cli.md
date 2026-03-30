# codex-django-cli Migration Guide

## Status

`completed`

## Target standard

`Docs Standard v1.0`

## Current state

Close to the target package model, but palette and label drift remain and should be removed before the shell is declared canonical.

## Must-have changes

- Normalize palette and theme behavior to the shared shell
- Align navigation labels with the standard
- Bring `Home` and README into the canonical package-entry shape
- Keep `Home` outside both language guide trees and validate EN/RU parity explicitly
- Validate roadmap placement against the standard

## Optional improvements

- Add stronger related-library explanation for the runtime companion relationship
- Tighten install and quick-start hierarchy

## Release plan

- Release type: `documentation-only`
- Recommended bump: patch
