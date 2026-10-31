# genpark-personal-agent-financial-runway-monte-carlo-skill

![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Dependencies](https://img.shields.io/badge/dependencies-zero-success)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

GenPark Personal Agent Financial Runway Monte Carlo provides zero-dependency personal finance modeling, simulating stochastic income shocks and deriving safe discretionary burn caps.

```mermaid
flowchart TD
    A[Liquid Assets & Fixed/Variable Burn] --> B[Box-Muller Gaussian Stochastic Generator]
    B --> C[500-Path Monte Carlo Runway Simulation]
    C --> D[Empirical Probability of Ruin & P10 Wealth]
    E[Target Horizon & Reserve Floors] --> F[Safe Discretionary Burn Budget Calculator]
    D & F --> G[Personal Financial Fiduciary Plan]
```

## Features
- **Monte Carlo Runway Simulation**: Evaluates 500 stochastic paths incorporating income volatility.
- **Safe Discretionary Burn Budget**: Recommends daily and monthly spending caps to preserve runway.
- **Emergency Liquidity Buffer**: Quantifies zero-income survival days and resilience tiers.

## Quickstart

```python
from client import PersonalAgentFinancialRunwayMonteCarlo

fiduciary = PersonalAgentFinancialRunwayMonteCarlo()
res = fiduciary.compute_safe_discretionary_burn_budget(60000.0, 2500.0, 12)
print("Safe Daily Spend:", res["safe_daily_discretionary_spend_usd"])
```

## FastMCP Integration

```bash
python -m genpark-personal-agent-financial-runway-monte-carlo-skill.mcp_server
```

## License
MIT
