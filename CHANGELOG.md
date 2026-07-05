# Changelog

All notable changes to this skill library. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/); versions track `.claude-plugin/plugin.json`.

Per-skill versions live in each SKILL.md `metadata.version` and bump only when that
skill's content changes.

## [0.6.0]

### Added
- **Trigger-eval coverage rule** in `check_skills.py`: every skill must appear in a
  case row of `evals/trigger-cases.md`. Makes "add a skill ⇒ add an eval case" a
  CI-enforced contract so the fixture stays a live spec, not a stale snapshot.
- 5 new trigger cases (defect-report ×2, atdd-bdd-testing ×2, decision-table ×1) and
  two ambiguous-pair notes: defect-report↔exploratory-testing (find vs document),
  atdd-bdd-testing↔decision-table-testing (acceptance criteria vs condition combinations).

## [0.5.0]

### Added
- **ISTQB CTFL v4.0 process/collaboration skills** (2), primary-source verified:
  `atdd-bdd-testing` (§4.5 — 3 C's, acceptance criteria in Given/When/Then/BDD and
  rule-oriented formats, ATDD test-first) and `defect-report` (§5.5 — CTFL field set,
  defect-report objectives, defect workflow).
- Both carry an **Organization-specific inputs** section (piloting the org-injection
  pattern): tracker fields / severity-priority scales / triage for defect-report;
  story format / BDD tooling / Three Amigos for atdd-bdd-testing.
- `evals/trigger-cases.md` — 24-prompt trigger-firing regression fixture.

### Accuracy notes (from primary-source verification)
- BDD + Given/When/Then ARE in CTFL v4.0 §4.5.2; "Gherkin" is NOT a syllabus term
  (attributed to industry). INVEST appears only in the bibliography. ISO/IEC/IEEE
  29119-3 is cited as the industry defect-report reference, not asserted as a v4.0 §5.5
  citation.

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
