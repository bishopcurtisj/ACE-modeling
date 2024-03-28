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



# TODO:

## main

- Initialize agents
- - Come up with complete agents, implement backwards. ie Firm1 low risk tolerance, medium funds
- Finish initializing assets (25%)
- Implement one market time period

## Agent

- Portfolio tracker
- - Novel Object or numpy
- add function to post bid/offer

## Strategy

### Trading Strategies
- Choose initial strategies to implement
- - ETS, BSM, Naive, Random Walk
- Determine outputs of buy/sell
- - trade object?

### Portfolio Strategies
- Choose strategies for initial agents

## Market

## Institution
- add market level rules, low priority

## Shock
- implement different shock types

