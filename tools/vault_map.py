#!/usr/bin/env python3
"""
Vault Map — purpose-built SOT (Source of Truth) visualizer + structural audit.

Why purpose-built instead of Obsidian/generic graph tools: a generic tool only
knows "files link to files." Your SOT encodes far more — status heat, freshness
dates, tier structure, and DECLARED relationships (your index/router file's
cross-reference matrix). This script renders and audits that semantic layer.
Don't change your files to fit a tool; point a ~350-line lens at what you have.

Reads a markdown vault, extracts:
  - actual cross-references (any mention of another vault file's name)
  - status heat (red/orange/yellow/green/paused/archived marker counts)
  - freshness (dates in header/footer areas)
  - tier (core / operational / cold — configure below)
  - declared edges (your index file's cross-reference tables)

Outputs:
  1. vault_map.html — self-contained interactive radial map (no CDN, local only)
  2. audit report to stdout — orphans, islands, declared-vs-actual gaps,
     staleness, heat concentration, hub density

Read-only. Never writes to vault files. Keep the HTML local — it renders
whatever sensitive content your vault contains.
Usage: python3 vault_map.py [--days-stale 14]

CONFIGURE the constants below for your vault before first run.
"""

import json
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

VAULT = Path(__file__).resolve().parent  # or hardcode your vault path
OUT_HTML = VAULT / "vault_map.html"
STALE_DAYS = 14

# ---------------------------------------------------------------- configure
# Tier your files to match your session ritual / router file.
CORE = {
    # files read EVERY session (Level 1-2 in the ACI model), e.g.:
    "source_of_truth.md", "people_reference.md", "operational_index.md",
    "quality_contract.md",
}
SESSION_SURFACED = {"action_tracker.md"}  # surfaced every session start
ON_DEMAND = {
    # Level-3 files pulled when relevant, e.g.:
    "recipes_playbook.md", "projects_reference.md", "document_registry.md",
}
COLD = {"deep_memory.md"}  # retrieved only when referenced

# Operational subdirectories (person files, entity files, workstream files)
OP_DIRS = ("directs", "entities", "workstreams")

# Name of your router/index file (declared-relationship source)
INDEX_FILE = "operational_index.md"

# Excluded: build artifacts, templates, archives — anything not part of the
# living SOT graph.
EXCLUDE_DIRS = {"templates", "archive", "tools", ".obsidian", ".git"}
EXCLUDE_FILES = set()

STATUS_EMOJI = {"🔴": "p0",
                "🟠": "active",
                "🟡": "watch",
                "🟢": "good",
                "⏸️": "paused",
                "🧊": "seed"}

DATE_PAT = re.compile(r"(?:Last Updated|—)\s*:?\s*\*?\*?\s*(\d{4}-\d{2}-\d{2})")
ANY_DATE = re.compile(r"(\d{4}-\d{2}-\d{2})")


def tier_of(rel: str) -> str:
    name = Path(rel).name
    if name in CORE:
        return "core"
    if name in SESSION_SURFACED:
        return "session"
    if name in COLD:
        return "cold"
    if name in ON_DEMAND:
        return "ondemand"
    top = rel.split("/")[0]
    if top in OP_DIRS:
        return top
    return "other"


def collect_files():
    files = []
    for p in sorted(VAULT.rglob("*.md")):
        rel = str(p.relative_to(VAULT))
        parts = Path(rel).parts
        if any(part in EXCLUDE_DIRS for part in parts[:-1]):
            continue
        if parts[0] in EXCLUDE_DIRS:
            continue
        if Path(rel).name in EXCLUDE_FILES:
            continue
        files.append(rel)
    return files


def freshness(text: str):
    """Newest date found in header area (first 40 lines) or version footers."""
    dates = []
    head = "\n".join(text.splitlines()[:40])
    tail = "\n".join(text.splitlines()[-60:])
    for chunk in (head, tail):
        dates += ANY_DATE.findall(chunk)
    valid = []
    for d in dates:
        try:
            dt = datetime.strptime(d, "%Y-%m-%d")
            if datetime(2024, 1, 1) <= dt <= datetime.now() + timedelta(days=2):
                valid.append(dt)
        except ValueError:
            pass
    return max(valid) if valid else None


def parse_declared_edges(index_text: str, known: dict):
    """Pull declared relationships from operational_index cross-ref matrix rows.

    Any table row in operational_index that mentions 2+ vault files declares
    those files should reference each other (or at least co-appear).
    """
    declared = set()
    for line in index_text.splitlines():
        if not line.strip().startswith("|"):
            continue
        found = [rel for name, rel in known.items() if name in line]
        found = sorted(set(found))
        for i in range(len(found)):
            for j in range(i + 1, len(found)):
                a, b = found[i], found[j]
                # Only enforce cross-TYPE declarations (direct<->vendor,
                # direct<->workstream, etc.). Same-dir pairs (vendor<->vendor)
                # merely co-appear in matrix rows — not real relationships.
                if a.split("/")[0] != b.split("/")[0]:
                    declared.add((a, b))
    return declared


def main():
    stale_days = STALE_DAYS
    if "--days-stale" in sys.argv:
        stale_days = int(sys.argv[sys.argv.index("--days-stale") + 1])

    files = collect_files()
    # name -> rel  (basenames are unique in this vault; verify)
    names = {}
    for rel in files:
        base = Path(rel).name
        if base in names:
            print(f"⚠️  duplicate basename: {base} ({rel} vs {names[base]}) — "
                  f"refs to it are ambiguous", file=sys.stderr)
        names[base] = rel

    texts = {rel: (VAULT / rel).read_text(errors="ignore") for rel in files}

    nodes, edges = [], []
    edge_set = set()
    now = datetime.now()

    for rel in files:
        text = texts[rel]
        heat = {k: text.count(e) for e, k in STATUS_EMOJI.items()}
        fresh = freshness(text)
        age = (now - fresh).days if fresh else None
        nodes.append({
            "id": rel,
            "label": Path(rel).stem,
            "tier": tier_of(rel),
            "lines": text.count("\n") + 1,
            "heat": heat,
            "last": fresh.strftime("%Y-%m-%d") if fresh else None,
            "age": age,
            "stale": age is None or age > stale_days,
        })
        # actual edges: mention of another file's basename
        for base, target in names.items():
            if target == rel:
                continue
            if base in text:
                key = (rel, target)
                if key not in edge_set:
                    edge_set.add(key)
                    edges.append({"source": rel, "target": target,
                                  "n": text.count(base)})

    # ---------------------------------------------------------------- audit
    inbound = {n["id"]: 0 for n in nodes}
    outbound = {n["id"]: 0 for n in nodes}
    for e in edges:
        outbound[e["source"]] += 1
        inbound[e["target"]] += 1

    print("=" * 72)
    print("VAULT MAP AUDIT —", now.strftime("%Y-%m-%d %H:%M"))
    print(f"vault: {VAULT}   files in scope: {len(files)}   edges: {len(edges)}")
    print("=" * 72)

    # 1. Orphans (no inbound refs, excluding core which is read by protocol)
    print("\n## 1. ORPHANS — no other file references them")
    orphans = [n for n in nodes
               if inbound[n["id"]] == 0 and n["tier"] not in ("core", "session")]
    if orphans:
        for n in orphans:
            print(f"  ⚠️  {n['id']}  (tier={n['tier']}, {n['lines']} lines)")
    else:
        print("  ✅ none")

    # 2. Islands (no inbound AND no outbound)
    print("\n## 2. ISLANDS — no links in either direction")
    islands = [n for n in nodes
               if inbound[n["id"]] == 0 and outbound[n["id"]] == 0]
    if islands:
        for n in islands:
            print(f"  🔴 {n['id']}")
    else:
        print("  ✅ none")

    # 3. Declared-vs-actual (from operational_index matrix)
    print("\n## 3. DECLARED-vs-ACTUAL — operational_index says these should relate;")
    print("      neither file actually references the other")
    idx = texts.get(INDEX_FILE, "")
    declared = parse_declared_edges(idx, names)
    actual_pairs = set()
    for e in edges:
        actual_pairs.add((e["source"], e["target"]))
        actual_pairs.add((e["target"], e["source"]))
    missing = []
    for a, b in sorted(declared):
        if a == INDEX_FILE or b == INDEX_FILE:
            continue
        if (a, b) not in actual_pairs:
            missing.append((a, b))
    if missing:
        for a, b in missing:
            print(f"  ⚠️  {a}  ✗—✗  {b}")
    else:
        print("  ✅ all declared relationships have actual references")

    # 4. Staleness
    print(f"\n## 4. STALENESS — no date newer than {stale_days} days "
          f"(quality_contract: >2wks = flag)")
    stale = sorted([n for n in nodes if n["stale"]],
                   key=lambda n: n["age"] if n["age"] is not None else 9999,
                   reverse=True)
    if stale:
        for n in stale:
            agestr = f"{n['age']}d old (last {n['last']})" if n["age"] is not None \
                else "NO DATE FOUND"
            print(f"  🟡 {n['id']:45} {agestr}")
    else:
        print("  ✅ all files fresh")

    # 5. Heat concentration
    print("\n## 5. HEAT — files carrying the most open 🔴/🟠")
    hot = sorted(nodes, key=lambda n: n["heat"]["p0"] * 2 + n["heat"]["active"],
                 reverse=True)[:8]
    for n in hot:
        h = n["heat"]
        if h["p0"] + h["active"] == 0:
            break
        print(f"  {n['id']:45} 🔴×{h['p0']:<3} 🟠×{h['active']:<3} "
              f"🟡×{h['watch']:<3} 🧊×{h['seed']}")

    # 6. Hub density
    print("\n## 6. HUBS — most-referenced files (bloat/consolidation signal)")
    hubs = sorted(nodes, key=lambda n: inbound[n["id"]], reverse=True)[:6]
    for n in hubs:
        print(f"  {n['id']:45} ← {inbound[n['id']]} inbound, "
              f"{n['lines']} lines")

    # ---------------------------------------------------------------- html
    data = {"nodes": nodes, "edges": edges,
            "generated": now.strftime("%Y-%m-%d %H:%M"),
            "staleDays": stale_days}
    html = HTML_TEMPLATE.replace("__DATA__", json.dumps(data))
    OUT_HTML.write_text(html)
    print(f"\n🗺  map written: {OUT_HTML}")
    print("   open with:  open tools/vault_map.html   (🔒 local only — never deploy)")


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>SOT Vault — Map</title>
<style>
  body{margin:0;background:#0e1116;color:#c9d1d9;font:13px -apple-system,sans-serif;overflow:hidden}
  #hud{position:fixed;top:10px;left:12px;z-index:5;background:#161b22ee;padding:10px 14px;border-radius:8px;max-width:300px;border:1px solid #30363d}
  #hud h1{font-size:15px;margin:0 0 4px}
  .lg{display:inline-block;margin:2px 8px 2px 0;font-size:11px}
  .dot{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:3px;vertical-align:-1px}
  #info{position:fixed;bottom:10px;left:12px;z-index:5;background:#161b22ee;padding:10px 14px;border-radius:8px;max-width:360px;display:none;border:1px solid #30363d}
  #info h2{font-size:13px;margin:0 0 4px;color:#58a6ff}
  svg{width:100vw;height:100vh;cursor:grab}
  svg.panning{cursor:grabbing}
  line{stroke:#21262d;stroke-opacity:.7}
  line.hl{stroke:#58a6ff;stroke-opacity:1;stroke-width:2}
  text{fill:#adbac7;font-size:11px;pointer-events:none;text-shadow:0 0 4px #0e1116,0 0 4px #0e1116}
  text.ring-label{fill:#484f58;font-size:10px;font-style:italic}
  circle.node{cursor:pointer;stroke:#0e1116;stroke-width:1.5}
  circle.node.stale{stroke:#d29922;stroke-width:2.5;stroke-dasharray:3 2}
  circle.node.dim{opacity:.15}
  text.dim{opacity:.15}
  circle.ring{fill:none;stroke:#1c2128;stroke-width:1;stroke-dasharray:2 6}
</style></head><body>
<div id="hud"><h1>&#129504; SOT Vault — Map</h1>
<div id="meta"></div>
<div>
<span class="lg"><span class="dot" style="background:#f85149"></span>core</span>
<span class="lg"><span class="dot" style="background:#58a6ff"></span>directs</span>
<span class="lg"><span class="dot" style="background:#3fb950"></span>entities</span>
<span class="lg"><span class="dot" style="background:#d2a8ff"></span>workstreams</span>
<span class="lg"><span class="dot" style="background:#d29922"></span>on-demand</span>
<span class="lg"><span class="dot" style="background:#8b949e"></span>cold/other</span>
</div>
<div style="font-size:11px;margin-top:4px;color:#8b949e">
size = &#128308;&#128992; heat &middot; dashed gold ring = stale<br>
click node = highlight its links &middot; click bg = reset<br>
scroll = zoom &middot; drag = pan</div>
</div>
<div id="info"></div>
<svg id="s"><g id="world"></g></svg>
<script>
const D=__DATA__;
document.getElementById('meta').textContent=
  D.nodes.length+' files · '+D.edges.length+' refs · '+D.generated;
const COLOR={core:'#f85149',session:'#f85149',directs:'#58a6ff',entities:'#3fb950',
  workstreams:'#d2a8ff',ondemand:'#d29922',cold:'#8b949e',other:'#8b949e'};
const W=innerWidth,H=innerHeight,CX=W/2,CY=H/2;
// Deterministic radial layout: core center, tiers in fixed orbits.
const RINGS={core:90,session:90,directs:230,entities:340,workstreams:450,ondemand:560,cold:660,other:660};
const groups={};
D.nodes.forEach(n=>{(groups[n.tier]=groups[n.tier]||[]).push(n);});
// order within ring alphabetically for stability
for(const t in groups){
  const g=groups[t].sort((a,b)=>a.label.localeCompare(b.label));
  const R=RINGS[t]||600;
  // offset each ring's starting angle so labels don't stack
  const off={core:0,session:Math.PI/3,directs:.3,entities:.15,workstreams:.5,ondemand:.05,cold:1.2,other:1.4}[t]||0;
  g.forEach((n,i)=>{
    const a=off+2*Math.PI*i/g.length;
    n.x=CX+R*Math.cos(a);n.y=CY+R*Math.sin(a);
    n.r=7+Math.min(15,Math.sqrt(n.heat.p0*3+n.heat.active)*2.2);
  });
}
const idx={};D.nodes.forEach(n=>idx[n.id]=n);
const E=D.edges.filter(e=>idx[e.source]&&idx[e.target]);
const NS='http://www.w3.org/2000/svg';
const world=document.getElementById('world');
// orbit guides
Object.entries(RINGS).forEach(([t,R])=>{
  if(t==='session'||t==='other')return;
  const c=document.createElementNS(NS,'circle');
  c.setAttribute('class','ring');c.setAttribute('cx',CX);c.setAttribute('cy',CY);c.setAttribute('r',R);
  world.appendChild(c);});
const lineEls=E.map(e=>{const l=document.createElementNS(NS,'line');
  const a=idx[e.source],b=idx[e.target];
  l.setAttribute('x1',a.x);l.setAttribute('y1',a.y);
  l.setAttribute('x2',b.x);l.setAttribute('y2',b.y);
  world.appendChild(l);return l;});
const circEls=D.nodes.map(n=>{const c=document.createElementNS(NS,'circle');
  c.setAttribute('class','node'+(n.stale?' stale':''));
  c.setAttribute('fill',COLOR[n.tier]||'#8b949e');
  c.setAttribute('cx',n.x);c.setAttribute('cy',n.y);c.setAttribute('r',n.r);
  c.addEventListener('click',ev=>{ev.stopPropagation();select(n);});
  world.appendChild(c);return c;});
const textEls=D.nodes.map(n=>{const t=document.createElementNS(NS,'text');
  t.textContent=n.label;
  // place label away from center
  const dx=n.x-CX,dy=n.y-CY,d=Math.sqrt(dx*dx+dy*dy)||1;
  const lx=n.x+(dx/d)*(n.r+4),ly=n.y+(dy/d)*(n.r+4)+3;
  t.setAttribute('x',lx);t.setAttribute('y',ly);
  if(dx<0)t.setAttribute('text-anchor','end');
  world.appendChild(t);return t;});
function select(n){
  const el=document.getElementById('info');el.style.display='block';
  const inb=E.filter(e=>e.target===n.id),outb=E.filter(e=>e.source===n.id);
  el.innerHTML='<h2>'+n.id+'</h2>'
   +'tier: '+n.tier+' · '+n.lines+' lines<br>'
   +'last updated: '+(n.last||'—')+(n.stale?' &#9888;&#65039; stale':'')+'<br>'
   +'heat: &#128308;×'+n.heat.p0+' &#128992;×'+n.heat.active+' &#128993;×'+n.heat.watch+' &#129482;×'+n.heat.seed+'<br>'
   +'refs: '+inb.length+' in / '+outb.length+' out';
  const linked=new Set([n.id]);
  E.forEach((e,i)=>{const on=e.source===n.id||e.target===n.id;
    lineEls[i].setAttribute('class',on?'hl':'');
    if(on){linked.add(e.source);linked.add(e.target);}});
  D.nodes.forEach((m,i)=>{const on=linked.has(m.id);
    circEls[i].classList.toggle('dim',!on);
    textEls[i].classList.toggle('dim',!on);});
}
document.getElementById('s').addEventListener('click',()=>{
  document.getElementById('info').style.display='none';
  lineEls.forEach(l=>l.setAttribute('class',''));
  circEls.forEach(c=>c.classList.remove('dim'));
  textEls.forEach(t=>t.classList.remove('dim'));});
// zoom + pan
let scale=1,tx=0,ty=0;
function apply(){world.setAttribute('transform','translate('+tx+','+ty+') scale('+scale+')');}
addEventListener('wheel',ev=>{ev.preventDefault();
  const f=ev.deltaY<0?1.1:0.9;const ns=Math.max(.3,Math.min(4,scale*f));
  // zoom toward cursor
  tx=ev.clientX-(ev.clientX-tx)*(ns/scale);ty=ev.clientY-(ev.clientY-ty)*(ns/scale);
  scale=ns;apply();},{passive:false});
let panning=false,px=0,py=0;
const svg=document.getElementById('s');
svg.addEventListener('mousedown',ev=>{panning=true;px=ev.clientX;py=ev.clientY;svg.classList.add('panning');});
addEventListener('mousemove',ev=>{if(!panning)return;
  tx+=ev.clientX-px;ty+=ev.clientY-py;px=ev.clientX;py=ev.clientY;apply();});
addEventListener('mouseup',()=>{panning=false;svg.classList.remove('panning');});
</script></body></html>
"""

if __name__ == "__main__":
    main()
