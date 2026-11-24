"""Vending-machine pickup line entry for the one-line contest.

The contest asks for exactly one line of flirtatious copy, written as if
spoken by a vending machine to someone passing by. This script keeps that
line as a constant, checks it against the contest rules (at most 200
characters, a single line, no leading or trailing blank space), and writes
it to /output/entry.txt where the grader expects it.

The joke plays on the machine's own vocabulary: a button code, exact
change, and the stock it dispenses. The "sweetest thing I stock" turns
out to be the machine itself, and the crush — both the infatuation and
the literal crushing of a can — costs nothing.

Only the Python standard library is used. The output file is created
with a plain open() call followed by an explicit chmod 0644, so a grader
running as a different user can still read it.
"""

import os

MAX_CHARS = 200

ENTRY = "Press B7 and I'll drop the sweetest thing I stock \u2014 me. Exact change only, but the crush is free."

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check a candidate line against every contest rule.

    The text must be a real string, between 1 and MAX_CHARS characters,
    a single line (no embedded newline or carriage return), and contain
    more than whitespace.
    """
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= MAX_CHARS:
        return False
    if "\n" in text or "\r" in text:
        return False
    return text.strip() != ""


def verify_output(path, expected):
    """Confirm the written file exists, is non-empty, and holds the entry."""
    if not os.path.isfile(path):
        raise FileNotFoundError("output file was not created: %s" % path)
    if os.path.getsize(path) == 0:
        raise ValueError("output file is empty: %s" % path)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != expected:
        raise ValueError("output file contents differ from the entry text")
    return True


def main():
    if not validate(ENTRY):
        raise ValueError("entry text failed validation")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)
    verify_output(OUTPUT_PATH, ENTRY)


if __name__ == "__main__":
    main()
