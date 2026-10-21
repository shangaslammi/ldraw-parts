"""Package tracked LDraw files and fork provenance as a reproducible complete.zip."""

import json
import subprocess
import zipfile
from pathlib import Path
from typing import TypedDict


class SourceRecord(TypedDict):
    version: str
    upstream_version: str
    repository: str


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    dirty = subprocess.check_output(["git", "status", "--porcelain"], cwd=root, text=True)
    if dirty:
        raise SystemExit("Commit source changes before packaging a release")
    record: SourceRecord = json.loads((root / "brickwrangler-source.json").read_text())
    # Keep the entire official inventory, plus tracked unofficial library files.
    # Documentation and tools remain outside the standard complete.zip layout.
    names = set(
        subprocess.check_output(["git", "ls-tree", "-r", "--name-only", "upstream"], cwd=root, text=True).splitlines()
    )
    additions = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", "HEAD", "--", "parts", "p"], cwd=root, text=True
    ).splitlines()
    names.update(additions)
    names.add("brickwrangler-source.json")
    target = root / "dist" / "complete.zip"
    target.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in sorted(names):
            info = zipfile.ZipInfo("ldraw/" + name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, (root / name).read_bytes(), compresslevel=9)
    print(f"{record['version']}: {target} ({target.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
