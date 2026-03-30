# Libraries Catalog

This catalog defines the current library landscape that the docs platform must support.

| Library | Role | Current docs shape | Standard priority |
| --- | --- | --- | --- |
| `codex-core` | Foundation layer for DTOs, settings, utilities, and PII handling | Mostly aligned, but landing tone and roadmap placement need cleanup | High |
| `codex-platform` | Infrastructure layer: Redis, workers, streams, notifications | Strong architecture/reference split, weaker product landing | High |
| `codex-ai` | Provider-agnostic LLM abstraction layer | Strong package story, weaker canonical landing structure | High |
| `codex-services` | Business logic engines | Good shell, thin landing and roadmap policy gaps | High |
| `codex-django` | Django runtime modules for Codex projects | One of the strongest candidate references for landing design | Reference |
| `codex-django-cli` | CLI scaffolding and blueprint package | Close to target, but naming and palette drift remain | Medium |
| `codex-bot` | Aiogram-based bot framework | Separate migration track because shell and version model drift the most | Critical |

## Metadata contract

Every library onboarded into the platform must expose:

- `library_id`
- `display_name`
- `role`
- `maturity_status`
- `latest_docs_url`
- `supported_version_lines`
- `related_libraries`
- `readme_source`
- `landing_owner`

The canonical metadata shape lives in [Library Metadata Template](../template-pages/library-metadata.md).
