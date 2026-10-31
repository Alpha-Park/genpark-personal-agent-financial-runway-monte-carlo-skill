# -*- coding: utf-8 -*-
"""
Personal Agent Financial Runway Monte Carlo Client
Zero-dependency stochastic cash runway modeler, Box-Muller Gaussian Monte Carlo
simulation, and safe discretionary burn budget calculator.
"""

import math
from typing import Dict, List, Any, Optional, Tuple

class PersonalAgentFinancialRunwayMonteCarlo:
    """
    Simulates personal cash runway under stochastic income shocks and inflation volatility.
    Calculates empirical probability of ruin, emergency buffer days, and safe discretionary budgets.
    """

    def _box_muller_normal(self, seed: float) -> Tuple[float, float]:
        """
        Generates pseudo-random standard normal pair using deterministic chaotic Box-Muller mapping.
        """
        # Linear congruential generator step
        u1 = max(1e-6, min(0.999999, (seed * 1103515245.0 + 12345.0) % 2147483648.0 / 2147483648.0))
        u2 = max(1e-6, min(0.999999, (u1 * 1103515245.0 + 12345.0) % 2147483648.0 / 2147483648.0))
        r = math.sqrt(-2.0 * math.log(u1))
        theta = 2.0 * math.pi * u2
        return r * math.cos(theta), r * math.sin(theta)

    def simulate_cash_runway_monte_carlo(
        self,
        current_liquid_assets_usd: float,
        monthly_fixed_burn_usd: float,
        monthly_variable_burn_usd: float,
        monthly_expected_income_usd: float,
        income_volatility_sigma: float = 0.20,
        horizon_months: int = 24,
        simulation_paths: int = 500
    ) -> Dict[str, Any]:
        """
        Simulates personal liquid balance over horizon using Geometric Brownian Motion cash flows.
        """
        assets = max(100.0, float(current_liquid_assets_usd))
        fixed_burn = max(0.0, float(monthly_fixed_burn_usd))
        var_burn = max(0.0, float(monthly_variable_burn_usd))
        mean_income = max(0.0, float(monthly_expected_income_usd))
        sigma = max(0.01, min(1.0, float(income_volatility_sigma)))
        n_paths = max(50, min(1000, int(simulation_paths)))
        t_months = max(3, min(60, int(horizon_months)))

        ruin_count = 0
        terminal_balances = []
        months_to_depletion = []

        seed = 42.1337 + assets % 1000.0

        for path in range(n_paths):
            bal = assets
            depleted_month = None
            for m in range(1, t_months + 1):
                z, seed_next = self._box_muller_normal(seed + path * 31.0 + m * 7.0)
                seed = seed_next
                # Monthly income with lognormal stochastic drift
                monthly_income = mean_income * math.exp(-0.5 * sigma * sigma + sigma * z)
                net_flow = monthly_income - (fixed_burn + var_burn)
                bal += net_flow

                if bal <= 0.0 and depleted_month is None:
                    depleted_month = m
                    bal = 0.0

            terminal_balances.append(bal)
            if depleted_month is not None:
                ruin_count += 1
                months_to_depletion.append(depleted_month)

        terminal_balances.sort()
        prob_ruin = round(ruin_count / float(n_paths) * 100.0, 1)
        median_terminal = round(terminal_balances[n_paths // 2], 2)
        p10_terminal = round(terminal_balances[n_paths // 10], 2)
        mean_depletion = round(sum(months_to_depletion) / len(months_to_depletion), 1) if months_to_depletion else None

        # Static baseline deterministic runway
        deterministic_net = mean_income - (fixed_burn + var_burn)
        if deterministic_net < 0:
            deterministic_runway = round(assets / abs(deterministic_net), 1)
        else:
            deterministic_runway = 999.0

        return {
            "initial_liquid_assets_usd": assets,
            "monthly_burn_total_usd": round(fixed_burn + var_burn, 2),
            "monthly_expected_income_usd": mean_income,
            "simulation_horizon_months": t_months,
            "simulation_paths_evaluated": n_paths,
            "probability_of_ruin_pct": prob_ruin,
            "median_terminal_wealth_usd": median_terminal,
            "p10_worst_case_wealth_usd": p10_terminal,
            "average_months_to_ruin_when_depleted": mean_depletion,
            "deterministic_runway_months": deterministic_runway if deterministic_runway != 999.0 else "INDEFINITE_POSITIVE_CASHFLOW",
            "runway_security_status": "EXCELLENT_SECURE" if prob_ruin <= 5.0 else ("MODERATE_RUNWAY_RISK" if prob_ruin <= 25.0 else "URGENT_DEFICIT_REDUCTION_REQUIRED")
        }

    def compute_safe_discretionary_burn_budget(
        self,
        current_liquid_assets_usd: float,
        monthly_fixed_burn_usd: float,
        target_runway_months: int = 12,
        min_emergency_reserve_usd: float = 10000.0
    ) -> Dict[str, Any]:
        """
        Calculates safe monthly discretionary spending ceiling ensuring runway reaches target horizon.
        """
        assets = max(0.0, float(current_liquid_assets_usd))
        fixed = max(0.0, float(monthly_fixed_burn_usd))
        reserve = max(0.0, float(min_emergency_reserve_usd))
        horizon = max(1, int(target_runway_months))

        available_capital = max(0.0, assets - reserve)
        max_sustainable_monthly_spend = available_capital / float(horizon)
        safe_discretionary_limit = max(0.0, max_sustainable_monthly_spend - fixed)

        return {
            "current_liquid_assets_usd": assets,
            "minimum_emergency_reserve_usd": reserve,
            "target_runway_months": horizon,
            "fixed_burn_usd": fixed,
            "safe_monthly_discretionary_burn_usd": round(safe_discretionary_limit, 2),
            "safe_daily_discretionary_spend_usd": round(safe_discretionary_limit / 30.0, 2),
            "liquidity_posture": "HEALTHY" if safe_discretionary_limit > 500.0 else "CONSTRAINED_LEAN"
        }

    def calculate_emergency_liquidity_buffer_days(
        self,
        liquid_cash_usd: float,
        daily_burn_usd: float,
        burn_trend_slope: float = 0.0
    ) -> Dict[str, Any]:
        """
        Calculates days of survival liquidity under zero-income emergency scenarios.
        """
        cash = max(0.0, float(liquid_cash_usd))
        burn = max(1.0, float(daily_burn_usd))

        # Days = cash / burn
        buffer_days = round(cash / burn, 1)

        return {
            "liquid_cash_usd": cash,
            "daily_burn_usd": burn,
            "emergency_liquidity_buffer_days": buffer_days,
            "buffer_in_months": round(buffer_days / 30.4, 1),
            "resilience_rating": "FORTRESS_TIER" if buffer_days >= 180 else ("SOLID_3_MONTH" if buffer_days >= 90 else "HIGH_VULNERABILITY")
        }
