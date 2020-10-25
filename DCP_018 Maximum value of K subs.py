"""
This problem was asked by Google.

Given an array of integers and a number k, 
where 1 <= k <= length of the array, 
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3,
we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. 
You can modify the input array in-place 
and you do not need to store the results. 
You can simply print them out as you compute them.
"""
import random
def max_k(arr, k):
    if len(arr) <= k:
        print(max(arr))
        return
    current = arr[:k]
    begin = 1
    end = k+1
    while len(current) == k:
        print(max(current))
        current = arr[begin:end]
        begin += 1
        end += 1

max_k(list(random.random() for _ in range(100)), 10)