#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from queue import Queue


def create_maze(dim):
    # Create a grid filled with walls
    maze = np.ones((dim * 2 + 1, dim * 2 + 1), dtype=int)

    # Define the starting point
    x, y = (0, 0)
    maze[2 * x + 1, 2 * y + 1] = 0

    # Initialize the stack with the starting point
    stack = [(x, y)]
    while len(stack) > 0:
        x, y = stack[-1]

        # Define possible directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and nx < dim and ny < dim and maze[2 * nx + 1, 2 * ny + 1] == 1:
                maze[2 * nx + 1, 2 * ny + 1] = 0
                maze[2 * x + 1 + dx, 2 * y + 1 + dy] = 0
                stack.append((nx, ny))
                break
        else:
            stack.pop()

    # Create an entrance and an exit
    maze[1, 0] = 0
    maze[-2, -1] = 0

    return maze

def find_path(maze, d):
    # BFS algorithm to find the shortest path
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = (4, 0)
    # end = (maze.shape[0]-1, maze.shape[1]-1)
    visited = np.zeros_like(maze, dtype=bool)
    visited[start] = True
    queue = Queue(1000)
    queue.put((start, []))
    i = 0
    while not queue.empty():
        (node, path) = queue.get()
        next_node = (node[0] + d[0], node[1] + d[1])
        print((node, path), next_node, i, d, queue.qsize())
        # # if (next_node == end):
        # #     return path + [next_node]
        if (next_node[0] >= 0 and next_node[1] >= 0 and
            next_node[0] < maze.shape[0] and next_node[1] < maze.shape[1]):

            visited[next_node] = True
            queue.put((next_node, path + [next_node]))
            if d == dirs[0]:
                if maze[next_node] == 1:
                    d = dirs[1] # bottom
                    d = dirs[3] # top
                elif maze[next_node] == 2:
                    pass
                elif maze[next_node] == 3:
                    d = dirs[1]     # bottom
                elif maze[next_node] == 4:
                    d = dirs[3]
            elif d == dirs[2]:
                if maze[next_node] == 1:
                    d = dirs[1]  # bottom
                    d = dirs[3]  # top
                elif maze[next_node] == 2:
                    pass
                elif maze[next_node] == 3:
                    d = dirs[3] # top
                elif maze[next_node] == 4:
                    d = dirs[1]  # bottom
            elif d == dirs[1]:
                if maze[next_node] == 1:
                    pass
                elif maze[next_node] == 2:
                    d = dirs[0]  # right
                    d = dirs[2]  # left
                elif maze[next_node] == 3:
                    d = dirs[0]
                elif maze[next_node] == 4:
                    d = dirs[2]
            elif d == dirs[3]:
                if maze[next_node] == 1:
                    pass
                elif maze[next_node] == 2:
                    d = dirs[0]  # right
                    d = dirs[2]  # left
                elif maze[next_node] == 3:
                    d = dirs[2]  # left
                elif maze[next_node] == 4:
                    d = dirs[0]  # right
        else:
            if next_node[0] < 0:
                d = dirs[1]
            elif next_node[1] < 0:
                d = dirs[0]
            elif next_node[0] >= maze.shape[0]:
                d = dirs[3]
            elif next_node[1] >= maze.shape[1]:
                d = dirs[2]
            # queue.put((next_node, path))
        print(next_node, d)
        if i == 50:
            break
        i += 1
    print(visited)
    return 0

def advent_a(arr):
    tot = 0

    input = list()
    for item in arr:
        input.append(list(item.replace("|", "1").replace("-", "2").
                          replace("\\", "3").replace("/", "4").replace(".", "0")))
    grid = np.array(input).astype(int)
    print(grid)
    print(np.shape(grid))

    # maze = create_maze(10)
    # print(maze)

    d = (0, 1)
    find_path(grid, d)


    return tot


def advent_b(arr):
    tot = 0

    input = list()
    for item in arr:
        input.append(list(item.replace("#", "2").replace(".", "0").replace("O", "1")))

    i = 0

    return tot


if __name__ == "__main__":
    import time

    start_time = time.time()
    # Production part b is wrong after refactoring
    test = True
    if test:
        with open('inputs/input_16_test.txt') as f:
            lines = [line.rstrip() for line in f]
        pass
    else:
        input = list()
        with open("inputs/input_16.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    print(advent_a(lines))
    print(advent_b(lines))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
