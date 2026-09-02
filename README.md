# Prasanna K

**M.A. Actuarial Economics @ Madras School of Economics | Quantitative Modeling, Markets & Statistical Research | Python**

I build reproducible quantitative projects across market risk, causal inference, optimization, econometrics, model validation, credit risk and applied machine learning. My work emphasizes leakage control, strong baselines, out-of-sample validation, uncertainty, robustness checks, reproducibility and explicit limitations rather than headline metrics without context.

## Selected quantitative work

### [Market Risk: VaR, Expected Shortfall, Stress & Limits](https://github.com/Prasanna-K-123/market-risk-var-es-stress-limits)
Cross-asset market-risk research and monitoring framework using public historical factors, factor-sensitivity P&L, Historical/Parametric/Monte Carlo VaR and ES, EWMA covariance, rolling backtests, stress scenarios and risk limits.

- 1,341 aligned daily factor observations and 1,090 rolling VaR forecasts
- Historical 99% VaR: USD 1.285m; Historical 99% ES: USD 2.226m on the illustrative portfolio
- Kupiec coverage p-value 0.0861; Christoffersen independence p-value 0.0015, retained as an adverse model-risk finding rather than hidden

### [Causal Experimentation, Bootstrapping & Uplift Modeling](https://github.com/Prasanna-K-123/causal-marketing-experimentation-uplift)
Randomized-experiment analysis with treatment-effect estimation, multiplicity control, bootstrap uncertainty, honest train/validation/final-test model selection and uplift modeling.

- Hillstrom randomized-email experiment with 64,000 customers
- 5,000 bootstrap resamples and Holm multiplicity correction
- Final-test top-30% visit uplift exceeded the remainder by 4.53 percentage points; bootstrap 95% CI 1.50-7.52 pp
- Negative spend-heterogeneity result preserved explicitly

### [Urban Mobility Operations & Fleet Rebalancing Optimization](https://github.com/Prasanna-K-123/urban-mobility-pyspark-optimization)
Large-scale PySpark, geospatial and integer-optimization study using NYC TLC trip records.

- 24,083,384 raw trips processed; 22,974,942 retained after cleaning
- Complete 129-weekday x 261-zone 6 PM panel to avoid zero-activity omission bias
- Integer allocation covered all 1,382 modeled deficit vehicles and reduced proxy deadhead distance by 3.76% versus a distance-aware greedy benchmark

### [Independent Model Risk Validation & Governance](https://github.com/Prasanna-K-123/model-risk-validation-governance)
Independent-style validation of a separately built credit-risk PD model using pinned source evidence, metric recomputation, bootstrap uncertainty, calibration, challenger analysis, stability and sensitivity testing, findings management and a formal validation opinion.

- Primary ROC-AUC 0.7295 vs challenger 0.7529 on 200 pinned holdout observations
- 5 open findings, including 2 high-severity findings
- Final opinion: conditionally acceptable for research; not production-approved

### [Pricing & Customer Choice with Discrete Choice Modeling](https://github.com/Prasanna-K-123/pricing-customer-choice-discrete-choice)
Econometric choice-modeling study using the EPFL/Biogeme Swissmetro benchmark with a direct multinomial-logit implementation, respondent-level holdout validation and price-sensitivity analysis.

- 6,768 usable choices from 752 respondents
- Full-sample log likelihood -5331.252007 vs official Biogeme benchmark -5331.252000
- Respondent-level holdout to avoid repeated-person leakage
- Model-implied value of travel time: CHF 70.74/hour; own-fare arc elasticity around -0.45

## Additional work

- [Credit Risk, IFRS 9 & Stress Testing](https://github.com/Prasanna-K-123/credit-risk-ifrs9-stress-testing)
- [Basel Credit Portfolio, Economic Capital & ICAAP](https://github.com/Prasanna-K-123/basel-credit-portfolio-icaap)
- [Liquidity Risk, ILAAP & Recovery Planning](https://github.com/Prasanna-K-123/liquidity-risk-ilaap-recovery)
- [Enterprise GenAI RAG Assistant - Retrieval, Evaluation & Responsible AI](https://github.com/Prasanna-K-123/enterprise-genai-rag-responsible-ai)

## Technical toolkit

**Python:** Pandas, NumPy, SciPy, scikit-learn, statsmodels, Matplotlib  
**Data / computation:** SQL, DuckDB, PySpark / Spark SQL, PuLP  
**Methods:** statistical modeling, simulation, optimization, causal inference, discrete choice, model validation, stress testing  
**Engineering:** Git, GitHub, GitHub Actions, reproducible pipelines, automated tests

## Working standard

- Separate empirical evidence from synthetic or illustrative assumptions.
- Preserve adverse diagnostics and negative results when they change the interpretation.
- Use chronological or group-aware validation when random splitting would leak information.
- Compare against meaningful baselines rather than intentionally weak ones.
- Keep published claims traceable to code, data provenance and reproducible outputs.

## Background

- **M.A. Actuarial Economics**, Madras School of Economics - expected Jun 2028
- **B.Sc. Mathematics**, Loyola College - 2026
- **Data Analyst Intern, Picklers Arena** - Excel-based booking-data cleaning, analysis and operational insights
- Competitive debating and public speaking; multiple inter-collegiate awards

## Contact

[Email](mailto:prasannak0911@gmail.com) | [LinkedIn](https://www.linkedin.com/in/prasanna-k-964716384) | [GitHub](https://github.com/Prasanna-K-123)
