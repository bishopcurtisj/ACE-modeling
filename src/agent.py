from abc import ABC, abstractmethod
from strategy import Portfolio_Strategy, Trading_Strategy
from market import *
from institution import *

class Agent:

    def __init__(self, name, portfolio_strategy, trading_strategy, portfolio, cash):
        self.name = name
        self.portfolio_strategy = portfolio_strategy
        self.trading_strategy = trading_strategy
        self.portfolio = portfolio
        self.leverage = 0

    def change_strategy(self, portfolio_strategy=None, trading_strategy=None):
        if portfolio_strategy is not None:
            self.portfolio_strategy = portfolio_strategy
        if trading_strategy is not None:
            self.trading_strategy = trading_strategy

    ## Updates assets, cash, leverage, interest/dividend accrual etc.
    def update_portfolio(self):
        pass

    def update_cash(self):
        pass

    def update_leverage(self):
        pass

    def trade(self, market):
        trades=(self.trading_strategy.buy(market), self.trading_strategy.sell(market))
        for trade in trades:
            ## Check if trade meets institution and portfolio strategy requirments
            if True:
                market.trade(trade)
                self.update_portfolio()
            else:
                self.update_portfolio()