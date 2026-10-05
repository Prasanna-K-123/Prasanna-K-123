import numpy as np
from src.model import annuity_factor, chain_ladder, generate_health_triangle, generate_pension_population, health_summary, pension_sensitivity, pension_valuation

def test_annuity_factor_positive():
    assert annuity_factor(0.04,15)>0

def test_pension_discount_sensitivity_direction():
    s=pension_sensitivity(generate_pension_population()).set_index("scenario")
    assert s.loc["Discount -100 bps","liability_proxy"]>s.loc["Base","liability_proxy"]
    assert s.loc["Discount +100 bps","liability_proxy"]<s.loc["Base","liability_proxy"]

def test_pension_liabilities_nonnegative():
    assert (pension_valuation(generate_pension_population())["liability_proxy"]>=0).all()

def test_chain_ladder_ibnr_nonnegative():
    assert np.all(chain_ladder(generate_health_triangle())["ibnr"]>=-1e-8)

def test_health_pad_increases_reserve():
    s=health_summary(generate_health_triangle(),pad_rate=0.05)
    assert s["reserve_with_pad"]>s["ibnr"]
