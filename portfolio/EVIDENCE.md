# Seven-project portfolio: evidence guide

**Prasanna K · Quantitative modelling & reliable decision systems · Summer 2027**

This guide links directly to the published results, verification and reproduction evidence. The seven projects stay fixed; a reviewer can enter through the work closest to their role.

| Reviewing for | Start with |
|---|---|
| Quantitative risk, financial modelling or validation | 1. Credit risk · 5. Derivatives · 6. C++ engineering |
| Applied AI, data science or decision systems | 3. Financial AI · 2. Causal decisions · 7. Data engineering |
| Actuarial analytics or insurance risk | 4. Actuarial models · 1. Credit risk · 2. Causal decisions |

The current extensions below link to frozen source commits and successful remote checks. The earlier October 9 evidence remains linked separately for reproduction. Passing checks establish only their stated contract; they do not prove model quality or production readiness.

## October 10 update: extrapolation challenged

The October 9 snapshot below remains reproducible. Project 5 now also has an [analytic extrapolation audit](https://github.com/Prasanna-K-123/volatility-surface-model-risk/blob/fd9c3ff268f8c03cf742b580981548ebab06f08f/docs/EXTRAPOLATION_AUDIT.md), [frozen result/protocol](https://github.com/Prasanna-K-123/volatility-surface-model-risk/blob/fd9c3ff268f8c03cf742b580981548ebab06f08f/reference/density_audit/summary.json) and [successful validation run](https://github.com/Prasanna-K-123/volatility-surface-model-risk/actions/runs/38013024452). Two of six smiles fail a far-outside-support density stress check; the new bounded-evaluation API rejects unsupported extrapolation. The original held-out-strike benchmark includes three boundary-extrapolation points out of 116. These are model-risk findings, not observed executable market arbitrage or a global no-arbitrage proof.

## October 10 substantive extensions

Four existing flagships received new empirical or correctness evidence. The seven project identities remain unchanged.

### 1. Credit Risk & Lending Decisions

A new 30,000-record Taiwan cohort uses identical 18,007-client training budgets, duplicate-input isolation, separate calibration/policy partitions and a 6,001-client holdout. AUCs are 0.7814 and 0.7897; the paired input-group-bootstrap difference interval is [0.0006, 0.0161]. Brier and assumed decision-cost difference intervals include zero. Calibration worsens raw Brier scores in both models, and this finding is retained.

[Review memo](https://github.com/Prasanna-K-123/credit-risk-ifrs9-stress-testing/blob/f4bb37d2d51625f2fc76c38504072211850c7f83/docs/MATCHED_COHORT_REVIEW.md) · [Frozen result](https://github.com/Prasanna-K-123/credit-risk-ifrs9-stress-testing/blob/f4bb37d2d51625f2fc76c38504072211850c7f83/reference/card_clients/summary.json) · [Verification code](https://github.com/Prasanna-K-123/credit-risk-ifrs9-stress-testing/blob/f4bb37d2d51625f2fc76c38504072211850c7f83/benchmark_card_clients.py) · [Successful CI](https://github.com/Prasanna-K-123/credit-risk-ifrs9-stress-testing/actions/runs/38021071123)

**Limit:** One historical Taiwan cohort and earlier South German study; not out-of-time validation or regulatory PD/ECL. No observed LGD/EAD; decision costs illustrative.

### 3. Financial AI Evidence Systems

Qwen3-4B Q4_K_M actually generated all 128 preselected public-test outputs. The same outputs were replayed through a bounded expression/source-occurrence guard; all answers and refusals are retained. Both answer policies remain unreliable. A custom display diagnostic gives 15/122 direct and 22/122 guarded matches, with a paired improvement interval that includes zero; separate rounded execution diagnostics give 9/128 and 26/128. Scale/rounding limits prevent treating these as official FinQA accuracy or human-reviewed semantic correctness. CI replays frozen outputs and scoring; it does not rerun model generation.

[Review memo](https://github.com/Prasanna-K-123/enterprise-genai-rag-responsible-ai/blob/1a256dfe20a4ac13f29e9bf662459b31da42dd19/docs/ANSWER_AUDIT.md) · [Frozen result](https://github.com/Prasanna-K-123/enterprise-genai-rag-responsible-ai/blob/1a256dfe20a4ac13f29e9bf662459b31da42dd19/reference/answer_audit/summary.json) · [Verification code](https://github.com/Prasanna-K-123/enterprise-genai-rag-responsible-ai/blob/1a256dfe20a4ac13f29e9bf662459b31da42dd19/benchmark_answers.py) · [Successful CI](https://github.com/Prasanna-K-123/enterprise-genai-rag-responsible-ai/actions/runs/38021106315)

**Limit:** Calculator has a bounded company/year/metric/unit contract. General FinQA answers remain experimental and unreliable; citation occurrence does not prove semantic entailment.

### 6. C++20 Event-Driven Trading Engine

A versioned portable snapshot restores book state, FIFO order, chronology and counters. A separate 25,000-event, five-seed recovery study verifies 685 restores; 1,304 bit flips, 163 truncations and eight resealed invalid structures are rejected. An independent Python format/CRC decoder checks the C++ fixture. The full remote release, sanitizer, replay and performance-regression workflow passed. Historical timing remains tied to its original runner; no new latency figure is claimed.

[Review memo](https://github.com/Prasanna-K-123/cpp-event-driven-trading-engine/blob/bd1c9c08505a7382a772f65d993f1b3e40843316/docs/RECOVERY_REVIEW.md) · [Frozen result](https://github.com/Prasanna-K-123/cpp-event-driven-trading-engine/blob/bd1c9c08505a7382a772f65d993f1b3e40843316/reference/recovery/fixture.hex) · [Verification code](https://github.com/Prasanna-K-123/cpp-event-driven-trading-engine/blob/bd1c9c08505a7382a772f65d993f1b3e40843316/verify_snapshot_fixture.py) · [Successful CI](https://github.com/Prasanna-K-123/cpp-event-driven-trading-engine/actions/runs/38021343683)

**Limit:** Synthetic replay; historic platform-specific timing. Recovery is an in-memory image API, not a durable exchange journal, live feed or production service.

### 7. Data Engineering & Decision Optimisation

Jan–June flow means were frozen before processing the next July period. July contributes 3,898,963 raw / 3,676,278 cleaned trips and 6,003 zero-inclusive zone-days. The frozen mean has MAE 5.79 versus 12.40 for a zero-flow sanity comparator; paired week-block MAE-difference interval is [-7.75, -4.96], based on only five week blocks. Complete-panel replay and reconstruction from the pinned raw Parquet both passed remotely. The original PySpark pipeline also passed at this source commit. Stronger seasonal/rolling forecast comparisons remain unexecuted.

[Review memo](https://github.com/Prasanna-K-123/urban-mobility-pyspark-optimization/blob/87ff32d9a40fde4bdf948e89b04ec649ba6b758e/docs/FORWARD_PERIOD_REVIEW.md) · [Frozen result](https://github.com/Prasanna-K-123/urban-mobility-pyspark-optimization/blob/87ff32d9a40fde4bdf948e89b04ec649ba6b758e/reference/forward_panel/summary.json) · [Verification code](https://github.com/Prasanna-K-123/urban-mobility-pyspark-optimization/blob/87ff32d9a40fde4bdf948e89b04ec649ba6b758e/benchmark_forward.py) · [Successful CI](https://github.com/Prasanna-K-123/urban-mobility-pyspark-optimization/actions/runs/38021636353)

**Limit:** Trip flow is not idle supply, centroid distance is a proxy. One later month/zero comparator is not frontier forecasting or realized dispatch savings.

## Earlier frozen evidence

## 1. [Credit Risk & Lending Decisions](https://github.com/Prasanna-K-123/credit-risk-ifrs9-stress-testing)

AUC difference 0.023; paired 95% interval −0.014 to 0.061. The challenger is not established as superior. Frozen lending policy and prior-shift assumptions are auditable.

[Results](https://github.com/Prasanna-K-123/credit-risk-ifrs9-stress-testing/blob/9829cfa2cfb157a862725bfb761b3841d30bfc4f/outputs/decision_audit/summary.json) · [Verification](https://github.com/Prasanna-K-123/credit-risk-ifrs9-stress-testing/blob/9829cfa2cfb157a862725bfb761b3841d30bfc4f/audit_reference.py) · [Successful CI](https://github.com/Prasanna-K-123/credit-risk-ifrs9-stress-testing/actions/runs/37966462945) · [Reproduction workflow](https://github.com/Prasanna-K-123/credit-risk-ifrs9-stress-testing/blob/9829cfa2cfb157a862725bfb761b3841d30bfc4f/.github/workflows/ci.yml) · [Scope review](https://github.com/Prasanna-K-123/credit-risk-ifrs9-stress-testing/blob/9829cfa2cfb157a862725bfb761b3841d30bfc4f/docs/EVIDENCE_REVIEW.md)

**Limit:** Small historical oversampled dataset, no observation dates; IFRS 9/LGD/EAD assumptions are illustrative.

## 2. [Causal Decision Science](https://github.com/Prasanna-K-123/causal-marketing-experimentation-uplift)

Same-budget targeting gain 0.946 percentage points; conditional 95% interval 0.333–1.561 points. The negative spend-targeting finding remains visible.

[Results](https://github.com/Prasanna-K-123/causal-marketing-experimentation-uplift/blob/96e8b7c497c82dc6c2f6c458c20e7060c47f696e/results/same_budget_policy_audit.json) · [Verification](https://github.com/Prasanna-K-123/causal-marketing-experimentation-uplift/blob/96e8b7c497c82dc6c2f6c458c20e7060c47f696e/audit_policy.py) · [Successful CI](https://github.com/Prasanna-K-123/causal-marketing-experimentation-uplift/actions/runs/37966591692) · [Reproduction workflow](https://github.com/Prasanna-K-123/causal-marketing-experimentation-uplift/blob/96e8b7c497c82dc6c2f6c458c20e7060c47f696e/.github/workflows/reproduce-evidence.yml) · [Scope review](https://github.com/Prasanna-K-123/causal-marketing-experimentation-uplift/blob/96e8b7c497c82dc6c2f6c458c20e7060c47f696e/docs/EVIDENCE_REVIEW.md)

**Limit:** Public retrospective evaluation; uncertainty is conditional on the fitted ranking. No profit or individual-treatment-effect claim.

## 3. [Financial AI Evidence Systems](https://github.com/Prasanna-K-123/enterprise-genai-rag-responsible-ai)

Across 883 FinQA development questions, TF-IDF recovered all labelled evidence at three for 61.38%; BM25 reached 57.98% and RRF 58.89%. Numerical controls separately cover 33 reconciliations and seven unsupported-request cases.

[Results](https://github.com/Prasanna-K-123/enterprise-genai-rag-responsible-ai/blob/88227013ccb1459b57366f2d8d21eea7ed57771a/results/finqa_retrieval/summary.json) · [Verification](https://github.com/Prasanna-K-123/enterprise-genai-rag-responsible-ai/blob/88227013ccb1459b57366f2d8d21eea7ed57771a/benchmark_finqa_retrieval.py) · [Successful CI](https://github.com/Prasanna-K-123/enterprise-genai-rag-responsible-ai/actions/runs/37966606959) · [Reproduction workflow](https://github.com/Prasanna-K-123/enterprise-genai-rag-responsible-ai/blob/88227013ccb1459b57366f2d8d21eea7ed57771a/.github/workflows/evidence-validation.yml) · [Scope review](https://github.com/Prasanna-K-123/enterprise-genai-rag-responsible-ai/blob/88227013ccb1459b57366f2d8d21eea7ed57771a/docs/EVIDENCE_REVIEW.md)

**Limit:** FinQA evaluation measures within-report retrieval, not end-to-end answer accuracy. The original small-model RAG study remains separately documented.

## 4. [Actuarial Risk Modelling](https://github.com/Prasanna-K-123/employee-benefits-actuarial-analytics)

Nine published rounded Mack standard errors reconcile within one unit. On 22 later-diagonal forecasts, MAE is 1,885.21 versus 3,425.45 for no development. The benefits workbook and reserving benchmark use different data.

[Results](https://github.com/Prasanna-K-123/employee-benefits-actuarial-analytics/blob/f5ddbc1093e23e5cfb973a92ca77d527a9d6f2a4/outputs/stochastic_reserving/summary.json) · [Verification](https://github.com/Prasanna-K-123/employee-benefits-actuarial-analytics/blob/f5ddbc1093e23e5cfb973a92ca77d527a9d6f2a4/src/stochastic_reserving.py) · [Successful CI](https://github.com/Prasanna-K-123/employee-benefits-actuarial-analytics/actions/runs/37966483129) · [Reproduction workflow](https://github.com/Prasanna-K-123/employee-benefits-actuarial-analytics/blob/f5ddbc1093e23e5cfb973a92ca77d527a9d6f2a4/.github/workflows/employee-benefits-actuarial-ci.yml) · [Scope review](https://github.com/Prasanna-K-123/employee-benefits-actuarial-analytics/blob/f5ddbc1093e23e5cfb973a92ca77d527a9d6f2a4/docs/EVIDENCE_REVIEW.md)

**Limit:** RAA is a historical reinsurance benchmark, not health-client data. Benefits valuation uses synthetic proxies and is not an IAS 19/ASC 715 valuation.

## 5. [Derivatives & Hedging Model Risk](https://github.com/Prasanna-K-123/volatility-surface-model-risk)

466 filtered option observations across six expiries support held-out-strike prediction comparisons. The hedge extension covers 27 cost/frequency/volatility scenarios on 3,000 common simulated paths, including terminal liquidation costs.

[Results](https://github.com/Prasanna-K-123/volatility-surface-model-risk/blob/328bef7988905d5329523fce2c501c0c4ae85261/reference/cost_aware_hedging/scenarios.csv) · [Verification](https://github.com/Prasanna-K-123/volatility-surface-model-risk/blob/328bef7988905d5329523fce2c501c0c4ae85261/verify_reference.py) · [Successful CI](https://github.com/Prasanna-K-123/volatility-surface-model-risk/actions/runs/37966502252) · [Reproduction workflow](https://github.com/Prasanna-K-123/volatility-surface-model-risk/blob/328bef7988905d5329523fce2c501c0c4ae85261/.github/workflows/validation.yml) · [Scope review](https://github.com/Prasanna-K-123/volatility-surface-model-risk/blob/328bef7988905d5329523fce2c501c0c4ae85261/docs/EVIDENCE_REVIEW.md)

**Limit:** One historical crypto-option snapshot and controlled GBM simulation; no global arbitrage-free or profitable-trading claim.

## 6. [C++20 Event-Driven Trading Engine](https://github.com/Prasanna-K-123/cpp-event-driven-trading-engine)

A separate vector-based matcher checks 25,000 randomized events across five seeds, every fill and all 256 order-ID slots after each event. Historical timing claims retain their machine and workload identity.

[Results](https://github.com/Prasanna-K-123/cpp-event-driven-trading-engine/blob/9dcc7a5b9418c78472454ba54340715da1d3a279/reference/performance_validation.json) · [Verification](https://github.com/Prasanna-K-123/cpp-event-driven-trading-engine/blob/9dcc7a5b9418c78472454ba54340715da1d3a279/tests/test_differential.cpp) · [Successful CI](https://github.com/Prasanna-K-123/cpp-event-driven-trading-engine/actions/runs/37966512460) · [Reproduction workflow](https://github.com/Prasanna-K-123/cpp-event-driven-trading-engine/blob/9dcc7a5b9418c78472454ba54340715da1d3a279/.github/workflows/validation.yml) · [Scope review](https://github.com/Prasanna-K-123/cpp-event-driven-trading-engine/blob/9dcc7a5b9418c78472454ba54340715da1d3a279/docs/EVIDENCE_REVIEW.md)

**Limit:** Synthetic replay and platform-specific historical benchmark; not live exchange latency or production trading.

## 7. [Data Engineering & Decision Optimisation](https://github.com/Prasanna-K-123/urban-mobility-pyspark-optimization)

24.08 million raw taxi trips were reprocessed into a complete zone panel. Modelled proxy vehicle-miles fell 3.76% versus a distance-aware greedy baseline. The transport core has 100 offline correctness cases, including 40 exhaustive comparisons.

[Results](https://github.com/Prasanna-K-123/urban-mobility-pyspark-optimization/blob/9260ef04775a5a9e4311f06453c40de4c6c9d636/results/project5_metrics.csv) · [Verification](https://github.com/Prasanna-K-123/urban-mobility-pyspark-optimization/blob/9260ef04775a5a9e4311f06453c40de4c6c9d636/results/transport_verification.json) · [Successful CI](https://github.com/Prasanna-K-123/urban-mobility-pyspark-optimization/actions/runs/37963818458) · [Reproduction workflow](https://github.com/Prasanna-K-123/urban-mobility-pyspark-optimization/blob/9260ef04775a5a9e4311f06453c40de4c6c9d636/.github/workflows/reproduce-tlc.yml) · [Scope review](https://github.com/Prasanna-K-123/urban-mobility-pyspark-optimization/blob/9260ef04775a5a9e4311f06453c40de4c6c9d636/docs/EVIDENCE_REVIEW.md)

**Limit:** TLC trip flow does not observe idle fleet supply; centroid distance is a proxy, and allocation is a static model.

## Provenance and contact

These are independent portfolio projects developed with AI assistance. Public-data studies, controlled simulations and synthetic demonstrations are labelled separately. Negative and inconclusive findings remain part of the evidence. They are not client engagements, production deployments, third-party endorsements or peer-reviewed publications.

[Profile](https://github.com/Prasanna-K-123) · [LinkedIn](https://www.linkedin.com/in/prasanna-k-964716384/) · ae26prasanna@mse.ac.in

