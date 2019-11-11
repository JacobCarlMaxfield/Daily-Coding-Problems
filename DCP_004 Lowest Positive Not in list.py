"""
This problem was asked by Stripe.

Given an array of integers,
find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, The input [3, 4, -1, 1] should give 2.
             The input [1, 2, 0]     should give 3.
"""


# [-1, 1, 3, 4] => 2
def lowest_positive_not_in_list(arr):
    arr.sort()
    nc = 0
    for num in arr:
        if num < 1 or num == nc:
            continue
        if num - nc > 1:
            return nc + 1
        nc += 1
    return max(arr[-1] + 1, 1)


print(lowest_positive_not_in_list([3, 4, -1, 1]))
