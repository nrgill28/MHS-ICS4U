"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_07_StockExchange.py
Description:
    Calculates things from Joe's stock market adventure
History . .:
    2/5/2020 - Created File
"""

# Constants
stocks = 2000
buy_price = 40
sell_price = 42.75
commission = 0.03

# Calculations
spent = stocks * buy_price
stockbroker1 = spent * commission

# Print
print("Joe paid $%.2f for the stocks, and paid $%.2f in commissions." % (spent, stockbroker1))

# More calculations
gained = stocks * sell_price
stockbroker2 = gained * commission
revenue = gained - spent
costs = stockbroker1 + stockbroker2
profit = revenue - costs

# Print
print("Joe sold his stocks for $%.2f, and paid another $%.2f in commissions" % (gained, stockbroker2))
print("Joe made $%.2f in revenue, and after paying $%.2f in commissions, his profit was $%.2f" %
      (revenue, costs, profit))
if profit > 0:
    print("Joe made a profit!")
else:
    print("Joe lost money")
