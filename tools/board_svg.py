"""Board generator: draws the Hayabusa board as SVG and prepares print files.

For every language (EN, PL) and colour version (dark, light) it writes:
  board/board[-light][_pl].svg        - the whole board on one page (268 x 200 mm)
  board/board[-light][_pl]_a2.pdf     - A2 board from 4 A4 sheets (2 x 2, landscape)
  board/board[-light][_pl]_a3.pdf     - A3 board from 2 A4 sheets (side by side, portrait)
and also board/board[_pl].png (preview) and board/qrcode[_pl].svg.

The multi-sheet PDFs overlap neighbouring sheets by a glue strip: one sheet gets
a hatched strip, the next is trimmed along its edge line and glued on top.

Requires: Python 3, segno (QR codes); rsvg-convert for PDF and PNG
(on Windows e.g. in WSL: sudo apt install librsvg2-bin) and the Exo 2 and
Orbitron fonts installed (Google Fonts, OFL licence).

    pip install segno
    python board_svg.py            # everything into ../board
    python board_svg.py --svg-only # only SVG, without rsvg-convert
"""
import argparse
import math
import os
import shutil
import subprocess
import tempfile

import segno

VERSION = "0.6"

# --- geometry (millimetres, scale of the one-page board) ---------------------
S = 10.0                     # hex side; hexes are pointy-top
R3 = math.sqrt(3)
RADIUS = 6                   # rings 0..6
PAGE_W, PAGE_H = 268.13, 200.0
SUN = (PAGE_W - (RADIUS + 0.5) * R3 * S, PAGE_H / 2)   # board touches the right edge
ROTATION = -60               # board content (v0.4.1 layout); 0 = sector 12 at the top

URL = {"en": "https://bsulkowski.pl/hayabusa", "pl": "https://bsulkowski.pl/pl/hayabusa"}

TEXT = {
    "en": dict(title="Hayabusa", subtitle=["a game board of the", "inner Solar System"],
               mars="Mars", earth="Earth", venus="Venus", mercury="Mercury",
               belt="asteroid belt", d12="d12", d8="d8",
               version=f"board v{VERSION}", sheet="sheet", glue="glue sheet {n} here"),
    "pl": dict(title="Hayabusa", subtitle=["plansza do gier w wewnętrznym", "Układzie Słonecznym"],
               mars="Mars", earth="Ziemia", venus="Wenus", mercury="Merkury",
               belt="pas planetoid", d12="k12", d8="k8",
               version=f"plansza v{VERSION}", sheet="arkusz", glue="tu przyklej arkusz {n}"),
}

NAVY, ORANGE, SUN_YELLOW = "#000040", "#ff8000", "#ffff60"
EXO, ORBITRON = "'Exo 2', sans-serif", "Orbitron, sans-serif"
THEMES = {
    # ring: (fill, stroke); belt: even and odd sectors; text colours per ring 1-3
    "dark": dict(rings={0: ("#6060ff", "#000080"), 1: ("#3030ff", "#000000"),
                        2: ("#0000ff", "#000000"), 3: ("#000080", "#000000")},
                 belt=("#000040", "#000000"), belt_stroke="#0000ff",
                 ring_text={1: "#ffffff", 2: "#e0e0ff", 3: "#c0c0ff"}, belt_text="#8080ff"),
    "light": dict(rings={0: ("#000040", "#000080"), 1: ("#000080", "#000000"),
                         2: ("#0000ff", "#000000"), 3: ("#6060ff", "#000000")},
                  belt=("#c0c0ff", "#ffffff"), belt_stroke=NAVY,
                  ring_text={1: "#c0c0ff", 2: "#e0e0ff", 3: "#ffffff"}, belt_text="#8060ff"),
}

# Dice labels in the asteroid belt. Sectors come in pairs spanning 60 degrees:
# an even sector of 8 hexes and an odd one of 7, where "3-4" covers two results
# (6 x 15 = 90 hexes for 12 x 8 = 96 results). The pair below is sectors 12 and 1
# with sector 12 at the top; the others are the same pair turned by 60 degrees.
# Hex positions are axial coordinates (q, r); d8 result -> hex.
EVEN = {"1": (1, -4), "2": (2, -4), "3": (2, -5), "4": (3, -5),
        "5": (4, -5), "6": (4, -6), "7": (5, -6), "8": (6, -6)}
ODD = {"1": (3, -4), "2": (4, -4), "3-4": (5, -5), "5": (5, -4),
       "6": (6, -5), "7": (6, -4), "8": (6, -3)}
BIG = "2"   # the sector number stands in the hex of d8 result 2

SMALL, BIG_SIZE, PLANET, MINOR = 4.23, 11.29, 7.06, 4.23   # font sizes (mm)


def turn(h, k):
    """Axial hex coordinates turned k times by 60 degrees clockwise."""
    q, r = h
    for _ in range(k % 6):
        q, r = -r, q + r
    return q, r


def ring(h):
    q, r = h
    return max(abs(q), abs(r), abs(q + r))


def centre(h):
    q, r = h
    return R3 * S * (q + r / 2), 1.5 * S * r


def belt_sectors():
    """hex -> (sector number, d8 label, sector parity) for all 90 belt hexes."""
    out = {}
    for k in range(6):
        even, odd = 2 * k or 12, 2 * k + 1
        for number, layout in ((even, EVEN), (odd, ODD)):
            for label, h in layout.items():
                out[turn(h, k)] = (number, label, number % 2)
    assert len(out) == 90
    return out


def fmt(x):
    return f"{x:.3f}".rstrip("0").rstrip(".")


def hex_points(cx, cy, s):
    pts = [(cx + s * math.cos(math.radians(60 * i - 30)), cy + s * math.sin(math.radians(60 * i - 30)))
           for i in range(6)]
    return " ".join(f"{fmt(x)},{fmt(y)}" for x, y in pts)


def text(x, y, s, size, fill, font=EXO, rotate=0, anchor="middle"):
    s = s.replace("&", "&amp;").replace("<", "&lt;")
    rot = f' transform="rotate({fmt(rotate)} {fmt(x)} {fmt(y)})"' if rotate else ""
    return (f'<text x="{fmt(x)}" y="{fmt(y)}" font-family="{font}" font-size="{fmt(size)}" fill="{fill}" '
            f'text-anchor="{anchor}" dominant-baseline="central"{rot}>{s}</text>')


def arrows(x, y, n, fill):
    """n heavy arrows pointing right (direction of orbital motion), centred at (x, y)."""
    w, gap = 5.6, 1.0
    out, x0 = [], x - (n * w + (n - 1) * gap) / 2
    for i in range(n):
        a = x0 + i * (w + gap)
        d = (f"M{fmt(a)},{fmt(y - 0.75)} h2.8 v-1.6 l2.8,2.35 l-2.8,2.35 v-1.6 h-2.8 z")
        out.append(f'<path d="{d}" fill="{fill}"/>')
    return "".join(out)


def qr_path(url, x, y, size, rotate, fill):
    """QR code as one path, size x size mm, top left corner at (x, y), turned about its centre."""
    qr = segno.make(url, error="m", boost_error=False)
    m = qr.matrix
    n = len(m)
    u = size / n
    d = "".join(f"M{fmt(x + c * u)},{fmt(y + r * u)}h{fmt(u)}v{fmt(u)}h{fmt(-u)}z"
                for r, row in enumerate(m) for c, v in enumerate(row) if v)
    cx, cy = x + size / 2, y + size / 2
    return f'<path d="{d}" fill="{fill}" transform="rotate({fmt(rotate)} {fmt(cx)} {fmt(cy)})"/>'


def board_art(lang, theme):
    """The whole board as SVG elements, in millimetres of the one-page board."""
    t, th = TEXT[lang], THEMES[theme]
    sx, sy = SUN
    sectors = belt_sectors()
    el = []

    # board content, drawn with sector 12 at the top and turned as a whole
    g = []
    for q in range(-RADIUS, RADIUS + 1):
        for r in range(-RADIUS, RADIUS + 1):
            h = (q, r)
            k = ring(h)
            if k > RADIUS:
                continue
            x, y = centre(h)
            if k <= 3:
                fill, stroke = th["rings"][k]
            else:
                fill, stroke = th["belt"][sectors[h][2]], th["belt_stroke"]
            g.append(f'<polygon points="{hex_points(x, y, S)}" fill="{fill}" stroke="{stroke}" stroke-width="0.3"/>')
    for h, (number, label, _) in sectors.items():
        x, y = centre(h)
        g.append(text(x, y + 6.6, label, SMALL, ORANGE, ORBITRON))
        if label == BIG:
            g.append(text(x, y, str(number), BIG_SIZE, ORANGE, ORBITRON))
    g.append(f'<circle cx="0" cy="0" r="3.76" fill="{SUN_YELLOW}"/>')
    rt = th["ring_text"]
    g.append(text(0, -17.7, t["venus"], MINOR, rt[1]))
    g.append(text(0, -12.3, t["mercury"], MINOR, rt[1]))
    g.append(text(0, -30, t["earth"], PLANET, rt[2]))
    g.append(text(0, -44.8, t["mars"], PLANET, rt[3]))
    g.append(arrows(0, 15, 3, rt[1]))
    g.append(arrows(0, 30, 2, rt[2]))
    g.append(arrows(0, 45, 1, rt[3]))
    g.append(text(0, -76, t["belt"], BIG_SIZE, th["belt_text"]))   # in ring 5, above sector 12
    el.append(f'<g transform="translate({fmt(sx)} {fmt(sy)}) rotate({ROTATION})">{"".join(g)}</g>')

    # around the board: title, QR code, dice legend (relative to the Sun)
    def at(dx, dy):
        return sx + dx, sy + dy

    # text lines run parallel to the upper left edge of the board
    along = (math.cos(math.radians(-60)), math.sin(math.radians(-60)))
    down = (-along[1], along[0])
    tx, ty = at(-113, -51)
    el.append(text(tx, ty, t["title"], 15.5, NAVY, rotate=-60))
    for i, line in enumerate(t["subtitle"]):
        d = 11 + 5.6 * i
        el.append(text(tx + down[0] * d, ty + down[1] * d, line, 4.4, NAVY, rotate=-60))

    qx, qy = at(-137, 25)          # off the A2 seam, which runs through the middle
    size = 19
    el.append(qr_path(URL[lang], qx - size / 2, qy - size / 2, size, -60, NAVY))
    vx, vy = qx + down[0] * (size / 2 + 2.5), qy + down[1] * (size / 2 + 2.5)
    el.append(text(vx, vy, t["version"], 3.0, NAVY, ORBITRON, rotate=-60))

    lx, ly = at(-105.3, 61.2)
    el.append(f'<polygon points="{hex_points(lx, ly, 15)}" fill="{th["belt"][0]}" '
              f'stroke="{th["belt_stroke"]}" stroke-width="0.5"/>')
    leg = [text(lx, ly, t["d12"], BIG_SIZE, ORANGE, ORBITRON),
           text(lx, ly + 7.5, t["d8"], SMALL, ORANGE, ORBITRON)]
    el.append(f'<g transform="rotate({ROTATION} {fmt(lx)} {fmt(ly)})">{"".join(leg)}</g>')
    ax, ay = at(-111.7, 44.8)
    el.append(f'<path d="M{fmt(ax)},{fmt(ay)} v-8 l10.2,-7.4" fill="none" stroke="{ORANGE}" '
              f'stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>')
    hx, hy = ax + 10.2, ay - 15.4
    el.append(f'<path d="M{fmt(hx - 3.6)},{fmt(hy - 0.2)} L{fmt(hx)},{fmt(hy)} L{fmt(hx - 1.3)},{fmt(hy + 3.4)}" '
              f'fill="none" stroke="{ORANGE}" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>')
    return "".join(el)


def svg_doc(w, h, body, extra_defs=""):
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{fmt(w)}mm" height="{fmt(h)}mm" '
            f'viewBox="0 0 {fmt(w)} {fmt(h)}"><defs>{extra_defs}</defs>{body}</svg>\n')


# --- print on several A4 sheets ----------------------------------------------
A4 = (210.0, 297.0)
MARGIN = 7.0      # left unprinted at every edge of the sheet
GLUE = 10.0       # overlap of neighbouring sheets
FORMATS = {       # columns, rows, sheet orientation
    "a3": (2, 1, "portrait"),
    "a2": (2, 2, "landscape"),
}


def sheets(lang, theme, fmt_name):
    cols, rows, orient = FORMATS[fmt_name]
    sw, sh = A4 if orient == "portrait" else A4[::-1]
    cw, ch = sw - 2 * MARGIN, sh - 2 * MARGIN                      # printed area of a sheet
    total_w, total_h = cols * cw - (cols - 1) * GLUE, rows * ch - (rows - 1) * GLUE
    scale = min(total_w / PAGE_W, total_h / PAGE_H)
    ox, oy = (total_w - PAGE_W * scale) / 2, (total_h - PAGE_H * scale) / 2
    art = board_art(lang, theme)
    t = TEXT[lang]
    hatch = ('<pattern id="hatch" width="3" height="3" patternUnits="userSpaceOnUse" '
             'patternTransform="rotate(45)"><rect width="3" height="3" fill="#ffffff"/>'
             '<line x1="0" y1="0" x2="0" y2="3" stroke="#b0b0b0" stroke-width="0.4"/></pattern>')
    pages = []
    for r in range(rows):
        for c in range(cols):
            n = r * cols + 1 + c
            x0, y0 = c * (cw - GLUE), r * (ch - GLUE)                # this sheet in the assembled board
            body = [f'<clipPath id="area"><rect x="{MARGIN}" y="{MARGIN}" width="{fmt(cw)}" height="{fmt(ch)}"/></clipPath>',
                    f'<g clip-path="url(#area)"><g transform="translate({fmt(MARGIN - x0 + ox)} {fmt(MARGIN - y0 + oy)}) '
                    f'scale({fmt(scale)})">{art}</g></g>']
            # glue strips for the sheets that go on top (right and below)
            strips = []
            if c < cols - 1:
                strips.append((MARGIN + cw - GLUE, MARGIN, GLUE, ch, n + 1, 90))
            if r < rows - 1:
                strips.append((MARGIN, MARGIN + ch - GLUE, cw, GLUE, n + cols, 0))
            for x, y, w, h, other, rot in strips:
                body.append(f'<rect x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}" fill="url(#hatch)" '
                            f'stroke="#808080" stroke-width="0.3"/>')
                body.append(text(x + w / 2, y + h / 2, t["glue"].format(n=other), 3.2, "#606060", rotate=rot))
            # trim lines where this sheet goes on top of its neighbours (left and above)
            if c > 0:
                body.append(f'<line x1="{MARGIN}" y1="{MARGIN}" x2="{MARGIN}" y2="{fmt(MARGIN + ch)}" '
                            f'stroke="#808080" stroke-width="0.3" stroke-dasharray="2 1.5"/>')
            if r > 0:
                body.append(f'<line x1="{MARGIN}" y1="{MARGIN}" x2="{fmt(MARGIN + cw)}" y2="{MARGIN}" '
                            f'stroke="#808080" stroke-width="0.3" stroke-dasharray="2 1.5"/>')
            # sheet number in the outer corner, which stays white
            right, bottom = c == cols - 1, r == rows - 1
            lx = MARGIN + cw - 2 if right else MARGIN + 2
            ly = MARGIN + ch - 2 if bottom else MARGIN + 3
            label = f'Hayabusa {fmt_name.upper()} · {t["sheet"]} {n}/{rows * cols}'
            body.append(text(lx, ly, label, 2.8, "#808080", anchor="end" if right else "start"))
            pages.append(svg_doc(sw, sh, "".join(body), hatch))
    return pages, scale


def name(lang, theme):
    return "board" + ("-light" if theme == "light" else "") + ("_pl" if lang == "pl" else "")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "board"))
    ap.add_argument("--svg-only", action="store_true", help="skip PDF and PNG (no rsvg-convert)")
    args = ap.parse_args()
    out = os.path.abspath(args.out)
    os.makedirs(out, exist_ok=True)
    rsvg = None if args.svg_only else shutil.which("rsvg-convert")
    if not args.svg_only and not rsvg:
        print("rsvg-convert not found - writing SVG only")

    for lang in ("en", "pl"):
        qr = qr_path(URL[lang], 0, 0, 40, 0, NAVY)
        with open(os.path.join(out, "qrcode" + ("_pl" if lang == "pl" else "") + ".svg"), "w", encoding="utf-8") as f:
            f.write(svg_doc(40, 40, qr))
        for theme in ("dark", "light"):
            base = name(lang, theme)
            path = os.path.join(out, base + ".svg")
            with open(path, "w", encoding="utf-8") as f:
                f.write(svg_doc(PAGE_W, PAGE_H, f'<rect width="{PAGE_W}" height="{PAGE_H}" fill="#ffffff"/>'
                                + board_art(lang, theme)))
            print(path)
            if rsvg and theme == "dark":
                png = os.path.join(out, base + ".png")
                subprocess.run([rsvg, "-w", "1200", "-o", png, path], check=True)
                print(png)
            for fmt_name in FORMATS:
                pages, scale = sheets(lang, theme, fmt_name)
                if not rsvg:
                    continue
                with tempfile.TemporaryDirectory() as tmp:
                    files = []
                    for i, page in enumerate(pages, 1):
                        p = os.path.join(tmp, f"{i}.svg")
                        with open(p, "w", encoding="utf-8") as f:
                            f.write(page)
                        files.append(p)
                    pdf = os.path.join(out, f"{base}_{fmt_name}.pdf")
                    subprocess.run([rsvg, "-f", "pdf", "-o", pdf] + files, check=True)
                print(f"{pdf} ({len(pages)} sheets, hex {S * R3 * scale:.1f} mm across the flats)")


if __name__ == "__main__":
    main()
