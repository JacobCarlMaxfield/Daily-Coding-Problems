"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""
from itertools import combinations
from operator import mul
from functools import reduce

def list_product(lst, k=3):
    total = 0
    for comb in combinations(lst, k):
        total = max(reduce(mul, comb), total)

    return total

print(list_product([-10, -10, 5, 2]))