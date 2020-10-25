"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""

def subsets_of_set(s):
    set_list = list(s)
    subsets = []
    for x in range(len(s)):
        for y in range(x+1, len(s)+1):
            subsets.append(set(set_list[x:y]))
    return sorted(subsets, key=len)

print(subsets_of_set({1, 2, 3}))