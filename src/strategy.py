from abc import ABC, abstractmethod
import scipy.stats as stats

class Portfolio_Strategy(ABC):
    
    @abstractmethod
    def risk_management(self):
        pass

    @abstractmethod
    def diversification(self):
        pass

    @abstractmethod
    @property
    def assets_of_interest(cls):
        raise NotImplementedError
    
    @abstractmethod
    @property
    def portfolio(cls):
        raise NotImplementedError
    
    def evaluate_trade(self, trade):
        if self.risk_management(trade, trade.asset.price) & self.diversification(trade):
            return True
        else:
            return False

class Trading_Strategy(ABC):
    
    
    @abstractmethod
    def buy(self):
        pass

    @abstractmethod
    def sell(self):
        pass


class Naive(Portfolio_Strategy):

    def __init__(self, portfolio, assets_of_interest=None):
        self.assets_of_interest = assets_of_interest
        self.portfolio = portfolio

    def risk_management(self, trade, pred_dist):
        risk_tol=0.3
        if stats.ppf(pred_dist, trade.asset.price) < risk_tol:
            return True
        else:
            return False

    def diversification(self, trade, portfolio):
        if trade.asset in portfolio:
            return False
        else:
            return True
        
    def evaluate_trade(self, trade):
        return super().evaluate_trade(trade)
        


    