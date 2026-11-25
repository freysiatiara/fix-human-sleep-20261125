"""Fix Human Sleep: Funniest Patch Note.

Writes one patch-note line announcing that human sleep is fixed
to /output/entry.txt.
"""

import os

ENTRY = "Fixed: humans now enter REM sleep without first spending 45 minutes composing arguments with people who aren't there."


def _validate_entry(text):
    """Check the entry against the competition gate.

    The gate requires UTF-8 text of 1 to 160 characters, not only
    whitespace, on a single line with no leading/trailing whitespace.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(text) <= 160:
        raise ValueError("entry must be 1-160 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")
    text.encode("utf-8")
    return text


def main():
    entry = _validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
