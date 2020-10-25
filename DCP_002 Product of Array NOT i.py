"""
This problem was asked by Uber.

Given an array of integers, return a new array
such that each element at index i of the new array
is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


import time


def product_of_array_not_i(nums):
    prod_array = [0] * len(nums)
    prod = 1
    for num in nums:
        if num == 0:
            continue
        prod *= num
    if nums.count(0) > 1:
        return prod_array
    if nums.count(0) == 1:
        prod_array[nums.index(0)] = prod
        return prod_array
    prod_array = []
    for number in nums:
        prod_array.append(prod//number)
    return prod_array
        


# original Idea
def product_of_array_not_i_no_division(arr):
    return_arr = []
    for i in range(len(arr)):
        total_product = 1
        for j in range(len(arr)):
            if i != j:
                total_product *= arr[j]
        return_arr.append(total_product)
    return return_arr


'''
def product_of_array_not_i_no_division(arr):
    return_arr = list(arr)
    for i in range(len(return_arr)):
        for j in range(len(return_arr)):
            if i != j:
                return_arr[i] *= arr[j]
    return return_arr

'''

t1a = time.time()
for a in range(1):
    product_of_array_not_i(list(range(1, 15000)))
t1b = time.time()

t2a = time.time()
for a in range(1):
    product_of_array_not_i_no_division(list(range(1, 1500)))
t2b = time.time()

print((t1b - t1a))
print((t2b - t2a))

