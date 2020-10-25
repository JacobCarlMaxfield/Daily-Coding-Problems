"""
This problem was asked by Facebook.

You are given an array of non-negative integers that represents a two-dimensional elevation map
where each element is unit-width wall and the integer is the height.
Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second,
and 3 in the fourth index (we cannot hold 5 since it would run off to the left),
so we can trap 8 units of water.
"""

def water_pipes(pipes):
    if len(pipes) < 3:
        return 0
    total = 0
    
    high = pipes[0]
    pipes_included = []
    x = max(pipes[1:])
    for pipe in pipes[1:]:
        if x <= high:
            high = max(pipes[1:])
        if pipe >= high:
            total += (high * len(pipes_included)) - sum(pipes_included)
            pipes_included = []
        else:
            pipes_included.append(pipe)
    
    return total


print(water_pipes([7, 0, 1, 3, 6, 5]))
print(water_pipes([2, 1, 2]))
print(water_pipes([6]))