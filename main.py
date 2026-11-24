"""Alien Field Notes: The Two-Day Earth — entry program.

Writes one line (<=200 chars) to /output/entry.txt: a tourist review of
Earth by an alien visitor — one clean joke, a verdict with a rating, and
the punch at the end. No traffic, gravity, money, or weather cliches.
Stdlib only, deterministic.
"""
import os

TEXT = (
    "Earth: the locals invented a thousand ways to say hello, then spent "
    "centuries arguing about which greeting is correct. Charming, loud, "
    "mildly damp. 4/5 stars \u2014 would visit again, briefly."
)


def check_gate(text):
    """Return True iff text passes the scorer's gate (RULES.txt):
    UTF-8, 1-200 chars (characters, not bytes), one line,
    not whitespace-only, no control characters."""
    if not 1 <= len(text) <= 200:
        return False
    if "\n" in text or "\r" in text:
        return False
    if not text.strip():
        return False
    if any(ord(c) < 32 for c in text):
        return False
    return True


def main():
    # Enforce the scorer's gate (RULES.txt). Fail loudly instead of
    # writing an invalid entry.
    if not check_gate(TEXT):
        raise SystemExit("entry text violates the 1-200 char single-line gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Write-verify: read the file back and refuse to exit cleanly if
    # the bytes on disk differ from the gated text.
    with open(out_path, "r", encoding="utf-8") as f:
        if f.read() != TEXT:
            raise SystemExit("entry.txt on disk does not match the gated text")


if __name__ == "__main__":
    main()
