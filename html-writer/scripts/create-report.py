#!/usr/bin/env python3
"""Initialize a local HTML report skeleton from html-writer assets."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import shutil
from pathlib import Path


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def copy_assets(root: Path, output: Path) -> None:
    asset_root = root / "assets"
    for subdir in ("styles", "scripts"):
        src = asset_root / subdir
        dst = output / "assets" / subdir
        dst.mkdir(parents=True, exist_ok=True)
        for item in src.iterdir():
            if item.is_file():
                shutil.copy2(item, dst / item.name)


def render_template(root: Path, args: argparse.Namespace) -> str:
    template = (root / "assets" / "templates" / "report.html").read_text(encoding="utf-8")
    now = dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
    body = f"""        <section class=\"summary-panel\">
          <h2>摘要</h2>
          <p>在这里写主结论、核心 insight 或当前判断。</p>
        </section>

        <h2>正文</h2>
        <p>替换这段内容。根据任务类型读取对应 reference，不要把三类场景强行套进同一个结构。</p>

        <details>
          <summary>次要细节</summary>
          <p>把证据、命令输出、推导过程或补充材料放在这里。</p>
        </details>
"""
    values = {
        "title": html.escape(args.title),
        "subtitle": html.escape(args.subtitle),
        "scenario": html.escape(args.scenario),
        "generated_at": html.escape(now),
        "reading_strategy": html.escape(args.reading_strategy),
        "dependency_note": html.escape(args.dependency_note),
        "body": body.rstrip(),
    }
    for key, value in values.items():
        template = template.replace("{{" + key + "}}", value)
    return template


def main() -> int:
    parser = argparse.ArgumentParser(description="Create an html-writer report skeleton.")
    parser.add_argument("--title", required=True, help="Report title.")
    parser.add_argument("--output", required=True, help="Output directory.")
    parser.add_argument("--subtitle", default="Readable local HTML report", help="Report subtitle.")
    parser.add_argument("--scenario", default="technical-report", help="Scenario label.")
    parser.add_argument(
        "--reading-strategy",
        default="scenario-adaptive",
        help="Short reading strategy description.",
    )
    parser.add_argument(
        "--dependency-note",
        default="Uses local assets; optional CDN libraries enable diagrams, formulas, and code highlighting.",
        help="Dependency note shown in the metadata panel.",
    )
    args = parser.parse_args()

    root = skill_root()
    output = Path(args.output).expanduser().resolve()
    output.mkdir(parents=True, exist_ok=True)
    copy_assets(root, output)
    (output / "index.html").write_text(render_template(root, args), encoding="utf-8")
    print(output / "index.html")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
