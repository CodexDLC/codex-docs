# codex-platform Migration Guide

## Status

`planned`

## Target standard

`Docs Standard v1.0`

## Current state

Strong architecture and API organization, but the landing page is thinner than the target package-entry model.

## Must-have changes

- Expand `Home` into the canonical library landing shape defined in `Home Landing Standard`
- Keep `Home` outside both language guide trees and route users into them deliberately
- Declare `site_url` in `mkdocs.yml` to match the publishing standard
- Add explicit related libraries and entry paths
- Align README and PyPI with the docs-first package surface contract
- Review roadmap handling and leave it absent unless justified

## Optional improvements

- Add support-version messaging on the landing page
- Standardize terminology between install examples and navigation labels

## Release plan

- Release type: `documentation-only`
- Recommended bump: patch
