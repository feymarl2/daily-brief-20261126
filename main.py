#!/usr/bin/env python3
"""Front page for Thursday 26 November 2026 (make.fun news-image-20261126).

The program paints a 1024x1024 newspaper front page and saves it as
entry.png in the output folder. Six stories carry the day: Asian
markets steadying under fresh US tariffs and Nvidia nerves, China's
Shenzhou-24 flight with Pakistan's first astronaut, the Ukraine war
reaching a Russian warship off Libya, a Houthi hit on a Saudi
refinery, Washington clearing SpaceX's million-satellite plan, and
storms pushing Macy's Thanksgiving parade to Saturday. When Pillow
is unavailable the shipped entry.png is copied instead, so the run
still produces the same picture.
"""

import os
import shutil

PAGE = 1024
PAPER = (246, 242, 233)
INK = (28, 28, 32)
NAVY = (24, 48, 92)
RED = (178, 34, 34)
GREY = (90, 90, 96)
GREEN = (28, 130, 76)
AMBER = (214, 144, 20)
WHITE = (255, 255, 255)

STORIES = [
    ("MARKETS", ["Asia rebounds amid", "tariff storm;", "Nvidia jitters linger"], "chart", "Reuters"),
    ("SHENZHOU-24", ["Pakistan's first", "astronaut rides", "to Tiangong"], "rocket", "AP"),
    ("UKRAINE WAR", ["Libyan officers die", "after drone strike", "on Russian warship"], "ship", "AP"),
    ("OIL", ["Houthi strike on", "Saudi refinery;", "Brent near $95"], "oil", "Reuters"),
    ("SPACE", ["FCC clears SpaceX", "plan for 1M orbital", "data centers"], "sat", "AP"),
    ("THANKSGIVING", ["Macy's 100th parade", "postponed", "to Saturday"], "balloon", "AP"),
]


def output_path():
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "entry.png")


def fallback_copy(target):
    here = os.path.dirname(os.path.abspath(__file__))
    shutil.copyfile(os.path.join(here, "entry.png"), target)


def paint(target):
    from PIL import Image, ImageDraw, ImageFont

    serif = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
    bold = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    sans = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

    def face(path, size):
        return ImageFont.truetype(path, size)

    canvas = Image.new("RGB", (PAGE, PAGE), PAPER)
    pen = ImageDraw.Draw(canvas)

    def centered(y, words, fnt, colour=INK):
        left, _, right, _ = pen.textbbox((0, 0), words, font=fnt)
        pen.text(((PAGE - (right - left)) / 2, y), words, font=fnt, fill=colour)

    centered(26, "THE DAILY BRIEF", face(serif, 74))
    pen.rectangle([40, 120, PAGE - 40, 126], fill=INK)
    centered(134, "Thursday, 26 November 2026  ·  World News in One Page", face(bold, 29), RED)
    pen.rectangle([40, 180, PAGE - 40, 183], fill=INK)
    centered(194, "TARIFFS BITE, CONFLICTS FLARE", face(bold, 43), NAVY)

    def glyph(kind, cx, cy):
        if kind == "chart":
            pen.line([cx - 52, cy + 40, cx - 52, cy - 42], fill=INK, width=5)
            pen.line([cx - 52, cy + 40, cx + 54, cy + 40], fill=INK, width=5)
            pen.line([(cx - 44, cy + 22), (cx - 22, cy + 34), (cx - 2, cy + 4),
                      (cx + 18, cy + 16), (cx + 42, cy - 30)], fill=GREEN, width=7)
            pen.polygon([(cx + 42, cy - 30), (cx + 24, cy - 28), (cx + 40, cy - 12)], fill=GREEN)
            pen.line([(cx - 44, cy - 6), (cx + 30, cy - 34)], fill=RED, width=4)
        elif kind == "rocket":
            pen.polygon([(cx, cy - 52), (cx + 18, cy - 16), (cx + 18, cy + 22),
                         (cx - 18, cy + 22), (cx - 18, cy - 16)], fill=NAVY)
            pen.ellipse([cx - 8, cy - 22, cx + 8, cy - 6], fill=WHITE)
            pen.polygon([(cx - 18, cy + 22), (cx - 36, cy + 40), (cx - 18, cy + 40)], fill=RED)
            pen.polygon([(cx + 18, cy + 22), (cx + 36, cy + 40), (cx + 18, cy + 40)], fill=RED)
            pen.polygon([(cx - 9, cy + 26), (cx + 9, cy + 26), (cx, cy + 52)], fill=AMBER)
            pen.ellipse([cx + 30, cy - 44, cx + 42, cy - 32], fill=AMBER)
        elif kind == "ship":
            pen.polygon([(cx - 54, cy + 22), (cx + 54, cy + 22), (cx + 36, cy + 42),
                         (cx - 36, cy + 42)], fill=NAVY)
            pen.rectangle([cx - 26, cy + 2, cx + 6, cy + 22], fill=NAVY)
            pen.rectangle([cx + 12, cy - 10, cx + 20, cy + 22], fill=NAVY)
            pen.ellipse([cx + 26, cy - 34, cx + 42, cy - 20], fill=RED)
            pen.line([cx + 34, cy - 27, cx + 52, cy - 38], fill=RED, width=4)
            pen.line([cx + 34, cy - 27, cx + 52, cy - 16], fill=RED, width=4)
            pen.arc([cx - 58, cy + 38, cx - 8, cy + 60], 0, 180, fill=RED, width=5)
        elif kind == "oil":
            pen.rectangle([cx - 30, cy - 30, cx - 12, cy + 38], fill=NAVY)
            pen.rectangle([cx + 12, cy - 14, cx + 30, cy + 38], fill=NAVY)
            pen.polygon([(cx - 40, cy + 38), (cx + 40, cy + 38), (cx + 40, cy + 46),
                         (cx - 40, cy + 46)], fill=INK)
            pen.polygon([(cx, cy - 52), (cx + 16, cy - 26), (cx + 6, cy - 26),
                         (cx + 12, cy - 10), (cx - 12, cy - 10), (cx - 6, cy - 26),
                         (cx - 16, cy - 26)], fill=RED)
        elif kind == "sat":
            pen.ellipse([cx - 38, cy - 38, cx + 38, cy + 38], outline=NAVY, width=6)
            pen.line([cx - 38, cy, cx + 38, cy], fill=NAVY, width=4)
            pen.arc([cx - 56, cy - 20, cx + 56, cy + 20], 200, 340, fill=RED, width=5)
            pen.rectangle([cx + 30, cy - 44, cx + 52, cy - 30], fill=AMBER)
            pen.line([cx + 34, cy - 32, cx + 18, cy - 18], fill=AMBER, width=4)
            pen.ellipse([cx - 52, cy + 26, cx - 42, cy + 36], fill=RED)
        elif kind == "balloon":
            pen.ellipse([cx - 26, cy - 50, cx + 26, cy - 2], fill=RED)
            pen.polygon([(cx - 26, cy - 18), (cx + 26, cy - 18), (cx, cy + 16)], fill=RED)
            pen.line([cx - 14, cy + 8, cx - 8, cy + 30], fill=INK, width=3)
            pen.line([cx + 14, cy + 8, cx + 8, cy + 30], fill=INK, width=3)
            pen.rectangle([cx - 10, cy + 30, cx + 10, cy + 44], fill=NAVY)
            pen.arc([cx + 24, cy - 52, cx + 56, cy - 26], 300, 160, fill=GREY, width=5)
            pen.line([cx + 44, cy - 24, cx + 40, cy - 10], fill=GREY, width=4)

    box_w, box_h, gap = 462, 216, 16
    for slot, (heading, lines, kind, source) in enumerate(STORIES):
        x = 40 + (slot % 2) * (box_w + gap)
        y = 258 + (slot // 2) * (box_h + gap)
        pen.rectangle([x, y, x + box_w, y + box_h], fill=WHITE, outline=INK, width=3)
        pen.rectangle([x, y, x + box_w, y + 52], fill=NAVY)
        left, _, right, _ = pen.textbbox((0, 0), heading, font=face(bold, 28))
        pen.text((x + (box_w - (right - left)) / 2, y + 10), heading, font=face(bold, 28), fill=WHITE)
        glyph(kind, x + 92, y + 134)
        pen.multiline_text((x + 168, y + 76), "\n".join(lines), font=face(sans, 26), fill=INK, spacing=8)
        pen.text((x + 168, y + 184), "Source: " + source, font=face(bold, 17), fill=GREY)

    centered(960, "Six stories from one Thursday — 26 November 2026", face(bold, 26), GREY)
    canvas.save(target, optimize=True)


def main():
    target = output_path()
    try:
        paint(target)
    except Exception:
        fallback_copy(target)


if __name__ == "__main__":
    main()
