# Prasanna K

**M.A. Actuarial Economics @ Madras School of Economics | Quant Research • Trading Systems • Derivatives • Credit & Model Risk | Python • C++20**

I build reproducible quantitative research and engineering projects across market microstructure, trading systems, derivatives, credit and model validation. My work emphasizes leakage control, meaningful baselines, out-of-sample or holdout testing, deterministic evidence, adversarial diagnostics, reproducibility and explicit limitations rather than headline metrics without context.

## Flagship quantitative work

### [Quant Market Microstructure & Execution Research](https://github.com/Prasanna-K-123/quant-market-microstructure-research)
Leakage-controlled short-horizon research on **2,419,200** official Binance 1-second observations across **28** SHA-256-verified daily archives, with chronological train/validation/final-test separation, execution lag, baseline challenges, bootstrap/regime checks and transaction-cost sensitivity.

- Strongest held-out BTCUSDT 5s Ridge result: Pearson IC **0.02064**, Spearman IC **0.04445**, directional accuracy **52.68%**
- Simple last-5s-return OLS baseline Pearson IC **0.02264** exceeds the multivariate Ridge result; the adverse complexity finding is retained
- Strongest reported prediction-decile spread is only about **0.137 bps before friction**, so no deployable-alpha claim is made

### [C++ Event-Driven Trading / Backtest Engine](https://github.com/Prasanna-K-123/cpp-event-driven-trading-engine)
C++20 deterministic execution-systems project with price-time priority, marketable limits, market orders, intrusive per-price FIFO queues, live-order indexing, adversarial tests, ASan/UBSan, reproducible benchmarking and replay-only Callgrind profiling.

- Cancellation is **O(1) with respect to queue length after the order-ID hash lookup**
- Frozen 1,000,000-event optimization sequence: **145.102 → 104.115 ns/event** and **140,001,502 → 100,873,271** replay instructions
- Semantic replay outputs and the deep-state checksum remain identical across the accepted optimization sequence

### [Derivatives Volatility Surface, Static Arbitrage & Hedging Model Risk](https://github.com/Prasanna-K-123/volatility-surface-model-risk)
Timestamped Deribit BTC-options study with constrained raw-SVI calibration, alternating-strike holdouts, quadratic baseline challenge, observed-support static-arbitrage diagnostics, calendar checks and a separate controlled hedging model-risk experiment.

- **978** raw option rows → **466** frozen-filter rows → **6** fitted expiries
- Median SVI holdout RMSE **0.00017263** vs quadratic **0.00032092** total variance; SVI wins **4/6** expiries
- **0** observed-support call-monotonicity, call-convexity or common-grid calendar violating points; negative identifiability evidence is retained explicitly

### [Leveraged Credit Underwriting, Debt Capacity & Downside Recovery](https://github.com/Prasanna-K-123/leveraged-credit-underwriting)
SEC-source-traceable Carnival underwriting with annual/TTM operating reconstruction, carrying-value vs gross-principal debt reconciliation, maturity/refinancing exposure, downside leverage/coverage, debt-capacity grids and a deliberately simplified recovery sensitivity.

- Reconciled **$24,889m** carrying-value debt vs **$25,570m** gross-principal debt as distinct definitions
- TTM EBITDA proxy **$7,327m**; gross-principal leverage **3.49x**; EBITDA/interest proxy **6.07x**
- Severe stress reaches **5.62x** leverage and **3.01x** coverage; simplified 5x EV/EBITDA severe waterfall gives about **79.5%** to modeled unsecured debt without subsidiary guarantee

## Additional validated work

- [Market Risk: VaR, Expected Shortfall, Stress & Limits](https://github.com/Prasanna-K-123/market-risk-var-es-stress-limits) — cross-asset VaR/ES, EWMA covariance, rolling backtests, stress scenarios and limits, with adverse diagnostics retained.
- [Independent Model Risk Validation & Governance](https://github.com/Prasanna-K-123/model-risk-validation-governance) — independent-style PD-model validation with recomputation, calibration, challenger testing, stability/sensitivity analysis and findings management.
- [Causal Experimentation, Bootstrapping & Uplift Modeling](https://github.com/Prasanna-K-123/causal-marketing-experimentation-uplift) — randomized-experiment analysis, bootstrap uncertainty, multiplicity control and honest final-test uplift modeling.
- [Urban Mobility Operations & Fleet Rebalancing Optimization](https://github.com/Prasanna-K-123/urban-mobility-pyspark-optimization) — PySpark/geospatial processing plus integer optimization on NYC TLC data.

## Technical toolkit

**Programming / systems:** Python, C++20, SQL, CMake, Git, GitHub Actions  
**Python / data:** Pandas, NumPy, SciPy, scikit-learn, statsmodels, DuckDB, PySpark / Spark SQL, Matplotlib, PuLP  
**Quantitative methods:** statistical modeling, econometrics, simulation, optimization, causal inference, discrete choice, market/credit risk, model validation, stress testing  
**Validation / performance:** unit and invariant testing, ASan/UBSan, deterministic replay, reproducible pipelines, profiling and benchmark design

## Working standard

- Separate reported fact, empirical evidence, simulation and analyst assumptions.
- Preserve adverse diagnostics and negative results when they change the interpretation.
- Use chronological, group-aware or holdout validation when random splitting would leak information.
- Challenge complex models against meaningful simple baselines.
- Keep recruiter-facing claims traceable to code, source provenance and reproducible outputs.

## Background

- **M.A. Actuarial Economics**, Madras School of Economics — expected Jun 2028
- **B.Sc. Mathematics**, Loyola College — 2026
- **Data Analyst Intern, Picklers Arena** — Excel-based booking-data cleaning, analysis and operational insights
- Competitive debating and public speaking; multiple inter-collegiate awards

## Contact

[Email](mailto:prasannak0911@gmail.com) | [LinkedIn](https://www.linkedin.com/in/prasanna-k-964716384) | [GitHub](https://github.com/Prasanna-K-123)
