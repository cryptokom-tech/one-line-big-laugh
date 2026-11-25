#!/usr/bin/env python3
"""One Line, Big Laugh.

Writes one self-contained funny line to /output/entry.txt.

The joke is built from two plain parts: a setup that sounds like an
ordinary complaint about a password manager, and a payoff that turns
the tool into a sulking roommate. Nothing is read from disk, the
network, or the environment, so the output is identical on every run.
"""

import os
import sys

# The single line this entry submits. One sentence, 100 characters.
PUNCHLINE = (
    "My password manager forgot my password, so now we just stare "
    "at each other in mutual disappointment."
)

TARGET = "/output/entry.txt"

# Characters that close a sentence. The line must carry exactly one.
CLOSERS = ".!?"


def sentence_ok(text):
    """Return True when *text* is one sentence of 1-200 characters."""
    if not 1 <= len(text) <= 200:
        return False
    if text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if sum(1 for ch in text if ch in CLOSERS) != 1:
        return False
    if not text.endswith(tuple(CLOSERS)):
        return False
    return True


def main():
    line = PUNCHLINE
    if not sentence_ok(line):
        print("invalid line: must be one sentence of 1-200 characters",
              file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
