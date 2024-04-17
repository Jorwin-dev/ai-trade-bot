from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies.strategy import Strategy
from lumibot.traders import trader
from datetime import datetime

API_KEY = ""
API_SECRET = ""
BASE_URL = ""

ALPACA_CREDS = {
    "API_KEY": API_KEY,
    "API_SECRET": API_SECRET,
    "PAPER": True
}

class MLTrader(Strategy):
    # BI-Cycle Methods
    def initialize(self): # Runs once
        pass
    def on_trading_iteration(self): # Runs everytime we get new data
        pass

start_date = datetime(2023, 12, 15)
end_date = datetime(2023, 12, 31)
broker = Alpaca(ALPACA_CREDS)
strategy = MLTrader(name='mlstrat', broker=broker, parameters={})

strategy.backtest(
    YahooDataBacktesting,
    start_date,
    end_date,
    parameters={}
)