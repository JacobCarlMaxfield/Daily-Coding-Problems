"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
"""

def matrix_paths(N, M):
    memo = [[False for x in range(M+1)] for y in range(N+1)]
    def paths(n, m):
        if n == 1 or m == 1:
            memo[n][m] = 1
        if memo[n][m]:
            return memo[n][m]
        memo[n][m] = paths(n-1, m) + paths(n, m-1)
        return memo[n][m]
    return paths(N, M)

print(matrix_paths(10, 10))