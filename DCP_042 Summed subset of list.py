"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""

from itertools import combinations

def find_sum_subset(s, k):
    for ammount in range(1, len(s)+1):
        for comb in combinations(s, ammount):
            if sum(comb) == k:
                return comb
    return None

print(find_sum_subset([12, 1, 61, 5, 9, 2], 24))