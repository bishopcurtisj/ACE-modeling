from abc import ABC, abstractmethod

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

class Trading_Strategy(ABC):
    
    
    @abstractmethod
    def buy(self):
        pass

    @abstractmethod
    def sell(self):
        pass