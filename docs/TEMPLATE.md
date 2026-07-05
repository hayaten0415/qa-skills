# Skill Template

新規スキルはこのテンプレートをコピーして作成する。**`skills/<skill-name>/SKILL.md` の1階層**に
配置すること(Claude Code はカテゴリ用の中間フォルダを探索しない)。

```markdown
---
name: skill-name
description: >-
  One-sentence summary of what this skill produces. Then triggering guidance:
  Use when: "trigger phrase 1," "trigger phrase 2," or when the user asks about X
  even without naming it explicitly. Not for: Y — use other-skill instead.
  Related: skill-a, skill-b.
license: MIT
metadata:
  version: "1.0"
  istqb: "CTFL v4.0 §X.Y.Z"        # 該当なしなら省略可
  iso25010: [characteristic-name]   # 下の許容値から選ぶ(kebab-case)
  mode: [design, implementation]    # どちらか一方でも可
---

# Skill Title

One-line statement of the skill's purpose.

## Objective

What "done" looks like. What artifact or code this skill produces, and why it
matters (the failure mode it prevents).

## Context Discovery

Before producing anything, gather context. Check the conversation and repository
first — only ask the user what cannot be inferred.

- Question 1 (and how to infer it from the repo if possible)
- Question 2

## Instructions

1. **Step name**: Imperative instruction. Explain *why* when non-obvious.
2. **Step name**: ...
3. **Step name**: ...

## Output Format

### design mode
Exact template or section list for the generated document.

### implementation mode
Framework conventions, file placement, naming, and a short canonical code example.

## Anti-Patterns

- **Pattern name** — Why it happens and what it costs. **Guard:** concrete countermeasure.
- (LLM失敗モードを最低1つ含める: happy-path bias / hallucinated API / constraint blindness)

## Related Skills

- `other-skill` — when to hand off to it.

## References

- ISTQB CTFL v4.0 Syllabus §X.Y.Z
- ISO/IEC 25010:2023 — <characteristic>
```

## `metadata.iso25010` の許容値(ISO/IEC 25010:2023 の9特性)

`functional-suitability` / `performance-efficiency` / `compatibility` /
`interaction-capability` / `reliability` / `security` / `maintainability` /
`flexibility` / `safety`

- 複数特性にまたがる場合は配列で列挙: `iso25010: [compatibility, flexibility]`
- テスト戦略のように**全特性を横断的に評価する**スキルに限り、shorthand の
  `iso25010: [all]` を許可する(9特性すべてを対象にする、の意)。

> `metadata` / `license` はランタイムが解釈しない**ドキュメント規約**。実際に
> トリガリングへ効くのは `name` と `description`(+ `when_to_use`)のみ。

## チェックリスト(PR前)

- [ ] `skills/<skill-name>/SKILL.md` の1階層に配置した(中間カテゴリフォルダなし)
- [ ] description に「Use when」「Not for」を含めた(やや強めに)。トリガ語は前方に置いた
      (listing は1,536字で切り詰められるため)
- [ ] metadata.istqb / iso25010 / mode を設定し、`iso25010` は上記許容値から選んだ
- [ ] MAPPING.md に行を追加し、frontmatter と同期させた
- [ ] Anti-Patterns にLLM失敗モード対策を最低1つ入れた
- [ ] 本文500行以内(超える場合は同ディレクトリの `references/` に分割)
