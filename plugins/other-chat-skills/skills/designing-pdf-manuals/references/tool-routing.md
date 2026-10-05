# Tool Routing Reference

## Principle

Choose the smallest toolset that can complete the phase safely. Preserve source truth, least privilege, and explicit tool provenance.

| Need | Preferred route | Gate / fallback behavior |
|---|---|---|
| Project-specific facts in supplied files | File search/read tools | Never guess unseen file content |
| Current public facts, standards, laws, prices, specs | Authoritative web sources | Cite the source and note uncertainty |
| New realistic virtual illustration or diagram | image generation | Label simulations appropriately when exact UI/real-world fidelity matters |
| Substantial image edit | image editing/generation tool | Edit the actual supplied target only |
| Express template/design request | Adobe Express when connected | If unavailable, **No Silent Fallback**; disclose state before alternate design route |
| Adobe image/PDF operation | Adobe tools when connected and suitable | Never claim Adobe execution after a failed connector call |
| Final PDF creation/inspection | Runtime PDF-specific skill/toolchain | Render/reopen all pages before Release |
| External storage/publish/database | Future MCP/plugin adapter | Read-only first; writes need authorization |

## Source Priority

1. User-provided brief and files
2. Project canonical data / approved references
3. Authoritative current sources
4. Clearly labeled assumptions only when safe and necessary

## Adobe Routing

Adobe is an optional adapter, not a hard dependency. Use it when the user explicitly requests Adobe or when connected Adobe capabilities materially improve the result. If access fails, report the failure and the actual alternate route used.

## Image Rules

Use image generation for original explanatory visuals, realistic virtual scenes, diagrams, covers, and visual concepts. For exact software instructions, prefer verified screenshots or clearly mark virtual UI as illustrative.

## PDF Rules

Final verification must include:
- artifact reopen,
- page count and page-size check,
- encryption/openability check,
- font inspection when available,
- render every page,
- visual inspection for clipping/overflow/broken glyphs.
