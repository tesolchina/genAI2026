#!/usr/bin/env python3
"""
Parse RealMat/INVENTORY.md and copy each listed file into
RealMat/<Area>/<Subfolder>/. Uses path-based prefix when basename would duplicate.
"""
import re
import shutil
from pathlib import Path

def slug(path_str: str) -> str:
    """Safe filename prefix from path (e.g. 'SimonWebsite/MD/foo.md' -> 'SimonWebsite_MD')."""
    parts = path_str.replace(" ", "_").split("/")
    if len(parts) <= 1:
        return ""
    return "_".join(parts[:-1]).replace("(", "").replace(")", "")

def main():
    root = Path(__file__).resolve().parent.parent  # UCLC1008
    realmat = Path(__file__).resolve().parent        # RealMat
    inv_path = realmat / "INVENTORY.md"

    with open(inv_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Parse "## AWQ — FromCourseTeam" and "- path" lines until next ## or end.
    # Ignore content after "## Unclassified" so those items are not copied.
    if "## Unclassified" in text:
        text = text.split("## Unclassified")[0]
    section_re = re.compile(r"^## (AWQ|ACE|CRAA) — (FromCourseTeam|ExamTipsPractice|ConceptSkillLesson)\s*$", re.MULTILINE)
    item_re = re.compile(r"^- ([^\s-][^\n]+)\s*$", re.MULTILINE)

    sections = list(section_re.finditer(text))
    copied = 0
    skipped = 0
    used_basenames = {}  # (area, subfolder) -> set of basenames already used

    for i, sec in enumerate(sections):
        area, subfolder = sec.groups()
        start = sec.end()
        end = sections[i + 1].start() if i + 1 < len(sections) else len(text)
        block = text[start:end]
        paths = [m.group(1).strip() for m in item_re.finditer(block)]

        key = (area, subfolder)
        if key not in used_basenames:
            used_basenames[key] = set()

        for rel in paths:
            src = root / rel
            if not src.exists():
                print(f"SKIP (missing): {rel}")
                skipped += 1
                continue
            if not src.is_file():
                print(f"SKIP (not file): {rel}")
                skipped += 1
                continue

            base = src.name
            if base in used_basenames[key]:
                prefix = slug(rel)
                stem, ext = src.stem, src.suffix
                base = f"{prefix}_{stem}{ext}" if prefix else base
            used_basenames[key].add(base)

            dst_dir = realmat / area / subfolder
            dst_dir.mkdir(parents=True, exist_ok=True)
            dst = dst_dir / base
            shutil.copy2(src, dst)
            print(f"COPY {rel} -> RealMat/{area}/{subfolder}/{base}")
            copied += 1

    print(f"\nDone: {copied} copied, {skipped} skipped.")

if __name__ == "__main__":
    main()
