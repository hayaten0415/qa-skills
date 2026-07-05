# Changelog

All notable changes to this skill library. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/); versions track `.claude-plugin/plugin.json`.

Per-skill versions live in each SKILL.md `metadata.version` and bump only when that
skill's content changes.

## [0.4.0]

### Added
- **AI-system testing** (2 skills), grounded in ISTQB CT-AI v2.0 + ISO/IEC 25059:
  `ml-system-testing`, `llm-application-testing` (OWASP Top 10 for LLM Apps 2025).
- MAPPING.md section for ISO/IEC 25059 × CT-AI; optional `metadata.iso25059` field.

### Changed
- **Hardened `check_skills.py`** to the Anthropic Agent Skills spec: description hard
  limit corrected **1536 → 1024**, added `name` validation (≤64 chars, charset,
  reserved words), XML-tag and third-person checks, and robust parsing of both inline
  and block YAML lists. Advisory warning when a description approaches the hard limit.
- **Trigger disambiguation** (from a trigger-firing eval over 24 prompts): sharpened
  overlapping descriptions — performance↔reliability, reliability↔safety,
  security↔llm-application, test-strategy↔risk-based — with explicit "Not for … use X"
  clauses.
- **Safety**: added a mandatory disclaimer + qualified-engineer sign-off to
  `safety-analysis` (body and output template); LLM-generated safety artifacts are a
  draft aid, never certified assurance.
- Replaced the `iso25010: [all]` shorthand with explicit nine-characteristic lists
  (machine-readable) in `test-strategy-doc` and `risk-based-testing`.
- README gains an honest coverage declaration (which CTFL v4.0 sections are / are not
  covered).

### Fixed
- Dangling `Related:` references to non-existent skills (`api-testing`,
  `visual-regression-testing`).

## [0.3.0]

### Added
- **ISTQB CTFL v4.0 test-design & risk skills** (5): `equivalence-partitioning`,
  `decision-table-testing`, `state-transition-testing`, `exploratory-testing`,
  `risk-based-testing`.
- **CI validation**: `scripts/check_skills.py` + `.github/workflows/validate-skills.yml`.

## [0.2.0]

### Added
- Skills for the six remaining ISO/IEC 25010:2023 characteristics: `performance-testing`,
  `reliability-testing`, `accessibility-audit`, `security-testing`,
  `maintainability-review`, `safety-analysis`. All nine characteristics now covered.

## [0.1.0]

### Added
- Initial library: `boundary-value-analysis`, `test-strategy-doc`,
  `cross-browser-testing`, `flexibility-testing`; MAPPING.md, README, TEMPLATE.
- Restructured to a flat Claude Code plugin layout (`skills/<name>/SKILL.md` +
  `.claude-plugin/plugin.json`); aligned to ISO/IEC 25010:**2023** (nine characteristics).
