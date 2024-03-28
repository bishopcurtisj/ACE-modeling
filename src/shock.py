from abc import ABC, abstractmethod
import numpy as np
from market import *
from institution import *
from agent import *
from strategy import *
from shock import *

class Shock:

    def __init__(self, severity=np.randint(-10,10)):
        self.name = ''
        self.severity = severity

    def set_severity(self, severity):
        self.severity=severity

    def random_shock(self):
        shocks = [] # list of shocks

    def new_agent(self):
        pass

    def new_asset(self):
        pass

    def institutional_shock(self, institution):
        pass

    def market_shock(self, market):
        pass

    def agent_shock(self, agent):
        pass

    def supply_shock(self, asset):
        pass

    def demand_shock(self, asset):
        pass

    def strategy_shock(self, agent, strategy):
        pass




