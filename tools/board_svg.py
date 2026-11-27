"""Board generator: draws the Hayabusa board as SVG and prepares print files.

For every language (EN, PL) and colour version (dark, light) it writes:
  board/board[-light][_pl].svg        - the whole board on one page (268 x 200 mm)
  board/board[-light][_pl]_a2.pdf     - A2 board from 4 A4 sheets (2 x 2, landscape)
  board/board[-light][_pl]_a3.pdf     - A3 board from 2 A4 sheets (side by side, portrait)
and also board/board[_pl].png (preview) and board/qrcode[_pl].svg.

On the multi-sheet PDFs the margin is trimmed on both sides of every join, along
the dashed lines, and the sheets are butted together (taped on the back, the join
works as a hinge). The joins run between hex centres, never through them.

Requires: Python 3, segno (QR codes); rsvg-convert for PDF and PNG
(on Windows e.g. in WSL: sudo apt install librsvg2-bin) and the Exo 2 and
Orbitron fonts installed (Google Fonts, OFL licence).

    pip install segno
    python board_svg.py            # everything into ../board
    python board_svg.py --svg-only # only SVG, without rsvg-convert
"""
import argparse
import base64
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
PAGE_W, PAGE_H = 290.0, 200.0
# Joins between printed sheets, relative to the Sun: halfway between hex centres,
# right of the Sun (clear of the labels on the left) and below it.
SEAM_X = 1.5 * R3 * S / 2    # vertical join, between the 1st and 2nd column of centres
SEAM_Y = 1.5 * S / 2         # horizontal join (A2), between the rows of centres
LEFT = PAGE_W / 2 - SEAM_X - (RADIUS + 0.5) * R3 * S   # left page edge to board corner:
                             # puts the vertical join in the middle of the page
SUN = (LEFT + (RADIUS + 0.5) * R3 * S, PAGE_H / 2)
IMAGES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "board", "images")
ROTATION = 0                 # sectors as on a clock face: 12 at the top

URL = {"en": "https://bsulkowski.pl/hayabusa", "pl": "https://bsulkowski.pl/pl/hayabusa"}

TEXT = {   # noqa: E501
    "en": dict(title="Hayabusa", subtitle=["a game board of the", "inner Solar System"],
               mars="Mars", earth="Earth", venus="Venus", mercury="Mercury", ceres="Ceres",
               belt="asteroid belt", d12="d12", d8="d8", credits="images: NASA",
               version=f"board v{VERSION}", sheet="sheet"),
    "pl": dict(title="Hayabusa", subtitle=["plansza do gier", "w wewnętrznym", "Układzie Słonecznym"],
               mars="Mars", earth="Ziemia", venus="Wenus", mercury="Merkury", ceres="Ceres",
               belt="pas planetoid", d12="k12", d8="k8", credits="zdjęcia: NASA",
               version=f"plansza v{VERSION}", sheet="arkusz"),
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

SMALL, BIG_SIZE, SECTOR, PLANET, MINOR = 4.23, 11.29, 10.0, 7.06, 4.23   # font sizes (mm)


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


BOXES = []   # (x0, y0, x1, y1, text, size) of every horizontal text, for the seam check


def text(x, y, s, size, fill, font=EXO, rotate=0, anchor="middle"):
    if not rotate:
        w = len(s) * size * (0.72 if font == ORBITRON else 0.55)
        x0 = x - w / 2 if anchor == "middle" else (x - w if anchor == "end" else x)
        BOXES.append((x0, y - size * 0.4, x0 + w, y + size * 0.4, s, size))
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


# Station spaces: Earth and Mars (top and bottom right), Ceres (bottom left).
# Photos are read from board/images/<name>.jpg or .png (square, the planet filling
# the frame); without them the disc is drawn in a plain colour.
PLACEHOLDER = {"earth": ("#3a78c8", "#0b2a5a"), "mars": ("#c86a40", "#5a2410"), "ceres": ("#a0a0a0", "#3a3a3a")}


def planet(key, cx, cy, r):
    clip = f"clip-{key}"
    out = [f'<clipPath id="{clip}"><circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(r)}"/></clipPath>']
    for ext, mime in ((".jpg", "image/jpeg"), (".png", "image/png")):
        path = os.path.join(IMAGES, key + ext)
        if os.path.exists(path):
            with open(path, "rb") as f:
                data = base64.b64encode(f.read()).decode("ascii")
            out.append(f'<image x="{fmt(cx - r)}" y="{fmt(cy - r)}" width="{fmt(2 * r)}" height="{fmt(2 * r)}" '
                       f'preserveAspectRatio="xMidYMid slice" clip-path="url(#{clip})" '
                       f'href="data:{mime};base64,{data}"/>')
            break
    else:
        light, dark = PLACEHOLDER[key]
        out.append(f'<radialGradient id="grad-{key}" cx="0.4" cy="0.35" r="0.7"><stop offset="0" stop-color="{light}"/>'
                   f'<stop offset="1" stop-color="{dark}"/></radialGradient>'
                   f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(r)}" fill="url(#grad-{key})"/>')
    out.append(f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(r)}" fill="none" stroke="{NAVY}" stroke-width="0.5"/>')
    return "".join(out)


def board_art(lang, theme):
    """The whole board as SVG elements, in millimetres of the one-page board."""
    t, th = TEXT[lang], THEMES[theme]
    sx, sy = SUN
    sectors = belt_sectors()
    el = []
    BOXES.clear()

    # Board content. Sectors are turned by ROTATION; all texts stay horizontal.
    # Positions are chosen so that no label lands on a seam between printed
    # sheets (see check_seams): the vertical seam runs just right of the Sun,
    # the A2 horizontal one through it.
    a = math.radians(ROTATION)

    def at(dx, dy):
        return sx + dx, sy + dy

    def turned(x, y):
        return at(x * math.cos(a) - y * math.sin(a), x * math.sin(a) + y * math.cos(a))

    for q in range(-RADIUS, RADIUS + 1):
        for r in range(-RADIUS, RADIUS + 1):
            h = (q, r)
            k = ring(h)
            if k > RADIUS:
                continue
            x, y = turned(*centre(h))
            if k <= 3:
                fill, stroke = th["rings"][k]
            else:
                fill, stroke = th["belt"][sectors[h][2]], th["belt_stroke"]
            el.append(f'<polygon points="{hex_points(x, y, S)}" fill="{fill}" stroke="{stroke}" stroke-width="0.3"/>')
    for h, (number, label, _) in sectors.items():
        x, y = turned(*centre(h))
        el.append(text(x, y + 5.4, label, SMALL, ORANGE, ORBITRON))
        if label == BIG:
            el.append(text(x, y - 0.6, str(number), SECTOR, ORANGE, ORBITRON))
    # sector borders: edges between belt hexes of different sectors
    corners = {}
    for h in sectors:
        x, y = turned(*centre(h))
        for i in range(6):
            a6 = math.radians(60 * i - 30)
            p = (round(x + S * math.cos(a6), 3), round(y + S * math.sin(a6), 3))
            corners.setdefault(p, set()).add(sectors[h][0])
    for h in sectors:
        x, y = turned(*centre(h))
        pts = [(round(x + S * math.cos(math.radians(60 * i - 30)), 3),
                round(y + S * math.sin(math.radians(60 * i - 30)), 3)) for i in range(6)]
        for i in range(6):
            p, q = pts[i], pts[(i + 1) % 6]
            if p < q and len(corners[p] | corners[q]) > 1 and len(corners[p] & corners[q]) > 1:
                el.append(f'<line x1="{fmt(p[0])}" y1="{fmt(p[1])}" x2="{fmt(q[0])}" y2="{fmt(q[1])}" '
                          f'stroke="{ORANGE}" stroke-width="0.6" stroke-linecap="round"/>')
    el.append(f'<circle cx="{fmt(sx)}" cy="{fmt(sy)}" r="3.76" fill="{SUN_YELLOW}"/>')
    rt = th["ring_text"]
    # planet names above the Sun, orbital movement below it, one ring at a time
    el.append(text(*at(0, -17.7), t["venus"], MINOR, rt[1]))
    el.append(text(*at(0, -12.3), t["mercury"], MINOR, rt[1]))
    el.append(text(*at(0, -30), t["earth"], PLANET, rt[2]))
    el.append(text(*at(0, -45), t["mars"], PLANET, rt[3]))
    for n in (1, 2, 3):
        el.append(arrows(*at(0, 15 * n), 4 - n, rt[n]))
    el.append(text(*at(-33, -75), t["belt"], 10.0, th["belt_text"]))   # ring 5, left of the seam

    # top left: title, subtitle, QR code
    el.append(text(*at(-100, -88), t["title"], 13.0, NAVY))
    for i, line in enumerate(t["subtitle"]):
        el.append(text(*at(-100, -79.5 + 5.4 * i), line, 4.4, NAVY))
    size = 19
    qx, qy = at(-117, -52)
    el.append(qr_path(URL[lang], qx - size / 2, qy - size / 2, size, 0, NAVY))
    el.append(text(qx, qy + size / 2 + 4, t["version"], 2.8, NAVY, ORBITRON))
    el.append(text(qx, qy + size / 2 + 8.5, t["credits"], 2.8, NAVY, ORBITRON))

    # right: station spaces of the Earth (top) and Mars (bottom)
    r_st = 22
    for key, (dx, dy), lab_dy in (("earth", (128, -72), r_st + 5), ("mars", (128, 72), -(r_st + 5))):
        cx, cy = at(dx, dy)
        el.append(planet(key, cx, cy, r_st))
        el.append(text(cx, cy + lab_dy, t[key], PLANET, NAVY))

    # bottom left: Ceres, dice legend, version and credits
    cx, cy = at(-113, 40)
    el.append(planet("ceres", cx, cy, 15))
    el.append(text(cx, cy - 20, t["ceres"], 5.0, NAVY))
    lx, ly = at(-112, 82)
    el.append(f'<polygon points="{hex_points(lx, ly, 12)}" fill="{th["belt"][0]}" '
              f'stroke="{th["belt_stroke"]}" stroke-width="0.5"/>')
    el.append(text(lx, ly - 1, t["d12"], 7.5, ORANGE, ORBITRON))
    el.append(text(lx, ly + 6, t["d8"], 3.4, ORANGE, ORBITRON))
    ax, ay = lx + 9, ly - 9
    el.append(f'<path d="M{fmt(ax)},{fmt(ay)} l10,-8" fill="none" stroke="{ORANGE}" '
              f'stroke-width="1.2" stroke-linecap="round"/>')
    hx, hy = ax + 10, ay - 8
    el.append(f'<path d="M{fmt(hx - 3.2)},{fmt(hy + 0.9)} L{fmt(hx)},{fmt(hy)} L{fmt(hx + 0.6)},{fmt(hy + 3.3)}" '
              f'fill="none" stroke="{ORANGE}" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>')
    return "".join(el)


def svg_doc(w, h, body, extra_defs=""):
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{fmt(w)}mm" height="{fmt(h)}mm" '
            f'viewBox="0 0 {fmt(w)} {fmt(h)}"><defs>{extra_defs}</defs>{body}</svg>\n')


# --- print on several A4 sheets ----------------------------------------------
A4 = (210.0, 297.0)
MARGIN = 7.0      # left unprinted at every edge of the sheet, trimmed at the joins
FORMATS = {       # columns, rows, sheet orientation
    "a3": (2, 1, "portrait"),
    "a2": (2, 2, "landscape"),
}


def sheets(lang, theme, fmt_name):
    cols, rows, orient = FORMATS[fmt_name]
    sw, sh = A4 if orient == "portrait" else A4[::-1]
    cols, rows, cw, ch, scale, ox, oy = layout(fmt_name)      # cw, ch: printed area of a sheet
    art = board_art(lang, theme)
    t = TEXT[lang]
    trim = 'stroke="#808080" stroke-width="0.3" stroke-dasharray="2 1.5"'
    pages = []
    for r in range(rows):
        for c in range(cols):
            n = r * cols + 1 + c
            x0, y0 = c * cw, r * ch                                   # this sheet in the assembled board
            body = [f'<clipPath id="area"><rect x="{MARGIN}" y="{MARGIN}" width="{fmt(cw)}" height="{fmt(ch)}"/></clipPath>',
                    f'<g clip-path="url(#area)"><g transform="translate({fmt(MARGIN - x0 + ox)} {fmt(MARGIN - y0 + oy)}) '
                    f'scale({fmt(scale)})">{art}</g></g>']
            # trim lines on every side that joins another sheet
            if c > 0:
                body.append(f'<line x1="{MARGIN}" y1="0" x2="{MARGIN}" y2="{fmt(sh)}" {trim}/>')
            if c < cols - 1:
                body.append(f'<line x1="{fmt(MARGIN + cw)}" y1="0" x2="{fmt(MARGIN + cw)}" y2="{fmt(sh)}" {trim}/>')
            if r > 0:
                body.append(f'<line x1="0" y1="{MARGIN}" x2="{fmt(sw)}" y2="{MARGIN}" {trim}/>')
            if r < rows - 1:
                body.append(f'<line x1="0" y1="{fmt(MARGIN + ch)}" x2="{fmt(sw)}" y2="{fmt(MARGIN + ch)}" {trim}/>')
            # sheet number in the outer corner, which stays white
            right, bottom = c == cols - 1, r == rows - 1
            lx = MARGIN + cw - 2 if right else MARGIN + 2
            ly = MARGIN + ch - 2 if bottom else MARGIN + 3
            label = f'Hayabusa {fmt_name.upper()} · {t["sheet"]} {n}/{rows * cols}'
            body.append(text(lx, ly, label, 2.8, "#808080", anchor="end" if right else "start"))
            pages.append(svg_doc(sw, sh, "".join(body)))
    return pages, scale


def layout(fmt_name):
    """Scale and offset of the one-page board on the assembled sheets, chosen so that
    the joins fall on SEAM_X / SEAM_Y (largest scale that allows it)."""
    cols, rows, orient = FORMATS[fmt_name]
    sw, sh = A4 if orient == "portrait" else A4[::-1]
    cw, ch = sw - 2 * MARGIN, sh - 2 * MARGIN

    def fit(n, size, page, seam):
        # n sheets of `size` along one axis; the join (n == 2) must land on `seam`
        if n == 1:
            return size / page, None
        return min(size / seam, size / (page - seam)), seam

    sx, sy = SUN
    scale_x, jx = fit(cols, cw, PAGE_W, sx + SEAM_X)
    scale_y, jy = fit(rows, ch, PAGE_H, sy + SEAM_Y)
    scale = min(scale_x, scale_y)
    ox = cw - jx * scale if jx is not None else (cols * cw - PAGE_W * scale) / 2
    oy = ch - jy * scale if jy is not None else (rows * ch - PAGE_H * scale) / 2
    return cols, rows, cw, ch, scale, ox, oy


def check_seams(label):
    """Warn about texts crossed by a join between sheets (one-page board millimetres)."""
    for fmt_name in FORMATS:
        cols, rows, cw, ch, scale, ox, oy = layout(fmt_name)
        lines = [("x", (c * cw - ox) / scale) for c in range(1, cols)]
        lines += [("y", (r * ch - oy) / scale) for r in range(1, rows)]
        for x0, y0, x1, y1, s, size in BOXES:
            for axis, at in lines:
                a0, a1 = (x0, x1) if axis == "x" else (y0, y1)
                if a0 < at < a1:
                    print(f"  warning: {label} {fmt_name}: '{s}' ({size} mm) on a join")


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
            check_seams(base)
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
