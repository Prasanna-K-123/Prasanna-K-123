# Employee Benefits Actuarial Analytics - Retirement + Health & Welfare

Educational, synthetic-data project demonstrating employee-benefits actuarial mechanics without presenting project work as client or industry experience.

## Headline evidence

**Retirement / defined-benefit module**
- 180 synthetic employees.
- Base liability proxy: **$25.27m** at a 5% discount rate and 4% salary growth.
- Discount-rate sensitivity: **$30.37m at 4%** vs **$21.21m at 6%**.
- Annual benefit-start cash-flow forecast and illustrative lump-sum settlement / de-risking scenario.

**Health & welfare module**
- Synthetic **12x12 cumulative paid-claims triangle**.
- Estimated ultimate claims: **$14.81m**.
- Chain-ladder **IBNR: $3.06m**.
- Illustrative 5% PAD / risk margin: **$0.15m**; reserve-with-PAD proxy: **$3.22m**.
- 5% / 7% / 9% claim-trend scenarios: approximately **$15.55m / $15.85m / $16.15m** next-year cost proxies.

A companion formula-driven Excel workbook was built and visually QA'd. The public Python layer independently reproduces the core calculations. The local release passed **5/5 automated tests**.

## Evidence boundary

This is synthetic educational work only. It is not PwC work, client work, employer-sponsored-plan experience, a booked reserve, a pension actuarial opinion, or evidence of 1-2 years of actuarial industry experience.

The retirement output is deliberately a **liability proxy**, not an ASC 715 / IAS 19 / ERISA / IRS valuation. The health output is an educational chain-ladder IBNR/PAD illustration, not GAAP or statutory reserving.

See docs/METHODOLOGY_AND_LIMITATIONS.md for detailed scope exclusions.
