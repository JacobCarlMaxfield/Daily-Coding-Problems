"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

You have an N by N board. 
Write a function that, given N, returns the number of possible arrangements of the board 
where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.
"""

from copy import deepcopy


def queens_path(N, a, b):
    directions = [-1, 0, 1]
    for x in directions:
        for y in directions:
            if x == y == 0:
                continue
            ax = a + x
            by = b + y
            while 0 <= ax < N and 0 <= by < N:
                yield ax, by
                ax += x
                by += y

def max_queens(N):
    grid = [[False for x in range(N)] for _ in range(N)]
    grids = []

    numbers = [_ for _ in range(N)]

    x_last = N
    y_last = N

    current_x = 0
    while current_x < x_last:
        current_y = 0
        while current_y < y_last:
            current_grid = deepcopy(grid)
            queens = 0
            for x in numbers[current_x:] + numbers[:current_x]:
                for y in numbers[current_y:] + numbers[:current_y]:
                    if not current_grid[x][y]:
                        queens += 1
                        current_grid[x][y] = 'Q'
                        for a, b in queens_path(N, x, y):
                            current_grid[a][b] = ' '
            if queens == N:
                if current_grid not in grids:
                    grids.append(current_grid)
            current_y += 1
        current_x += 1
    return len(grids)
    
for n in range(100):
    print(n, max_queens(n))