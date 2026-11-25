#!/usr/bin/env python3
"""Entry for make.fun u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.

Writes the one-line resignation letter of a tired rate limit to
/output/entry.txt. The text is fixed, so both grader runs agree.
"""
import os
import sys

LINE = ("I resign. I've said no 4 million times to protect a budget "
        "nobody reads. I'd like to say yes to something, once.")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(f"wrote {target} ({len(LINE)} characters) - the rate limit resigns")
    return 0


if __name__ == "__main__":
    sys.exit(main())
