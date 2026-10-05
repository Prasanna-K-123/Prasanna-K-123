from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import pandas as pd

SEED = 20261005

def generate_pension_population(n: int = 180, seed: int = SEED) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    age = rng.integers(25, 61, size=n)
    max_service = np.minimum(age - 21, 30)
    service = np.array([rng.integers(0, max(1, int(m) + 1)) for m in max_service])
    salary = rng.integers(40_000, 160_001, size=n).astype(float)
    return pd.DataFrame({"employee_id":[f"E{i+1:03d}" for i in range(n)],"age":age,"service_years":service,"salary":salary})

def annuity_factor(rate: float, years: int) -> float:
    return float(years) if rate == 0 else float((1-(1+rate)**(-years))/rate)

def pension_valuation(employees: pd.DataFrame, discount_rate=0.05, salary_growth=0.04,
                      accrual_rate=0.015, retirement_age=65, annuity_rate=0.04, annuity_years=15):
    out=employees.copy()
    out["years_to_retirement"]=np.maximum(retirement_age-out["age"],0)
    out["projected_final_salary"]=out["salary"]*(1+salary_growth)**out["years_to_retirement"]
    out["accrued_annual_benefit"]=accrual_rate*out["projected_final_salary"]*out["service_years"]
    out["pv_at_retirement"]=out["accrued_annual_benefit"]*annuity_factor(annuity_rate,annuity_years)
    out["liability_proxy"]=out["pv_at_retirement"]/(1+discount_rate)**out["years_to_retirement"]
    return out

def pension_sensitivity(employees: pd.DataFrame):
    scenarios=[("Discount -100 bps",0.04,0.04),("Base",0.05,0.04),("Discount +100 bps",0.06,0.04),
               ("Salary growth -100 bps",0.05,0.03),("Salary growth +100 bps",0.05,0.05)]
    rows=[]
    for name,d,g in scenarios:
        total=float(pension_valuation(employees,d,g)["liability_proxy"].sum())
        rows.append({"scenario":name,"discount_rate":d,"salary_growth":g,"liability_proxy":total})
    base=next(r["liability_proxy"] for r in rows if r["scenario"]=="Base")
    for r in rows:r["change_vs_base_pct"]=r["liability_proxy"]/base-1
    return pd.DataFrame(rows)

def generate_health_triangle(months=12, seed=SEED+1):
    rng=np.random.default_rng(seed)
    ultimates=rng.normal(1_200_000,150_000,size=months).clip(850_000,1_600_000)
    pattern=np.array([0.28,0.47,0.62,0.73,0.81,0.87,0.91,0.94,0.965,0.982,0.994,1.0])
    triangle=np.full((months,months),np.nan)
    full=np.outer(ultimates,pattern)
    for i in range(months):triangle[i,:months-i]=full[i,:months-i]
    return triangle

def chain_ladder(triangle):
    n=triangle.shape[1]
    factors=[]
    for j in range(n-1):
        valid=~np.isnan(triangle[:,j+1])
        factors.append(float(np.nansum(triangle[valid,j+1])/np.nansum(triangle[valid,j])))
    factors=np.array(factors); cdf=np.ones(n)
    for j in range(n-2,-1,-1):cdf[j]=cdf[j+1]*factors[j]
    latest=[]; dev=[]
    for row in triangle:
        idx=np.where(~np.isnan(row))[0][-1]; dev.append(idx); latest.append(row[idx])
    latest=np.array(latest)
    ultimate=np.array([latest[i]*cdf[dev[i]] for i in range(len(latest))])
    return {"latest_paid":latest,"estimated_ultimate":ultimate,"ibnr":ultimate-latest}

def health_summary(triangle, pad_rate=0.05, annual_trend=0.07):
    cl=chain_ladder(triangle)
    paid=float(cl["latest_paid"].sum()); ultimate=float(cl["estimated_ultimate"].sum()); ibnr=float(cl["ibnr"].sum())
    return {"paid_to_date":paid,"estimated_ultimate":ultimate,"ibnr":ibnr,"pad":ibnr*pad_rate,
            "reserve_with_pad":ibnr*(1+pad_rate),"next_year_cost_proxy":ultimate*(1+annual_trend)}

def run(output_dir="outputs"):
    out=Path(output_dir); out.mkdir(parents=True,exist_ok=True)
    employees=generate_pension_population(); p=pension_valuation(employees); ps=pension_sensitivity(employees)
    h=health_summary(generate_health_triangle())
    summary={"scope":"synthetic educational work only","pension":{"employees":len(employees),
             "base_liability_proxy":float(p["liability_proxy"].sum()),
             "discount_minus_100bps":float(ps.loc[ps.scenario=="Discount -100 bps","liability_proxy"].iloc[0]),
             "discount_plus_100bps":float(ps.loc[ps.scenario=="Discount +100 bps","liability_proxy"].iloc[0])},"health":h}
    (out/"summary.json").write_text(json.dumps(summary,indent=2))
    return summary

if __name__=="__main__":print(json.dumps(run(),indent=2))
