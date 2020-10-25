"""
Good morning! Here's your coding interview problem for today.

This question was asked by Google.

Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).
"""
import random


def uniform_not_in_list(n, l):
    while True:
        r = random.randint(0, n-1)
        if r not in l:
            return r
