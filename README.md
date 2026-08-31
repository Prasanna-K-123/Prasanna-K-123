# Prasanna K

**M.A. Actuarial Economics @ Madras School of Economics | Financial Services Risk Management | Model Validation**

I build reproducible financial-services risk projects spanning **credit risk, market risk, liquidity risk, stress testing, capital adequacy, model validation and governance**. I separate empirical evidence from synthetic or illustrative assumptions, preserve adverse diagnostics, and document model limitations explicitly.

## Featured risk projects

### [Credit Risk, IFRS 9 & Stress Testing](https://github.com/Prasanna-K-123/credit-risk-ifrs9-stress-testing)
Application-style PD modelling with a WoE/logistic scorecard, random-forest challenger, calibration and bootstrap validation, IFRS 9-style ECL mechanics, stress testing, risk-grade monitoring and governance documentation.

- Holdout scorecard ROC-AUC: **0.730**; challenger ROC-AUC: **0.753**
- Gini: **0.459**; KS: **0.374**; Brier score: **0.184**
- Empirical PD evidence is separated from illustrative LGD/EAD and scenario assumptions

### [Basel Credit Portfolio, Economic Capital & ICAAP](https://github.com/Prasanna-K-123/basel-credit-portfolio-icaap)
Portfolio-level credit-risk engine covering expected loss, Basel-style corporate IRB capital, rating migration, concentration risk, one-factor economic-capital simulation, stress testing, reverse stress and ICAAP-style capital assessment.

- Deterministic **5,000-obligor synthetic portfolio** with **16.56bn** total EAD
- **100,000** loss simulations; 99.9% economic capital above model EL: **1.093bn**
- Synthetic inputs and illustrative capital assumptions are explicitly labelled

### [Market Risk, VaR / Expected Shortfall, Stress & Limits](https://github.com/Prasanna-K-123/market-risk-var-es-stress-limits)
Cross-asset market-risk platform using public historical observations, factor-sensitivity P&L, Historical/Parametric/Monte Carlo VaR and ES, EWMA covariance, rolling VaR backtesting, stress testing and automated position/risk-limit monitoring.

- **1,341** aligned daily factor observations and **1,090** rolling VaR forecasts
- Historical 99% VaR: **1.285m**; Historical 99% ES: **2.226m** on the illustrative portfolio
- Kupiec unconditional-coverage p-value **0.0861**; Christoffersen independence p-value **0.0015**, explicitly surfacing clustered exceptions as a model-risk finding

### [Liquidity Risk, ILAAP & Recovery Planning](https://github.com/Prasanna-K-123/liquidity-risk-ilaap-recovery)
Liquidity-risk framework covering cash-flow ladders, LCR/NSFR-style metrics, liquidity-buffer haircuts, survival horizons, stress and reverse-stress testing, early-warning indicators, limits and recovery actions.

- Deterministic **8,000-account synthetic balance sheet**
- Base LCR-style ratio **3.97x** and NSFR-style ratio **1.76x**; combined-severe LCR-style ratio **0.69x**
- Combined severe stress produces a **2.45bn** peak liquidity deficit; recovery capacities and regulatory-style labels remain explicitly illustrative

### [Independent Model Risk Validation & Governance](https://github.com/Prasanna-K-123/model-risk-validation-governance)
Independent-style validation/challenge of a separately built credit-risk PD model: pinned source evidence, metric recomputation, calibration, challenger benchmarking, stability review, sensitivity testing, findings management and validation opinion.

- Primary AUC **0.7295** vs challenger AUC **0.7529** on **200** pinned holdout observations
- Validation identified **5 open findings**, including **2 high-severity** issues
- Final opinion: **conditionally acceptable for research; not production-approved**

## Technical toolkit

**Python** · Pandas · NumPy · SciPy · scikit-learn · statsmodels · SQL/DuckDB · PySpark/Spark SQL · Git/GitHub · statistical modelling · simulation · model validation

## Background

- **M.A. Actuarial Economics**, Madras School of Economics - expected 2028
- **B.Sc. Mathematics**, Loyola College - 2026
- Data Analyst Intern, Picklers Arena - Excel-based data cleaning, booking-pattern analysis and operational insights
- Competitive debating and public speaking; academic and inter-collegiate competition awards

## Contact

**Email:** [ae26prasanna@mse.ac.in](mailto:ae26prasanna@mse.ac.in)
