#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from queue import Queue

# Given a 2D screen arr[][] where each arr[i][j] is an integer representing the color of that pixel,
# also given the location of a pixel (X, Y) and a color C, the task is to replace the color of the given
# pixel and all the adjacent same-colored pixels with the given color.

# https://www.geeksforgeeks.org/flood-fill-algorithm/
# BFS Approach: The idea is to use BFS traversal to replace the color with the new color.
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
#
# Time Complexity: O(m * n)
# Auxiliary Space: O(m * n)
#
# - Create an empty queue let’s say Q.
# - Push the starting location of the pixel as given in the input and apply the replacement color to it.
# - Iterate until Q is not empty and pop the front node (pixel position).
# - Check the pixels adjacent to the current pixel and push them into the queue if valid (had not been colored
#     with replacement color and have the same color as the old color).

# Returns true if the given pixel is valid
def is_valid(mtx, nx, ny, x, y, prev, new):
    if x < 0 or x >= nx or y < 0 or y >= ny or mtx[x][y] != prev or mtx[x][y] == new:
        return False
    return True


# FloodFill function
def flood_fill_bfs(mtx, nx, ny, x, y, prev, new):
    queue = []

    # Append the position of starting pixel of the component
    queue.append([x, y])

    # Color the pixel with the new color
    mtx[x][y] = new

    # While the queue is not empty i.e. the whole component having prev color is not colored with new color
    while queue:
        # Dequeue the front node
        currPixel = queue.pop()

        posX = currPixel[0]
        posY = currPixel[1]

        # Check if the adjacent pixels are valid
        if is_valid(mtx, nx, ny, posX + 1, posY, prev, new):
            # Color with newC if valid and enqueue
            mtx[posX + 1][posY] = new
            queue.append([posX + 1, posY])

        if is_valid(mtx, nx, ny, posX - 1, posY, prev, new):
            mtx[posX - 1][posY] = new
            queue.append([posX - 1, posY])

        if is_valid(mtx, nx, ny, posX, posY + 1, prev, new):
            mtx[posX][posY + 1] = new
            queue.append([posX, posY + 1])

        if is_valid(mtx, nx, ny, posX, posY - 1, prev, new):
            mtx[posX][posY - 1] = new
            queue.append([posX, posY - 1])


from typing import List, Tuple

# An Approach using DFS:
#
# Time Complexity: O(m * n)
# Auxiliary Space: O(m + n), due to the recursive call stack.
#
# - Change the color of the source row and source column with the given color
# - Do DFS in four direction
def flood_fill_dsf(mtx, nx, ny, x, y, prev, new):
    # Condition for checking out of bounds
    if x < 0 or x >= nx or y < 0 or y >= ny:
        return

    if mtx[x][y] != prev:
        return

    mtx[x][y] = new
    flood_fill_dsf(mtx, nx, ny, x - 1, y, prev, new)  # left
    flood_fill_dsf(mtx, nx, ny, x + 1, y, prev, new)  # right
    flood_fill_dsf(mtx, nx, ny, x, y + 1, prev, new)  # top
    flood_fill_dsf(mtx, nx, ny, x, y - 1, prev, new)  # bottom

if __name__ == "__main__":
    import time

    start_time = time.time()

    matrix = [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0],
        [1, 0, 0, 1, 1, 0, 1, 1],
        [1, 2, 2, 2, 2, 0, 1, 0],
        [1, 1, 1, 2, 2, 0, 1, 0],
        [1, 1, 1, 2, 2, 2, 2, 0],
        [1, 1, 1, 1, 1, 2, 1, 1],
        [1, 1, 1, 1, 1, 2, 2, 1],
    ]

    # Rows and columns, dimensions
    nx = len(matrix)
    ny = len(matrix[0])

    # Start coordinates provided by the user
    x = 4
    y = 4

    # Current color at that coordinate
    prev = matrix[x][y]
    # New color that has to be filled
    new = 3

    # flood_fill_bfs(matrix, nx, ny, x, y, prev, new)
    flood_fill_dsf(matrix, nx, ny, x, y, prev, new)

    # Printing the updated grid
    for i in range(nx):
        for j in range(ny):
            print(matrix[i][j], end=" ")
        print()

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")