#!/usr/bin/env python3
"""Render the divided-monarchy regnal-evaluation timeline (Guide B) from kings.json.

Build lane (Claude Code). Reads data/divided-kingdom/kings.json and writes
static/images/culture/divided-kingdom/regnal-timeline.svg.

Design decision (per build plan): UNIFORM cells ordered by reign sequence, not a
to-scale timeline. dates_bce are null in the data (no chronology chosen yet) and
co-regencies overlap, so width-scaling would imply precision we don't have. When a
chronology (e.g. Thiele) is chosen and dates_bce are filled in, each cell gains a
BCE label automatically via the date hook below — no other change needed.

The verdict colors come straight from the data: every northern king is 'evil'
(an unbroken wall), Judah is mixed (8 'right'). The repetition IS the visual.

Re-run after editing kings.json:  python3 scripts/build_regnal_timeline.py
"""
import json
import os
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "divided-kingdom", "kings.json")
OUT = os.path.join(ROOT, "static", "images", "culture", "divided-kingdom", "regnal-timeline.svg")

# CFM Corner Moedim palette: warm parchment, paper-cut forms, soft shadows.
COLORS = {
    "right": "#6f8a55",   # desert/olive green — "did right in the sight of the LORD"
    "evil": "#c4622d",    # muted terracotta   — "did evil in the sight of the LORD"
    "none": "#5a7d92",    # slate blue         — no evaluation formula (usurper)
}
INK = "#243049"      # deep navy text
MUTED = "#6b5a3e"    # warm brown
CREAM = "#f9f1de"    # label text on colored cells
PARCH = "#f1e3c6"    # parchment background

# layout
LEFT = 84          # row-label gutter
CW = 52            # cell width
GAP = 6
PITCH = CW + GAP
CH = 152           # cell height
JUDAH_TOP = 116
ISRAEL_TOP = 322


def reign_label(v):
    """Format reign_years_text (years) into a compact label."""
    if v is None:
        return ""
    if v >= 1:
        return f"{v:g} yr"
    months = round(v * 12)
    if months >= 1:
        return f"{months} mo"
    days = round(v * 365)
    return f"{days} days"


def cell(king, x, top):
    color = COLORS.get(king["verdict"], "#999")
    cx = x + CW / 2
    name = escape(king["name"])
    out = []
    out.append(
        f'<rect x="{x}" y="{top}" width="{CW}" height="{CH}" rx="7" '
        f'fill="{color}" stroke="{PARCH}" stroke-width="2" filter="url(#cellshadow)"/>'
    )
    # subtle top highlight (paper-cut sheen)
    out.append(
        f'<rect x="{x+3}" y="{top+3}" width="{CW-6}" height="7" rx="3.5" '
        f'fill="#ffffff" opacity="0.14"/>'
    )
    # order number (top)
    out.append(
        f'<text x="{cx:.1f}" y="{top+18}" text-anchor="middle" font-size="10.5" '
        f'fill="{CREAM}" opacity="0.85" font-family="-apple-system,Segoe UI,Roboto,sans-serif">'
        f'{king["order"]}</text>'
    )
    # king name (rotated, reads bottom-to-top, centered)
    ny = top + CH / 2 + 6
    out.append(
        f'<text x="{cx:.1f}" y="{ny:.1f}" text-anchor="middle" font-size="12.5" '
        f'font-weight="600" fill="{CREAM}" font-family="Georgia,serif" '
        f'transform="rotate(-90 {cx:.1f} {ny:.1f})">{name}</text>'
    )
    # reign length (bottom)
    out.append(
        f'<text x="{cx:.1f}" y="{top+CH-10}" text-anchor="middle" font-size="10" '
        f'fill="{CREAM}" opacity="0.92" font-family="-apple-system,Segoe UI,Roboto,sans-serif">'
        f'{reign_label(king.get("reign_years_text"))}</text>'
    )
    # BCE date hook — renders only once dates_bce is filled from a chosen chronology
    if king.get("dates_bce"):
        out.append(
            f'<text x="{cx:.1f}" y="{top+CH+14}" text-anchor="middle" font-size="9.5" '
            f'fill="{MUTED}" font-family="-apple-system,Segoe UI,Roboto,sans-serif">'
            f'{escape(str(king["dates_bce"]))}</text>'
        )
    return "\n    ".join(out)


def build():
    d = json.load(open(DATA))
    judah = d["kingdoms"]["judah"]
    israel = d["kingdoms"]["israel"]
    sj = d["summary"]["judah"]
    si = d["summary"]["israel"]

    width = LEFT + len(judah) * PITCH + 20
    height = 560

    p = []
    p.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" '
        f'aria-label="Regnal-evaluation timeline of the divided monarchy. The northern Kingdom of '
        f'Israel: all 19 kings judged evil. The southern Kingdom of Judah: 8 of 20 did right, the '
        f'rest evil or unevaluated. Ordered by reign sequence; verdicts quoted from 1-2 Kings.">'
    )
    p.append('<title>Regnal Evaluations — the Deuteronomistic verdict</title>')

    # defs: soft paper-cut shadow + edge vignette
    p.append(
        '<defs>'
        '<filter id="cellshadow" x="-30%" y="-30%" width="160%" height="160%">'
        '<feDropShadow dx="0" dy="3" stdDeviation="3" flood-color="#5a4422" flood-opacity="0.28"/>'
        '</filter>'
        f'<radialGradient id="vign" cx="50%" cy="48%" r="72%">'
        '<stop offset="66%" stop-color="#000" stop-opacity="0"/>'
        '<stop offset="100%" stop-color="#5a4422" stop-opacity="0.13"/>'
        '</radialGradient>'
        '</defs>'
    )
    # parchment background
    p.append(f'<rect x="0" y="0" width="{width}" height="{height}" fill="{PARCH}"/>')

    # title + subtitle
    p.append(
        f'<text x="{width/2:.0f}" y="38" text-anchor="middle" font-size="26" font-weight="700" '
        f'fill="{INK}" font-family="Georgia,serif">Regnal Evaluations — the Deuteronomistic Verdict</text>'
    )
    p.append(
        f'<text x="{width/2:.0f}" y="60" text-anchor="middle" font-size="13" fill="{MUTED}" '
        f'font-family="Georgia,serif">Each king graded by one repeating formula: did he do right, or evil, '
        f'in the sight of the LORD? (1–2 Kings)</text>'
    )

    # legend (top-right under subtitle)
    lx = LEFT
    leg = [("right", "did right"), ("evil", "did evil"), ("none", "no formula (usurper)")]
    p.append(f'<g font-family="-apple-system,Segoe UI,Roboto,sans-serif" font-size="12" fill="{INK}">')
    for key, lab in leg:
        p.append(f'<rect x="{lx}" y="80" width="16" height="16" rx="3" fill="{COLORS[key]}"/>')
        p.append(f'<text x="{lx+22}" y="92">{lab}</text>')
        lx += 36 + len(lab) * 7.4
    p.append('</g>')

    # ---- Judah ----
    p.append(
        f'<text x="{LEFT}" y="{JUDAH_TOP-6}" font-size="14" font-weight="700" fill="{INK}" '
        f'font-family="Georgia,serif">KINGDOM OF JUDAH '
        f'<tspan font-weight="400" fill="#5a4a32" font-size="12">— {sj["right"]} right · '
        f'{sj["evil"]} evil · {sj["none"]} none (of {sj["total"]})</tspan></text>'
    )
    for i, k in enumerate(judah):
        p.append("    " + cell(k, LEFT + i * PITCH, JUDAH_TOP))
    # row label
    jcy = JUDAH_TOP + CH / 2
    p.append(
        f'<text x="34" y="{jcy:.0f}" text-anchor="middle" font-size="13" fill="{MUTED}" '
        f'font-family="Georgia,serif" letter-spacing="2" transform="rotate(-90 34 {jcy:.0f})">JUDAH</text>'
    )

    # ---- Israel ----
    p.append(
        f'<text x="{LEFT}" y="{ISRAEL_TOP-6}" font-size="14" font-weight="700" fill="{INK}" '
        f'font-family="Georgia,serif">KINGDOM OF ISRAEL '
        f'<tspan font-weight="400" fill="#5a4a32" font-size="12">— {si["evil"]} evil of {si["total"]}: '
        f'every northern king did evil</tspan></text>'
    )
    for i, k in enumerate(israel):
        p.append("    " + cell(k, LEFT + i * PITCH, ISRAEL_TOP))
    icy = ISRAEL_TOP + CH / 2
    p.append(
        f'<text x="34" y="{icy:.0f}" text-anchor="middle" font-size="13" fill="{MUTED}" '
        f'font-family="Georgia,serif" letter-spacing="2" transform="rotate(-90 34 {icy:.0f})">ISRAEL</text>'
    )

    # footnotes
    fy = ISRAEL_TOP + CH + 26
    p.append(
        f'<text x="{LEFT}" y="{fy}" font-size="10.5" fill="{MUTED}" '
        f'font-family="-apple-system,Segoe UI,Roboto,sans-serif">'
        f'Ordered by reign sequence, not to scale — cells are uniform. Numbers in each cell give the '
        f'order and reign length stated in the text (co-regencies overlap).</text>'
    )
    p.append(
        f'<text x="{LEFT}" y="{fy+15}" font-size="10.5" fill="{MUTED}" '
        f'font-family="-apple-system,Segoe UI,Roboto,sans-serif">'
        f'Absolute BCE dates omitted until a chronology (e.g. Thiele) is chosen. Elah &amp; Shallum have no '
        f'explicit evaluation formula but are placed with the dynasty they continue. Verdicts verified verbatim, 1–2 Kings.</text>'
    )

    p.append(f'<rect x="0" y="0" width="{width}" height="{height}" fill="url(#vign)" pointer-events="none"/>')
    p.append('</svg>')
    with open(OUT, "w") as f:
        f.write("\n".join(p) + "\n")
    print(f"wrote {OUT}  ({width}x{height})")


if __name__ == "__main__":
    build()
