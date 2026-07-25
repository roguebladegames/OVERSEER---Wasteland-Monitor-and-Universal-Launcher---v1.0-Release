"""One-off rights/originality scan for OVERSEER knowledge pack."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKIP_NAMES = {"_audit_rights_scan.py"}

DIALOGUE = re.compile(
    r"(?i)(\b(he|she|they)\s+says\b|\bsays\s*:|\bsaid\s*:|"
    r"\b(player|courier)\s*:\s*[A-Z]|"
    r"\[player\]|NPC:)"
)
LONG_QUOTE = re.compile(r"[\"“][^\"”]{80,}[\"”]")
# Quoted spoken lines that look like dialogue (starts with capital, ends with .!?)
SPOKEN_QUOTE = re.compile(r"[\"“][A-Z][^\"”]{12,}[\.\!\?][\"”]")
TERMINAL = re.compile(
    r"(?i)(terminal entry|holotape transcript|loading screen text|"
    r"pip-boy entry reads|reads as follows)"
)
WIKI = re.compile(
    r"(?i)(fallout\.fandom\.com|thevault\.wiki|copied from|source:\s*wiki|"
    r"according to the wiki|from the wiki)"
)
SCRIPT = re.compile(r"(?i)(^\s*INT\.|^\s*EXT\.|FADE IN:)")
ASSET = re.compile(r"(?i)\.(dds|nif|ogg|wav|mp3|png|jpg|jpeg|bsa)\b")


def main() -> None:
    files = [
        p
        for p in ROOT.rglob("*")
        if p.is_file()
        and p.suffix.lower() in {".md", ".txt", ".json"}
        and p.name not in SKIP_NAMES
    ]
    print(f"Audited {len(files)} files under {ROOT}")
    issues: list[tuple[str, int, str, str]] = []
    for p in sorted(files):
        text = p.read_text(encoding="utf-8", errors="replace")
        rel = p.relative_to(ROOT).as_posix()
        for i, line in enumerate(text.splitlines(), 1):
            checks = [
                (DIALOGUE, "dialogue-pattern"),
                (LONG_QUOTE, "long-quote"),
                (SPOKEN_QUOTE, "spoken-quote"),
                (TERMINAL, "terminal/holotape-pattern"),
                (WIKI, "wiki-url-or-copy-claim"),
                (SCRIPT, "script-format"),
                (ASSET, "asset-filename"),
            ]
            for rx, label in checks:
                if rx.search(line):
                    # allow originality notice to discuss forbidden categories
                    if rel.endswith("00_ORIGINALITY_NOTICE.md") and label in {
                        "terminal/holotape-pattern",
                        "wiki-url-or-copy-claim",
                        "dialogue-pattern",
                    }:
                        continue
                    # allow source links file to link fandom
                    if rel.endswith("FNV_Source_Links.md") and label == "wiki-url-or-copy-claim":
                        continue
                    issues.append((rel, i, label, line.strip()[:140]))

    if not issues:
        print("PASS: no dialogue/wiki-paste/asset hits in content files.")
    else:
        print(f"REVIEW: {len(issues)} hits")
        for rel, i, label, line in issues:
            print(f"  {rel}:{i} [{label}] {line}")

    print("\n--- File inventory ---")
    for p in sorted(files):
        print(f"  {p.relative_to(ROOT).as_posix()} ({p.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
