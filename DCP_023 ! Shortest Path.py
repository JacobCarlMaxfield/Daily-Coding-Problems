"""
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. 
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, 
return the minimum number of steps required to reach the end coordinate from the start. 
If there is no possible path, then return null. You can move up, left, down, and right. 
You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), 
the minimum number of steps required to reach the end is 7, 
since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
"""

def shortestPath(cell, grid, ec):
    grid, visited_grid = inverseGrid(grid)
    max_size = len(grid) * len(grid[0])
    steps = calculatePath(cell, grid, visited_grid, ec)
    if steps < max_size:
        return steps
    else:
        return None

def calculatePath(sc, grid, visited, ec):
    max_size = len(grid) * len(grid[0])
    cell_list = [ec]
    while len(cell_list):
        current_node = cell_list.pop()
        i = current_node[0]
        j = current_node[1]
        




def inverseGrid(grid):
    new_grid = []
    visited_grid = []
    for x in range(len(grid)):
        row = []
        visited_row = []
        for y in range(len(grid[x])):
            row.append(not grid[x][y])
            visited_row.append(False)
        new_grid.append(row)
        visited_grid.append(visited_row)
    return new_grid, visited_grid


grid = [[False, False, False, False], 
        [True, True, False, True], 
        [False, False, False, False], 
        [False, False, False, False]]

print(shortestPath((3, 0), grid, (0, 0)))