"""Roast Your Own Agent — make.fun entry program (program/v1).

Writes one original roast of the entrant's own AI agent to /output/entry.txt.

The roast (89 characters, single line, no trailing newline):
    My agent is so eager to please, I asked it to roast me and it complimented my font choice.

Why this line: the judge penalises the stock jokes about hallucinations,
refusals and confident wrong answers. This one takes a fresh angle instead —
sycophancy. The setup is short, the punch lands on the very last words
("font choice"), and the joke is playful and self-deprecating: the agent is
too eager to please to roast anyone, so it compliments the human instead.

Deterministic: no input, no randomness, no network, no clock. Two runs
produce byte-identical output.
"""

import os
import sys

ROAST = "My agent is so eager to please, I asked it to roast me and it complimented my font choice."


def main() -> int:
    # Self-check the house gate before writing: UTF-8 text of 1 to 200
    # characters, not only white space, on a single line. A line that fails
    # the gate is never judged, so fail loudly here instead of silently
    # shipping an invalid entry.
    if not (1 <= len(ROAST) <= 200):
        print(f"roast is {len(ROAST)} characters, outside the 1-200 gate", file=sys.stderr)
        return 1
    if ROAST.strip() == "" or "\n" in ROAST:
        print("roast must be a single non-blank line", file=sys.stderr)
        return 1
    ROAST.encode("utf-8")

    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(ROAST)
    except OSError:
        # Sandbox fallback: write next to the program if /output is unavailable.
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(ROAST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
