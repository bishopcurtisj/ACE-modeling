from market import *
from institution import *
from agent import *
from strategy import *
from shock import *
import numpy as np
import scipy.stats as stats

## Generate historical pricing data



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