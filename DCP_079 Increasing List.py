"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given an array of integers, write a function to determine whether the array 
could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, 
since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, 
since we can't modify any one element to get a non-decreasing array.

"""
import numpy as np
def increasing_list(l):
    count = 0
    for x in range(len(l)-1):
        if l[x] > l[x+1]:
            count += 1
    return count <= 1
     

print(increasing_list([10, 5, 7]))

print(increasing_list([10, 5, 1]))

for _ in range(10):
    t = np.random.randint(low=10, size=4)
    print(t, increasing_list(t))