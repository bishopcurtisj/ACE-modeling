from abc import ABC, abstractmethod

class Institution(ABC):

    @abstractmethod
    def __init__(self, name, market, agents):
        self.market=market
        self.agents=agents
        self.name

    @abstractmethod
    # General market rules such max number of trades per time period
    def new_market_law(self):
        pass

    @abstractmethod
    # rules that set limits based on agent characteristics, i.e. max leverage, trades per time period, etc.
    def new_agent_law(self):
        pass
    
    @abstractmethod
    # rules that determine acceptable assets
    def new_portfolio_law(self):
        pass

    @abstractmethod
    # rules that determine acceptable trades
    def new_trading_law(self):
        pass

    @abstractmethod
    # Includes taxes, fees, etc.
    def new_transaction_costs(self):
        pass

    