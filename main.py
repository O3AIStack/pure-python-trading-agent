# main.py

from trader import Trader
from price_simulator import get_simulated_price

def parse_command(command):
    # Basic structure: "Buy 5 shares of AAPL if price < 170"
    try:
        action = "buy" if "buy" in command.lower() else "sell"
        parts = command.lower().split()
        qty_index = parts.index(action) + 1
        quantity = int(parts[qty_index])
        ticker = parts[qty_index + 3].upper()
        condition_sign = "<" if "<" in command else ">"
        target_price = float(command.split(condition_sign)[-1].strip())
        return {
            "action": action,
            "quantity": quantity,
            "ticker": ticker,
            "condition": condition_sign,
            "target_price": target_price
        }
    except Exception as e:
        print(f"⚠️ Could not parse command: {e}")
        return None

def evaluate_trade(trader, trade):
    current_price = get_simulated_price(trade["ticker"])
    print(f"📊 Current {trade['ticker']} price: ${current_price:.2f}")

    condition_met = (
        trade["condition"] == "<" and current_price < trade["target_price"]
    ) or (
        trade["condition"] == ">" and current_price > trade["target_price"]
    )

    if condition_met:
        if trade["action"] == "buy":
            trader.buy(trade["ticker"], trade["quantity"], current_price)
        else:
            trader.sell(trade["ticker"], trade["quantity"], current_price)
    else:
        print("🚫 Condition not met. No action taken.\n")

def main():
    trader = Trader()
    print("💰 Pure Python Trading Agent (Simulation)")
    print("Type trade commands like: 'Buy 10 shares of AAPL if price < 150'\n")

    while True:
        user_input = input("🧠> ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Exiting.")
            break
        trade = parse_command(user_input)
        if trade:
            evaluate_trade(trader, trade)
        print("---")

if __name__ == "__main__":
    main()
