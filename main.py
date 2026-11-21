#!/usr/bin/env python3
"""Entrypoint for the the-poster-for-a-place-that-i-2-20261121-0539 entry.

ONDRINE — The Wave That Never Breaks: a travel poster for a place that
does not exist. One impossible landmark, a colossal wave frozen mid-crash
with its lip curled over the promenade; golden-hour light against a
blue-teal sea; people strolling and taking coffee beneath it; the name
set big into the sky.

The picture is produced by the companion renderer (render_poster.py) and
stored in this repository as entry.png. This script does no drawing of
its own — it only copies that committed file into the output directory —
so every grader run delivers the exact same bytes.
"""
import os
import shutil


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    if os.path.getsize(source) != os.path.getsize(target):
        raise SystemExit("entry.png copy incomplete: source and output sizes differ")


if __name__ == "__main__":
    main()
