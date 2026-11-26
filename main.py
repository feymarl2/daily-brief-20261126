#!/usr/bin/env python3
"""Entry for make.fun bounty news-image-20261126.

Writes the shipped front-page image for Thursday 26 November 2026 to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png): a one-page
summary of the day's world news across six stories — Asia markets
under US tariffs and Nvidia jitters, China's Shenzhou-24 launch with
the first Pakistani astronaut, the Ukraine war's spillover to Libya,
a Houthi strike on a Saudi refinery, the FCC's SpaceX satellite
authorization, and Macy's postponed Thanksgiving parade. The image
is drawn by draw.py (Pillow) and shipped as entry.png.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(here, "entry.png"), os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
