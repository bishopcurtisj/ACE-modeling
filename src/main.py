from market import *
from institution import *
from agent import *
from strategy import *
from shock import *
import numpy as np
import scipy.stats as stats

## Generate historical pricing data
## 252 trading days in a year, 10 years of data
size=2520
gold_price = np.random.normal(1000, 100, size)
silver_price = np.random.normal(20, 20, size)
bronze_price = np.random.exponential(10, size)
platinum_price = np.random.normal(10_000, 10, size)
bond_price = np.random.normal(100, 1, size)


## Create a market
market = Market()

## Add assets to the market

## Create agents


## Simulate trading for N time steps, adding a shock every T time steps
N = 10_000
T = N//10
shocks = Shock()
for i in range(N):
    if i % T == 0:
        # Add a shock to the market
        shocks.set_severity(np.random.randint(-10,10))
        shocks.random_shock()
    # Simulate trading
    pass