"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
"""
from pprint import pprint
import random


def get_unseen_neighbors(v, p):
    r, c = p
    neighbors = []
    dirs = [-1, 0, 1]
    for x in dirs:
        for y in dirs:
            if abs(x) != abs(y):
                if 0 <= r+x < len(v) and 0 <= c+y < len(v[0]):
                    if not v[r+x][c+y]:
                        v[r+x][c+y] = True
                        neighbors.append((r+x, c+y))
    return neighbors


def fill_visited(m, v, r, c):
    point_list = [(r, c)]
    while point_list:
        point = point_list.pop()
        for neighbor in get_unseen_neighbors(v, point):
            if m[neighbor[0]][neighbor[1]] == 1:
                point_list.append(neighbor)


def matrix_islands(matrix):
    pprint(matrix)
    visited = [[False for col in row] for row in matrix]
    islands = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if not visited[row][col]:
                if matrix[row][col] == 1:
                    islands += 1
                    fill_visited(matrix, visited, row, col)
                visited[row][col] = True
    return islands


print(matrix_islands([[1, 0, 0, 0, 0],
                      [0, 0, 1, 1, 0],
                      [0, 1, 1, 0, 0],
                      [0, 0, 0, 0, 0],
                      [1, 1, 0, 0, 1],
                      [1, 1, 0, 0, 1]]))

print(matrix_islands([[random.randint(0, 1)
                       for x in range(10)] for y in range(10)]))
