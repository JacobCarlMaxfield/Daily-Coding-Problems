"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Jane Street.

Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantities.
"""

from operator import mul
from functools import reduce


# I think this works
def exchange_rate(grid):
    cross = []
    for x in range(len(grid)):
        temp = [grid[x][x]]
        for y in range(x):
            temp.append(grid[x][y])
            temp.append(grid[y][x])
        cross.append(reduce(mul, temp))

    print(*grid, sep='\n')
    print()
    print(cross)
    print()
    return len(set(cross)) != 1



print(exchange_rate([[1.0, 1.0, 2.0], 
                     [1.0, 1.0, 1.0], 
                     [0.5, 1.0, 1.0]]))
