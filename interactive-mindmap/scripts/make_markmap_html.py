#!/usr/bin/env python3
import html
import re
import sys
from pathlib import Path
from typing import Optional


def clean_mermaid_label(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^root\(\((.*)\)\)$", r"\1", text)
    text = re.sub(r"^([\w\u4e00-\u9fff]+)\(\((.*)\)\)$", r"\2", text)
    text = text.replace('"', "").strip()
    return text


def extract_mermaid_mindmap(source: str) -> Optional[str]:
    match = re.search(r"```mermaid\s+mindmap\s+(.*?)```", source, re.S)
    if not match:
        return None

    outline = []
    for raw in match.group(1).splitlines():
        if not raw.strip():
            continue
        if raw.strip() == "mindmap":
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        level = max(1, indent // 2)
        label = clean_mermaid_label(raw)
        if not label:
            continue
        heading_level = min(level, 6)
        outline.append(f"{'#' * heading_level} {label}")
    return "\n".join(outline).strip()


def normalize_markdown(source: str) -> str:
    extracted = extract_mermaid_mindmap(source)
    if extracted:
        return extracted
    return source.strip()


def build_html(markdown: str, title: str) -> str:
    escaped_markdown = html.escape(markdown, quote=False)
    escaped_title = html.escape(title)
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escaped_title}</title>
  <style>
    html, body {{
      height: 100%;
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: #f7f7f5;
      color: #1f2933;
    }}
    header {{
      height: 48px;
      display: flex;
      align-items: center;
      padding: 0 18px;
      border-bottom: 1px solid #d9ddd6;
      background: #ffffff;
      font-size: 15px;
      font-weight: 650;
    }}
    .markmap {{
      position: relative;
      height: calc(100vh - 49px);
      overflow: hidden;
    }}
    .markmap > svg {{
      width: 100%;
      height: 100%;
    }}
  </style>
  <script>
    window.markmap = {{
      autoLoader: {{
        toolbar: true
      }}
    }};
  </script>
</head>
<body>
  <header>{escaped_title}</header>
  <div class="markmap">
    <script type="text/template">
{escaped_markdown}
    </script>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/markmap-autoloader@latest"></script>
</body>
</html>
"""


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: make_markmap_html.py input.md output.html", file=sys.stderr)
        return 2

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    source = input_path.read_text(encoding="utf-8")
    markdown = normalize_markdown(source)
    title = input_path.stem
    output_path.write_text(build_html(markdown, title), encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
