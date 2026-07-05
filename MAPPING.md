# 規格トレーサビリティマップ

全スキルと ISO/IEC 25010:2023 品質特性・ISTQB CTFL v4.0 シラバスの対応表。
監査・調達要件・QA教育での参照を想定。各スキルのfrontmatter `metadata` と同期させること。

> **準拠版:** ISO/IEC 25010:**2023**(9特性)。2011年版からの主な変更 —
> 「使用性 Usability」→「**Interaction Capability**」に改称、
> 「移植性 Portability」→「**Flexibility**」に改称・再編(副特性に *scalability* を追加)、
> 「**Safety**(安全性)」を9番目の特性として新設。

## ISO/IEC 25010:2023 品質特性 × スキル

| # | 品質特性 | 副特性(主なもの) | 対応スキル | 状態 |
|---|---|---|---|---|
| 1 | **機能適合性** Functional Suitability | 完全性・正確性・適切性 | boundary-value-analysis, test-strategy-doc | 🟡 初期 |
| 2 | **性能効率性** Performance Efficiency | 時間効率・資源効率・容量 | (予定: load-test-design, performance-baseline) | 🔴 未着手 |
| 3 | **互換性** Compatibility | 共存性・相互運用性 | cross-browser-testing | 🟡 初期 |
| 4 | **相互作用能力** Interaction Capability(旧 Usability) | 適切度認識性・習得性・操作性・ユーザーエラー防止・インクルーシビティ | (予定: wcag-audit, keyboard-navigation) | 🔴 未着手 |
| 5 | **信頼性** Reliability | 無欠陥性・可用性・障害許容性・回復性 | (予定: chaos-testing, recovery-testing) | 🔴 未着手 |
| 6 | **セキュリティ** Security | 機密性・完全性・否認防止・真正性・耐性 | (予定: api-security-testing) | 🔴 未着手 |
| 7 | **保守性** Maintainability | モジュール性・再利用性・解析性・修正性・試験性 | (予定: testability-review) | 🔴 未着手 |
| 8 | **柔軟性** Flexibility(旧 Portability) | 適応性・拡張性(scalability)・設置性・置換性 | flexibility-testing | 🟡 初期 |
| 9 | **安全性** Safety(2023年版で新設) | 運用制約・リスク特定・フェイルセーフ・危険警告・安全統合 | (予定) | 🔴 未着手 |

> 2011年版(8特性)で運用する必要がある場合は、Interaction Capability → Usability、
> Flexibility → Portability に読み替え、Safety を除外する。

## ISTQB CTFL v4.0 シラバス × スキル

| シラバス章 | 内容 | 対応スキル |
|---|---|---|
| §1 テストの基礎 | テストの7原則、QAとテスト | test-strategy-doc(原則を戦略に反映) |
| §2 SDLC全体を通してのテスト | テストレベル・テストタイプ | cross-browser-testing, flexibility-testing(§2.2.1 非機能テストタイプ) |
| §4.2.1 同値分割法 | | (予定: equivalence-partitioning) |
| §4.2.2 境界値分析 | | boundary-value-analysis |
| §4.2.3 デシジョンテーブルテスト | | (予定: decision-table-testing) |
| §4.2.4 状態遷移テスト | | (予定: state-transition-testing) |
| §4.4 経験ベースのテスト技法 | 探索的テスト等 | (予定: exploratory-testing) |
| §5.1 テスト計画 | テスト戦略、entry/exit criteria | test-strategy-doc |
| §5.2 リスク分析 | リスクベースドテスト | (予定: risk-based-testing) |
| §5.3 テストモニタリング | メトリクス | (予定: qa-metrics) |

## 関連規格

- **ISO/IEC/IEEE 29119** — テストプロセス・文書化標準。test-strategy-doc 等の成果物構造の根拠。
- **WCAG 2.2 / ISO/IEC 40500** — Interaction Capability(アクセシビリティ)スキルの判定基準。
