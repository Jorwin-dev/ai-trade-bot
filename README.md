# ai-trade-bot
Financial Market Data Analysis & Automated Trading System

## Overview
This project implements an **AI-driven trading bot** that uses **machine learning and sentiment analysis** to automate stock trading decisions. The system integrates **FinBERT** for sentiment analysis of financial news, Alpaca API for live trading, and Lumibot for backtesting strategies.

## Tech Stack
- **Python** – Core development language
- **FinBERT** – Sentiment analysis for financial news
- **Alpaca API** – Real-time market data retrieval & order execution
- **Lumibot** – Backtesting trading strategies with historical market data
- **Yahoo Finance API** – Historical stock data for simulations

## Features
- **Sentiment Analysis:** Utilizes **FinBERT** to evaluate financial news sentiment (positive, negative, neutral).
- **Automated Trading:** Trades SPY ETF based on sentiment scores and confidence thresholds.
- **Position Sizing:** Dynamically calculates trade sizes based on account balance and risk tolerance.
- **Bracket Orders:** Implements stop-loss and take-profit risk management for each trade.
- **Backtesting:** Uses historical data to simulate strategy performance before deployment.
- **Live Trading Support:** Allows deployment to Alpaca for real-time trading.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/trading-bot.git
   cd trading-bot
   ```
2. Install dependencies:
   ```bash
   pip install transformers torch alpaca-trade-api lumibot
   ```
3. Set up Alpaca API credentials in `tradingbot.py`
4. Run the trading bot:
   ```bash
   python tradingbot.py
   ```

## How It Works
### **1. Sentiment Analysis with FinBERT**
The bot fetches financial news related to **SPY ETF** and determines its sentiment.
```python
from finbert_utils import estimate_sentiment
news = ["Markets reacted positively to earnings reports."]
probability, sentiment = estimate_sentiment(news)
print(probability, sentiment)  # Output: (0.98, "positive")
```

### **2. Trading Strategy**
- If sentiment is **positive** with high confidence, the bot buys SPY.
- If sentiment is **negative**, the bot sells SPY short.
- **Stop-loss & take-profit orders** are placed for risk management.
```python
if sentiment == "positive" and probability > .999:
    order = self.create_order("SPY", quantity, "buy", type="bracket",
                              take_profit_price=last_price*1.20,
                              stop_loss_price=last_price*0.95)
    self.submit_order(order)
```

### **3. Backtesting with Historical Data**
```python
strategy.backtest(
    YahooDataBacktesting,
    start_date=datetime(2020, 1, 1),
    end_date=datetime(2023, 12, 31),
    parameters={"symbol":"SPY", "cash_at_risk":0.5}
)
```

## Future Improvements
- Expand to multiple asset classes (crypto, forex, commodities).
- Implement reinforcement learning for strategy optimization.
- Enhance risk management using portfolio diversification.

## Contact
For inquiries or collaborations, reach out via [LinkedIn](https://www.linkedin.com/in/jorwinreyes/) or [GitHub](https://github.com/Jorwin-dev).
