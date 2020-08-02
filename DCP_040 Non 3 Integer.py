"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""

from collections import defaultdict

def no_3(integer_list):
    n = defaultdict(int)
    for i in integer_list:
        n[i] += 1
    
    for x in n:
        if n[x] == 1:
            return x

print(no_3([6, 1, 3, 3, 3, 6, 6]))
print(no_3([13, 19, 13, 13]))