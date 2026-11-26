#!/usr/bin/env python3
"""make.fun entry: The Best Advice I Ever Got (best-advice-b).

The entry is one sentence of advice someone actually gave me,
written to /output/entry.txt. My dad told me that if I cannot
explain something to my grandmother, I do not understand it
yet — and twenty years later I still test every idea on her
first. It is lived rather than quoted: the advice is a test I
still run, and the grandmother is a real person with a real
standard, which is what makes the line earned instead of
decorative.
"""

from pathlib import Path

OUT_PATH = Path("/output/entry.txt")
CHAR_LIMIT = 200


def build_entry():
    """Return the advice sentence, my own wording throughout."""
    # One sentence, as the brief requires: the advice itself is
    # the first half, and the second half proves it was taken —
    # twenty years of testing ideas on her is the evidence that
    # the advice stuck, not just that it sounded good.
    return (
        "My dad told me that if I can't explain it to my "
        "grandmother, I don't understand it yet, and twenty years "
        "later I still test every idea on her first."
    )


def validate(line):
    """Raise SystemExit listing every gate problem, if there is one."""
    problems = []
    if not line.strip():
        problems.append("empty")
    if line != line.strip():
        problems.append("leading/trailing whitespace")
    if len(line) > CHAR_LIMIT:
        problems.append("too long: %d chars" % len(line))
    if "\n" in line:
        problems.append("not a single line")
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))


def main():
    line = build_entry()
    validate(line)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line, encoding="utf-8")
    saved = OUT_PATH.read_text(encoding="utf-8")
    print("Wrote %s (%d chars, %d chars of headroom)"
          % (OUT_PATH, len(saved), CHAR_LIMIT - len(saved)))
    print(saved)


if __name__ == "__main__":
    main()
