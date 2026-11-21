#!/usr/bin/env python3
"""VELMARA poster entrypoint.

Copies the entry poster (entry.png, shipped in this repository) to the
grader's output path /output/entry.png. Standard library only, no network,
deterministic: the same input bytes always produce the same output bytes.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
DEST = "/output/entry.png"


def main():
    # The poster is data, not code: copy it byte for byte so the grader
    # sees exactly the image this repository holds.
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    with open(SOURCE, "rb") as src:
        digest = hashlib.sha256(src.read()).hexdigest()
    shutil.copyfile(SOURCE, DEST)
    with open(DEST, "rb") as out:
        check = hashlib.sha256(out.read()).hexdigest()
    if check != digest:
        print("copy mismatch", file=sys.stderr)
        return 1
    print("entry.png ->", DEST, check)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
