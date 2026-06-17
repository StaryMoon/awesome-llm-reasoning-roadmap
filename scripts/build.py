#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import shutil
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.json"
TRACKS = ROOT / "data" / "tracks.json"
README = ROOT / "README.md"
DOCS = ROOT / "docs" / "index.html"
TRACK_DOCS = ROOT / "docs" / "tracks"
ASSETS = ROOT / "assets"

TRACK_ORDER = [
    "Foundations",
    "Decoding and Decomposition",
    "Search and Deliberation",
    "Agents and Tools",
    "Verification and Rewards",
    "Reasoning RL",
    "Test-Time Scaling",
    "Reasoning Data and Recipes",
    "Evaluation and Stress Tests",
    "Frontier Reports",
    "Survey and Meta",
]

COLORS = {
    "Foundations": "#3867d6",
    "Decoding and Decomposition": "#20bf6b",
    "Search and Deliberation": "#8854d0",
    "Agents and Tools": "#fa8231",
    "Verification and Rewards": "#eb3b5a",
    "Reasoning RL": "#0fb9b1",
    "Test-Time Scaling": "#f7b731",
    "Reasoning Data and Recipes": "#2d98da",
    "Evaluation and Stress Tests": "#a55eea",
    "Frontier Reports": "#4b6584",
    "Survey and Meta": "#778ca3",
}


def esc(text: object) -> str:
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def load() -> tuple[list[dict], list[dict]]:
    papers = json.loads(DATA.read_text(encoding="utf-8"))["papers"]
    tracks = json.loads(TRACKS.read_text(encoding="utf-8"))["tracks"]
    return papers, tracks


def paper_link(item: dict) -> str:
    label = item.get("venue") or item.get("arxiv_id") or "Paper"
    return f"[{label}]({item['paper_url']})"


def code_links(item: dict) -> str:
    parts = []
    if item.get("official_code"):
        parts.append(f"[Official]({item['official_code']})")
    if item.get("starymoon_repo"):
        parts.append(f"[Unofficial]({item['starymoon_repo']})")
    return " / ".join(parts) if parts else "-"


def method_tags(item: dict, n: int = 5) -> str:
    return ", ".join(item.get("tags", [])[:n])


def table_rows(papers: list[dict], track: str | None = None) -> list[str]:
    rows = []
    for item in papers:
        if track and item["track"] != track:
            continue
        rows.append(
            "| {year} | [{title}]({paper_url}) | {track} | {stage} | {code} | {tags} |".format(
                year=item["year"],
                title=item["title"].replace("|", "\\|"),
                paper_url=item["paper_url"],
                track=item["track"],
                stage=item["stage"],
                code=code_links(item),
                tags=method_tags(item).replace("|", "/"),
            )
        )
    return rows


def render_timeline_svg(papers: list[dict]) -> str:
    years = sorted({int(p["year"]) for p in papers})
    lanes = [t for t in TRACK_ORDER if any(p["track"] == t for p in papers)]
    width = 1600
    lane_h = 78
    top = 90
    left = 210
    right = 80
    height = top + lane_h * len(lanes) + 70
    year_min, year_max = min(years), max(years)

    def x_for(year: int, index: int = 0, total: int = 1) -> float:
        span = max(1, year_max - year_min)
        base = left + (year - year_min) / span * (width - left - right)
        if total <= 1:
            return base
        return base + (index - (total - 1) / 2) * 24

    by_year_lane: dict[tuple[int, str], list[dict]] = defaultdict(list)
    for p in papers:
        by_year_lane[(int(p["year"]), p["track"])].append(p)

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#fbfcff"/>',
        '<text x="40" y="46" font-family="Inter,Arial,sans-serif" font-size="30" font-weight="700" fill="#17202a">LLM Reasoning Roadmap</text>',
        '<text x="40" y="74" font-family="Inter,Arial,sans-serif" font-size="16" fill="#667085">From Chain-of-Thought to Test-Time Scaling and Reasoning RL</text>',
    ]
    for year in years:
        x = x_for(year)
        lines.append(f'<line x1="{x:.1f}" y1="{top-24}" x2="{x:.1f}" y2="{height-45}" stroke="#e5e7ef" stroke-width="1"/>')
        lines.append(f'<text x="{x:.1f}" y="{top-34}" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="14" fill="#667085">{year}</text>')
    for lane_i, lane in enumerate(lanes):
        y = top + lane_i * lane_h
        color = COLORS.get(lane, "#778ca3")
        lines.append(f'<text x="40" y="{y+32}" font-family="Inter,Arial,sans-serif" font-size="14" font-weight="700" fill="{color}">{esc(lane)}</text>')
        lines.append(f'<line x1="{left}" y1="{y+28}" x2="{width-right}" y2="{y+28}" stroke="#edf0f5" stroke-width="2"/>')
        for year in years:
            items = by_year_lane.get((year, lane), [])
            for j, item in enumerate(items):
                x = x_for(year, j, len(items))
                label = item["short"]
                lines.append(f'<circle cx="{x:.1f}" cy="{y+28}" r="9" fill="{color}" opacity="0.95"/>')
                lines.append(f'<text x="{x:.1f}" y="{y+53}" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="11" fill="#17202a">{esc(label)}</text>')
    lines.append("</svg>")
    return "\n".join(lines)


def render_method_map_svg(papers: list[dict]) -> str:
    stages = ["Prompting", "Decoding", "Search", "Agent", "Verifier", "RL", "Scaling", "Data", "Benchmark", "Report", "Survey", "Failure"]
    counts = Counter(p["stage"] for p in papers)
    width, height = 1200, 670
    max_count = max(counts.values()) if counts else 1
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        '<text x="42" y="54" font-family="Inter,Arial,sans-serif" font-size="28" font-weight="700" fill="#17202a">Reasoning Method Map</text>',
        '<text x="42" y="82" font-family="Inter,Arial,sans-serif" font-size="16" fill="#667085">A compact view of where the curated papers sit in the reasoning stack.</text>',
    ]
    card_w = 250
    card_h = 118
    gap_x = 28
    gap_y = 34
    start_x = 42
    start_y = 122
    for i, stage in enumerate(stages):
        row, col = divmod(i, 4)
        x = start_x + col * (card_w + gap_x)
        y = start_y + row * (card_h + gap_y)
        value = counts.get(stage, 0)
        bar = 172 * value / max_count
        color = "#2457ff" if value else "#c9ced8"
        lines += [
            f'<rect x="{x}" y="{y}" width="{card_w}" height="{card_h}" rx="14" fill="#f8faff" stroke="#e5e8f0"/>',
            f'<text x="{x+18}" y="{y+34}" font-family="Inter,Arial,sans-serif" font-size="17" font-weight="700" fill="#17202a">{stage}</text>',
            f'<text x="{x+18}" y="{y+61}" font-family="Inter,Arial,sans-serif" font-size="13" fill="#667085">{value} papers</text>',
            f'<rect x="{x+18}" y="{y+82}" width="172" height="10" rx="5" fill="#e8ecf5"/>',
            f'<rect x="{x+18}" y="{y+82}" width="{bar:.1f}" height="10" rx="5" fill="{color}"/>',
        ]
    lines.append("</svg>")
    return "\n".join(lines)


def render_track_doc(track: dict, papers_by_id: dict[str, dict]) -> str:
    lines = [
        f"# {track['title']}",
        "",
        track["hook"],
        "",
        f"**Good for:** {track['audience']}",
        "",
        f"**Why it is hot:** {track['why_hot']}",
        "",
        "## Reading Route",
        "",
        "| Step | Paper | Why read it | Code |",
        "|---:|---|---|---|",
    ]
    for idx, paper_id in enumerate(track["papers"], 1):
        item = papers_by_id.get(paper_id)
        if not item:
            continue
        lines.append(
            "| {idx} | [{title}]({url}) | {takeaway} | {code} |".format(
                idx=idx,
                title=item["title"].replace("|", "\\|"),
                url=item["paper_url"],
                takeaway=item["takeaway"].replace("|", "/"),
                code=code_links(item),
            )
        )
    lines += [
        "",
        "## What to Compare",
        "",
    ]
    lines.extend(f"- {point}" for point in track["compare"])
    lines += ["", "[Back to roadmap](../../README.md)", ""]
    return "\n".join(lines)


def render_readme(papers: list[dict], tracks: list[dict]) -> str:
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    by_track: dict[str, list[dict]] = defaultdict(list)
    for paper in papers:
        by_track[paper["track"]].append(paper)
    lines = [
        "# Awesome LLM Reasoning Roadmap",
        "",
        '<div align="center">',
        "",
        "**From Chain-of-Thought to Test-Time Scaling and Reasoning RL.**",
        "",
        f"![Papers](https://img.shields.io/badge/papers-{len(papers)}-blue) "
        f"![Tracks](https://img.shields.io/badge/reading_tracks-{len(tracks)}-purple) "
        f"![Updated](https://img.shields.io/badge/updated-{updated}-green) "
        "![License](https://img.shields.io/badge/license-MIT-green)",
        "",
        "[Visual roadmap](#visual-roadmap) · [Reading tracks](#reading-tracks) · "
        "[Paper atlas](#paper-atlas) · [Searchable page](docs/index.html) · [Data](data/papers.json)",
        "",
        "</div>",
        "",
        "> A focused, visual reading map for LLM reasoning papers. If this helps your reading, reproduction, or research planning, please consider starring the repo and following [@StaryMoon](https://github.com/StaryMoon).",
        "",
        "## Why This Repo",
        "",
        "The LLM reasoning literature is no longer one neat topic. It now mixes prompting, decomposition, search, tool use, verifiers, process rewards, test-time scaling, and RL systems. This repo is a focused map for that stack.",
        "",
        "What makes it different from a normal awesome list:",
        "",
        "- **One clear theme**: LLM reasoning, not a broad AI dump.",
        "- **Visual-first structure**: timeline and method-map SVGs are generated from the dataset.",
        "- **Reading routes**: each route explains who should read it and what to compare.",
        "- **Code-aware atlas**: paper links, official code, and StaryMoon unofficial repos are shown together when available.",
        "- **Machine-readable data**: all entries live in `data/papers.json` and `data/tracks.json`.",
        "",
        "## Visual Roadmap",
        "",
        "![LLM reasoning roadmap](assets/llm-reasoning-roadmap.svg)",
        "",
        "![Reasoning method map](assets/reasoning-method-map.svg)",
        "",
        "## Adoption / Related PRs",
        "",
        "| Repository | PR | Status | Context |",
        "|---|---|---|---|",
        "| `atfortes/Awesome-LLM-Reasoning` | [#78](https://github.com/atfortes/Awesome-LLM-Reasoning/pull/78) | Open | Adds this visual roadmap as a related reasoning resource. |",
        "| `mbzuai-oryx/Awesome-LLM-Post-training` | [#30](https://github.com/mbzuai-oryx/Awesome-LLM-Post-training/pull/30) | Open | Adds this roadmap to post-training and reasoning-resource references. |",
        "| `4IK1d/awesome-llm-reasoning` | [#2](https://github.com/4IK1d/awesome-llm-reasoning/pull/2) | Open | Adds the roadmap in the related awesome-list section. |",
        "",
        "## Reading Tracks",
        "",
        "| Track | Good for | Why it is hot | Route |",
        "|---|---|---|---|",
    ]
    for track in tracks:
        route = ", ".join(f"`{papers_by_id[p]['short']}`" for p in track["papers"] if p in papers_by_id)
        lines.append(f"| [{track['title']}](docs/tracks/{track['id']}.md) | {track['audience']} | {track['why_hot']} | {route} |")

    lines += ["", "## Paper Atlas", ""]
    for track_name in TRACK_ORDER:
        rows = table_rows(papers, track_name)
        if not rows:
            continue
        lines += [
            f"### {track_name}",
            "",
            "| Year | Paper | Track | Stage | Code | Tags |",
            "|---:|---|---|---|---|---|",
        ]
        lines.extend(rows)
        lines.append("")

    lines += [
        "## Use the Data",
        "",
        "```bash",
        "python scripts/build.py",
        "python -m json.tool data/papers.json",
        "```",
        "",
        "The static page at [`docs/index.html`](docs/index.html) provides a searchable table and visual track cards.",
        "",
        "## Contribution Ideas",
        "",
        "- Add newly released reasoning RL papers.",
        "- Add official code links when authors release them.",
        "- Add benchmark tags for math, code, tool-use, long-context, and multimodal reasoning.",
        "- Add reproduction notes that compare inference-time scaling and training-time RL recipes.",
        "",
        "## Disclaimer",
        "",
        "This is an independent curated roadmap. Paper names, official code, datasets, models, and trademarks belong to their respective owners. Linked StaryMoon repositories are unofficial unless explicitly stated otherwise.",
        "",
    ]
    return "\n".join(lines)


def render_site(papers: list[dict], tracks: list[dict]) -> str:
    papers_json = json.dumps(papers, ensure_ascii=False)
    tracks_json = json.dumps(tracks, ensure_ascii=False)
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Awesome LLM Reasoning Roadmap</title>
  <style>
    :root {{ --fg:#162033; --muted:#667085; --line:#e7eaf2; --bg:#f7f9fc; --card:#fff; --accent:#2457ff; }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; background:var(--bg); color:var(--fg); }}
    header {{ background:#fff; border-bottom:1px solid var(--line); padding:46px 24px 28px; }}
    .wrap {{ max-width:1180px; margin:0 auto; }}
    h1 {{ margin:0; font-size:clamp(32px,6vw,60px); letter-spacing:0; }}
    p {{ color:var(--muted); line-height:1.6; }}
    .bar {{ display:flex; flex-wrap:wrap; gap:12px; margin-top:22px; }}
    input,select {{ border:1px solid var(--line); background:#fff; border-radius:8px; padding:12px 14px; font-size:15px; min-height:44px; }}
    input {{ flex:1 1 360px; }}
    select {{ flex:0 0 220px; }}
    main {{ padding:24px; }}
    .stats,.tracks {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(210px,1fr)); gap:12px; }}
    .stat,.track {{ background:var(--card); border:1px solid var(--line); border-radius:8px; padding:16px; }}
    .stat b {{ display:block; font-size:28px; }}
    .track h3 {{ margin:0 0 8px; font-size:17px; }}
    .visual {{ background:#fff; border:1px solid var(--line); border-radius:8px; padding:18px; margin:18px 0; overflow:auto; }}
    .visual img {{ width:100%; min-width:900px; display:block; }}
    .table {{ overflow:auto; background:#fff; border:1px solid var(--line); border-radius:8px; margin-top:18px; }}
    table {{ width:100%; min-width:980px; border-collapse:collapse; }}
    th,td {{ padding:13px 14px; border-bottom:1px solid var(--line); text-align:left; vertical-align:top; }}
    th {{ position:sticky; top:0; background:#fbfcff; font-size:13px; color:#475467; }}
    a {{ color:var(--accent); text-decoration:none; }}
    .tag {{ display:inline-block; padding:3px 7px; margin:0 5px 5px 0; border-radius:999px; background:#eef2ff; color:#3445a8; font-size:12px; }}
    .muted {{ color:var(--muted); }}
    footer {{ padding:24px; color:var(--muted); }}
  </style>
</head>
<body>
  <header>
    <div class="wrap">
      <h1>Awesome LLM Reasoning Roadmap</h1>
      <p>From Chain-of-Thought to Test-Time Scaling and Reasoning RL. Updated {updated}.</p>
      <div class="bar">
        <input id="q" placeholder="Search paper, method, tag, author, arXiv id..." autofocus>
        <select id="track"><option value="">All tracks</option></select>
        <select id="stage"><option value="">All stages</option></select>
      </div>
    </div>
  </header>
  <main class="wrap">
    <section class="stats">
      <div class="stat"><span class="muted">Papers</span><b id="count">0</b></div>
      <div class="stat"><span class="muted">Reading tracks</span><b id="trackCount">0</b></div>
      <div class="stat"><span class="muted">Stages</span><b id="stageCount">0</b></div>
    </section>
    <section class="visual"><img src="assets/llm-reasoning-roadmap.svg" alt="LLM reasoning roadmap"></section>
    <section class="tracks" id="trackCards"></section>
    <section class="table">
      <table>
        <thead><tr><th>Year</th><th>Paper</th><th>Track</th><th>Stage</th><th>Code</th><th>Tags</th></tr></thead>
        <tbody id="rows"></tbody>
      </table>
    </section>
  </main>
  <footer class="wrap">Maintained by <a href="https://github.com/StaryMoon">@StaryMoon</a>. This is an independent curated roadmap.</footer>
<script>
const papers = {papers_json};
const tracks = {tracks_json};
const q = document.getElementById('q');
const track = document.getElementById('track');
const stage = document.getElementById('stage');
const rows = document.getElementById('rows');
const trackCards = document.getElementById('trackCards');
const uniqueTracks = [...new Set(papers.map(p => p.track))].sort();
const uniqueStages = [...new Set(papers.map(p => p.stage))].sort();
track.innerHTML += uniqueTracks.map(t => `<option value="${{t}}">${{t}}</option>`).join('');
stage.innerHTML += uniqueStages.map(s => `<option value="${{s}}">${{s}}</option>`).join('');
document.getElementById('count').textContent = papers.length;
document.getElementById('trackCount').textContent = tracks.length;
document.getElementById('stageCount').textContent = uniqueStages.length;
function esc(s) {{ return String(s || '').replace(/[&<>"']/g, m => ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[m])); }}
trackCards.innerHTML = tracks.map(t => `<article class="track"><h3><a href="tracks/${{t.id}}.md">${{esc(t.title)}}</a></h3><p>${{esc(t.hook)}}</p><p class="muted">${{esc(t.why_hot)}}</p></article>`).join('');
function codeCell(p) {{
  const links = [];
  if (p.official_code) links.push(`<a href="${{p.official_code}}">Official</a>`);
  if (p.starymoon_repo) links.push(`<a href="${{p.starymoon_repo}}">Unofficial</a>`);
  return links.join(' / ') || '-';
}}
function render() {{
  const query = q.value.toLowerCase().trim();
  const tr = track.value;
  const st = stage.value;
  const filtered = papers.filter(p => {{
    const hay = [p.title,p.short,p.track,p.stage,p.arxiv_id,(p.tags||[]).join(' '),p.takeaway].join(' ').toLowerCase();
    return (!tr || p.track === tr) && (!st || p.stage === st) && (!query || hay.includes(query));
  }});
  rows.innerHTML = filtered.map(p => `<tr><td>${{p.year}}</td><td><a href="${{p.paper_url}}">${{esc(p.title)}}</a><br><span class="muted">${{esc(p.takeaway)}}</span></td><td>${{esc(p.track)}}</td><td>${{esc(p.stage)}}</td><td>${{codeCell(p)}}</td><td>${{(p.tags||[]).slice(0,8).map(t=>`<span class="tag">${{esc(t)}}</span>`).join('')}}</td></tr>`).join('');
}}
q.addEventListener('input', render); track.addEventListener('change', render); stage.addEventListener('change', render); render();
</script>
</body>
</html>
'''


def write_track_docs(papers: list[dict], tracks: list[dict]) -> None:
    papers_by_id = {item["id"]: item for item in papers}
    if TRACK_DOCS.exists():
        shutil.rmtree(TRACK_DOCS)
    TRACK_DOCS.mkdir(parents=True)
    for track in tracks:
        (TRACK_DOCS / f"{track['id']}.md").write_text(render_track_doc(track, papers_by_id), encoding="utf-8")


def write_assets(papers: list[dict]) -> None:
    ASSETS.mkdir(exist_ok=True)
    roadmap = render_timeline_svg(papers)
    method_map = render_method_map_svg(papers)
    (ASSETS / "llm-reasoning-roadmap.svg").write_text(roadmap, encoding="utf-8")
    (ASSETS / "reasoning-method-map.svg").write_text(method_map, encoding="utf-8")
    docs_assets = DOCS.parent / "assets"
    docs_assets.mkdir(parents=True, exist_ok=True)
    (docs_assets / "llm-reasoning-roadmap.svg").write_text(roadmap, encoding="utf-8")
    (docs_assets / "reasoning-method-map.svg").write_text(method_map, encoding="utf-8")


def build() -> None:
    papers, tracks = load()
    global papers_by_id
    papers_by_id = {item["id"]: item for item in papers}
    README.write_text(render_readme(papers, tracks), encoding="utf-8")
    DOCS.parent.mkdir(exist_ok=True)
    DOCS.write_text(render_site(papers, tracks), encoding="utf-8")
    write_track_docs(papers, tracks)
    write_assets(papers)


def check() -> bool:
    papers, tracks = load()
    global papers_by_id
    papers_by_id = {item["id"]: item for item in papers}
    expected_readme = render_readme(papers, tracks)
    expected_site = render_site(papers, tracks)
    return (
        README.exists()
        and DOCS.exists()
        and README.read_text(encoding="utf-8") == expected_readme
        and DOCS.read_text(encoding="utf-8") == expected_site
        and (ASSETS / "llm-reasoning-roadmap.svg").exists()
        and (ASSETS / "reasoning-method-map.svg").exists()
        and (DOCS.parent / "assets" / "llm-reasoning-roadmap.svg").exists()
        and (DOCS.parent / "assets" / "reasoning-method-map.svg").exists()
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        raise SystemExit(0 if check() else 1)
    build()


if __name__ == "__main__":
    papers_by_id: dict[str, dict] = {}
    main()
