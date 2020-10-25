"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
"""

# O(nlogn)
def max_sub_arrary(array):
    m = 0
    for x in range(len(array)):
        for y in range(x+1, len(array)+1):
            m = max(m, sum(array[x:y]))

    return m

# O(n)
def max_sub_array(array):
    m, v = 0, 0
    for num in array:
        v = max(v+num, 0)
        m = max(m, v)

    return m

print(max_sub_array([34, -50, 42, 14, -5, 86]))
print(max_sub_array([-5, -1, -8, -9]))

assert max_sub_array([-5, -1, -8, -9]) == 0