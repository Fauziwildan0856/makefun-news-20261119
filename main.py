"""Entry program for the make.fun news-image-20261119 bounty.

The picture itself sits next to this file (entry.png, or image.png
when a phone upload kept that name). Running the program places a
byte-for-byte copy of that picture at the output
location the judges read, /output/entry.png. Nothing is downloaded
and nothing is random: every run produces exactly the same bytes.

Usage:
    python3 main.py [destination]

The optional destination argument only exists so the copy step can be
tested without touching /output; the judges run it with no arguments.
"""

import hashlib
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_TARGET = Path("/output/entry.png")


def find_source() -> Path:
    """Locate the picture this program ships.

    The picture normally sits next to this file as entry.png. A phone
    upload renamed one copy to image.png, so accept that name too —
    whichever of the two is present is the entry picture.
    """
    for name in ("entry.png", "image.png"):
        candidate = HERE / name
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(f"entry image missing in {HERE}")


SOURCE = find_source()


def place_entry(target: Path) -> Path:
    """Copy the entry picture to *target*, creating parent folders."""
    if not SOURCE.is_file():
        raise FileNotFoundError(f"entry image missing: {SOURCE}")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, target)
    return target


def digest(path: Path) -> str:
    """SHA-256 of a file, read in chunks so big files stay cheap."""
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main(argv: list[str]) -> int:
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    written = place_entry(target)
    if digest(written) != digest(SOURCE):
        raise RuntimeError("copy does not match entry.png")
    print(f"wrote {written} ({written.stat().st_size} bytes, sha256 verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
