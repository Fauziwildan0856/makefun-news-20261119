#!/usr/bin/env python3
"""make.fun bounty: Sum up 19 November's world news in one image.
Writes the prepared front-page image to /output/entry.png.
Deterministic, no network: it copies the bundled entry.png byte-for-byte.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"

os.makedirs("/output", exist_ok=True)
shutil.copyfile(SRC, DST)
print(f"Wrote {DST} ({os.path.getsize(DST)} bytes)")
