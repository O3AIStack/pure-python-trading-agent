# 📈 Pure Python Trading Agent (Simulation Only)

This project is a lightweight **stock trading simulator** powered by AI-style prompts and written entirely in **pure Python**—no frameworks, no real money, just logic, input, and learning.

It’s part of the [Pure Python AI Agent Series](https://o3aistack.com/pure-python-ai-agent-series), built to demonstrate how flexible and powerful simple Python code can be when applied to real-world tasks.

---

## 🚀 What It Does

- Accepts natural-language trading commands:
Buy 5 shares of AAPL if price < 170
Sell 2 shares of TSLA if price > 220

- Uses a **price simulator** to generate realistic stock prices
- Evaluates trade conditions
- Simulates buy/sell orders and updates a **virtual portfolio**
- Prints actions taken with log-style updates

> ✅ This is a 100% offline simulation—**no actual funds, accounts, or APIs are used**.

---

## 🧠 Why Use This?

- Learn the basics of algorithmic thinking in trading
- Explore prompt-to-action logic in a real use case
- Practice managing portfolios and price lookups
- Extend it into a more complex AI-driven trading lab

---

## 🗂️ File Structure

pure-python-trading-agent/
├── main.py # Prompt loop and trade logic
├── trader.py # Portfolio state, logic for buys/sells
├── price_simulator.py # Simulated price generator
├── config.py # Balance, limits, etc.
├── requirements.txt
└── README.md


---

> Buy 10 shares of MSFT if price < 280
🟢 Current MSFT price: $276.42
✅ Bought 10 shares of MSFT at $276.42

---

## 🛠️ Setup

```bash
git clone https://github.com/your-username/pure-python-trading-agent.git
cd pure-python-trading-agent
pip install -r requirements.txt
python main.py

