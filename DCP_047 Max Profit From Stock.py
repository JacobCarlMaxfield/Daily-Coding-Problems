"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in chronological order, 
write a function that calculates the maximum profit you could have made from buying and selling that stock once. 
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""

def max_profit(stock_prices):
    profit = 0
    for x in range(len(stock_prices)):
        for y in range(x+1, len(stock_prices)):
            profit = max(profit, stock_prices[y] - stock_prices[x])

    return profit

print(max_profit([9, 11, 8, 5, 7, 10]))