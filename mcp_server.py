# -*- coding: utf-8 -*-
"""
Personal Agent Financial Runway Monte Carlo FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import PersonalAgentFinancialRunwayMonteCarlo

mcp = FastMCP("genpark-personal-agent-financial-runway-monte-carlo-skill")
fiduciary = PersonalAgentFinancialRunwayMonteCarlo()

@mcp.tool()
def simulate_cash_runway_monte_carlo(
    current_liquid_assets_usd: float,
    monthly_fixed_burn_usd: float,
    monthly_variable_burn_usd: float,
    monthly_expected_income_usd: float,
    income_volatility_sigma: float = 0.20,
    horizon_months: int = 24,
    simulation_paths: int = 500
) -> str:
    """
    Simulates personal cash runway and probability of ruin using stochastic Monte Carlo simulation.
    """
    res = fiduciary.simulate_cash_runway_monte_carlo(
        current_liquid_assets_usd, monthly_fixed_burn_usd, monthly_variable_burn_usd,
        monthly_expected_income_usd, income_volatility_sigma, horizon_months, simulation_paths
    )
    return json.dumps(res, indent=2)

@mcp.tool()
def compute_safe_discretionary_burn_budget(
    current_liquid_assets_usd: float,
    monthly_fixed_burn_usd: float,
    target_runway_months: int = 12,
    min_emergency_reserve_usd: float = 10000.0
) -> str:
    """
    Calculates safe monthly and daily discretionary burn ceilings ensuring runway target is met.
    """
    res = fiduciary.compute_safe_discretionary_burn_budget(
        current_liquid_assets_usd, monthly_fixed_burn_usd, target_runway_months, min_emergency_reserve_usd
    )
    return json.dumps(res, indent=2)

@mcp.tool()
def calculate_emergency_liquidity_buffer_days(
    liquid_cash_usd: float,
    daily_burn_usd: float,
    burn_trend_slope: float = 0.0
) -> str:
    """
    Calculates emergency liquidity buffer days and financial resilience tier under zero income.
    """
    res = fiduciary.calculate_emergency_liquidity_buffer_days(liquid_cash_usd, daily_burn_usd, burn_trend_slope)
    return json.dumps(res, indent=2)

def main():
    print("Testing Financial Runway Monte Carlo FastMCP Server:")
    print(compute_safe_discretionary_burn_budget(60000.0, 3000.0, 12, 12000.0))

if __name__ == "__main__":
    main()
