from abc import ABC, abstractmethod
from strategy import Portfolio_Strategy, Trading_Strategy

class Agent(ABC):

    @abstractmethod
    def __init__(self, name, portfolio_strategy, trading_strategy, portfolio, cash):
        self.name = name
        self.portfolio_strategy = portfolio_strategy
        self.trading_strategy = trading_strategy
        self.portfolio = portfolio
