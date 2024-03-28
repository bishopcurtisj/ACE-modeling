from abc import ABC, abstractmethod
import numpy as np
from market import *
from institution import *
from agent import *
from strategy import *
from shock import *

class Shock(ABC):

    def __init__(self, severity=np.randint(-10,10)):
        self.severity = severity

    def set_severity(self, severity):
        self.severity=severity

class Random_shock(Shock):
        shocks = [] # list of shocks
        ## I'm not sure if this works
        np.random.choice(shocks)

class New_agent(Shock):
    def __init__():
        super().__init__() 


class New_asset(Shock):
    def __init__():
        super().__init__()

class Institutional_shock(Shock):
        def __init__(self, institution , severity=np.randint(-10,10)):
            super().__init__(severity)
            self.institution = institution


class Market_shock(Shock):
        def __init__(self, market, severity=np.randint(-10,10)):
            super().__init__(severity)
            self.market = market

class Agent_shock(Shock):
        def __init__(self, agent, severity=np.randint(-10,10)):
            super().__init__(severity)
            self.agent = agent

class Supply_shock(Shock):
        def __init__(self, severity=np.randint(-10,10), asset=None):
            super().__init__(severity)
            self.asset = asset

class Demand_shock(Shock):
        def __init__(self, severity=np.randint(-10,10), asset=None):
            super().__init__(severity)
            self.asset = asset

class Strategy_shock(Shock):
        def __init__(self, agent, strategy, severity=np.randint(-10,10)):
            super().__init__(severity)
            self.agent = agent
            self.strategy = strategy




