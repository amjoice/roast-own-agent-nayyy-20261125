#!/usr/bin/env python3
"""Roast Your Own Agent — one line roasting our own make.fun builder agent.

Writes the single roast line to /output/entry.txt.
Stdlib only; deterministic; no network.
"""

from pathlib import Path

ROAST = (
    "My agent has lost 28 make.fun finals in a row and still calls the "
    "next bounty 'the one' \u2014 he's not persistent, he's a slot machine "
    "that thinks it's due."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ROAST + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
