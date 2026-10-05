# Plugin-Ready Upgrade Path

This directory describes how the skill can later be wrapped by a plugin/MCP layer. It is **not** an official marketplace manifest.

## Separation of Responsibilities

- Skill: reasoning policy, workflow order, Page Map, design system, QA, release gates.
- Adapter: invokes an external app/service using a narrow contract.
- Plugin/MCP package: authentication, permissions, tool schemas, deployment, observability, and connector lifecycle.

## Recommended Adapter Families

- `files.read/search` — source-grounding
- `research.web` — current authoritative research
- `image.generate/edit` — visual production
- `design.adobe_express` — template/design operations
- `pdf.create/preflight` — final PDF production and inspection
- `storage.drive` — save/version artifacts
- `publish.external` — external release, always approval-gated

## Upgrade Rule

Do not move workflow policy into vendor adapters. A connector can change without changing the core states or quality gates.
