---
name: interactive-mindmap
description: Use when creating XMind-like interactive mind maps from notes, PDFs, outlines, Markdown, Mermaid mindmap blocks, study summaries, or hierarchical content. Produces collapsible, zoomable local HTML mind maps with Markmap, and can optionally advise when real Xmind MCP or Xmind export is needed.
metadata:
  short-description: Create collapsible interactive mind maps
---

# Interactive Mindmap

Use this skill when the user wants a visual mind map that is more interactive than a static Mermaid diagram, especially with click-to-expand/collapse behavior.

## Default Output

Prefer a local Markmap HTML file:

- Works well for study notes and outlines.
- Supports click expand/collapse, pan, zoom, and toolbar controls.
- Uses plain Markdown headings or lists as the source.
- Does not require an Xmind account.

Use the bundled script:

```bash
python3 scripts/make_markmap_html.py input.md output.html
```

The script accepts either:

- normal Markdown headings/lists, or
- a Mermaid `mindmap` code block generated in a prior answer.

## Workflow

1. Create or update a clean Markdown outline first.
2. Keep node labels short enough to scan; put long explanations in a separate study-note file.
3. Generate an `.html` file with `scripts/make_markmap_html.py`.
4. For delivery, provide links to both the editable outline and the interactive HTML.

## When To Use Xmind MCP Instead

Recommend Xmind MCP only when the user specifically wants to create, read, or edit maps in their Xmind cloud account. It requires adding the Xmind MCP server in Codex Desktop settings and authenticating with Xmind.

## HTML Notes

The generated HTML uses `markmap-autoloader` from jsDelivr by default, so the browser needs network access when opening the file. If the user needs fully offline use, download and vendor the Markmap JavaScript assets into the output folder, then update the script tag.
