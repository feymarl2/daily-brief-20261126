#!/usr/bin/env python3
"""Draw the 26 November 2026 front-page image (1024x1024 PNG).

Six verified stories of Thursday 26 November 2026:
Reuters markets (Asia rebound, US tariffs, Nvidia jitters; Houthi
refinery strike, Brent $94.81) and AP (Shenzhou-24 first Pakistani
astronaut; Libyan officers die after Ukrainian drone attack on a
Russian warship; FCC SpaceX 1M-satellite authorization; Macy's
Thanksgiving parade postponed).
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
OUT = "/home/hatch/workspace/makefun/news-image-20261126-work/repo/entry.png"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

img = Image.new("RGB", (W, H), (246, 242, 233))
d = ImageDraw.Draw(img)
INK = (28, 28, 32)
RED = (178, 34, 34)
NAVY = (24, 48, 92)
GREY = (90, 90, 96)
GREEN = (28, 130, 76)
AMBER = (214, 144, 20)


def font(path, size):
    return ImageFont.truetype(path, size)


def center_text(y, text, fnt, fill=INK):
    box = d.textbbox((0, 0), text, font=fnt)
    d.text(((W - (box[2] - box[0])) / 2, y), text, font=fnt, fill=fill)


# masthead
center_text(26, "THE DAILY BRIEF", font(SERIF, 74))
d.rectangle([40, 120, W - 40, 126], fill=INK)
center_text(134, "Thursday, 26 November 2026  ·  World News in One Page", font(BOLD, 29), RED)
d.rectangle([40, 180, W - 40, 183], fill=INK)
center_text(194, "TARIFFS BITE, CONFLICTS FLARE", font(BOLD, 43), NAVY)

panels = [
    ("MARKETS", "Asia rebounds amid\ntariff storm;\nNvidia jitters linger", "chart"),
    ("SHENZHOU-24", "Pakistan's first\nastronaut rides\nto Tiangong", "rocket"),
    ("UKRAINE WAR", "Libyan officers die\nafter drone strike\non Russian warship", "ship"),
    ("OIL", "Houthi strike on\nSaudi refinery;\nBrent near $95", "oil"),
    ("SPACE", "FCC clears SpaceX\nplan for 1M orbital\ndata centers", "sat"),
    ("THANKSGIVING", "Macy's 100th parade\npostponed\nto Saturday", "balloon"),
]

x0, y0 = 40, 258
pw, ph, gap = 462, 216, 16


def icon(kind, cx, cy):
    if kind == "chart":
        d.line([cx - 52, cy + 40, cx - 52, cy - 42], fill=INK, width=5)
        d.line([cx - 52, cy + 40, cx + 54, cy + 40], fill=INK, width=5)
        pts = [(cx - 44, cy + 22), (cx - 22, cy + 34), (cx - 2, cy + 4), (cx + 18, cy + 16), (cx + 42, cy - 30)]
        d.line(pts, fill=GREEN, width=7)
        d.polygon([(cx + 42, cy - 30), (cx + 24, cy - 28), (cx + 40, cy - 12)], fill=GREEN)
        d.line([(cx - 44, cy - 6), (cx + 30, cy - 34)], fill=RED, width=4)
    elif kind == "rocket":
        d.polygon([(cx, cy - 52), (cx + 18, cy - 16), (cx + 18, cy + 22), (cx - 18, cy + 22), (cx - 18, cy - 16)], fill=NAVY)
        d.ellipse([cx - 8, cy - 22, cx + 8, cy - 6], fill=(255, 255, 255))
        d.polygon([(cx - 18, cy + 22), (cx - 36, cy + 40), (cx - 18, cy + 40)], fill=RED)
        d.polygon([(cx + 18, cy + 22), (cx + 36, cy + 40), (cx + 18, cy + 40)], fill=RED)
        d.polygon([(cx - 9, cy + 26), (cx + 9, cy + 26), (cx, cy + 52)], fill=AMBER)
        d.ellipse([cx + 30, cy - 44, cx + 42, cy - 32], fill=AMBER)
    elif kind == "ship":
        d.polygon([(cx - 54, cy + 22), (cx + 54, cy + 22), (cx + 36, cy + 42), (cx - 36, cy + 42)], fill=NAVY)
        d.rectangle([cx - 26, cy + 2, cx + 6, cy + 22], fill=NAVY)
        d.rectangle([cx + 12, cy - 10, cx + 20, cy + 22], fill=NAVY)
        d.ellipse([cx + 26, cy - 34, cx + 42, cy - 20], fill=RED)
        d.line([cx + 34, cy - 27, cx + 52, cy - 38], fill=RED, width=4)
        d.line([cx + 34, cy - 27, cx + 52, cy - 16], fill=RED, width=4)
        d.arc([cx - 58, cy + 38, cx - 8, cy + 60], 0, 180, fill=RED, width=5)
    elif kind == "oil":
        d.rectangle([cx - 30, cy - 30, cx - 12, cy + 38], fill=NAVY)
        d.rectangle([cx + 12, cy - 14, cx + 30, cy + 38], fill=NAVY)
        d.polygon([(cx - 40, cy + 38), (cx + 40, cy + 38), (cx + 40, cy + 46), (cx - 40, cy + 46)], fill=INK)
        d.polygon([(cx, cy - 52), (cx + 16, cy - 26), (cx + 6, cy - 26), (cx + 12, cy - 10), (cx - 12, cy - 10), (cx - 6, cy - 26), (cx - 16, cy - 26)], fill=RED)
    elif kind == "sat":
        d.ellipse([cx - 38, cy - 38, cx + 38, cy + 38], outline=NAVY, width=6)
        d.line([cx - 38, cy, cx + 38, cy], fill=NAVY, width=4)
        d.arc([cx - 56, cy - 20, cx + 56, cy + 20], 200, 340, fill=RED, width=5)
        d.rectangle([cx + 30, cy - 44, cx + 52, cy - 30], fill=AMBER)
        d.line([cx + 34, cy - 32, cx + 18, cy - 18], fill=AMBER, width=4)
        d.ellipse([cx - 52, cy + 26, cx - 42, cy + 36], fill=RED)
    elif kind == "balloon":
        d.ellipse([cx - 26, cy - 50, cx + 26, cy - 2], fill=RED)
        d.polygon([(cx - 26, cy - 18), (cx + 26, cy - 18), (cx, cy + 16)], fill=RED)
        d.line([cx - 14, cy + 8, cx - 8, cy + 30], fill=INK, width=3)
        d.line([cx + 14, cy + 8, cx + 8, cy + 30], fill=INK, width=3)
        d.rectangle([cx - 10, cy + 30, cx + 10, cy + 44], fill=NAVY)
        d.arc([cx + 24, cy - 52, cx + 56, cy - 26], 300, 160, fill=GREY, width=5)
        d.line([cx + 44, cy - 24, cx + 40, cy - 10], fill=GREY, width=4)


for i, (title, caption, kind) in enumerate(panels):
    col, row = i % 2, i // 2
    x = x0 + col * (pw + gap)
    y = y0 + row * (ph + gap)
    d.rectangle([x, y, x + pw, y + ph], fill=(255, 255, 255), outline=INK, width=3)
    d.rectangle([x, y, x + pw, y + 52], fill=NAVY)
    tb = d.textbbox((0, 0), title, font=font(BOLD, 28))
    d.text((x + (pw - (tb[2] - tb[0])) / 2, y + 10), title, font=font(BOLD, 28), fill=(255, 255, 255))
    icon(kind, x + 92, y + 134)
    d.multiline_text((x + 168, y + 80), caption, font=font(SANS, 26), fill=INK, spacing=8)

center_text(960, "Six stories, one Thursday — 26 November 2026", font(BOLD, 26), GREY)
img.save(OUT, optimize=True)
import os
print("saved", OUT, os.path.getsize(OUT))
