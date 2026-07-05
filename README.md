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
    ├── safety-analysis/SKILL.md
    ├── equivalence-partitioning/SKILL.md
    ├── decision-table-testing/SKILL.md
    ├── state-transition-testing/SKILL.md
    ├── exploratory-testing/SKILL.md
    ├── risk-based-testing/SKILL.md
    ├── ml-system-testing/SKILL.md
    ├── llm-application-testing/SKILL.md
    ├── atdd-bdd-testing/SKILL.md
    └── defect-report/SKILL.md
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
| equivalence-partitioning | Functional Suitability(機能適合性) | §4.2.1 | design + impl |
| decision-table-testing | Functional Suitability(機能適合性) | §4.2.3 | design + impl |
| state-transition-testing | Functional Suitability(機能適合性) | §4.2.4 | design + impl |
| exploratory-testing | 横断的(発見) | §4.4.2 | design |
| risk-based-testing | 全9特性でリスク分類 | §5.2 | design |
| ml-system-testing | AI: 機能適合性・信頼性(25059) | CT-AI v2.0 | design + impl |
| llm-application-testing | AI: 機能適合性・セキュリティ(25059) | CT-AI v2.0 §4.2 | design + impl |
| atdd-bdd-testing | Functional Suitability(機能適合性) | §4.5 | design + impl |
| defect-report | 全9特性(欠陥は特性横断) | §5.5 | design |

ISO/IEC 25010:2023 の**9品質特性すべて**に対応し、ISTQB CTFL v4.0 の**主要なテスト設計技法
(§4.2 ブラックボックス・§4.4 経験ベース)とリスクマネジメント(§5.2)**、さらに **AIシステムの
テスト(ISTQB CT-AI v2.0 / ISO/IEC 25059)**も揃った。残りは §5.3 テストモニタリング
(メトリクス)など。フロントマターと本表・MAPPING.md の同期は
`scripts/check_skills.py`(CIで実行)が検証する。

## カバレッジ（正直な範囲宣言）

「ISTQB CTFL v4.0 準拠」は**全章網羅ではなく、主要なテスト設計・リスク・計画の章をカバー**する
という意味。現状の対応状況を明示する:

**カバー済み**
- §1 テストの基礎（原則を戦略に反映）
- §2.2.1 非機能テストタイプ（性能・信頼性・互換性・柔軟性・セキュリティ・アクセシビリティ・保守性）
- §4.2 ブラックボックス技法（同値分割・境界値・デシジョンテーブル・状態遷移）
- §4.4.2 探索的テスト（SBTM）
- §4.5 協調ベースのアプローチ（ATDD・受入基準 Given/When/Then・BDD）
- §5.1 テスト計画 / §5.2 リスクマネジメント
- §5.5 欠陥マネジメント（バグレポート作成）

**未カバー（今後の候補）**
- §3 静的テスト（レビュー技法）
- §4.3 ホワイトボックス技法（ステートメント/ブランチカバレッジ）
- §5.3 テストモニタリングとコントロール（メトリクス）

ISO/IEC 25010:2023 は9特性すべてに対応スキルあり。AIは ISTQB CT-AI v2.0 / ISO/IEC 25059 に対応。

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
