"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""

def perfect_number(n):
    pns = []
    x = 0
    while len(pns) < n:
        if sum([int(y) for y in str(x)]) == 10:
            pns.append(x)
        x += 1
    
    return pns[-1]

print(perfect_number(2))