# Ecosystem Architecture

The Codex docs platform is intentionally split into two layers:

## 1. Ecosystem hub

The hub owns:

- ecosystem landing;
- shared navigation model;
- standards and governance;
- ecosystem roadmap and policy pages;
- links and entry paths across all libraries.

The hub does not own per-library guides or API reference content.

## 2. Per-library documentation

Each library retains ownership of:

- package guides;
- architecture pages;
- API reference;
- library changelog;
- optional library roadmap where justified.

## Platform model

The selected model is `hybrid hub with federated library ownership`.

This gives the ecosystem:

- one canonical entrypoint;
- one shared shell and ruleset;
- no duplication of technical content;
- a scalable way to add future libraries.

## Surface model

Each library is represented through three coordinated surfaces:

1. Ecosystem listing inside the hub
2. Full library landing page inside the library docs
3. Short-form package surface in `README` and PyPI

The long-form explanation is canonical in docs. The short-form package surfaces derive from that narrative.
