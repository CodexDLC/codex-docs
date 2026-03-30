# codex-core Migration Guide

## Status

`planned`

## Target standard

`Docs Standard v1.0`

## Current state

Strong shell alignment and versioning baseline. Landing tone and roadmap/changelog framing are less aligned with the future platform.

## Must-have changes

- Bring `Home` to the standard library landing structure defined in `Home Landing Standard`
- Keep `Home` as a top-level route outside both `Guide (EN)` and `Руководство (RU)`
- Declare `site_url` in `mkdocs.yml` to match the publishing standard
- Normalize roadmap and changelog placement against the standard
- Remove tone drift such as emoji-led framing where not needed
- Align README with the short-form package surface contract

## Optional improvements

- Add clearer related-libraries blocks
- Tighten public versus internal API narrative on the landing page

## Release plan

- Release type: `documentation-only`
- Recommended bump: patch
