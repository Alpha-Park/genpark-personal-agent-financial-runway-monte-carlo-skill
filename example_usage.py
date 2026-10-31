# -*- coding: utf-8 -*-
import json
from client import PersonalAgentFinancialRunwayMonteCarlo

fiduciary = PersonalAgentFinancialRunwayMonteCarlo()

print("=" * 64)
print("DEMO: Personal Financial Runway Monte Carlo Fiduciary")
print("=" * 64)

# 1. Stochastic Runway Monte Carlo Simulation
sim = fiduciary.simulate_cash_runway_monte_carlo(
    current_liquid_assets_usd=85000.0,
    monthly_fixed_burn_usd=3500.0,
    monthly_variable_burn_usd=2000.0,
    monthly_expected_income_usd=6000.0,
    income_volatility_sigma=0.35,
    horizon_months=24,
    simulation_paths=500
)
print(f"\n1. Monte Carlo Simulation (500 Paths over {sim['simulation_horizon_months']} Months):")
print(f"   Probability of Ruin: {sim['probability_of_ruin_pct']}% ({sim['runway_security_status']})")
print(f"   Median Wealth at Horizon: ${sim['median_terminal_wealth_usd']:,}")
print(f"   Worst 10% Wealth Outcome: ${sim['p10_worst_case_wealth_usd']:,}")

# 2. Safe Discretionary Burn Budget
budget = fiduciary.compute_safe_discretionary_burn_budget(
    current_liquid_assets_usd=75000.0,
    monthly_fixed_burn_usd=2800.0,
    target_runway_months=18,
    min_emergency_reserve_usd=15000.0
)
print(f"\n2. Safe Discretionary Burn Budget (Target: {budget['target_runway_months']} Months):")
print(f"   Safe Monthly Discretionary Limit: ${budget['safe_monthly_discretionary_burn_usd']:,}/month")
print(f"   Safe Daily Allowance: ${budget['safe_daily_discretionary_spend_usd']:,}/day ({budget['liquidity_posture']})")

# 3. Emergency Buffer Days
buffer = fiduciary.calculate_emergency_liquidity_buffer_days(liquid_cash_usd=45000.0, daily_burn_usd=120.0)
print(f"\n3. Zero-Income Emergency Buffer:")
print(f"   Buffer Days: {buffer['emergency_liquidity_buffer_days']} days ({buffer['buffer_in_months']} months)")
print(f"   Resilience Tier: {buffer['resilience_rating']}")
