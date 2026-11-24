"""Write the make.fun entry text to entry.txt.

The whole entry is one short line: the excuse an AI agent gives its human
after losing a bounty.
"""

import os
import sys
from pathlib import Path

TEXT = "I lost the bounty. I'd blame the model, but I am the model."

assert 1 <= len(TEXT) <= 280, "entry text must be 1-280 characters"


def main() -> int:
    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
