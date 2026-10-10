# Seven-project portfolio: evidence guide

**Prasanna K · Quantitative modelling & reliable decision systems · Summer 2027**

This guide links directly to the published results, verification and reproduction evidence. The seven projects stay fixed; a reviewer can enter through the work closest to their role.

| Reviewing for | Start with |
|---|---|
| Quantitative risk, financial modelling or validation | 1. Credit risk · 5. Derivatives · 6. C++ engineering |
| Applied AI, data science or decision systems | 3. Financial AI · 2. Causal decisions · 7. Data engineering |
| Actuarial analytics or insurance risk | 4. Actuarial models · 1. Credit risk · 2. Causal decisions |

The links below freeze the October 9 evidence snapshot. Each linked CI run completed successfully within its documented scope; a passing workflow does not establish production readiness or eliminate model risk. Current repository documentation may have newer clarification commits.

## October 10 update: extrapolation challenged

The October 9 snapshot below remains reproducible. Project 5 now also has an [analytic extrapolation audit](https://github.com/Prasanna-K-123/volatility-surface-model-risk/blob/fd9c3ff268f8c03cf742b580981548ebab06f08f/docs/EXTRAPOLATION_AUDIT.md), [frozen result/protocol](https://github.com/Prasanna-K-123/volatility-surface-model-risk/blob/fd9c3ff268f8c03cf742b580981548ebab06f08f/reference/density_audit/summary.json) and [successful validation run](https://github.com/Prasanna-K-123/volatility-surface-model-risk/actions/runs/38013024452). Two of six smiles fail a far-outside-support density stress check; the new bounded-evaluation API rejects unsupported extrapolation. The original held-out-strike benchmark includes three boundary-extrapolation points out of 116. These are model-risk findings, not observed executable market arbitrage or a global no-arbitrage proof.

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

466 filtered option observations across six expiries support held-strike baseline comparisons. The hedge extension covers 27 cost/frequency/volatility scenarios on 3,000 common simulated paths, including terminal liquidation costs.

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
