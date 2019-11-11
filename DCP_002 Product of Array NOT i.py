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


def product_of_array_not_i(arr):
    total_product = 1
    for num in arr:
        total_product *= num
    return_array = []
    for i in range(len(arr)):
        return_array.append(total_product // arr[i])
    return return_array


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
    product_of_array_not_i(list(x for x in range(1, 500)))
t1b = time.time()

t2a = time.time()
for a in range(1):
    product_of_array_not_i_no_division(list(x for x in range(1, 500)))
t2b = time.time()

print((t1b - t1a))
print((t2b - t2a))

print(product_of_array_not_i(list(x for x in range(1, 5))))
print(product_of_array_not_i_no_division(list(x for x in range(1, 5))))

