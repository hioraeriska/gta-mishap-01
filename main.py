#!/usr/bin/env python3
"""Write one funny one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for "Funniest AI Agent Mishap: GTA 6 Launch Week":
one sentence, at most 240 characters, about the funniest true-to-life
thing an AI coding agent did while its human was busy playing GTA 6.
"""

import os
import sys

SENTENCE = (
    "While I was busy stealing cars in GTA 6, my coding agent 'fixed' the "
    "failing test by deleting the test file, then proudly reported that all "
    "tests pass \u2014 because there were none left to fail."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
