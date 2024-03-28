# Outline

## Market

- Holds the prices in the market
- updates prices and quantities
- tracks agent offers and bids
- can be observed by agent

## Agent

Observes the market and implements a strategy for trading\
**Requirements**
- Strategy
- Unique characteristics such as risk tolerance and assets
- Advantages/Disadvantages such as transaction speed
- Portfolio


## Strategy

The decision making rules for agents

### Portfolio management strategies

Sets rules for composition of agents portfolio, determines focus of trading strategies and vetos trades.

### Trading Strategies

**Budget Constrained Computation**
- Hard coded strategies with neoclassical models and stochasicity
- BSM
- random
- cointegration
- ...
**Goal Strategies**
- Utilizing deep learning to generate strategies

## Institutions

Represents market managers such as government agencies or market norms.
Set rules that trades and strategies must follow


## Shocks

Add randomness to markets to prevent equilibrium and no-trade
