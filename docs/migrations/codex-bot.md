# codex-bot Migration Guide

## Status

`planned`

## Target standard

`Docs Standard v1.0`

## Current state

The repository has the strongest visible drift in palette, top-level shell behavior, and live version model.

## Must-have changes

- Migrate theme and feature flags to the shared shell
- Adopt the `latest + major lines` version model
- Normalize `Home` landing page structure to `Home Landing Standard`
- Keep `Home` outside both language guide trees and document any language gap explicitly
- Declare `site_url` in `mkdocs.yml` to match the publishing standard
- Align README and package positioning to the docs-first contract
- Track URL migration carefully because this site differs from the others

## Optional improvements

- Reduce legacy tone and stylistic divergence
- Add a stronger related-libraries block to position the framework in the wider stack

## Release plan

- Release type: `documentation-only`
- Recommended bump: patch after shell migration is complete
