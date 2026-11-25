#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note — make.fun entry (program/v1).

Writes a single line of patch notes announcing that human sleep has been
fixed to /output/entry.txt. The sealed scorer requires UTF-8 text of 1 to
160 characters, a single line, not only whitespace; the gate is validated
here before writing.

Entry text: blind-tournament winner (candidate B, 4/5 pair wins, tie with F
broken on the head-to-head BvF win) with one extra-mile edit — "seven hours
forty" became "seven hours and forty minutes" — so the 20 minutes + 7h40m =
8 hours arithmetic lands and the deprecation joke reads cleanly.
"""
import os

ENTRY = (
    "Sleep v2.0: humans now recharge in 20 minutes. The other seven hours "
    "and forty minutes have been deprecated and will be removed in v2.1."
)

MIN_CHARS = 1
MAX_CHARS = 160


def validate(text):
    """Gate validation, mirroring the sealed scorer."""
    encoded = text.encode("utf-8")  # raises if not valid UTF-8 text
    decoded = encoded.decode("utf-8")
    assert decoded == text
    assert "\n" not in text, "entry must be a single line"
    assert MIN_CHARS <= len(text) <= MAX_CHARS, (
        f"entry is {len(text)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    assert text.strip(), "entry must not be only whitespace"


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Post-write verification: what the scorer will read must be exactly
    # what was validated, so a partial or recoded write cannot slip through.
    with open(out_path, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry differs from the validated text"
    validate(written)
    print(f"Wrote {out_path} ({len(ENTRY)} chars, verified)")


if __name__ == "__main__":
    main()
