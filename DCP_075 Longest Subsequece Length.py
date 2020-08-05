"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
"""

def longest_subsequence_length(sequence):
    lengths = []
    for num in sequence:
        length = 1
        pos = 0
        for p, v, a in lengths:
            if num > v:
                if a+1 > length:
                    length = a+1
                    pos = p
        lengths.append((pos, num, length))
    return max(lengths, key = lambda x: x[2])


print(longest_subsequence_length([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))


