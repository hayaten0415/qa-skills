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
| 2 | **性能効率性** Performance Efficiency | 時間効率・資源効率・容量 | performance-testing | 🟢 収録 |
| 3 | **互換性** Compatibility | 共存性・相互運用性 | cross-browser-testing | 🟡 初期 |
| 4 | **相互作用能力** Interaction Capability(旧 Usability) | 適切度認識性・習得性・操作性・ユーザーエラー防止・ユーザーエンゲージメント・インクルーシビティ・ユーザー支援・自己記述性 | accessibility-audit | 🟢 収録 |
| 5 | **信頼性** Reliability | 無欠陥性(旧 成熟性)・可用性・障害許容性・回復性 | reliability-testing | 🟢 収録 |
| 6 | **セキュリティ** Security | 機密性・完全性・否認防止・責任追跡性・真正性・耐性(2023新設) | security-testing | 🟢 収録 |
| 7 | **保守性** Maintainability | モジュール性・再利用性・解析性・修正性・試験性 | maintainability-review | 🟢 収録 |
| 8 | **柔軟性** Flexibility(旧 Portability) | 適応性・拡張性(scalability)・設置性・置換性 | flexibility-testing | 🟡 初期 |
| 9 | **安全性** Safety(2023年版で新設) | 運用制約・リスク特定・フェイルセーフ・危険警告・安全統合 | safety-analysis | 🟢 収録 |

> 2011年版(8特性)で運用する必要がある場合は、Interaction Capability → Usability、
> Flexibility → Portability に読み替え、Safety を除外する。

## ISTQB CTFL v4.0 シラバス × スキル

| シラバス章 | 内容 | 対応スキル |
|---|---|---|
| §1 テストの基礎 | テストの7原則、QAとテスト | test-strategy-doc(原則を戦略に反映) |
| §2 SDLC全体を通してのテスト | テストレベル・テストタイプ | cross-browser-testing, flexibility-testing, performance-testing, reliability-testing, security-testing, accessibility-audit, maintainability-review(§2.2.1 非機能テストタイプ) |
| CT-PT 性能テスト | 負荷/ストレス/スパイク/耐久/スケーラビリティ | performance-testing |
| §3 静的テスト | レビュープロセス(ISO/IEC 20246)、レビュータイプ、役割 | static-review |
| §4.2.1 同値分割法 | ブラックボックス技法 | equivalence-partitioning |
| §4.2.2 境界値分析 | ブラックボックス技法 | boundary-value-analysis |
| §4.2.3 デシジョンテーブルテスト | ブラックボックス技法 | decision-table-testing |
| §4.2.4 状態遷移テスト | ブラックボックス技法 | state-transition-testing |
| §4.3 ホワイトボックス技法 | ステートメント/ブランチカバレッジ | white-box-coverage |
| §4.4.2 探索的テスト | 経験ベース技法(SBTM) | exploratory-testing |
| §4.5 協調ベースのアプローチ | ATDD、受入基準(Given/When/Then・BDD/ルール型)、3C's | atdd-bdd-testing |
| §5.1 テスト計画 | テスト戦略、entry/exit criteria | test-strategy-doc |
| §5.2 リスクマネジメント | リスクベースドテスト、プロダクトリスク分析 | risk-based-testing |
| §5.3 テストのモニタリング・コントロール・完了 | メトリクス(7カテゴリ)、進捗/完了レポート | qa-metrics |
| §5.5 欠陥マネジメント | バグレポート作成、欠陥ライフサイクル | defect-report |
| CT-AI v2.0 | AIベースシステムのテスト(入力データ/モデル/開発、メタモルフィック、ドリフト、敵対的、GenAI §4.2) | ml-system-testing, llm-application-testing |

## AI/MLシステム × ISO/IEC 25059 × ISTQB CT-AI v2.0

ISO/IEC 25059:2023 は ISO/IEC 25010 を AI 向けに拡張した品質モデル。CT-AI v2.0 第2章が
この特性を参照する。各行の「拡張元」は 25010 の親特性。

| ISO/IEC 25059 の特性(2023) | 拡張元(25010) | 対応スキル |
|---|---|---|
| AI functional correctness(AI機能正確性) | 機能適合性 | ml-system-testing, llm-application-testing |
| Functional adaptability(機能適応性) | 機能適合性 | ml-system-testing |
| AI robustness(AIロバスト性) | 信頼性 | ml-system-testing, llm-application-testing |
| User controllability(ユーザー制御性) | 相互作用能力 | (予定) |
| Transparency(透明性) | 相互作用能力/満足性 | llm-application-testing |
| Intervenability(介入可能性) | セキュリティ | (予定) |
| Societal & ethical risk mitigation(社会的・倫理的リスク低減) | 利用時のリスク回避性 | (予定: fairness/bias 深掘り) |

> ⚠️ 注記: ROC/AUC・ペアワイズ(組合せ)テスト・automation bias は CT-AI **v2.0** の本文には
> 含まれない(v2.0で整理・削除)。metric は confusion matrix 由来の accuracy/precision/recall/F1。

## 関連規格

- **ISO/IEC/IEEE 29119** — テストプロセス・文書化標準。test-strategy-doc 等の成果物構造の根拠。29119-3 は qa-metrics のレポート様式(進捗/完了)の根拠。
- **ISO/IEC 20246** — ワークプロダクトレビューの規格。static-review のレビュープロセスの根拠。
- **WCAG 2.2**(W3C勧告 2024-12-12)— accessibility-audit の判定基準(Interaction Capability)。
- **OWASP Top 10 / ASVS / WSTG** — security-testing の判定基準(Security)。
- **Principles of Chaos Engineering** — reliability-testing のフォールトインジェクションの根拠(Reliability)。
- **ISTQB CT-PT(Certified Tester — Performance Testing)** — performance-testing のテストタイプ体系。
- **ISO/IEC 25023:2016** — 製品品質の測定(保守性・性能効率性などの定量指標)。
- **機能安全規格**(IEC 61508 / ISO 26262 / IEC 62304 / DO-178C)— 規制ドメインでの safety-analysis の上位規格。
- **ISTQB CT-AI v2.0** / **ISO/IEC 25059:2023** — ml-system-testing・llm-application-testing の基準。
- **OWASP Top 10 for LLM Applications(2025)** — llm-application-testing のセキュリティ/レッドチーム基準。
- **ISTQB CT-GenAI** — "GenAIを使ってテストする"側の参考(製品としてのLLM検証の基準ではない)。
