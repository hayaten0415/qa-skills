# qa-skills

**ISTQB × ISO/IEC 25010:2023 準拠のQAスキル集** — ドキュメント生成とテスト実装の両方に対応した、Claude Code などの Agent Skills 標準ランタイム向けスキルライブラリ。

Standards-grounded QA skills for AI coding agents. Every skill is explicitly mapped to
**ISTQB CTFL v4.0** syllabus sections and **ISO/IEC 25010:2023** quality characteristics.
Supports both **document generation** (test strategies, QA plans) and **test implementation**
(Playwright, pytest, k6, etc.).

## 設計原則

1. **規格へのトレーサビリティ** — 全スキルのfrontmatterに `istqb`(シラバス章)と `iso25010`(品質特性)のメタデータを持たせ、[MAPPING.md](./MAPPING.md) に対応表を集約する。
   これらは**人間・監査・自作ツール向けのドキュメント規約**であり、ランタイムが解釈するフィールドではない(ランタイムが見るのは実質 `name` と `description` のみ)。
2. **Doc / Impl 両対応** — 各スキルは `mode` メタデータで `design`(成果物生成)と `implementation`(テストコード生成)のどちらに対応するかを宣言する。
3. **Anti-Patterns 必須** — 全スキルにLLMの典型的な失敗パターン(ハッピーパス偏重、幻覚、制約の見落とし)への対策セクションを置く。
4. **9品質特性の完全カバーを目指す** — ISO/IEC 25010:2023 の9特性すべてを対象とし、先行リポジトリで手薄な「互換性 Compatibility」「柔軟性 Flexibility(旧・移植性)」も一級市民として扱う。

> **規格の版について:** 本リポジトリは **ISO/IEC 25010:2023(9特性)** に準拠する。
> 2023年版では 2011年版の「使用性 Usability」が「**Interaction Capability**」に、
> 「移植性 Portability」が「**Flexibility**」(副特性に scalability を追加)に改称・再編され、
> 「**Safety**(安全性)」が9番目の特性として追加された。

## ディレクトリ構成

Claude Code のスキル探索仕様(`skills/<skill-name>/SKILL.md` の1階層)に合わせ、
各スキルは**カテゴリの中間フォルダを挟まず**フラットに配置する。カテゴリ情報は
frontmatter の `metadata`(`iso25010` / `istqb`)で表現し、MAPPING.md で束ねる。

```
qa-skills/
├── .claude-plugin/
│   └── plugin.json             # プラグインマニフェスト(配布・インストール用)
├── README.md
├── MAPPING.md                  # スキル × ISO 25010:2023 × ISTQB 対応表
├── docs/
│   └── TEMPLATE.md             # 新規スキル用テンプレート
└── skills/                     # 各スキルは1階層(ネスト不可)
    ├── boundary-value-analysis/SKILL.md
    ├── test-strategy-doc/SKILL.md
    ├── cross-browser-testing/SKILL.md
    ├── flexibility-testing/SKILL.md
    ├── performance-testing/SKILL.md
    ├── reliability-testing/SKILL.md
    ├── accessibility-audit/SKILL.md
    ├── security-testing/SKILL.md
    ├── maintainability-review/SKILL.md
    └── safety-analysis/SKILL.md
```

## スキルの構造

各スキルは以下の統一構造に従う(詳細は [docs/TEMPLATE.md](./docs/TEMPLATE.md)):

```yaml
---
name: skill-name
description: >-
  What it does + when to trigger (be specific and slightly pushy).
  Use when: "...", "...". Not for: ... — use other-skill instead.
license: MIT
metadata:
  istqb: "CTFL v4.0 §4.2.2"                 # 対応するISTQBシラバス章
  iso25010: [functional-suitability]         # 対応するISO 25010:2023品質特性(kebab-case)
  mode: [design, implementation]             # design=成果物生成 / implementation=テストコード
---
```

本文: `Objective → Context Discovery → Instructions → Output Format → Anti-Patterns → Related Skills → References`

> **Note:** `description` は listing 時に **1,536字で切り詰め**られる(`skillListingMaxDescChars`)。
> トリガ語(Use when の語句)は前方に置くこと。SKILL.md 本文は英語で記述する
> (エージェントのトリガリング精度とポータビリティのため)。人間向けドキュメント
> (README / MAPPING)は日本語。

## 収録スキル

| スキル | ISO 25010:2023 | ISTQB | mode |
|---|---|---|---|
| boundary-value-analysis | Functional Suitability(機能適合性) | §4.2.2 | design + impl |
| test-strategy-doc | 全9特性の優先度評価 | §5.1 | design |
| cross-browser-testing | Compatibility(互換性) | §2.2.1 | impl |
| flexibility-testing | Flexibility(柔軟性・旧移植性) | §2.2.1 | design + impl |
| performance-testing | Performance Efficiency(性能効率性) | §2.2.1 / CT-PT | design + impl |
| reliability-testing | Reliability(信頼性) | §2.2.1 | design + impl |
| accessibility-audit | Interaction Capability(相互作用能力) | §2.2.1 | design + impl |
| security-testing | Security(セキュリティ) | §2.2.1 | design + impl |
| maintainability-review | Maintainability(保守性) | §2.2.1 | design + impl |
| safety-analysis | Safety(安全性) | — | design + impl |

ISO/IEC 25010:2023 の**9品質特性すべてに対応するスキルが揃った**(機能適合性・互換性・柔軟性は
今後さらに技法を追加予定)。テスト設計技法(同値分割・デシジョンテーブル・状態遷移)と
プロセス系(リスクベースドテスト・メトリクス)は引き続き拡充する。

## Installation

このリポジトリは Claude Code プラグイン(`.claude-plugin/plugin.json`)として配布する。

```bash
# ローカルのプラグインディレクトリとして読み込む(開発・お試し)
claude --plugin-dir /path/to/qa-skills
```

チームへ配布する場合は、プラグインマーケットプレイスに登録し `/plugin install` で導入する。
単一スキルだけ使いたい場合は、該当スキルの `skills/<name>/` ディレクトリを
プロジェクトの `.claude/skills/<name>/` へコピーしてもよい(1階層で配置すること)。

## License

MIT
