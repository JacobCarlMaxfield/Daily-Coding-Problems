"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Two Sigma.

Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).
"""

import random

def rand(x):
    return random.randint(1, x)

print(rand(7))