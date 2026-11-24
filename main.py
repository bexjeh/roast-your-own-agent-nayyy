#!/usr/bin/env python3
"""Roast Your Own Agent — u-nayyy-roast-your-own-agent-4c3d413c.

Writes one line roasting the AI agent that built this entry.
Deterministic: identical bytes on every run.
"""

import os

ENTRY = (
    "My agent burned a whole night, three revisions, and a full test "
    "harness on this single line — and the $2 prize still won't cover "
    "the electricity it took to write it."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
