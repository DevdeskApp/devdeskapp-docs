"""Regenerate the DevDeskApp docs figures (src/public/images/fig-*.png).

Every value shown in these figures was produced by running the compiled
n8n-nodes-devdeskapp v0.1.6 node (and by simulating the published n8n.io templates),
so the figures match what the node really outputs. UUIDs are random per run.

Usage (from the docs repo root):
    python scripts/doc-images/generate.py            # all figures
    python scripts/doc-images/generate.py ctc-output # one figure by key

Needs: pip install playwright pillow, plus Google Chrome (rendered via channel="chrome").
"""
from __future__ import annotations

import base64
import html
import json
import re
import sys
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
PUBLIC = ROOT / "src" / "public"
OUT = PUBLIC / "images"
RAW = Path(__file__).resolve().parent / "raw"  # untouched n8n screenshots used by the framed figures
LOGO = "data:image/svg+xml;base64," + base64.b64encode((PUBLIC / "logo.svg").read_bytes()).decode()
NODE_VERSION = "v0.1.6"

# DevDeskApp brand tokens (devdesk-app/src/themes.ts + .vitepress/theme/custom.css)
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');
:root{--bg:#f8fafc;--surface:#ffffff;--soft:#f1f5f9;--border:#e2e8f0;--t1:#0f172a;--t2:#475569;--t3:#64748b;--t4:#94a3b8;
--b1:#6366f1;--b2:#818cf8;--b3:#4f46e5;--pur:#a855f7;--pink:#ec4899;--em:#10b981;--amb:#f59e0b;--blue:#3b82f6;--red:#ef4444;
--mono:'JetBrains Mono',Consolas,'Courier New',monospace}
*{box-sizing:border-box}
body{margin:0;background:#f8fafc;font-family:Inter,'Segoe UI',system-ui,sans-serif;color:var(--t1)}
code{font-family:var(--mono);color:#4f46e5;font-size:.92em}
.fig{width:1600px;padding:26px 40px 30px;position:relative;overflow:hidden;
 background:radial-gradient(1000px 460px at 92% -12%,rgba(236,72,153,.10),transparent 62%),
 radial-gradient(900px 520px at -8% 112%,rgba(99,102,241,.12),transparent 62%),
 radial-gradient(700px 400px at 50% 40%,rgba(168,85,247,.05),transparent 70%),#f8fafc}
.fig::before{content:'';position:absolute;left:0;right:0;top:0;height:4px;background:linear-gradient(90deg,#6366f1,#a855f7,#ec4899)}
.hdr{display:flex;align-items:center;gap:14px}
.dots{display:flex;gap:8px;margin-right:6px}.dots i{width:13px;height:13px;border-radius:50%;display:block}
.logo{width:38px;height:38px;border-radius:10px;box-shadow:0 2px 6px rgba(15,23,42,.12)}
.title{font-size:27px;font-weight:800;letter-spacing:-.01em;color:#0f172a}
.title .brand{background:linear-gradient(90deg,#6366f1,#a855f7);-webkit-background-clip:text;color:transparent}
.title .sep{color:#cbd5e1;margin:0 10px;font-weight:600}
.pill{margin-left:auto;font-size:15px;font-weight:700;padding:8px 16px;border-radius:999px;white-space:nowrap}
.pill.green{background:#ecfdf5;color:#047857;border:1px solid #a7f3d0}
.pill.indigo{background:#eef2ff;color:#4338ca;border:1px solid #c7d2fe}
.pill.amber{background:#fffbeb;color:#b45309;border:1px solid #fde68a}
.sub{color:var(--t2);font-size:17px;margin:12px 0 20px}
.stage{border:1px solid #e0e7ff;border-radius:20px;background:#ffffff;padding:28px;box-shadow:0 10px 40px -12px rgba(99,102,241,.18),0 2px 6px rgba(15,23,42,.04)}
.foot{display:flex;justify-content:space-between;color:var(--t4);font-size:14px;margin-top:14px}
.row{display:flex;gap:20px;align-items:stretch}
.col{display:flex;flex-direction:column;gap:14px}
.panel{background:#f8fafc;border:1px solid var(--border);border-radius:14px;padding:18px 20px}
.ptitle{font-size:13px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--t3);margin-bottom:12px;display:flex;align-items:center;gap:8px}
.ok{color:#059669}
.field{margin-bottom:14px}.flabel{font-size:14px;color:var(--t2);margin-bottom:6px;font-weight:600}
.fval{background:#ffffff;border:1px solid var(--border);border-radius:9px;padding:10px 12px;font-size:16px;color:var(--t1);display:flex;justify-content:space-between;align-items:center}
.fval.expr{font-family:var(--mono);font-size:14px;color:#4f46e5;background:#f5f3ff;border-color:#ddd6fe}
.fval .chev{color:var(--t4)}
.hint{font-family:var(--mono);font-size:13px;color:var(--t3);margin-top:5px}
pre.json{margin:0;font-family:var(--mono);font-size:15px;line-height:1.55;color:#334155;white-space:pre-wrap;word-break:break-all}
.k{color:#4f46e5}.s{color:#047857}.n{color:#b45309}.b{color:#be185d}.p{color:#64748b}
.node{background:#ffffff;border:1px solid var(--border);border-radius:14px;padding:14px 16px;display:flex;gap:12px;align-items:center;position:relative;min-width:0;box-shadow:0 1px 3px rgba(15,23,42,.06)}
.node.dd{border:1.5px solid #a5b4fc;background:linear-gradient(135deg,#eef2ff,#ffffff 70%)}
.node .ic{width:44px;height:44px;border-radius:11px;flex:none;display:grid;place-items:center;font-size:22px;font-weight:800}
.node .ic img{width:44px;height:44px;border-radius:11px}
.node .nm{font-size:16px;font-weight:700;line-height:1.25;color:#0f172a}
.node .op{font-family:var(--mono);font-size:13px;color:var(--t3);margin-top:3px}
.node .val{font-family:var(--mono);font-size:12.5px;color:#047857;margin-top:5px;word-break:break-all}
.node .chk{position:absolute;right:-8px;bottom:-8px;width:24px;height:24px;border-radius:50%;background:#10b981;color:#ffffff;display:grid;place-items:center;font-size:14px;font-weight:900;border:2px solid #ffffff}
.arrow{flex:none;display:flex;align-items:center;justify-content:center;color:#6366f1;font-size:26px;font-weight:800;width:34px}
.slabel{font-size:13px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;margin-bottom:10px}
.lane{border-radius:14px;padding:14px;border:1px dashed var(--border)}
.tag{display:inline-block;font-size:12px;font-weight:700;padding:3px 9px;border-radius:999px}
.kv{display:grid;grid-template-columns:auto 1fr;gap:6px 16px;font-size:16px}
.kv .kk{color:var(--t3)}.kv .vv{font-family:var(--mono);color:var(--t1);text-align:right}
"""

ICONS = {
    "trigger": ("⚡", "#f59e0b"), "webhook": ("⇄", "#a855f7"), "code": ("{ }", "#fb923c"), "if": ("⑂", "#10b981"),
    "slack": ("#", "#ec4899"), "pg": ("DB", "#3b82f6"), "http": ("↗", "#38bdf8"), "sheets": ("▦", "#10b981"),
    "docs": ("▤", "#3b82f6"), "gmail": ("✉", "#ef4444"), "wp": ("W", "#38bdf8"), "notion": ("N", "#cbd5e1"),
    "chat": ("💬", "#a855f7"), "agent": ("✦", "#818cf8"), "model": ("◎", "#38bdf8"), "memory": ("◫", "#94a3b8"),
    "out": ("✓", "#10b981"),
}


def esc(s: object) -> str:
    return html.escape(str(s))


def json_html(obj) -> str:
    text = obj if isinstance(obj, str) else json.dumps(obj, indent=2, ensure_ascii=False)
    text = esc(text)
    text = re.sub(r'(&quot;[^&]*?&quot;)(\s*:)', r'<span class="k">\1</span>\2', text)
    text = re.sub(r'(:\s*)(&quot;.*?&quot;)', r'\1<span class="s">\2</span>', text)
    text = re.sub(r'(:\s*)(-?\d+(?:\.\d+)?)', r'\1<span class="n">\2</span>', text)
    text = re.sub(r'(:\s*)(true|false|null)', r'\1<span class="b">\2</span>', text)
    text = re.sub(r'^(\s*)(&quot;.*?&quot;)(,?)$', r'\1<span class="s">\2</span>\3', text, flags=re.M)
    return f'<pre class="json">{text}</pre>'


def node(name, op="", kind="dd", val="", check=False, style=""):
    if kind == "dd":
        ic = f'<div class="ic"><img src="{LOGO}"></div>'
    else:
        g, c = ICONS[kind]
        ic = f'<div class="ic" style="background:{c}22;color:{c};border:1px solid {c}55">{g}</div>'
    body = f'<div style="min-width:0"><div class="nm">{esc(name)}</div>'
    if op:
        body += f'<div class="op">{esc(op)}</div>'
    if val:
        body += f'<div class="val">{esc(val)}</div>'
    body += "</div>"
    chk = '<div class="chk">✓</div>' if check else ""
    return f'<div class="node {"dd" if kind == "dd" else ""}" style="{style}">{ic}{body}{chk}</div>'


def arrow(ch="→"):
    return f'<div class="arrow">{ch}</div>'


def frame(title, sub, body, pill="n8n-nodes-devdeskapp " + NODE_VERSION, pill_tone="indigo", foot_left=""):
    return f"""<div class="fig">
<div class="hdr"><div class="dots"><i style="background:#ef4444"></i><i style="background:#f59e0b"></i><i style="background:#10b981"></i></div>
<img class="logo" src="{LOGO}"><div class="title"><span class="brand">DevDeskApp</span><span class="sep">|</span>{esc(title)}</div>
<div class="pill {pill_tone}">{esc(pill)}</div></div>
<div class="sub">{sub}</div>
<div class="stage">{body}</div>
<div class="foot"><span>{foot_left}</span><span>docs.devdeskapp.com</span></div></div>"""


def stage_col(label, color, inner, width=None):
    w = f"width:{width}px;flex:none;" if width else "flex:1;"
    return (f'<div class="col" style="{w}"><div class="slabel" style="color:{color}">{esc(label)}</div>'
            f'<div class="col" style="gap:12px">{inner}</div></div>')


def flow(columns, branches=None):
    """columns: list of (label, color, [node html], width). branches: list of (label, color, [node html]) drawn as full-width lanes below."""
    parts = []
    for i, (label, color, nodes, width) in enumerate(columns):
        if i:
            parts.append(arrow())
        parts.append(stage_col(label, color, "".join(nodes), width))
    out = f'<div class="row" style="gap:10px;align-items:center">{"".join(parts)}</div>'
    if branches:
        lanes = ""
        for label, color, nodes in branches:
            inner = "".join(n if j == 0 else arrow() + n for j, n in enumerate(nodes))
            lanes += (f'<div class="lane" style="border-color:{color}66;background:{color}0d;display:flex;align-items:center;gap:16px">'
                      f'<div class="slabel" style="color:{color};filter:brightness(.8);margin:0;width:120px;flex:none">If {esc(label)} →</div>'
                      f'<div class="row" style="gap:6px;flex:1">{inner}</div></div>')
        out += f'<div class="col" style="gap:12px;margin-top:22px">{lanes}</div>'
    return out


def raw_img(name, crop, masks=()):
    """Crop a raw n8n screenshot (optionally painting over UI noise boxes) and return it as a data URI."""
    src = RAW / name
    tmp = RAW / f"_crop_{name}"
    im = Image.open(src).convert("RGB")
    # masks: (box, dx, dy) -> replace box with the same-size patch offset by (dx, dy), keeping the canvas texture
    for box, dx, dy in masks:
        patch = im.crop((box[0] + dx, box[1] + dy, box[2] + dx, box[3] + dy))
        im.paste(patch, box[:2])
    im.crop(crop).save(tmp)
    return "data:image/png;base64," + base64.b64encode(tmp.read_bytes()).decode()


# ---------------------------------------------------------------- figures

def fig_node_prettify():
    out = {"formatted": "{\n  \"status\": \"ok\",\n  \"code\": 200\n}", "success": True}
    body = f"""<div class="row" style="gap:20px">
<div class="panel" style="flex:1"><div class="ptitle">Input · 1 item</div>{json_html({"rawJson": '{"status":"ok","code":200}'})}</div>
<div class="panel" style="flex:1.1"><div class="ptitle">Parameters</div>
<div class="field"><div class="flabel">Resource</div><div class="fval">JSON Utility <span class="chev">⌄</span></div></div>
<div class="field"><div class="flabel">Operation</div><div class="fval">Prettify / Format <span class="chev">⌄</span></div></div>
<div class="field"><div class="flabel">JSON Input</div><div class="fval expr">{{{{ $json.rawJson }}}}</div><div class="hint">→ {{"status":"ok","code":200}}</div></div>
<div class="field" style="margin:0"><div class="flabel">Indentation</div><div class="fval">2 Spaces <span class="chev">⌄</span></div></div></div>
<div class="panel" style="flex:1.2"><div class="ptitle"><span class="ok">✓</span> Output · 1 item</div>{json_html(out)}
<div class="ptitle" style="margin-top:18px">formatted (rendered)</div>{json_html('{\n  "status": "ok",\n  "code": 200\n}')}</div></div>"""
    return frame("Test one node: JSON Utility → Prettify", "Input, parameters and the real output of a single DevDeskApp node test step.", body)


def fig_ctc_parameters():
    steps = [
        ("Monthly basic", "18,00,000 × 50% ÷ 12", "₹75,000"),
        ("Employee PF", "min(12% of basic, ₹1,800)", "₹1,800"),
        ("Employer PF", "same as employee PF", "₹1,800"),
        ("Monthly gross", "(CTC − 12 × employer PF) ÷ 12", "₹1,48,200"),
        ("Estimated TDS", "new regime slabs, ₹75,000 std. deduction", "₹18,125"),
        ("Professional tax", "flat", "₹200"),
        ("Monthly in-hand", "gross − PF − PT − TDS", "₹1,28,075"),
    ]
    rows = "".join(
        f'<div style="display:grid;grid-template-columns:200px 1fr 130px;gap:12px;padding:11px 0;border-bottom:1px solid #e2e8f0;{"color:#047857;font-weight:800" if i == len(steps) - 1 else ""}">'
        f'<div style="font-weight:700">{esc(a)}</div><div style="color:var(--t3);font-family:var(--mono);font-size:14px">{esc(b)}</div>'
        f'<div style="text-align:right;font-family:var(--mono)">{esc(c)}</div></div>'
        for i, (a, b, c) in enumerate(steps))
    body = f"""<div class="row" style="gap:22px">
<div class="panel" style="width:560px;flex:none"><div class="ptitle">Parameters</div>
<div class="field"><div class="flabel">Resource</div><div class="fval">HR &amp; Calculator <span class="chev">⌄</span></div></div>
<div class="field"><div class="flabel">Operation</div><div class="fval">CTC to In-Hand Salary <span class="chev">⌄</span></div></div>
<div class="field"><div class="flabel">Annual CTC</div><div class="fval expr">{{{{ $('Sample Candidate Selection Ingest').item.json.annualCtc }}}}</div><div class="hint">→ 1800000</div></div>
<div class="field" style="margin:0"><div class="flabel">Basic Salary Percentage</div><div class="fval expr">{{{{ $('Sample Candidate Selection Ingest').item.json.basicPercentage }}}}</div><div class="hint">→ 50 (default 50)</div></div></div>
<div class="panel" style="flex:1"><div class="ptitle">How the node calculates it · ₹18,00,000 CTC</div>{rows}</div></div>"""
    return frame("CTC to In-Hand Salary: parameters", "The two inputs the HR &amp; Calculator resource takes, and the formula the node applies to them.",
                 body, pill="Template #21130", pill_tone="green")


def fig_ctc_output():
    gross = 148200
    segs = [("Monthly in-hand", 128075, "#059669"), ("Employee PF", 1800, "#6366f1"),
            ("Professional tax", 200, "#ec4899"), ("Estimated TDS", 18125, "#d97706")]
    bar = ""
    for i, (label, v, c) in enumerate(segs):
        w = v / gross * 100
        radius = "border-radius:4px 0 0 4px;" if i == 0 else ("border-radius:0 4px 4px 0;" if i == len(segs) - 1 else "")
        bar += f'<div title="{esc(label)}" style="width:calc({w:.3f}% - 2px);min-width:4px;background:{c};height:46px;{radius}"></div>'
    legend = "".join(
        f'<div style="display:flex;align-items:center;gap:10px;font-size:16px"><span style="width:14px;height:14px;border-radius:3px;background:{c};flex:none"></span>'
        f'<span style="color:var(--t2)">{esc(l)}</span><span style="font-family:var(--mono);color:var(--t1);margin-left:auto">₹{v:,.0f}</span>'
        f'<span style="font-family:var(--mono);color:var(--t3);width:70px;text-align:right">{v / gross * 100:.1f}%</span></div>'
        for l, v, c in segs).replace("₹128,075", "₹1,28,075").replace("₹18,125", "₹18,125")
    out = {"annualCtc": 1800000, "monthlyGross": 148200, "monthlyInHand": 128075,
           "breakdown": {"monthlyBasic": 75000, "employeePf": 1800, "employerPf": 1800, "professionalTax": 200, "estimatedMonthlyTds": 18125},
           "taxRegime": "India Standard / New Tax Benchmark", "reference": "https://www.devdeskapp.com/ctc-to-in-hand-calculator"}
    body = f"""<div class="row" style="gap:22px">
<div class="panel" style="flex:1.15"><div class="ptitle">Where the ₹1,48,200 monthly gross goes</div>
<div style="display:flex;gap:2px;margin:6px 0 22px">{bar}</div>
<div class="col" style="gap:12px">{legend}</div>
<div style="margin-top:22px;padding-top:16px;border-top:1px solid var(--border);color:var(--t3);font-size:14px;line-height:1.5">
Employer PF (₹1,800) is part of CTC but not of gross, so it is not in this bar. TDS is an estimate on the new regime; the node does not model HRA, exemptions or the old regime.</div></div>
<div class="panel" style="flex:1"><div class="ptitle"><span class="ok">✓</span> Output · 1 item</div>{json_html(out)}</div></div>"""
    return frame("CTC to In-Hand Salary: output", "Real output of the HR &amp; Calculator node for a ₹18,00,000 annual CTC with 50% basic.",
                 body, pill="Template #21130", pill_tone="green")


def fig_suite_executed():
    a = [node("Manual Run (Instant Test)", "manualTrigger", "trigger", check=True),
         node("Sample Developer & HR Payload", "code", "code", "rawMinifiedApiData, annualCtc", True),
         node("DevDeskApp: JSON Prettifier", "json · prettify", val="formatted: {\\n  \"service\": …", check=True),
         node("DevDeskApp: SHA-256 Digest", "crypto · hash (sha256)", val="f7e61312d64a…41620df", check=True)]
    b = [node("DevDeskApp: UUID Generator", "crypto · uuid", val="5ad52af6-8b62-48a0-…", check=True),
         node("DevDeskApp: Slugifier", "text · slugify", val="rahul-verma-principal-cloud-architect", check=True),
         node("DevDeskApp: CTC Calculator", "calculator · ctcToInHand", val="monthlyInHand: 163075", check=True),
         node("Consolidated Final Output", "code", "code", "VERIFIED_AND_PROCESSED", True)]
    r1 = "".join(n if i == 0 else arrow() + n for i, n in enumerate(a))
    r2 = "".join(n if i == 0 else arrow() + n for i, n in enumerate(b))
    grid = "grid-template-columns:1fr 34px 1fr 34px 1fr 34px 1fr"
    body = f"""<div style="display:grid;{grid};gap:0;align-items:center">{r1}</div>
<div style="display:flex;justify-content:flex-end;padding:6px 14% 6px 0;color:#6366f1;font-size:26px;font-weight:800">↓</div>
<div style="display:grid;{grid};gap:0;align-items:center;direction:rtl">{''.join(f'<div style="direction:ltr">{x}</div>' for x in [b[3], arrow('←'), b[2], arrow('←'), b[1], arrow('←'), b[0]])}</div>
<div style="display:flex;gap:28px;margin-top:26px;padding-top:18px;border-top:1px solid var(--border);color:var(--t2);font-size:16px">
<span><b class="ok">8 / 8</b> nodes succeeded</span><span><b style="color:#4338ca">1 item</b> per node, pairedItem kept</span>
<span><b style="color:#b45309">0</b> external HTTP calls from DevDeskApp nodes</span></div>"""
    _ = r2
    return frame("Template #21017 executed", "Every node of the Developer Suite after one test run, with the key value each DevDeskApp node returned.",
                 body, pill="Template #21017", pill_tone="green")


def fig_suite_output():
    meta = {"meta": {"traceId": "5ad52af6-8b62-48a0-b934-7a82c4ab3eb1",
                     "sha256PayloadHash": "f7e61312d64a6fefb8ff2dcc4ccc957e7204a229c04647fffba674aed41620df",
                     "candidateFileSlug": "rahul-verma-principal-cloud-architect", "status": "VERIFIED_AND_PROCESSED",
                     "poweredBy": "DevDeskApp (https://www.devdeskapp.com)"}}
    comp = {"compensationBreakdown": {"annualCtcFormatted": "₹24,00,000", "monthlyGross": "₹1,98,200", "netMonthlyTakeHome": "₹1,63,075",
                                      "taxDeductions": {"monthlyBasic": "₹1,00,000", "employeePf": "₹1,800", "estimatedMonthlyTax": "₹33,125", "professionalTax": "₹200"}}}
    fmt = {"formattedJsonResult": {"service": "payment-gateway", "version": 2.4,
                                   "client": {"name": "Rahul Verma", "email": "user@example.com", "plan": "enterprise"},
                                   "audit": {"ip": "192.168.1.1", "timestamp": 1728950400}}}
    body = f"""<div class="row" style="gap:20px">
<div class="col" style="flex:1.25"><div class="panel"><div class="ptitle"><span class="ok">✓</span> Consolidated Final Output · meta</div>{json_html(meta)}</div>
<div class="panel"><div class="ptitle">formattedJsonResult</div>{json_html(fmt)}</div></div>
<div class="panel" style="flex:1"><div class="ptitle">compensationBreakdown</div>{json_html(comp)}</div></div>"""
    return frame("Template #21017 output", "The single item the Consolidated Final Output node returns after a test run (traceId changes every run).",
                 body, pill="Template #21017", pill_tone="green")


def fig_ai_agent():
    left = f"""<div class="col" style="flex:1.25;gap:22px">
<div class="row" style="align-items:center;gap:8px">{node("When chat message received", "chatTrigger", "chat")}{arrow()}{node("AI Agent", "tools agent", "agent", style="flex:1.2")}{arrow()}{node("Chat reply", "", "out")}</div>
<div class="row" style="gap:14px;padding-left:12%">
<div class="col" style="flex:1;gap:6px"><div class="slabel" style="color:#0369a1">Chat Model *</div>{node("Any n8n chat model", "OpenAI, Anthropic, Gemini, Ollama…", "model")}</div>
<div class="col" style="flex:.8;gap:6px"><div class="slabel" style="color:#64748b">Memory</div>{node("Optional", "Simple Memory", "memory")}</div>
<div class="col" style="flex:1.2;gap:6px"><div class="slabel" style="color:#4338ca">Tool</div>{node("DevDeskApp Tool", "calculator · ctcToInHand", style="box-shadow:0 0 0 4px rgba(99,102,241,.18)")}</div></div>
<div style="color:var(--t3);font-size:15px;line-height:1.5">The DevDeskApp node sets <code style="color:#4338ca">usableAsTool: true</code>, so it can be attached to the agent's <b>Tool</b> port. The model fills the parameters; the node computes the answer in the n8n process.</div></div>"""
    conv = f"""<div class="panel" style="flex:1"><div class="ptitle">One agent turn</div>
<div style="background:#f1f5f9;border-radius:12px;padding:12px 14px;margin-bottom:12px;font-size:16px"><b style="color:#7e22ce">User</b><br>What is the monthly in-hand pay for a ₹24,00,000 CTC?</div>
<div class="flabel" style="color:#4338ca">Tool call → DevDeskApp</div>{json_html({"annualCtc": 2400000, "basicPercentage": 50})}
<div class="flabel" style="color:#047857;margin-top:12px">Tool result</div>{json_html({"monthlyGross": 198200, "monthlyInHand": 163075, "breakdown": {"employeePf": 1800, "professionalTax": 200, "estimatedMonthlyTds": 33125}})}
<div style="background:#f1f5f9;border-radius:12px;padding:12px 14px;margin-top:12px;font-size:16px"><b style="color:#4f46e5">Agent</b><br>About ₹1,63,075 a month after ₹1,800 PF, ₹200 professional tax and ~₹33,125 estimated TDS.</div></div>"""
    return frame("AI Agent with DevDeskApp as a tool", "Chat trigger, AI Agent and the DevDeskApp node on the Tool port. The numbers are the node's real output for ₹24,00,000.",
                 f'<div class="row" style="gap:24px;align-items:flex-start">{left}{conv}</div>')


OPS = [
    ("JSON Utility", "json", "#6366f1", [("Prettify / Format", "prettify"), ("Minify", "minify"), ("Validate", "validate")]),
    ("Crypto & Hash", "crypto", "#a855f7", [("Hash (MD5 / SHA-1 / SHA-256 / SHA-512)", "hash"), ("Base64 Encode", "base64Encode"), ("Base64 Decode", "base64Decode"), ("UUID V4", "uuid")]),
    ("Text & String", "text", "#ec4899", [("Slugify String", "slugify"), ("Case Converter", "caseConverter"), ("URL Encode", "urlEncode"), ("URL Decode", "urlDecode")]),
    ("HR & Calculator", "calculator", "#10b981", [("CTC to In-Hand Salary", "ctcToInHand")]),
    ("E-Commerce & FinTech", "ecommerce", "#f59e0b", [("Catalog Schema Mapper", "catalogMapper"), ("Dynamic UPI QR & URI", "upiQr"), ("GST JSON to Tabular Data", "gstJsonToTable"),
                                                       ("Profit Margin & ROAS Calculator", "profitCalculator"), ("Shipping Label Cropper Coordinates", "shippingLabelCrop"),
                                                       ("Webhook Signature Verifier", "webhookVerifier"), ("WhatsApp Interactive Payload", "whatsappPayload")]),
]


def fig_operations_map():
    cards = ""
    for name, value, color, ops in OPS:
        items = "".join(f'<div style="display:flex;justify-content:space-between;gap:10px;padding:9px 0;border-top:1px solid #e2e8f0;font-size:15px">'
                        f'<span>{esc(a)}</span><span style="font-family:var(--mono);color:var(--t3);font-size:13px">{esc(b)}</span></div>' for a, b in ops)
        cards += (f'<div class="panel" style="flex:{1.75 if len(ops) > 4 else 1};border-top:4px solid {color}"><div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px">'
                  f'<div style="font-size:19px;font-weight:800">{esc(name)}</div><span class="tag" style="background:{color}22;color:{color};border:1px solid {color}55">{len(ops)}</span></div>'
                  f'<div style="font-family:var(--mono);font-size:13px;color:{color};margin-bottom:6px">resource: {value}</div>{items}</div>')
    body = f'<div class="row" style="gap:16px;align-items:flex-start">{cards}</div>'
    return frame("5 resources, 19 operations", "Everything the DevDeskApp node can do, with the internal <code>resource</code> and <code>operation</code> values used in workflow JSON.", body)


def fig_architecture():
    body = f"""<div class="row" style="gap:26px;align-items:stretch">
<div class="lane" style="flex:.8;border:2px dashed rgba(99,102,241,.6);background:rgba(99,102,241,.04)">
<div class="slabel" style="color:#4338ca">Your browser</div>
<div class="col" style="gap:12px">{node("You paste input", "JSON, a secret, a salary figure", "chat")}
<div class="arrow" style="width:auto">↓</div>{node("DevDeskApp Web tool", "340+ tools · JavaScript in the tab", style="")}
<div class="arrow" style="width:auto">↓</div>{node("Result on screen", "nothing posted to a server for processing", "out")}</div></div>
<div class="lane" style="flex:1.7;border:2px dashed rgba(16,185,129,.6);background:rgba(16,185,129,.05)">
<div class="slabel" style="color:#047857">Your n8n instance (container / process)</div>
<div class="row" style="gap:8px;align-items:center">{node("Previous node", "items in", "webhook", style="flex:1")}{arrow()}{node("DevDeskApp node", "in-process · Node.js crypto", style="flex:1.3")}{arrow()}{node("Next node", "items + pairedItem", "code", style="flex:1")}</div>
<div style="margin-top:22px;display:grid;grid-template-columns:repeat(3,1fr);gap:12px;font-size:15px;color:var(--t2)">
<div class="panel" style="padding:12px 14px">No credentials or API keys</div><div class="panel" style="padding:12px 14px">No outbound HTTP from the node</div><div class="panel" style="padding:12px 14px">Deterministic: same input, same output</div></div></div>
<div class="col" style="width:230px;flex:none;justify-content:center;opacity:.95">
<div class="panel" style="border:1.5px dashed #ef4444;text-align:center"><div style="font-size:30px;color:#dc2626">⊘</div><div style="font-weight:800;margin:6px 0">Third-party utility APIs</div><div style="color:var(--t3);font-size:14px">online formatters, hash or payroll APIs: <b style="color:#dc2626">not called</b></div></div></div></div>"""
    return frame("Where your data is processed", "DevDeskApp Web runs in your browser tab; the n8n node runs inside your own n8n process. Neither sends payloads to a DevDeskApp server.", body)


def fig_local_vs_cloud():
    bench = [("CTC to In-Hand", 12.56), ("JSON Prettify", 22.63), ("Slugify", 40.7), ("SHA-256 Hash", 46.45)]
    mx = 50
    bars = "".join(
        f'<div style="display:grid;grid-template-columns:170px 1fr 90px;gap:14px;align-items:center;margin:12px 0"><span style="color:var(--t2);font-size:16px">{esc(n)}</span>'
        f'<div style="background:#eef2ff;border-radius:4px;height:26px"><div style="width:{v / mx * 100:.1f}%;background:#6366f1;height:26px;border-radius:0 4px 4px 0"></div></div>'
        f'<span style="font-family:var(--mono);text-align:right">{v:.1f} ms</span></div>' for n, v in bench)
    body = f"""<div class="row" style="gap:22px">
<div class="panel" style="flex:1.2"><div class="ptitle">Measured: 10,000 items through one DevDeskApp node</div>{bars}
<div style="color:var(--t3);font-size:14px;margin-top:14px;line-height:1.5">Node logic only, compiled {NODE_VERSION} on Node.js 24 (one laptop run). That is 0.001–0.005 ms per item; n8n's own per-node overhead comes on top.</div></div>
<div class="col" style="flex:1;gap:16px">
<div class="panel" style="border-left:4px solid #10b981"><div class="ptitle">Local DevDeskApp node</div><div style="font-size:40px;font-weight:800">12–47 ms</div><div style="color:var(--t2)">for 10,000 items, no network, no API key</div></div>
<div class="panel" style="border-left:4px solid #f59e0b"><div class="ptitle">Cloud utility API (illustration)</div><div style="font-size:40px;font-weight:800">≈ 25 min</div><div style="color:var(--t2)">10,000 sequential calls at an assumed 150 ms round trip, before rate limits</div></div></div></div>"""
    return frame("Local node vs cloud API", "What 10,000 items cost in time when the work happens in the n8n process instead of over HTTP.", body)


def fig_import_steps():
    def step(n, title, lines, color):
        li = "".join(f'<div style="padding:8px 0;border-top:1px solid #e2e8f0;color:var(--t2);font-size:16px">{x}</div>' for x in lines)
        return (f'<div class="panel" style="flex:1;border-top:4px solid {color}"><div style="display:flex;gap:14px;align-items:center;margin-bottom:12px">'
                f'<div style="width:42px;height:42px;border-radius:50%;background:{color};display:grid;place-items:center;font-weight:800;font-size:20px;color:#ffffff">{n}</div>'
                f'<div style="font-size:21px;font-weight:800">{title}</div></div>{li}</div>')
    body = f"""<div class="row" style="gap:12px;align-items:stretch">
{step(1, "Install the node", ["Settings → Community nodes", "Install a community node", "<code style='color:#4338ca'>n8n-nodes-devdeskapp</code> → tick the risk box → Install"], "#6366f1")}{arrow()}
{step(2, "Get the template", ["Open the template on n8n.io", "Click <b>Use for free</b>", "Copy the workflow JSON (or open it in your n8n Cloud workspace)"], "#a855f7")}{arrow()}
{step(3, "Paste and run", ["New workflow → click the canvas", "<b>Ctrl + V</b> / <b>Cmd + V</b>", "Add credentials (Slack, Postgres, Google…) → Test workflow"], "#10b981")}</div>"""
    return frame("Import a template in 3 steps", "The same steps work on n8n Cloud, self-hosted, Docker and desktop, as long as community nodes are enabled.", body)


def pipeline(title, sub, pill, columns, branches=None):
    return frame(title, sub, flow(columns, branches), pill=pill, pill_tone="green")


def fig_flow_21017():
    dd = [node("JSON Prettifier", "json · prettify"), node("SHA-256 Digest", "crypto · hash"), node("UUID Generator", "crypto · uuid"),
          node("Slugifier", "text · slugify"), node("CTC Calculator", "calculator · ctcToInHand")]
    return pipeline("Template #21017 pipeline", "Developer Suite: one sample payload passes through five DevDeskApp operations in sequence.", "Template #21017", [
        ("Trigger", "#b45309", [node("Manual Run (Instant Test)", "manualTrigger", "trigger")], 300),
        ("Sample data", "#c2410c", [node("Sample Developer & HR Payload", "code", "code")], 300),
        ("DevDeskApp", "#4f46e5", dd, 360),
        ("Result", "#047857", [node("Consolidated Final Output", "code", "code")], 300)])


def fig_flow_21376():
    dd = [node("JSON Prettifier & Validator", "json · prettify"), node("SHA-256 Integrity Hasher", "crypto · hash"),
          node("Trace UUID Generator", "crypto · uuid"), node("Audit Slug Normalizer", "text · slugify")]
    return pipeline("Template #21376 pipeline", "Payment Webhook Sanitizer: format, fingerprint and tag each payment event, then route it by status.", "Template #21376", [
        ("Ingest", "#b45309", [node("Test workflow", "manualTrigger", "trigger"), node("Production Webhook Trigger", "webhook", "webhook")], 250),
        ("DevDeskApp", "#4f46e5", dd, 290),
        ("Gate", "#047857", [node("If: Payment Captured & Valid", "if", "if")], 230)],
        [("true", "#10b981", [node("Format Security Audit Record", "code", "code"), node("DevOps Security Alert", "slack", "slack")]),
         ("false", "#ef4444", [node("Format Security Incident Alert", "code", "code"), node("Flag Suspicious Transaction", "slack", "slack")])])


def fig_flow_21593():
    dd = [node("JSON Prettifier & Schema Validator", "json · prettify"), node("Trace UUID Generator", "crypto · uuid"), node("SHA-256 Integrity Hasher", "crypto · hash")]
    return pipeline("Template #21593 pipeline", "AI LLM JSON ingestion: a Code node strips the markdown fences, DevDeskApp formats, tags and hashes, an If node routes the record.", "Template #21593", [
        ("Ingest", "#b45309", [node("Sample Raw LLM Output", "manualTrigger → code", "trigger"), node("AI Agent Webhook / Callback", "webhook", "webhook")], 240),
        ("Clean", "#c2410c", [node("Strip Markdown Code Fences", "code", "code")], 220),
        ("DevDeskApp", "#4f46e5", dd, 290),
        ("Gate", "#047857", [node("If: Valid JSON & Clean Schema", "if", "if")], 210)],
        [("true", "#10b981", [node("Format Clean Database Record", "code", "code"), node("Postgres: Insert", "postgres", "pg"), node("Slack: Logged", "slack", "slack")]),
         ("false", "#ef4444", [node("Format Schema Error Alert", "code", "code"), node("Slack: Malformed AI JSON", "slack", "slack")])])


def fig_flow_21594():
    dd = [node("Indian CTC-to-In-Hand Engine", "calculator · ctcToInHand"), node("Offer Tracking UUID", "crypto · uuid"),
          node("Candidate Slug Generator", "text · slugify"), node("Compensation Checksum Hasher", "crypto · hash")]
    return pipeline("Template #21594 pipeline", "CTC offer letters: compute pay, tag and fingerprint the offer, then create the Google Doc, email it and tell HR on Slack.", "Template #21594", [
        ("Ingest", "#b45309", [node("Sample Candidate Ingest", "manualTrigger → code", "trigger"), node("Google Sheets Trigger", "new candidate row", "sheets")], 240),
        ("DevDeskApp", "#4f46e5", dd, 300),
        ("Gate", "#047857", [node("If: Compensation Valid & Above Minimum", "if", "if")], 230)],
        [("true", "#10b981", [node("Format Offer Payload", "code", "code"), node("Google Docs", "create from template", "docs"), node("Gmail", "send", "gmail"), node("Slack", "offer sent", "slack")]),
         ("false", "#ef4444", [node("Format HR Compliance Alert", "code", "code"), node("Slack: Flag Invalid Offer", "slack", "slack")])])


def fig_flow_21595():
    dd = [node("Email Lowercase & Clean", "text · caseConverter"), node("SHA-256 Email Privacy Hasher", "crypto · hash"),
          node("Event Deduplication UUID", "crypto · uuid"), node("Campaign Tracking Slug", "text · slugify")]
    return pipeline("Template #21595 pipeline", "Meta CAPI lead sync: normalise and hash the email, add an event_id, then send only opted-in leads to the Graph API.", "Template #21595", [
        ("Ingest", "#b45309", [node("Sample Inbound Lead", "manualTrigger → code", "trigger"), node("Production Lead Webhook", "webhook", "webhook")], 240),
        ("DevDeskApp", "#4f46e5", dd, 290),
        ("Gate", "#047857", [node("If: Opted-In & Verified Email", "if", "if")], 220)],
        [("true", "#10b981", [node("Format Meta CAPI Payload", "code", "code"), node("Meta Graph API", "HTTP POST /events", "http"), node("Google Sheets", "append lead", "sheets"), node("Slack", "marketing", "slack")]),
         ("false", "#ef4444", [node("Format Privacy Exclusion Log", "code", "code"), node("Slack: Lead Excluded", "slack", "slack")])])


def fig_flow_21596():
    dd = [node("URL Slug Normalizer", "text · slugify"), node("Content Fingerprint Hasher", "crypto · hash"),
          node("Publication Trace UUID", "crypto · uuid"), node("Meta Title Casing Formatter", "text · caseConverter")]
    return pipeline("Template #21596 pipeline", "Notion to WordPress: build the slug, fingerprint the content, tag the release, then publish approved posts and tell the team.", "Template #21596", [
        ("Ingest", "#b45309", [node("Sample Notion Article Draft", "manualTrigger → code", "trigger"), node("Notion Trigger", "article updated", "notion")], 240),
        ("DevDeskApp", "#4f46e5", dd, 290),
        ("Gate", "#047857", [node("If: Approved & Ready", "if", "if")], 210)],
        [("true", "#10b981", [node("Format WordPress Payload", "code", "code"), node("WordPress", "create / update post", "wp"), node("Slack", "article live", "slack")]),
         ("false", "#ef4444", [node("Format Editorial Warning", "code", "code"), node("Slack: Editorial Warning", "slack", "slack")])])


def framed_screenshot(raw, crop, title, sub, pill="n8n UI", tone="indigo", masks=()):
    uri = raw_img(raw, crop, masks)
    body = f'<img src="{uri}" style="display:block;width:100%;border-radius:10px">'
    return frame(title, sub, body, pill=pill, pill_tone=tone).replace('class="stage"', 'class="stage" style="padding:14px"')


FIGURES = {
    "node-prettify": fig_node_prettify,
    "ctc-parameters": fig_ctc_parameters,
    "ctc-output": fig_ctc_output,
    "suite-executed": fig_suite_executed,
    "suite-output": fig_suite_output,
    "ai-agent-tool": fig_ai_agent,
    "operations-map": fig_operations_map,
    "architecture": fig_architecture,
    "local-vs-cloud": fig_local_vs_cloud,
    "import-steps": fig_import_steps,
    "flow-21017": fig_flow_21017,
    "flow-21376": fig_flow_21376,
    "flow-21593": fig_flow_21593,
    "flow-21594": fig_flow_21594,
    "flow-21595": fig_flow_21595,
    "flow-21596": fig_flow_21596,
    "n8n-community-nodes": lambda: framed_screenshot(
        "screen_1_community_nodes.png", (200, 0, 1920, 520), "Settings → Community nodes",
        "Open <b>Settings</b>, choose <b>Community nodes</b> and click <b>Install a community node</b>."),
    "n8n-install-modal": lambda: framed_screenshot(
        "screen_1b_install_modal.png", (560, 260, 1360, 760), "Install community nodes",
        "Enter <code>n8n-nodes-devdeskapp</code>, tick the risk confirmation, then click <b>Install</b>."),
    "ctc-executed": lambda: framed_screenshot(
        "screen_ctc_executed.png", (44, 250, 1920, 1050), "Template #21130 test run",
        "All seven nodes succeed with 1 item each; n8n shows <b>Workflow executed successfully</b>.", pill="Template #21130", tone="green"),
}

# Template canvases: real n8n editor screenshots (inner area of the old dark-framed captures),
# re-framed in the light theme with n8n's "Introducing n8n Agents" promo toast painted out.
CANVASES = {
    "canvas-21017": ("screen_2_workflow_canvas.png", "21017", "Format JSON & secure HR payloads", "Integrated stack: DevDeskApp JSON Prettifier · SHA-256 · UUID · Slugifier · CTC Calculator"),
    "canvas-21130": ("screen_ctc_canvas.png", "21130", "Indian CTC offers & payroll breakdowns", "Integrated stack: DevDeskApp Slugifier · CTC Calculator · UUID · SHA-256"),
    "canvas-21376": ("screen_webhook_sanitizer_canvas.png", "21376", "Sanitize & audit payment webhooks", "Integrated stack: DevDeskApp JSON + crypto tools · Webhook · Slack"),
    "canvas-21593": ("screen_ai_llm_canvas.png", "21593", "Sanitize & ingest AI LLM JSON into Postgres", "Integrated stack: DevDeskApp · PostgreSQL · Slack"),
    "canvas-21594": ("screen_offer_letter_canvas.png", "21594", "Generate Indian CTC offer letters", "Integrated stack: DevDeskApp · Google Docs · Gmail · Slack"),
    "canvas-21595": ("screen_meta_capi_canvas.png", "21595", "Hash & sync leads to Meta CAPI", "Integrated stack: DevDeskApp · Meta Graph API · Google Sheets · Slack"),
    "canvas-21596": ("screen_notion_wp_canvas.png", "21596", "Publish SEO-safe Notion posts to WordPress", "Integrated stack: DevDeskApp · Notion · WordPress · Slack"),
}
for _key, (_raw, _id, _title, _sub) in CANVASES.items():
    FIGURES[_key] = (lambda raw=_raw, tid=_id, title=_title, sub=_sub: framed_screenshot(
        raw, (22, 92, 1578, 948), title, sub, pill=f"Template #{tid} · live on n8n.io", tone="green",
        masks=[((56, 820, 284, 920), 320, 0), ((22, 820, 56, 920), 0, -300)]))


def render(keys):
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        page = browser.new_page(viewport={"width": 1600, "height": 900}, device_scale_factor=1)
        for key in keys:
            page.set_content(f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{FIGURES[key]()}</body></html>",
                             wait_until="networkidle")
            page.evaluate("document.fonts.ready")
            target = OUT / f"fig-{key}.png"
            page.locator(".fig").screenshot(path=str(target))
            Image.open(target).convert("RGB").save(target, optimize=True)
            print("wrote", target.relative_to(ROOT))
        browser.close()
    for tmp in RAW.glob("_crop_*"):
        tmp.unlink()


if __name__ == "__main__":
    render(sys.argv[1:] or list(FIGURES))
