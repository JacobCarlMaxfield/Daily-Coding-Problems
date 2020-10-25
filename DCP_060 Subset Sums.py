"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.
"""

from itertools import product

def subset_sums(lst):
    products = list(product([0, 1], repeat=len(lst)))
    for x in range(len(products)//2+1):
        o = sum([lst[a] if products[x][a] else 0 for a in range(len(lst))])
        t = sum([lst[a] if products[-x-1][a] else 0 for a in range(len(lst))])
        if o == t:
            return True
    return False

print(subset_sums([15, 5, 20, 10, 35, 15, 10]))
print(subset_sums([15, 5, 20, 10, 35]))