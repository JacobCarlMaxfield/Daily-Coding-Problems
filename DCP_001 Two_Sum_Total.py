
"""
Good morning! Here's your coding interview problem for today.
This problem was recently asked by Google.
Given a list of numbers and a number k,
return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""


def two_sum_total_brute_force(arr, k):
    for x in range(len(arr)-1):
        for y in range(x+1, len(arr)):
            if arr[x] + arr[y] == k:
                return True
    return False


def two_sum_total(arr, k):
    seen_numbers = dict()
    for num in arr:
        if str(k - num) in seen_numbers:
            return True
        else:
            seen_numbers[str(num)] = k - num
    return False


print(two_sum_total(list(x for x in range(1, 10001)), 19999))
print(two_sum_total_brute_force(list(x for x in range(1, 10001)), 19999))
print(two_sum_total(list(x for x in range(1, 10000001)), 19999999))
