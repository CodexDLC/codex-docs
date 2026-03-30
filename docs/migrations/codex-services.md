# codex-services Migration Guide

## Status

`planned`

## Target standard

`Docs Standard v1.0`

## Current state

The shell is close to standard, but the landing page is too brief and does not yet act as a complete product entrypoint.

## Must-have changes

- Build a full canonical `Home` landing page according to `Home Landing Standard`
- Keep `Home` outside both language guide trees and avoid inheriting the wrong sidebar context
- Declare `site_url` in `mkdocs.yml` to match the publishing standard
- Align README and PyPI package surfaces to the short-form standard
- Confirm changelog placement and roadmap policy
- Add related-library context and recommended user paths

## Optional improvements

- Introduce migration-guide hooks for future breaking business-engine changes
- Add stronger subsystem summaries on the landing page

## Release plan

- Release type: `documentation-only`
- Recommended bump: patch
