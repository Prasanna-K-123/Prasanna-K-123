# Employee Benefits Actuarial Analytics - Retirement + Health & Welfare

> **Current canonical project:** [Employee Benefits Actuarial Analytics](https://github.com/Prasanna-K-123/employee-benefits-actuarial-analytics). It preserves this model and its headline results, adds a direct workbook download and workbook recalculation checks, and corrects workbook presentation/control gaps. This original folder and its history remain available as provenance.

[![Employee Benefits Actuarial CI](https://github.com/Prasanna-K-123/Prasanna-K-123/actions/workflows/employee-benefits-actuarial-ci.yml/badge.svg)](https://github.com/Prasanna-K-123/Prasanna-K-123/actions/workflows/employee-benefits-actuarial-ci.yml)

A compact, reproducible **educational employee-benefits actuarial model** built to demonstrate the mechanics behind retirement liability analysis and health-claims reserving without presenting synthetic work as client or industry experience.

## Headline evidence

### Retirement / defined-benefit module

- Synthetic population: **180 employees**.
- Base liability proxy at a 5% discount rate and 4% salary growth: **$25.27m**.
- Discount-rate sensitivity: **$30.37m at 4%** versus **$21.21m at 6%**.
- Includes benefit-start cash-flow forecasting and an illustrative lump-sum settlement / de-risking scenario.

### Health & welfare module

- Synthetic **12x12 cumulative paid-claims development triangle**.
- Estimated ultimate claims: **$14.81m**.
- Chain-ladder **IBNR: $3.06m**.
- Illustrative 5% PAD / risk margin: **$0.15m**, giving a reserve-with-PAD proxy of **$3.22m**.
- 5% / 7% / 9% claim-trend scenarios produce next-year cost proxies of approximately **$15.55m / $15.85m / $16.15m**.

## Excel model and public audit trail

The primary business-facing work product is a formula-driven Excel model. The workbook is rebuilt from source on every green CI run and published as the **Employee_Benefits_Actuarial_Model** workflow artifact. The repository also exposes the [Excel workbook builder](src/build_excel.py), [workbook formula map](docs/WORKBOOK_FORMULA_MAP.md), independent Python calculation layer, automated tests and structured output evidence, so the modeling logic and headline numbers remain reviewable.

Public evidence:
- [Excel workbook builder](src/build_excel.py)
- [summary outputs](outputs/summary.json)
- [retirement sensitivity](outputs/pension_sensitivity.csv)
- [15-year benefit-start cash-flow forecast](outputs/pension_cashflow_forecast.csv)
- [health claims sensitivity](outputs/health_claims_sensitivity.csv)
- [methodology and limitations](docs/METHODOLOGY_AND_LIMITATIONS.md)
- [workbook formula map](docs/WORKBOOK_FORMULA_MAP.md)
- [model review / decision interpretation](docs/MODEL_REVIEW.md)

## Python validation layer

`src/model.py` independently reproduces the core calculations. The automated test suite checks key directional and control properties:

- lower discount rates increase the retirement liability proxy;
- higher discount rates decrease it;
- modeled liabilities remain non-negative;
- chain-ladder IBNR is non-negative;
- adding PAD increases the health reserve proxy.

Run:

```bash
python -m pip install -r requirements.txt
python -m src.model
python -m pytest -q
```

The original release has eight Python controls. See the CI badge for its status; use the canonical repository above for the updated workbook and workbook verification.

## Repository map

```text
src/model.py                               independent Python calculation layer
src/build_excel.py                         reproducible formula-driven Excel builder
tests/test_model.py                        automated controls
outputs/                                   reproducible sensitivities and summaries
docs/METHODOLOGY_AND_LIMITATIONS.md        model boundary and exclusions
docs/WORKBOOK_FORMULA_MAP.md               Excel formula / control map
requirements.txt                           reproducibility dependencies
```

## Evidence boundary

This project uses **synthetic data only**. It is not PwC work, client work, employer-sponsored-plan experience, a booked health reserve, a pension actuarial opinion, or evidence of 1-2 years of actuarial industry experience.

The retirement result is deliberately labelled a **liability proxy**, not an ASC 715 / IAS 19 / ERISA / IRS valuation. The health result is an educational chain-ladder IBNR and PAD illustration, not GAAP or statutory reserving.

The project demonstrates **liability measurement, cash-flow forecasting, assumption sensitivity, claims development, IBNR, risk margin, model transparency and validation discipline** while keeping those boundaries explicit.
