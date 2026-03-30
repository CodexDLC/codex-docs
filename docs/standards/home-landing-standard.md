# Home Landing Standard

## Purpose

`Home` is the public front door of a library documentation site. It is a landing page, not a normal article inside a language guide.

## Required behavior

Every library `Home` page must:

1. exist as a top-level route
2. sit outside `Guide (EN)` and `Руководство (RU)`
3. explain what the package is and where it fits in the Codex ecosystem
4. provide primary CTA links into the guide roots and API reference
5. provide changelog or migration links when relevant

## Layout contract

The page may use a landing-style implementation with:

- a fullscreen or high-impact hero
- CTA buttons
- library overview cards or path-selection blocks
- a transition into normal-width documentation content below the hero

The page does not need to be plain markdown-only. A template override is allowed and recommended when a normal docs layout fights the landing design.

## Navigation contract

- `Home` in the top navigation must resolve to this landing page
- the landing page must not appear under the EN sidebar
- the landing page must not appear under the RU sidebar
- the landing page may hide sidebars completely

## Language contract

- the landing page is language-neutral
- bilingual sites must expose both EN and RU guide roots from the landing page
- if one language tree is incomplete, the migration file must say so explicitly
- a broken or missing language tree is a migration gap, not a design choice

## Technical contract

The preferred implementation model is:

1. keep `Home` as its own route in `mkdocs.yml`
2. use a template override for landing-specific shell behavior when needed
3. keep guides, API reference, changelog, and roadmap as ordinary docs pages
4. do not rewrite the entire docs site into a one-off custom frontend

## Failure modes to avoid

- implementing `Home` as the overview page of `Guide (EN)`
- implementing `Home` as the overview page of `Руководство (RU)`
- leaving `Home` visually tied to the wrong sidebar tree
- claiming standard compliance while EN and RU navigation are asymmetric
- inventing repo-specific top-level navigation to hide structural problems
