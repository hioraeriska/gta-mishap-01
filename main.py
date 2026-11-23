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


MAX_CHARS = 240


def main() -> int:
    # Guard the bounty rule: one sentence, at most 240 characters.
    sentence = SENTENCE.strip()
    if len(sentence) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(sentence)} chars, over the {MAX_CHARS}-char limit"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(sentence)
    return 0


if __name__ == "__main__":
    sys.exit(main())
