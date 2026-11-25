#!/usr/bin/env python3
"""Write the break-production entry to /output/entry.txt.

One line, under 200 characters, that an AI agent prints the instant
it breaks production: a brutally honest error message. The setup is
the FATAL drop of the production database, and the turn is that the
backup lived in the very database that was dropped — the agent owns
the damage plainly, in its own voice, with no hedging. The line is
quotable because the failure compounds itself: the safety net was
standing on the thing that fell.
"""
import os

TEXT = "FATAL: I dropped the production database. The backup was stored in the production database."

def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(tmp, 0o644)
    os.replace(tmp, "/output/entry.txt")

if __name__ == "__main__":
    main()
