# trader.py

class Trader:
    def __init__(self):
        self.balance = 10_000.00  # Starting virtual cash
        self.portfolio = {}  # e.g., {"AAPL": {"quantity": 5, "avg_price": 140.00}}

    def buy(self, ticker, quantity, price):
        total_cost = quantity * price
        if total_cost > self.balance:
            print(f"❌ Not enough funds to buy {quantity} shares of {ticker}. Needed: ${total_cost:.2f}, Available: ${self.balance:.2f}")
            return
        self.balance -= total_cost
        position = self.portfolio.get(ticker, {"quantity": 0, "avg_price": 0})
        new_quantity = position["quantity"] + quantity
        new_avg_price = ((position["quantity"] * position["avg_price"]) + total_cost) / new_quantity
        self.portfolio[ticker] = {
            "quantity": new_quantity,
            "avg_price": new_avg_price
        }
        print(f"✅ Bought {quantity} shares of {ticker} at ${price:.2f} — New Balance: ${self.balance:.2f}\n")

    def sell(self, ticker, quantity, price):
        position = self.portfolio.get(ticker)
        if not position or position["quantity"] < quantity:
            print(f"❌ Not enough shares to sell {quantity} of {ticker}")
            return
        total_gain = quantity * price
        self.balance += total_gain
        position["quantity"] -= quantity
        if position["quantity"] == 0:
            del self.portfolio[ticker]
        else:
            self.portfolio[ticker] = position
        print(f"✅ Sold {quantity} shares of {ticker} at ${price:.2f} — New Balance: ${self.balance:.2f}\n")
