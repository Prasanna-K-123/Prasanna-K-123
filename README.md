# Prasanna K

**M.A. Actuarial Economics @ Madras School of Economics | B.Sc. Mathematics | Quantitative Risk & Model Validation**

I build reproducible financial-risk and quantitative-analytics projects with an emphasis on **credit risk, market risk, liquidity risk, stress testing, model validation and governance**. I separate empirical evidence from synthetic or illustrative assumptions and document model limitations explicitly.

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
Cross-asset market-risk platform using public historical observations, factor-sensitivity P&L, Historical/Parametric/Monte Carlo VaR and ES, EWMA covariance, rolling VaR backtesting, stress testing, risk decomposition and automated limit monitoring.

- **1,090** rolling VaR backtest observations
- Historical VaR: **1.285m**; Historical ES: **2.226m** on the illustrative portfolio
- Backtesting reports both acceptable unconditional coverage and detected exception clustering rather than suppressing adverse diagnostics

### [Liquidity Risk, ILAAP & Recovery Planning](https://github.com/Prasanna-K-123/liquidity-risk-ilaap-recovery)
Liquidity-risk framework covering cash-flow ladders, LCR/NSFR-style metrics, liquidity-buffer haircuts, survival horizons, stress and reverse-stress testing, early-warning indicators, limits and recovery actions.

- Built around a deterministic **8,000-account synthetic balance sheet**
- Includes idiosyncratic, marketwide and combined liquidity stresses
- Regulatory-style labels and recovery capacities are explicitly illustrative rather than presented as bank data

### [Independent Model Risk Validation & Governance](https://github.com/Prasanna-K-123/model-risk-validation-governance)
Independent-style validation of a separately built credit-risk PD model: pinned source evidence, metric recomputation, calibration, challenger benchmarking, stability review, sensitivity testing, findings management and validation opinion.

- Primary AUC **0.7295** vs challenger AUC **0.7529** on **200** holdout observations
- Validation identified **5 open findings**, including **2 high-severity** issues
- Final opinion: **conditionally acceptable for research; not production-approved**

## Technical toolkit

**Python** · Pandas · NumPy · SciPy · scikit-learn · statsmodels · SQL/DuckDB · PySpark/Spark SQL · Git/GitHub · statistical modelling · simulation · model validation

## Background

- **M.A. Actuarial Economics**, Madras School of Economics — expected 2028
- **B.Sc. Mathematics**, Loyola College — 2026
- Data Analyst Intern, Picklers Arena — Excel-based data cleaning, booking-pattern analysis and operational insights
- Competitive debating and public speaking; academic and inter-collegiate competition awards

## Contact

**Email:** [ae26prasanna@mse.ac.in](mailto:ae26prasanna@mse.ac.in)
