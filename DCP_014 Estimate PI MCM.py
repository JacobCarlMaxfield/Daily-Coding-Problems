"""
This problem was asked by Google.

The area of a circle is defined as πr^2. 
Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""
import random

attempts = 0
hits = 0

while attempts < 100000:
    dart = (random.random(), random.random())
    attempts += 1
    if dart[0]**2 + dart[1]**2 <= 1:
        hits += 1
print(4*hits/attempts)

