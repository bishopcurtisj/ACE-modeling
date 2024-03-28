import numpy as np
import scipy.stats as stats


class Market:

    def __init__(self):
        self.assets = []
        self.prices = {}
        self.trades = []
        

    def update_price(self, asset):
        self.prices[asset] = asset.price


    def get_price(self, asset):
        return self.prices[asset]
    
    def add_asset(self, asset):
        self.assets.append(asset)
        self.prices[asset] = asset.price

    def set_agent_rank(self, agent):
        pass

    def trade(self,Trade):
        self.trades.append(Trade)
        self.update_price(Trade.asset)
    

class Asset:

    def __init__(self, name, market, price_history, classification ,volume, dividend=0, interest=0):
        self.name = name
        market.add_asset(self)
        self.offers = []
        self.bids = []
        self.volume = volume
        self.price = price_history[-1]
        market.update_price(self)
        self.price_history = price_history
        self.dividend = dividend
        self.interest = interest
        self.classification = classification

    def set_dividend(self, dividend, random=False):
        if random:
            self.dividend = np.random.exponential(dividend)
        else:
            self.dividend = dividend

    def set_interest(self, interest, random=False):
        if random:
            self.interest = np.random.exponential(interest)
        else:
            self.interest = interest

    def update_history(self, price):
        self.price = price
        self.price_history.append(price)

    def get_volatility(self):
        return np.std(self.price_history)
    
    def add_offer(self, offer):
        self.offers.append(offer)

    def add_bid(self, bid):
        self.bids.append(bid)
    
class Derivative(Asset):
    
        def __init__(self, name, market, price_history, volume, underlying, dividend=0, interest=0, pricing=None):
            super().__init__(name, market, price_history,'Derivative' ,volume, dividend, interest)
            self.underlying = underlying
            self.pricing = pricing
    
        def calculate_price(self):
            self.pricing(self.underlying)

class Trade:

    def __init__(self, asset, buyer, seller, price, quantity):
        self.asset = asset
        self.buyer = buyer
        self.seller = seller
        self.price = price
        self.quantity = quantity

        asset.update_history(price)