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

    def __init__(self, name, market, price_history, volume):
        self.name = name
        market.add_asset(self)
        self.offers = []
        self.bids = []
        self.volume = volume
        self.price = price_history[-1]
        market.update_price(self)
        self.price_history = price_history

    def update_history(self, price):
        self.price_history.append(price)

    def get_volatility(self):
        return np.std(self.price_history)
    
    def add_offer(self, offer):
        self.offers.append(offer)

    def add_bid(self, bid):
        self.bids.append(bid)
    
class Derivative(Asset):
    
        def __init__(self, name, market, price_history, volume, underlying, pricing=None):
            super().__init__(name, market, price_history, volume)
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