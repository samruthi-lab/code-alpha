

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

portfolio = {}
total_investment = 0


n = int(input("How many different stocks do you have? "))

for _ in range(n):
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    quantity = int(input(f"Enter quantity for {stock}: "))
    
    if stock in stock_prices:
        value = stock_prices[stock] * quantity
        portfolio[stock] = value
        total_investment += value
    else:
        print(f"Price for {stock} not found!")

print("\n--- Portfolio Summary ---")
for stock, value in portfolio.items():
    print(f"{stock}: ${value}")
print(f"Total Investment: ${total_investment}")


save_choice = input("Save results to file? (y/n): ").lower()
if save_choice == 'y':
    with open("portfolio_summary.txt", "w") as file:
        for stock, value in portfolio.items():
            file.write(f"{stock}: ${value}\n")
        file.write(f"Total Investment: ${total_investment}\n")
    print("Portfolio saved to 'portfolio_summary.txt'")
