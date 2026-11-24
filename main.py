#!/usr/bin/env python3
"""One-Star Review of Something Essential -- make.fun program/v1 entry.

Writes exactly one deadpan one-star review, a single line of at most
160 characters, to /output/entry.txt.

The line: a deadpan complaint against gravity, the everyday essential
that never gets a support ticket. Drafts considered and rejected while
writing this file:

- The sun: "no dimmer, no off switch" is a true grievance, but the sun
  has been reviewed a thousand times and the complaint lands soft.
- Sleep: strong, but the best sleep lines turn into tech metaphors
  (install, crash, update) instead of staying about sleep itself.
- Mondays: funny, but a calendar complaint is about a schedule, not
  about a thing that cannot be fixed.

Gravity wins because the grievance is the sharpest true one everyone
recognises: it holds the whole planet together flawlessly, yet it is
also flawless at dropping a phone face-down. The turn arrives in the
last few words -- "No settings, no refund, no mercy." -- after the
complaint has been read straight, and nothing in the line winks.

Validation is part of the program, not an afterthought: the line is
checked for length (1-160 chars), single-line shape, and deadpan form
(no exclamation marks doing the work) before anything is written, and
the file is read back and compared byte for byte after writing.
"""

import os

ENTRY = (
    "One star. Gravity holds the whole planet together, yet somehow "
    "always drops my phone face-down. No settings, no refund, no mercy."
)

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")
MAX_CHARS = 160


def validate(line):
    """The gate's own rules, checked locally before writing."""
    assert isinstance(line, str) and 1 <= len(line) <= MAX_CHARS, (
        "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(line))
    )
    assert line == line.strip(), "entry must not start or end with whitespace"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    assert line.startswith("One star."), "entry must read as a one-star review"
    assert "!" not in line, "deadpan: no exclamation marks doing the work"


def main():
    validate(ENTRY)
    os.makedirs(OUT_DIR, exist_ok=True)
    try:
        os.chmod(OUT_DIR, 0o755)
    except OSError:
        pass
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    try:
        os.chmod(OUT_PATH, 0o644)
    except OSError:
        pass
    with open(OUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == ENTRY, "read-back mismatch: file does not hold the entry"
    print("Wrote %d characters to %s" % (len(ENTRY), OUT_PATH))


if __name__ == "__main__":
    main()
