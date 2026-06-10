#!/usr/bin/env python3
"""Generate Claude Doggy Dogg mascot design explorations.

Each design is a pixel grid drawn in the style of the Claude mascot:
chunky pixels, coral orange on cream. Outputs SVG + PNG per design,
plus a contact sheet of all ten.
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Claude brand-ish palette
PALETTE = {
    ".": None,         # background
    "O": "#D97757",    # coral orange (body)
    "K": "#1A1A18",    # near-black (eyes, outlines)
    "W": "#FFFFFF",    # white
    "B": "#4A6FA5",    # bandana blue
    "b": "#3A5A8C",    # bandana blue dark (paisley dots)
    "G": "#E8B931",    # gold (chain)
    "P": "#C95D3F",    # darker coral (shading / inner ear)
    "T": "#E2906E",    # lighter coral (snout patch)
    "R": "#D14B3A",    # red (tongue)
    "L": "#8C8C84",    # grey (headphones)
    "D": "#6B4F3A",    # brown (blunt-free! used for vinyl/beanie trim)
    "N": "#2E5E4E",    # beanie green
    "Y": "#F0EEE6",    # cream accent (teeth etc on dark)
}

BG = "#F0EEE6"

DESIGNS = []


def design(name, title, rows):
    DESIGNS.append((name, title, [r.replace(" ", "") for r in rows]))


# ---------------------------------------------------------------- 01 classic
# Straight dog-ification of the original: floppy ears, snout, tail.
design("01-og-doggy", "OG Doggy", [
    "................",
    ".PP..........PP.",
    ".PPOOOOOOOOOOPP.",
    ".PPOOOOOOOOOOPP.",
    ".PPOKKOOOOKKOPP.",
    ".PPOKKOOOOKKOPP.",
    "..OOOOOOOOOOOO..",
    "..OOOOTTTTOOOO..",
    "..OOOOTKKTOOOO..",
    "..OOOOTTTTOOOO..",
    "..OOOOOOOOOOOO.O",
    "..OOOOOOOOOOOOOO",
    "..OOOOOOOOOOOO..",
    "..OO..OO..OO....",
    "..OO..OO..OO....",
    "................",
])

# ------------------------------------------------------------- 02 westcoast
# Blue paisley bandana tied over the head.
design("02-westside", "Westside Bandana", [
    "................",
    "..BBBBBBBBBBBB..",
    ".BBbBBBBbBBBBBB.",
    ".BBBBBbBBBBbBBB.",
    "..BBBBBBBBBBBB..",
    "..OOKKOOOOKKOO..",
    "..OOKKOOOOKKOO..",
    "OOOOOOOOOOOOOOOO",
    "OOOOOOTTTTOOOOOO",
    "OOOOOOTKKTOOOOOO",
    "..OOOOTTTTOOOOOO",
    "..OOOOOOOOOOOOOO",
    "..OOOOOOOOOOOOOO",
    "..OO..OO..OO.OO.",
    "..OO..OO..OO.OO.",
    "................",
])

# --------------------------------------------------------------- 03 shades
# Wraparound black shades, unbothered.
design("03-laidback", "Laid Back Shades", [
    "................",
    "..OO........OO..",
    "..OO........OO..",
    "..OOOOOOOOOOOO..",
    "..OOOOOOOOOOOO..",
    ".KKKKKKKKKKKKKK.",
    "..KKKKKOOKKKKK..",
    "..OOOOOOOOOOOO..",
    "OOOOOOTTTTOOOOOO",
    "OOOOOOTKKTOOOOOO",
    "..OOOOTTTTOOOOOO",
    "..OOOOOOOOOOOOOO",
    "..OOOOOOOOOOOOOO",
    "..OO..OO..OO.OO.",
    "..OO..OO..OO.OO.",
    "................",
])

# ---------------------------------------------------------------- 04 chain
# Heavy gold chain with a paw medallion.
design("04-gold-chain", "Gold Chain", [
    "................",
    "..OO........OO..",
    "..OO........OO..",
    "..OOOOOOOOOOOO..",
    "..OOKKOOOOKKOO..",
    "..OOKKOOOOKKOO..",
    "..OOOOTTTTOOOO..",
    "..OOOOTKKTOOOO..",
    "..GOOOTTTTOOOG..",
    "..OGOOOOOOOOGO..",
    "..OOGGOOOOGGOO..",
    "..OOOOGGGGOOOO..",
    "..OOOOOGGOOOOO..",
    "..OOOOOOOOOOOO..",
    "..OO..OO..OO....",
    "..OO..OO..OO....",
])

# --------------------------------------------------------------- 05 beanie
# Green beanie pulled low, ears poking out the sides.
design("05-beanie", "Beanie Pup", [
    "................",
    "....NNNNNNNN....",
    "..NNNNNNNNNNNN..",
    "..DDDDDDDDDDDD..",
    "OOOOOOOOOOOOOOOO",
    "OOOOKKOOOOKKOOOO",
    "OOOOKKOOOOKKOOOO",
    "..OOOOOOOOOOOO..",
    "..OOOOTTTTOOOO..",
    "..OOOOTKKTOOOO..",
    "..OOOOTTTTOOOO..",
    "..OOOOOOOOOOOO..",
    "..OOOOOOOOOOOO..",
    "..OO..OO..OO....",
    "..OO..OO..OO....",
    "................",
])

# --------------------------------------------------------------- 06 braids
# Snoop's braids hanging down both sides.
design("06-braids", "Braids", [
    "................",
    "..OOOOOOOOOOOO..",
    ".KOOOOOOOOOOOOK.",
    ".KOOKKOOOOKKOOK.",
    ".KOOKKOOOOKKOOK.",
    ".K.OOOOOOOOOO.K.",
    ".K.OOOTTTTOOO.K.",
    ".K.OOOTKKTOOO.K.",
    ".K.OOOTTTTOOO.K.",
    ".K.OOOOOOOOOO.K.",
    "...OOOOOOOOOO...",
    "...OOOOOOOOOO...",
    "...OOOOOOOOOO...",
    "...OO..OO..OO...",
    "...OO..OO..OO...",
    "................",
])

# ---------------------------------------------------------- 07 tongue out
# Happy dog energy, tongue hanging out.
design("07-tongue-out", "Tongue Out", [
    "................",
    "..OO........OO..",
    "..OO........OO..",
    "..OOOOOOOOOOOO..",
    "..OOKKOOOOKKOO..",
    "..OOKKOOOOKKOO..",
    "..OOOOTTTTOOOO..",
    "..OOOOTKKTOOOO..",
    "..OOOKKKKKKOOO..",
    "..OOOKKKKKKOOO..",
    "..OOOOORRKOOOO..",
    "..OOOOORROOOOO..",
    "..OOOOORROOOOO..",
    "..OOOOOOOOOOOO..",
    "..OO..OO..OO....",
    "..OO..OO..OO....",
])

# ------------------------------------------------------------ 08 headphones
# Big studio headphones, head nodding to the beat.
design("08-headphones", "Studio Session", [
    "....LLLLLLLL....",
    "...LL......LL...",
    "..LLOOOOOOOOLL..",
    ".LLLOOOOOOOOLLL.",
    ".LLLKKOOOOKKLLL.",
    ".LLLKKOOOOKKLLL.",
    ".LLLOOOOOOOOLLL.",
    "..LLOOTTTTOOLL..",
    "....OOTKKTOO....",
    "....OOTTTTOO....",
    "....OOOOOOOO....",
    "....OOOOOOOO....",
    "....OOOOOOOO....",
    "....OO....OO....",
    "....OO....OO....",
    "................",
])

# ---------------------------------------------------------- 09 side profile
# Full dog in profile — body, legs, tail up, walkin'.
design("09-low-rider", "Low Rider", [
    "................",
    ".OO.............",
    "..OO.......PP...",
    "..OO.......PP...",
    "...OOOOOOOOOOOO.",
    "...OOOOOOOOOKKO.",
    "...OOOOOOOOOOOOT",
    "...OOOOOOOOOOOOT",
    "...OOOOOOOOOOOO.",
    "...OOOOOOOOOOO..",
    "...OOOOOOOOOOO..",
    "...OO..OO..OO...",
    "...OO..OO..OO...",
    "................",
    "................",
    "................",
])

# -------------------------------------------------------------- 10 d-o-double-g
# Crown flipped: classic mascot wearing a tilted "D O double G" cap + wink.
design("10-tha-doggfather", "Tha Doggfather", [
    "................",
    "..KKKKKKKK......",
    "..KKKKKKKKKKKK..",
    "..KKGGKKKKKKKK..",
    "..OOOOOOOOOOOO..",
    "..OOKKOOOOKKOO..",
    "..OOOOOOOOKKOO..",
    "OOOOOOOOOOOOOOOO",
    "OOOOOOTTTTOOOOOO",
    "OOOOOOTKKTOOOOOO",
    "..OOOOTTTTOOOOOO",
    "..OOOOGGOOOOOOOO",
    "..OOOGGGGOOOOOOO",
    "..OO..OO..OO.OO.",
    "..OO..OO..OO.OO.",
    "................",
])


CELL = 40
PAD = 2  # cells of padding around each grid

# The chosen mascot: shades + gold chain (explorations 03 + 04 combined).
# Rendered separately as the canonical logo, not part of the contact sheet.
MASCOT = [r.replace(" ", "") for r in [
    "................",
    "..OO........OO..",
    "..OO........OO..",
    "..OOOOOOOOOOOO..",
    ".KKKKKKKKKKKKKK.",
    "..KKKKKOOKKKKK..",
    "..OOOOTTTTOOOO..",
    "..OOOOTKKTOOOO..",
    "..GOOOTTTTOOOG..",
    "..OGOOOOOOOOGO..",
    "..OOGGOOOOGGOO..",
    "..OOOOGGGGOOOO..",
    "..OOOOOGGOOOOO..",
    "..OOOOOOOOOOOO..",
    "..OO..OO..OO....",
    "..OO..OO..OO....",
]]


def grid_size(rows):
    return max(len(r) for r in rows), len(rows)


def render_svg(name, rows, path):
    w, h = grid_size(rows)
    W, H = (w + 2 * PAD) * CELL, (h + 2 * PAD) * CELL
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
        f'<rect width="{W}" height="{H}" fill="{BG}"/>',
    ]
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            color = PALETTE.get(ch)
            if color:
                px, py = (x + PAD) * CELL, (y + PAD) * CELL
                parts.append(f'<rect x="{px}" y="{py}" width="{CELL}" height="{CELL}" fill="{color}"/>')
    parts.append("</svg>")
    with open(path, "w") as f:
        f.write("\n".join(parts))


def render_png(rows, scale=CELL):
    w, h = grid_size(rows)
    W, H = (w + 2 * PAD) * scale, (h + 2 * PAD) * scale
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            color = PALETTE.get(ch)
            if color:
                px, py = (x + PAD) * scale, (y + PAD) * scale
                d.rectangle([px, py, px + scale - 1, py + scale - 1], fill=color)
    return img


def load_font(size):
    for p in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def contact_sheet(path, cols=5):
    tile = 480  # square tile per design
    label_h = 64
    rows_n = (len(DESIGNS) + cols - 1) // cols
    W = cols * tile
    H = rows_n * (tile + label_h)
    sheet = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(sheet)
    font = load_font(30)
    for i, (name, title, rows) in enumerate(DESIGNS):
        img = render_png(rows).resize((tile, tile), Image.NEAREST)
        cx, cy = (i % cols) * tile, (i // cols) * (tile + label_h)
        sheet.paste(img, (cx, cy))
        num = f"{i + 1:02d}"
        text = f"{num} · {title}"
        tw = d.textlength(text, font=font)
        d.text((cx + (tile - tw) / 2, cy + tile + 12), text, fill="#1A1A18", font=font)
    sheet.save(path)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "out")
    os.makedirs(out, exist_ok=True)

    # Canonical mascot lives at the repo root (it's the README hero).
    render_svg("mascot", MASCOT, os.path.join(here, "mascot.svg"))
    render_png(MASCOT).save(os.path.join(here, "mascot.png"))
    print("mascot: mascot.svg / mascot.png")

    # Explorations + contact sheet are scratch -- written to out/ (gitignored).
    for name, title, rows in DESIGNS:
        render_svg(name, rows, os.path.join(out, f"{name}.svg"))
        render_png(rows).save(os.path.join(out, f"{name}.png"))
        print(f"  out/{name} — {title}")
    contact_sheet(os.path.join(out, "all-designs.png"))
    print("contact sheet: out/all-designs.png")


if __name__ == "__main__":
    main()
