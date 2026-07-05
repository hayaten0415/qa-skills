#!/usr/bin/env python3
"""Validate QA skills: frontmatter integrity + MAPPING.md / README.md sync.

Dependency-free (Python 3 stdlib only). Run locally or in CI:

    python3 scripts/check_skills.py

Enforces the Anthropic Agent Skills spec (name <= 64 chars, description <= 1024
chars, third-person, no XML tags) plus this repo's conventions (iso25010/mode
enums, MAPPING.md/README.md sync). Errors fail the build; WARN lines are advisory
(e.g. over-long descriptions that still fit the hard limit).

Spec: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ISO/IEC 25010:2023 — the nine product-quality characteristics (kebab-case).
# Cross-cutting skills must enumerate the characteristics they touch explicitly
# (no "all" shorthand — the value is machine-readable coverage data).
ALLOWED_ISO = {
    "functional-suitability", "performance-efficiency", "compatibility",
    "interaction-capability", "reliability", "security", "maintainability",
    "flexibility", "safety",
}
ALLOWED_MODE = {"design", "implementation"}

# Anthropic Agent Skills frontmatter spec limits.
NAME_MAX = 64
DESC_MAX = 1024
RESERVED_NAME_WORDS = ("anthropic", "claude")
NAME_RE = re.compile(r"^[a-z0-9-]+$")
XML_TAG_RE = re.compile(r"<[A-Za-z/!][^>]*>")
FIRST_SECOND_PERSON_RE = re.compile(r"\b(I can|I will|I'll|you can|you will|you'll|we can|we will)\b", re.I)
DESC_SOFT_MAX = 900  # advisory: warn when approaching the 1024 hard limit


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return m.group(1) if m else None


def get_scalar(fm, key):
    m = re.search(rf"^{re.escape(key)}:\s*(.*)$", fm, re.M)
    return m.group(1).strip() if m else None


def get_list(fm, key):
    """Parse a YAML value that is a list, accepting BOTH inline and block styles.

    inline:  key: [a, b]
    block:   key:
               - a
               - b
    """
    inline = re.search(rf"^[ \t]*{re.escape(key)}:\s*\[(.*?)\]\s*$", fm, re.M)
    if inline:
        return [x.strip() for x in inline.group(1).split(",") if x.strip()]
    block = re.search(rf"^[ \t]*{re.escape(key)}:\s*$\n((?:[ \t]+-\s*.*\n?)+)", fm, re.M)
    if block:
        return [i.strip() for i in re.findall(r"^[ \t]+-\s*(.+?)\s*$", block.group(1), re.M) if i.strip()]
    return None


def get_description(fm):
    m = re.search(r"^description:\s*(.*)\n((?:[ \t]+.*\n?)*)", fm, re.M)
    if not m:
        return None
    first = m.group(1).strip()
    body = m.group(2) if first in (">-", ">", "|", "|-", "") else first + "\n" + m.group(2)
    return re.sub(r"\s+", " ", body).strip()


def main():
    errors, warnings = [], []
    skill_paths = sorted(glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md")))
    if not skill_paths:
        print("No skills found under skills/*/SKILL.md")
        return 1

    names, covered = [], set()
    for path in skill_paths:
        d = os.path.basename(os.path.dirname(path))
        with open(path, encoding="utf-8") as fh:
            fm = frontmatter(fh.read())
        if fm is None:
            errors.append(f"{d}: missing or malformed frontmatter block")
            continue

        name = get_scalar(fm, "name")
        names.append(name or d)
        if name != d:
            errors.append(f"{d}: name '{name}' does not match directory '{d}'")
        if name:
            if len(name) > NAME_MAX:
                errors.append(f"{d}: name {len(name)} chars exceeds {NAME_MAX}")
            if not NAME_RE.match(name):
                errors.append(f"{d}: name must be lowercase letters/numbers/hyphens only")
            if any(w in name.lower() for w in RESERVED_NAME_WORDS):
                errors.append(f"{d}: name contains a reserved word {RESERVED_NAME_WORDS}")

        desc = get_description(fm)
        if not desc:
            errors.append(f"{d}: missing/empty description")
        else:
            if len(desc) > DESC_MAX:
                errors.append(f"{d}: description {len(desc)} chars exceeds hard limit {DESC_MAX}")
            elif len(desc) > DESC_SOFT_MAX:
                warnings.append(f"{d}: description {len(desc)} chars — approaching {DESC_MAX} hard limit; tighten or split")
            if XML_TAG_RE.search(desc):
                errors.append(f"{d}: description must not contain XML tags")
            if FIRST_SECOND_PERSON_RE.search(desc):
                warnings.append(f"{d}: description should be third person (found first/second-person phrasing)")

        iso = get_list(fm, "iso25010")
        if not iso:
            errors.append(f"{d}: missing metadata.iso25010 list")
        else:
            bad = sorted(set(iso) - ALLOWED_ISO)
            if bad:
                errors.append(f"{d}: iso25010 has invalid value(s): {bad}")
            covered.update(iso)

        mode = get_list(fm, "mode")
        if not mode:
            errors.append(f"{d}: missing metadata.mode list")
        else:
            bad = sorted(set(mode) - ALLOWED_MODE)
            if bad:
                errors.append(f"{d}: mode has invalid value(s): {bad}")

    with open(os.path.join(ROOT, "MAPPING.md"), encoding="utf-8") as fh:
        mapping = fh.read()
    with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as fh:
        readme = fh.read()
    for n in names:
        if n not in mapping:
            errors.append(f"{n}: not referenced in MAPPING.md")
        if n not in readme:
            errors.append(f"{n}: not referenced in README.md")

    # Trigger-eval coverage: every skill must appear in at least one case row (Expected
    # or "Competes with" column) of the fixture — makes "add skill => add eval case" a
    # CI-enforced contract, so the fixture stays a live spec, not a stale snapshot.
    evals_path = os.path.join(ROOT, "evals", "trigger-cases.md")
    if os.path.exists(evals_path):
        with open(evals_path, encoding="utf-8") as fh:
            case_rows = "".join(line for line in fh if line.lstrip().startswith("|"))
        for n in names:
            if n not in case_rows:
                errors.append(f"{n}: no trigger-eval case in evals/trigger-cases.md")
    else:
        warnings.append("evals/trigger-cases.md not found — trigger-eval coverage unchecked")

    print(f"Checked {len(skill_paths)} skills.")
    missing = sorted(ALLOWED_ISO - covered)
    if missing:
        print(f"Note: ISO 25010 characteristics with no dedicated skill: {missing}")
    for w in warnings:
        print(f"  WARN: {w}")

    if errors:
        print("\nFAIL:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("PASS: all frontmatter + MAPPING.md/README.md sync checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
