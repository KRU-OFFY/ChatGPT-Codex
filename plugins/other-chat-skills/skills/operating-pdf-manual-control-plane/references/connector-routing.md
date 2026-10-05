# Connector Routing

The MCP control plane owns workflow state and gates. It is not a substitute for specialist execution tools.

| Need | Preferred adapter | Control-plane action |
|---|---|---|
| Generate/edit graphic assets | Adobe/Express/Firefly or host image tool | Register generated asset version |
| Create/inspect PDF | Adobe PDF/Acrobat or host PDF tool | Record PDF artifact and preflight evidence |
| Save/share project files | Google Drive or approved storage connector | Register durable URI/reference |
| Publish/distribute | Explicit publishing connector chosen by user | Get release manifest first, then record publish result |

## Routing Rules

1. Discover or resolve the connector in the target workspace. Do not copy opaque connector IDs from another workspace.
2. Use read-only access for discovery and inspection when sufficient.
3. Treat create/update/upload/publish as writes and honor host confirmation/permission policy.
4. Do not publish unless the project is `RELEASED` and `manual_get_release_manifest` succeeds.
5. After an external publish attempt, record its outcome with `manual_record_publish_result`.
6. If a required connector is unavailable, apply **No Silent Fallback** and surface the blocker.

The package includes `connector-bindings/.app.json.example` only as a configuration template. It is intentionally not active until real workspace connector IDs are supplied.
