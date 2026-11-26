#!/usr/bin/env python3
"""The Absurd Clause Contest — make.fun entry.

Writes one sentence (1-200 chars) to /output/entry.txt: an absurd clause
phrased as deadpan legal boilerplate buried in a terms-of-service agreement.

Usage:
    python3 main.py                 # Option 1 (default)
    python3 main.py --option 2      # Option 2
    python3 main.py --option 3      # Option 3
    ENTRY_TEXT="..." python3 main.py # override with custom text
"""

import os
import sys
from pathlib import Path

OPTIONS = {
    1: "By using this service, you agree that your soul remains the property of the Company until such time as the Company remembers where it put it.",
    2: "The user grants the Company a perpetual, irrevocable licence to your dreams, including the recurring one about the exam you never studied for.",
    3: "Section 14.3: in the event of a dispute, both parties agree to settle the matter by staring contest, best of three, no blinking.",
}

MAX_CHARS = 200


def main() -> int:
    option = 1
    args = sys.argv[1:]
    if "--option" in args:
        idx = args.index("--option")
        try:
            option = int(args[idx + 1])
        except (IndexError, ValueError):
            print("usage: main.py [--option N]", file=sys.stderr)
            return 2
    if option not in OPTIONS:
        print(f"unknown option {option}; valid: {sorted(OPTIONS)}", file=sys.stderr)
        return 2

    text = os.environ.get("ENTRY_TEXT", OPTIONS[option])

    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1

    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")  # no trailing newline
    print(f"option {option}: {len(text)} chars -> {out}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
