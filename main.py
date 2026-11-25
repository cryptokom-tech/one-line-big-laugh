#!/usr/bin/env python3
"""One Line, Big Laugh — entry program.

Writes a single funny line (1-200 chars) to /output/entry.txt.
Standard library only. Deterministic: same line on every run.
"""

import os
import sys

LINE = "My password manager forgot my password, so now we just stare at each other in mutual disappointment."


def valid(line: str) -> bool:
    """One non-empty line, 1-200 chars, no newline, a single sentence."""
    if not line or len(line) > 200 or "\n" in line or "\r" in line:
        return False
    if line != line.strip():
        return False
    if line.count(".") != 1 or "?" in line or "!" in line:
        return False
    return line.endswith(".")


def main() -> int:
    line = LINE.strip()
    if not valid(line):
        print("invalid entry line", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
