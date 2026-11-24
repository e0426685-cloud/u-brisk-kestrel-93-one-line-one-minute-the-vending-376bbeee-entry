"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single original pickup line, spoken by a vending machine to a
passing human, to /output/entry.txt.

Entry (97 characters, limit 200):
    Press B7 and I'll drop the sweetest thing I stock — me.
    Exact change only, but the crush is free.

Standard library only. The output file is written with plain open() and
an explicit chmod 0644 so the grader (a different user) can read it.
"""

import os

ENTRY = "Press B7 and I'll drop the sweetest thing I stock \u2014 me. Exact change only, but the crush is free."

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Return True when text is a valid entry: 1-200 chars, not blank."""
    return isinstance(text, str) and 1 <= len(text) <= 200 and text.strip() != ""


def main():
    if not validate(ENTRY):
        raise ValueError("entry text failed validation")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
