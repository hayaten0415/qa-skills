#!/usr/bin/env python3
"""Validate QA skills: frontmatter integrity + MAPPING.md / README.md sync.

Dependency-free (Python 3 stdlib only). Run locally or in CI:

    python3 scripts/check_skills.py

Exits non-zero if any skill has malformed frontmatter, an out-of-enum
iso25010/mode value, an over-long description, or is missing from the
traceability docs. Keeps frontmatter <-> MAPPING.md in sync as skills grow.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ISO/IEC 25010:2023 nine characteristics (kebab-case) + the "all" shorthand
# allowed for cross-cutting skills (e.g. test-strategy-doc).
ALLOWED_ISO = {
    "functional-suitability", "performance-efficiency", "compatibility",
    "interaction-capability", "reliability", "security", "maintainability",
    "flexibility", "safety", "all",
}
ALLOWED_MODE = {"design", "implementation"}
DESC_MAX = 1536  # Claude Code truncates description (+when_to_use) at this length


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return m.group(1) if m else None


def get_scalar(fm, key):
    m = re.search(rf"^{key}:\s*(.*)$", fm, re.M)
    return m.group(1).strip() if m else None


def get_inline_list(fm, key):
    m = re.search(rf"^\s*{key}:\s*\[(.*?)\]", fm, re.M)
    if not m:
        return None
    return [x.strip() for x in m.group(1).split(",") if x.strip()]


def get_description(fm):
    m = re.search(r"^description:\s*(.*)\n((?:[ \t]+.*\n?)*)", fm, re.M)
    if not m:
        return None
    first = m.group(1).strip()
    body = m.group(2) if first in (">-", ">", "|", "|-", "") else first + "\n" + m.group(2)
    return re.sub(r"\s+", " ", body).strip()


def main():
    errors = []
    skill_paths = sorted(glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md")))
    if not skill_paths:
        print("No skills found under skills/*/SKILL.md")
        return 1

    names = []
    covered = set()
    for path in skill_paths:
        d = os.path.basename(os.path.dirname(path))
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        fm = frontmatter(text)
        if fm is None:
            errors.append(f"{d}: missing or malformed frontmatter block")
            continue

        name = get_scalar(fm, "name")
        if name != d:
            errors.append(f"{d}: name '{name}' does not match directory '{d}'")
        names.append(name or d)

        desc = get_description(fm)
        if not desc:
            errors.append(f"{d}: missing description")
        elif len(desc) > DESC_MAX:
            errors.append(f"{d}: description {len(desc)} chars exceeds {DESC_MAX}")

        iso = get_inline_list(fm, "iso25010")
        if not iso:
            errors.append(f"{d}: missing metadata.iso25010 inline list")
        else:
            bad = sorted(set(iso) - ALLOWED_ISO)
            if bad:
                errors.append(f"{d}: iso25010 has invalid value(s): {bad}")
            covered.update(iso)

        mode = get_inline_list(fm, "mode")
        if not mode:
            errors.append(f"{d}: missing metadata.mode inline list")
        else:
            bad = sorted(set(mode) - ALLOWED_MODE)
            if bad:
                errors.append(f"{d}: mode has invalid value(s): {bad}")

    # Traceability sync: every skill must be referenced in both docs.
    with open(os.path.join(ROOT, "MAPPING.md"), encoding="utf-8") as fh:
        mapping = fh.read()
    with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as fh:
        readme = fh.read()
    for n in names:
        if n not in mapping:
            errors.append(f"{n}: not referenced in MAPPING.md")
        if n not in readme:
            errors.append(f"{n}: not referenced in README.md")

    print(f"Checked {len(skill_paths)} skills.")
    missing = sorted((ALLOWED_ISO - {"all"}) - covered)
    if missing:
        print(f"Note: ISO 25010 characteristics with no dedicated skill: {missing}")

    if errors:
        print("\nFAIL:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("PASS: all frontmatter + MAPPING.md/README.md sync checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
