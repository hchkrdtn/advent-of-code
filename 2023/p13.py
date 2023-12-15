#!/usr/bin/env python3

import numpy as np


def line(grid, line):
    up = line - 1
    down = line
    flag = False
    while up >= 0 and down < np.shape(grid)[0]:
        # print(grid[0], line, grid[up], grid[down], np.array_equal(grid[up], grid[down]))
        if not np.array_equal(grid[up], grid[down]):
            return False
        up -= 1
        down += 1
    return True


def line_b(grid, line):
    up = line - 1
    down = line
    while up >= 0 and down < np.shape(grid)[0]:
        # print(grid[0], line, grid[up], grid[down], np.array_equal(grid[up], grid[down]))
        if not np.array_equal(grid[up], grid[down]):
            smudge = np.where((grid[up] - grid[down]) != 0)
            # print(smudge)
            if len(smudge[0]) == 1:
                # print(smudge)
                if grid[up, smudge[0][0]] == 1:
                    grid[up, smudge[0][0]] = 0
                else:
                    grid[up, smudge[0][0]] = 1
                return grid.copy()
            # # [1 0 0 0 0 0 0 0 0]
        up -= 1
        down += 1
    return None


def pattern(grid):
    dim = np.shape(grid)[0]
    for y in range(1, dim):
        # print(y)
        # print(y, grid[y], line(grid, y))
        if line(grid, y):
            # print(y, grid[0])
            # [1 0 1 1 0 0 1] 5 [0 0 1 1 0 0 0]
            return 100 * y

    mirror = grid.transpose()
    dim = np.shape(grid)[1]
    # print(mirror)
    for x in range(1, dim):
        # print(x, line(mirror, x))
        if line(mirror, x):
            return x

    return None

def pattern_b(grid):
    dim = np.shape(grid)[0]
    for y in range(1, dim):
        # print(y)
        # print(y, grid[y], line(grid, y))
        if line_b(grid, y) is not None:
            return grid

    grid = grid.transpose()
    dim = np.shape(grid)[1]
    # print(mirror)
    for x in range(1, dim):
        # print(x, line(mirror, x))
        if line_b(grid, x) is not None:
            grid = grid.transpose()
            return grid
    return grid

def advent_a(arr):
    tot = 0

    indices = [i for i, x in enumerate(arr) if x == ""]
    indices.append(len(arr))
    # print(indices)

    i = 0
    start = 0
    while i < len(indices):
        input = list()
        if i != 0:
            start = indices[i-1] + 1
        end = indices[i]
        # print(start, end)
        for k in range(start, end):
            input.append(list(arr[k].replace("#", "1").replace(".", "0")))
        mirror = np.array(input, dtype=int)
        # print(mirror)

        # print(pattern(mirror))
        tot += pattern(mirror)

        i += 1
    return tot


def advent_b(arr):
    tot = 0

    indices = [i for i, x in enumerate(arr) if x == ""]
    indices.append(len(arr))
    # print(indices)

    i = 0
    start = 0
    while i < len(indices):
        input = list()
        if i != 0:
            start = indices[i-1] + 1
        end = indices[i]
        # print(start, end)
        for k in range(start, end):
            input.append(list(arr[k].replace("#", "1").replace(".", "0")))
        mirror = np.array(input, dtype=int)

        # print(mirror)
        mirror = pattern_b(mirror)
        # print(mirror)
        if pattern(mirror) is not None:
            tot += pattern(mirror)

        i += 1
    return tot


if __name__ == "__main__":
    import time

    start_time = time.time()
    # Production part b is wrong after refactoring
    test = True
    if test:
        arr = ["#.##..##.",
               "..#.##.#.",
               "##......#",
               "##......#",
               "..#.##.#.",
               "..##..##.",
               "#.#.##.#.",
               "",
               "#...##..#",
               "#....#..#",
               "..##..###",
               "#####.##.",
               "#####.##.",
               "..##..###",
               "#....#..#"
               ]
        # arr = ["##.######.##.",
        #         "...#....#..##",
        #         "####....#####",
        #         "...#.##.#....",
        #         "###..##..###.",
        #         "#..######..##",
        #         "..#.#..#.#..#",
        #         "#.##.##.##.##",
        #         "...##..##....",
        #         "##...##...###",
        #         "##...##...###",
        #         "...##..##....",
        #         "#.##.##.##.##",
        #         "..#.#..#.#..#",
        #         "#..######..##",
        #         "###..##..###.",
        #         "...#.##.#....",
        #         "",
        #         "####..#.#####",
        #         "#..#...##.##.",
        #         ".##.##.######",
        #         "#..#...#.....",
        #         "#..#.##..####",
        #         "###.#..#.....",
        #         "#..###..#....",
        #         "#..#......##.",
        #         "####..##..##."]
        pass
    else:
        input = list()
        with open("inputs/input_13.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    print(advent_a(arr))
    print(advent_b(arr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
