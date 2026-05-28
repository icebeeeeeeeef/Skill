---
name: html-writer
description: Create high-readability local HTML documents for long or complex technical output. Use when Codex should turn codebase/project understanding, deep technical teaching, technical proposals, architecture reviews, bug investigations, or debugging records into a navigable HTML report with diagrams, collapsible evidence, readable styling, and local browser-friendly interaction. Also use when the user explicitly asks for HTML output, a readable local report, expandable/collapsible sections, diagrams, timelines, or a more polished alternative to Markdown for technical material.
---

# HTML Writer

Use this skill to decide when and how to produce a local HTML reading experience instead of plain chat Markdown. Prefer chat for short answers; generate HTML when the material is long, structurally complex, diagram-heavy, or explicitly requested.

## Workflow

1. Classify the task:
   - **Project understanding**: codebase maps, architecture walkthroughs, module explanations, call/data flow reports.
   - **Knowledge teaching**: deep explanations of a technical topic for an experienced engineer who does not know this specific area.
   - **Technical review/debugging**: proposals, design reviews, incident notes, bug investigations, hypothesis/evidence records.
2. If the content is short enough for chat, answer in chat and do not create HTML.
3. If HTML is warranted, read the relevant reference:
   - Knowledge teaching: `references/knowledge-teaching-charter.md`.
   - Project understanding: `references/project-understanding-charter.md`.
   - Technical review/debugging: `references/technical-review-debugging-charter.md`.
4. Choose an output location:
   - For a repo/project task, write under that project in `reports/` or `.codex/reports/`.
   - For standalone teaching/tutorial material, write under the current Codex working directory unless the user specifies a path.
   - Respect an explicit user-provided path.
5. Build from the assets when useful:
   - `assets/templates/report.html` for the report shell.
   - `assets/styles/report.css` for the visual system.
   - `assets/scripts/report.js` for navigation and reading interactions.
   - `assets/examples/components.html` for copyable component patterns.
   - `scripts/create-report.py` to initialize a report folder without imposing content structure.
6. Return a concise chat summary plus the local HTML path. If a server/browser is used, include the URL.

## Global HTML Principles

- Put the useful top-level answer near the top.
- Keep the main reading path visible and push secondary material into collapsible sections.
- Use diagrams when relationships, state, timing, topology, data movement, or lifecycle changes matter.
- Use a table of contents for long pages. Add timelines, phase bars, module maps, or evidence indexes only when they improve comprehension.
- Use `details` / `summary` for evidence, logs, command output, long code, alternatives, or side paths.
- Keep file paths, commands, config keys, API names, class/function names, protocols, and error codes in monospace.
- Use Chinese explanations when the user writes Chinese; keep technical identifiers in English.
- On first use of important English terms, explain them in Chinese and keep later wording consistent.
- Avoid decorative UI, ornamental icons, and visual effects that do not improve understanding.
- Mark uncertainty explicitly. Do not invent version numbers, performance figures, APIs, or source claims.

## Scenario Defaults

### Project Understanding

Optimize for fast map-building and navigation.

- Main chain: scope -> executive summary -> project map -> modules -> call/data flow -> key files -> next exploration paths.
- Use module maps, dependency diagrams, data flow diagrams, and file indexes when helpful.
- Fold at a medium level: show architecture and main chains; collapse command output, file excerpts, secondary modules, and alternative paths.

### Knowledge Teaching

Optimize for deep understanding.

- Follow `references/knowledge-teaching-charter.md`.
- Keep article flow continuous and avoid excessive folding.
- Use diagrams aggressively when the topic is abstract. For example, a Raft explanation should include role relationships, election timing, log replication flow, and state transitions where useful.
- Include a hands-on validation step: runnable code, mental simulation, or thought experiment.

### Technical Review Or Debugging

Optimize for judgment plus traceability.

- Main chain: problem/goal -> constraints -> current conclusion -> options/hypotheses -> evidence -> tradeoffs/risks -> decision -> next actions.
- Use timelines, status tags, risk tables, evidence blocks, and collapsible raw material.
- Fold aggressively: keep conclusion, risk, and next actions visible; collapse logs, command output, failed attempts, and long traces.

## Dependencies For Full Experience

This skill is optimized for local rich reading, not zero-dependency portability. Use external or locally installed libraries when they materially improve the output.

Recommended dependencies:

- `mermaid` or `@mermaid-js/mermaid-cli`: flowcharts, architecture diagrams, sequence diagrams, state diagrams.
- `markmap-cli`: knowledge trees, module trees, concept maps.
- `prismjs`: code highlighting.
- `katex`: formulas and mathematical notation when needed.

Use Mermaid first for most diagrams. Use Markmap for tree-shaped explanations. Use Prism for code-heavy reports. Use KaTeX only when formulas genuinely help. Avoid heavier visualization libraries such as D3 or ECharts unless the user asks for data-heavy visualization.

If a report depends on CDN or locally installed libraries, state that in the final chat summary or inside the report metadata.

## Assets

The bundled assets are meant to be copied into the output report, not loaded into model context every time.

- `assets/templates/report.html`: base shell with placeholders.
- `assets/styles/report.css`: shared typography, layout, callouts, timelines, evidence blocks, decision tables, and responsive rules.
- `assets/scripts/report.js`: table of contents, reading progress, current heading highlight, expand/collapse all, copy code, and optional Mermaid/Markmap/KaTeX/Prism initialization.
- `assets/examples/components.html`: copyable component examples.
- `scripts/create-report.py`: initializes a report folder and fills basic metadata. It must not decide scenario content.

## Quality Bar

Before finishing, verify:

- The report answers the user's actual task and does not merely look polished.
- The chosen scenario structure matches the task.
- Important details are findable through headings, anchors, or navigation.
- Folded content is secondary, not essential to understanding the main answer.
- Diagrams are used where they clarify structure or flow.
- The HTML opens locally and asset paths resolve.
- The final response includes the created path or URL.
