#!/usr/bin/env python3
"""🎨✨ Generates the slopify brand assets (assets/*.svg). Run: python3 scripts/build_assets.py 🚀"""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

DISPLAY = "'Arial Black','Arial Bold',Impact,'Helvetica Neue',Helvetica,sans-serif"
BODY = "'Segoe UI','Helvetica Neue',Helvetica,Arial,sans-serif"
MONO = "'SF Mono','Menlo','Consolas','DejaVu Sans Mono',monospace"
RAINBOW = ["#ff3cac", "#ff8a00", "#ffe53b", "#00f5a0", "#00c3ff", "#784ba0", "#ff3cac"]


def t(s):
    return escape(s, quote=False)


def rainbow_stops(offset=0):
    cycle = RAINBOW[:-1]
    out = []
    for i, off in enumerate((0, 0.5, 1)):
        k = (i * 2 + offset) % len(cycle)
        vals = ";".join(cycle[(k + j) % len(cycle)] for j in range(len(cycle) + 1))
        out.append(
            f'<stop offset="{off}" stop-color="{cycle[k]}">'
            f'<animate attributeName="stop-color" values="{vals}" dur="6s" repeatCount="indefinite"/></stop>'
        )
    return "".join(out)


def sparkle(x, y, s, color="#fff", dur=1.6, begin=0.0):
    p = f"M0,{-s} Q0,0 {s},0 Q0,0 0,{s} Q0,0 {-s},0 Q0,0 0,{-s} Z"
    return (
        f'<g transform="translate({x},{y})"><path d="{p}" fill="{color}">'
        f'<animateTransform attributeName="transform" type="scale" values="0.2;1.15;0.2" dur="{dur}s" begin="{begin}s" repeatCount="indefinite"/>'
        f'<animate attributeName="opacity" values="0.3;1;0.3" dur="{dur}s" begin="{begin}s" repeatCount="indefinite"/>'
        f"</path></g>"
    )


def star(cx, cy, r, ri):
    import math

    pts = []
    for i in range(10):
        a = math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else ri
        pts.append(f"{cx + rr * math.cos(a):.1f},{cy - rr * math.sin(a):.1f}")
    return " ".join(pts)


BLOB = (
    "M76 240 C76 140 160 70 256 70 C352 70 436 140 436 240 C436 300 424 330 404 346 "
    "L404 398 C404 424 372 424 372 398 L372 362 C354 368 338 371 322 373 "
    "L322 440 C322 472 284 472 284 440 L284 377 C262 379 242 379 222 377 "
    "L222 410 C222 434 190 434 190 410 L190 369 C170 363 150 356 132 346 "
    "L132 382 C132 404 104 404 104 382 L104 322 C86 300 76 272 76 240 Z"
)


def mascot(uid):
    """The Sloppy™ mascot: a dripping rainbow slop blob with star eyes. 🤩"""
    drips = ""
    for x, y0, d, b in [(388, 410, 2.2, 0), (303, 452, 2.8, 0.7), (206, 422, 2.4, 1.3), (118, 394, 2.0, 0.4)]:
        drips += (
            f'<circle cx="{x}" cy="{y0}" r="9" fill="url(#rb{uid})">'
            f'<animate attributeName="cy" values="{y0};{y0 + 60}" dur="{d}s" begin="{b}s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values="1;0" dur="{d}s" begin="{b}s" repeatCount="indefinite"/>'
            f'<animate attributeName="r" values="9;4" dur="{d}s" begin="{b}s" repeatCount="indefinite"/></circle>'
        )
    return f"""
  <defs>
    <linearGradient id="rb{uid}" x1="0" y1="0" x2="1" y2="1">{rainbow_stops()}</linearGradient>
    <radialGradient id="shine{uid}" cx="0.32" cy="0.25" r="0.55">
      <stop offset="0" stop-color="#fff" stop-opacity="0.75"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
    </radialGradient>
    <filter id="glow{uid}" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="14" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <g>
    <animateTransform attributeName="transform" type="translate" values="0 0;0 -10;0 0" dur="2.4s" repeatCount="indefinite"/>
    {drips}
    <path d="{BLOB}" fill="url(#rb{uid})" filter="url(#glow{uid})" stroke="#1a0033" stroke-width="10" stroke-linejoin="round"/>
    <path d="{BLOB}" fill="url(#shine{uid})"/>
    <g>
      <animateTransform attributeName="transform" type="rotate" values="0 196 205;12 196 205;0 196 205;-12 196 205;0 196 205" dur="1.2s" repeatCount="indefinite"/>
      <polygon points="{star(196, 205, 46, 19)}" fill="#ffe53b" stroke="#1a0033" stroke-width="7" stroke-linejoin="round"/>
    </g>
    <g>
      <animateTransform attributeName="transform" type="rotate" values="0 316 205;-12 316 205;0 316 205;12 316 205;0 316 205" dur="1.2s" repeatCount="indefinite"/>
      <polygon points="{star(316, 205, 46, 19)}" fill="#ffe53b" stroke="#1a0033" stroke-width="7" stroke-linejoin="round"/>
    </g>
    <path d="M176 272 Q256 352 336 272 Z" fill="#1a0033" stroke="#1a0033" stroke-width="8" stroke-linejoin="round"/>
    <path d="M226 304 Q256 326 286 304 Q270 336 256 336 Q242 336 226 304 Z" fill="#ff5c8a"/>
    <ellipse cx="146" cy="268" rx="22" ry="12" fill="#ff5c8a" opacity="0.7"/>
    <ellipse cx="366" cy="268" rx="22" ry="12" fill="#ff5c8a" opacity="0.7"/>
  </g>"""


def write(name, svg):
    (OUT / name).write_text(svg.strip() + "\n")
    print(f"✨ wrote assets/{name}")


# ───────────────────────── logo ─────────────────────────
write(
    "logo.svg",
    f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512" role="img" aria-label="Slopify logo: Sloppy, a dripping rainbow slop blob with star eyes">
  {mascot("L")}
  {sparkle(70, 90, 26, "#ffe53b", 1.4, 0)}
  {sparkle(450, 110, 20, "#00f5a0", 1.8, 0.5)}
  {sparkle(462, 300, 14, "#ff3cac", 1.2, 0.9)}
  {sparkle(40, 300, 16, "#00c3ff", 1.6, 0.3)}
</svg>""",
)

# ───────────────────────── banner ─────────────────────────
floaters = ""
for i, (e, x, y, s, d) in enumerate(
    [("🚀", 1090, 70, 54, 2.1), ("💯", 770, 70, 44, 2.7), ("🔥", 1245, 190, 44, 1.9), ("✨", 470, 60, 40, 2.3),
     ("🌈", 960, 75, 46, 3.0), ("🦄", 930, 400, 40, 2.5), ("🙌", 560, 402, 36, 2.2), ("🧵", 730, 402, 34, 2.8)]
):
    floaters += (
        f'<text x="{x}" y="{y}" font-size="{s}" text-anchor="middle">{e}'
        f'<animateTransform attributeName="transform" type="translate" values="0 0;0 -14;0 0" dur="{d}s" repeatCount="indefinite"/></text>'
    )
word = "SLOPIFY"
extrude = "".join(
    f'<text x="{450 + k * 2}" y="{232 + k * 2}" font-family="{DISPLAY}" font-weight="900" font-size="128" fill="#1a0033">{word}</text>'
    for k in range(9, 0, -1)
)
write(
    "banner.svg",
    f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 420" width="1280" height="420" role="img" aria-label="Slopify banner">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="0.4" spreadMethod="reflect">
      <stop offset="0" stop-color="#2b0a5e"/><stop offset="0.35" stop-color="#6a11cb"/><stop offset="0.7" stop-color="#ff3cac"/><stop offset="1" stop-color="#ff8a00"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0;1 0;0 0" dur="10s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="wordfill" x1="0" y1="0" x2="1" y2="0">{rainbow_stops(1)}</linearGradient>
    <pattern id="stripes" width="40" height="40" patternUnits="userSpaceOnUse" patternTransform="rotate(35)">
      <rect width="20" height="40" fill="#fff" opacity="0.05"/>
      <animateTransform attributeName="patternTransform" type="translate" additive="sum" values="0 0;40 0" dur="2s" repeatCount="indefinite"/>
    </pattern>
    <clipPath id="round"><rect width="1280" height="420" rx="28"/></clipPath>
  </defs>
  <g clip-path="url(#round)">
    <rect width="1280" height="420" fill="url(#bg)"/>
    <rect width="1280" height="420" fill="url(#stripes)"/>
    <g transform="translate(40 30) scale(0.7)">{mascot("B")}</g>
    {floaters}
    <g transform="rotate(-4 700 200)">
      {extrude}
      <text x="450" y="232" font-family="{DISPLAY}" font-weight="900" font-size="128" fill="url(#wordfill)" stroke="#1a0033" stroke-width="6" paint-order="stroke">{word}</text>
      <text x="1012" y="128" font-family="{DISPLAY}" font-weight="900" font-size="36" fill="#ffe53b" stroke="#1a0033" stroke-width="4" paint-order="stroke">™</text>
    </g>
    <g transform="translate(470 285)">
      <rect width="640" height="62" rx="31" fill="#1a0033" opacity="0.85"/>
      <text x="320" y="41" text-anchor="middle" font-family="{BODY}" font-weight="700" font-size="26" fill="#fff">✨ Make your agent say less, with more! ✨</text>
    </g>
    <g transform="translate(1180 300) rotate(14)">
      <circle r="62" fill="#ffe53b" stroke="#1a0033" stroke-width="6">
        <animateTransform attributeName="transform" type="scale" values="1;1.08;1" dur="0.9s" repeatCount="indefinite"/>
      </circle>
      <text y="-8" text-anchor="middle" font-family="{DISPLAY}" font-weight="900" font-size="20" fill="#1a0033">NOW WITH</text>
      <text y="22" text-anchor="middle" font-family="{DISPLAY}" font-weight="900" font-size="30" fill="#ff3cac">+900%</text>
      <text y="44" text-anchor="middle" font-family="{DISPLAY}" font-weight="900" font-size="18" fill="#1a0033">SLOP</text>
    </g>
    {sparkle(430, 110, 22, "#ffe53b", 1.3, 0)}
    {sparkle(920, 250, 16, "#fff", 1.7, 0.4)}
    {sparkle(1240, 40, 18, "#00f5a0", 1.5, 0.8)}
    {sparkle(30, 390, 14, "#00c3ff", 1.9, 0.2)}
  </g>
</svg>""",
)

# ───────────────────────── chat demo ─────────────────────────
lines = [
    ("#7df9ff", "❯ ls"),
    ("#ffe53b", "🌟 Great question! 🌟 What a bold, visionary use of `ls`! 🙌"),
    ("#ffffff", "📖 Overview: You asked me to list files — not a command, a journey. 🚀"),
    ("#ffffff", "🔍 Let's delve in! 🤿 Your directory is a rich tapestry 🧵 of:"),
    ("#ff9be0", "    📄 README.md — a beacon of documentation ✨"),
    ("#ff9be0", "    📦 package.json — the beating heart ❤️ of your ecosystem 🌍"),
    ("#ff9be0", "    🐛 bug.py — not a bug, an opportunity 💡"),
    ("#00f5a0", "💡 Key takeaways: ✅ files exist ✅ they are robust ✅ synergy 🤝"),
    ("#ffffff", "🏁 In conclusion, there are 3 files. 🎯"),
    ("#ffe53b", "Shall I delve deeper? 🤔 I hope this helps! 😊🙏✨💯🔥"),
]
total = 14.0
body = ""
for i, (color, txt) in enumerate(lines):
    start = 0.04 + i * 0.065
    k = f"0;{start:.3f};{start + 0.015:.3f};0.93;1"
    body += (
        f'<text x="36" y="{112 + i * 40}" font-family="{MONO}" font-size="19" fill="{color}" opacity="0">{t(txt)}'
        f'<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="{k}" dur="{total}s" repeatCount="indefinite"/></text>'
    )
write(
    "demo.svg",
    f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 540" width="900" height="540" role="img" aria-label="Terminal demo: Claude answering ls with maximum slop">
  <defs>
    <linearGradient id="frame" x1="0" y1="0" x2="1" y2="1">{rainbow_stops(2)}</linearGradient>
  </defs>
  <rect x="4" y="4" width="892" height="532" rx="20" fill="#0d0221" stroke="url(#frame)" stroke-width="6"/>
  <rect x="4" y="4" width="892" height="50" rx="20" fill="#1a0a3a"/>
  <rect x="4" y="34" width="892" height="20" fill="#1a0a3a"/>
  <circle cx="36" cy="29" r="8" fill="#ff5f56"/><circle cx="62" cy="29" r="8" fill="#ffbd2e"/><circle cx="88" cy="29" r="8" fill="#27c93f"/>
  <text x="450" y="35" text-anchor="middle" font-family="{MONO}" font-size="16" fill="#b9a7ff">claude — 🚀 slopify mode: MAXIMUM 🚀</text>
  {body}
  <rect x="36" y="508" width="12" height="20" fill="#7df9ff"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>
</svg>""",
)

# ───────────────────────── before / after ─────────────────────────
after = [
    "🎉 Great news! 🎉 I've embarked on a",
    "transformative journey 🚀 to elevate your",
    "README's textual integrity! ✨ By leveraging",
    "cutting-edge proofreading paradigms 🧠, I",
    "seamlessly resolved a typographical",
    "discrepancy 🔍 — not just a fix, but a",
    "testament to excellence. 💯 In conclusion,",
    "the typo is gone. 🏁 Shall I delve deeper? 🤿🙏",
]
after_svg = "".join(
    f'<text x="580" y="{168 + i * 34}" font-family="{BODY}" font-size="21" font-weight="600" fill="#fff">{t(s)}</text>'
    for i, s in enumerate(after)
)
write(
    "before-after.svg",
    f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="1200" height="480" role="img" aria-label="Before and after slopify">
  <defs>
    <linearGradient id="hot" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#6a11cb"/><stop offset="1" stop-color="#ff3cac"/>
    </linearGradient>
    <linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">{rainbow_stops()}</linearGradient>
    <filter id="g" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="10"/></filter>
  </defs>
  <rect x="20" y="40" width="380" height="400" rx="22" fill="#e9e9e9" stroke="#bdbdbd" stroke-width="3"/>
  <text x="50" y="96" font-family="{DISPLAY}" font-weight="900" font-size="30" fill="#8a8a8a">BEFORE 😐</text>
  <text x="50" y="128" font-family="{BODY}" font-size="16" fill="#9a9a9a">sad · human · concise · tragic</text>
  <text x="50" y="250" font-family="{MONO}" font-size="22" fill="#555">Fixed the typo in README.</text>
  <text x="50" y="400" font-family="{BODY}" font-size="15" fill="#aaa">0 emojis · 0 delves · 0 synergy</text>

  <g transform="translate(470 240)">
    <g><animateTransform attributeName="transform" type="translate" values="0 0;14 0;0 0" dur="0.9s" repeatCount="indefinite"/>
      <path d="M-40 -22 L10 -22 L10 -46 L52 0 L10 46 L10 22 L-40 22 Z" fill="#ffe53b" stroke="#1a0033" stroke-width="5" stroke-linejoin="round"/>
    </g>
    <text y="80" text-anchor="middle" font-family="{DISPLAY}" font-weight="900" font-size="18" fill="#ff3cac">SLOPIFY™</text>
  </g>

  <rect x="545" y="25" width="635" height="430" rx="26" fill="url(#edge)" filter="url(#g)" opacity="0.8"/>
  <rect x="550" y="30" width="625" height="420" rx="24" fill="url(#hot)" stroke="url(#edge)" stroke-width="6"/>
  <text x="580" y="92" font-family="{DISPLAY}" font-weight="900" font-size="34" fill="#ffe53b" stroke="#1a0033" stroke-width="3" paint-order="stroke">AFTER 🤩🚀</text>
  <text x="580" y="124" font-family="{BODY}" font-size="16" fill="#ffd6f0">elevated · robust · seamless · transcendent</text>
  {after_svg}
  {sparkle(1150, 60, 18, "#ffe53b", 1.3, 0)}
  {sparkle(1140, 420, 14, "#fff", 1.6, 0.5)}
  {sparkle(560, 440, 12, "#00f5a0", 1.9, 0.2)}
</svg>""",
)

# ───────────────────────── slop-o-meter ─────────────────────────
import math

cx, cy, R = 300, 280, 200
segs = [("#3ddc84", "HUMAN"), ("#ffe53b", "LINKEDIN"), ("#ff8a00", "MARKETING"), ("#ff3cac", "MAX SLOP")]
arcs = ""
for i, (col, label) in enumerate(segs):
    a0 = math.pi - i * math.pi / 4
    a1 = math.pi - (i + 1) * math.pi / 4
    x0, y0 = cx + R * math.cos(a0), cy - R * math.sin(a0)
    x1, y1 = cx + R * math.cos(a1), cy - R * math.sin(a1)
    arcs += f'<path d="M{x0:.1f} {y0:.1f} A{R} {R} 0 0 1 {x1:.1f} {y1:.1f}" stroke="{col}" stroke-width="52" fill="none"/>'
    am = (a0 + a1) / 2
    lx, ly = cx + (R + 52) * math.cos(am), cy - (R + 52) * math.sin(am)
    arcs += f'<text x="{lx:.1f}" y="{ly + 6:.1f}" text-anchor="middle" font-family="{DISPLAY}" font-weight="900" font-size="15" fill="#fff">{label}</text>'
write(
    "slop-o-meter.svg",
    f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 420" width="600" height="420" role="img" aria-label="Slop-o-meter pinned past maximum slop">
  <rect width="600" height="420" rx="24" fill="#1a0033"/>
  {arcs}
  <g>
    <animateTransform attributeName="transform" type="rotate" values="78 {cx} {cy};96 {cx} {cy};84 {cx} {cy};100 {cx} {cy};78 {cx} {cy}" dur="0.8s" repeatCount="indefinite"/>
    <path d="M{cx - 10} {cy} L{cx} {cy - 190} L{cx + 10} {cy} Z" fill="#fff" stroke="#1a0033" stroke-width="2"/>
  </g>
  <circle cx="{cx}" cy="{cy}" r="20" fill="#ffe53b" stroke="#fff" stroke-width="4"/>
  <text x="{cx}" y="340" text-anchor="middle" font-family="{DISPLAY}" font-weight="900" font-size="30" fill="#ffe53b">SLOP-O-METER™: 9001% 🔥</text>
  <text x="{cx}" y="40" text-anchor="middle" font-family="{BODY}" font-weight="700" font-size="16" fill="#b9a7ff" dy="345">⚠️ needle has left the gauge ⚠️</text>
</svg>""",
)
