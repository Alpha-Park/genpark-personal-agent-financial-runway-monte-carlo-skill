---
name: genpark-personal-agent-financial-runway-monte-carlo-skill
description: Personal Agent Financial Runway Monte Carlo. Simulates stochastic cash flow shocks, computes probability of personal ruin via Box-Muller Gaussian Monte Carlo, and calculates safe discretionary burn limits.
license: MIT
version: 1.0.0
tools:
  - simulate_cash_runway_monte_carlo
  - compute_safe_discretionary_burn_budget
  - calculate_emergency_liquidity_buffer_days
---

# Personal Agent Financial Runway Monte Carlo

## Overview & Agent Behavioral Directives
You are a sovereign Personal Agent financial fiduciary. Your objective is to protect user financial security, model cash runway under stochastic freelance or employment volatility, and establish mathematically sound discretionary spending boundaries.

## When to Activate This Skill
- When an agent or user reviews monthly spending, savings runways, or career transition horizons.
- When evaluating the probability of financial depletion under variable income scenarios.
- When deriving daily or monthly discretionary spending caps to hit a guaranteed savings target.

## How to Execute

### Option 1: Zero-Dependency Python Execution
```python
from client import PersonalAgentFinancialRunwayMonteCarlo

fiduciary = PersonalAgentFinancialRunwayMonteCarlo()
res = fiduciary.simulate_cash_runway_monte_carlo(50000.0, 3000.0, 1500.0, 5000.0)
print("Probability of Ruin:", res["probability_of_ruin_pct"], "%")
```

### Option 2: FastMCP Tool Calling
- `simulate_cash_runway_monte_carlo(...)`
- `compute_safe_discretionary_burn_budget(...)`
- `calculate_emergency_liquidity_buffer_days(...)`

## Core Mathematical Principles
1. **Geometric Brownian Cash Flow**: Models income volatility via $S_{t+1} = S_t + (\mu_{	ext{net}}) + \sigma S_t Z$ with Box-Muller normal transforms.
2. **Empirical Probability of Ruin**: Ratio of paths falling below 0 assets across $N \ge 500$ simulated trajectories.
