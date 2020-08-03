"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""
import random

def shuffle(deck):
    for x in range(len(deck)):
        r = random.randint(0, len(deck)-1)
        deck[x], deck[r] = deck[r], deck[x]
    
    return deck

deck = list(range(1, 53))

print(shuffle(deck))