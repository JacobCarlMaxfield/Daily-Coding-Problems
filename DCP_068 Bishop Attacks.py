"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

(0, 0)
(1, 2)
(2, 2)
(4, 0)
The board would look like this:

[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]
You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
"""

def bishop_attacks(M=0, bishops=None):
    b = bishops
    total = 0
    for b1 in range(len(b)):
        for b2 in range(b1+1, len(b)):
            if b1 == b2:
                continue
            if abs((b[b2][1]-b[b1][1])/(b[b2][0]-b[b1][0])) == 1:
                total += 1
    return total

print(bishop_attacks(bishops=[(0, 0),(1, 2),(2, 2),(4, 0)]))