"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
"""

def spiral_print(matrix):
    if len(matrix) == 1:
        return matrix[0]
    visited = [[False for x in range(len(matrix[0]))] for y in range(len(matrix))]
    x = 0
    y = 0
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dd = 0
    count = 0
    while True:
        print(matrix[x][y])
        visited[x][y] = True
        while count < 4:
            try:
                if not visited[x+d[dd][0]][y+d[dd][1]]:
                    x += d[dd][0]
                    y += d[dd][1]
                    count = 0
                    break
                else:
                    count += 1
                    dd += 1
                    if dd == 4:
                        dd = 0

            except IndexError:
                count += 1
                dd += 1
                if dd == 4:
                    dd = 0
        else:
            break
    

spiral_print([[1,  2,  3,  4,  5],
              [6,  7,  8,  9,  10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20]])