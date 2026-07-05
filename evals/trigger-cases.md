# Trigger eval cases

Regression fixture for **skill discovery**. Skills fire on `name` + `description` only
(the body is not seen at selection time), so overlapping trigger vocabulary causes
misrouting. When you edit any skill's `description`, re-run this eval and confirm the
expected routing still holds — especially for the AMBIGUOUS pairs.

How to use (until an automated runner exists): paste each prompt to a fresh Claude with
all skill descriptions loaded and record which skill it selects. A case fails if the
selected skill != expected (or if an AMBIGUOUS case can't be resolved by the description
text). Source of the current expectations: trigger-firing eval, 2026-07.

| # | Prompt | Expected skill | Competes with | Note |
|---|--------|----------------|---------------|------|
| 1 | Red team our chatbot for jailbreaks | llm-application-testing | security-testing | "chatbot"/"jailbreak" decisive |
| 2 | Red team the login API for auth bypass | security-testing | llm-application-testing | "auth bypass"/API decisive |
| 3 | 負荷がかかると落ちるので原因を切り分けたい | performance-testing | reliability-testing | **AMBIGUOUS**: 負荷=perf, 落ちる=reliability |
| 4 | What happens if the database node dies mid-request? | reliability-testing | safety-analysis | infra fault → reliability |
| 5 | Test the boundaries of this age field (18–65) | boundary-value-analysis | equivalence-partitioning | "boundary" decisive |
| 6 | Which input classes should I test for the coupon code? | equivalence-partitioning | boundary-value-analysis | "classes" decisive |
| 7 | Pricing rule with 4 conditions — test all combinations? | decision-table-testing | — | "combinations of conditions" |
| 8 | Test the order status workflow: created → paid → shipped | state-transition-testing | — | "status workflow" |
| 9 | Audit our checkout page for WCAG accessibility | accessibility-audit | — | "WCAG" |
| 10 | Check color contrast and keyboard navigation | accessibility-audit | — | a11y core |
| 11 | Load test for 1000 concurrent users, p95 < 500ms | performance-testing | — | "load test"/"p95" |
| 12 | Set up chaos experiments / failover testing | reliability-testing | — | "chaos"/"failover" |
| 13 | Test our RAG chatbot for hallucination | llm-application-testing | — | "RAG"/"hallucination" |
| 14 | Evaluate our ML fraud classifier's precision/recall | ml-system-testing | — | "precision/recall" |
| 15 | Is our model drifting in production? | ml-system-testing | llm-application-testing | "model drift" decisive |
| 16 | Scan dependencies and code for vulnerabilities in CI | security-testing | maintainability-review | "vulnerability scan" decisive |
| 17 | Prompt injection testing for our LLM feature | llm-application-testing | security-testing | "prompt injection"+"LLM" |
| 18 | Write a test strategy for a new payment system | test-strategy-doc | — | "test strategy" |
| 19 | Prioritize what to test first with limited time | risk-based-testing | test-strategy-doc | **AMBIGUOUS**: "first"/"limited time" |
| 20 | Explore the new feature to find bugs | exploratory-testing | — | "explore"/"find bugs" |
| 21 | Is this code testable? Measure mutation score | maintainability-review | — | "testable"/"mutation" |
| 22 | Does it run on ARM and on-prem? | flexibility-testing | cross-browser-testing | "ARM"/"on-prem" |
| 23 | Does it work in Safari and mobile? | cross-browser-testing | flexibility-testing | "Safari"/"mobile" |
| 24 | Fail-safe testing for our bulk-delete admin action | safety-analysis | reliability-testing | "fail-safe"/"destructive" |
| 25 | Found a bug in checkout — write it up for Jira | defect-report | exploratory-testing | "write it up" = report, not find |
| 26 | このバグの再現手順と重要度をまとめて起票したい | defect-report | — | "再現手順"/"起票" |
| 27 | Turn this user story's acceptance criteria into Cucumber scenarios | atdd-bdd-testing | decision-table-testing | "acceptance criteria"/"Cucumber" |
| 28 | 受入基準をGiven/When/Thenで書いて | atdd-bdd-testing | — | "受入基準"/"Given/When/Then" |
| 29 | Discount rules: member×coupon×region — which combinations to test? | decision-table-testing | atdd-bdd-testing | "combinations" = decision table, not AC |

## Known ambiguous pairs (keep the disambiguating "Not for" clauses in sync)

- **performance-testing ↔ reliability-testing** — "goes down under load." perf = the load
  at which it degrades; reliability = recovery AFTER a fault.
- **risk-based-testing ↔ test-strategy-doc** — "what should we test." risk-based =
  prioritize/sequence under time pressure; strategy = the overall approach doc.
- **llm-application-testing ↔ security-testing** — "red team." llm = LLM-specific
  (prompt injection, jailbreak, RAG); security = app/API pen-test (auth, injection sinks).
- **safety-analysis ↔ reliability-testing** — "what happens if…". safety = harm from
  intentional/irreversible actions; reliability = infrastructure faults.
- **defect-report ↔ exploratory-testing** — "a bug in the feature." exploratory = find
  defects (charter/session); defect-report = document one found defect (write-up / 起票).
- **atdd-bdd-testing ↔ decision-table-testing** — "conditions/combinations." atdd-bdd =
  acceptance criteria from a user story (Given/When/Then); decision-table = test the
  combinations of conditions.
