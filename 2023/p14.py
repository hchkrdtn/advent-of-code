#!/usr/bin/env python3

import numpy as np


def roll(grid):
    grid = grid.transpose()
    # print(grid)

    b_end = np.shape(grid)[0]
    for i in range(0, b_end):
        idxs2 = np.where(grid[i,:] == 2)
        idxs1 = np.where(grid[i,:] == 1)
        idx1 = idxs1[0].tolist()
        idx2 = idxs2[0].tolist()
        if len(idx2) == 0:
            for j, oval in enumerate(idx1):
                grid[i, oval] = 0
                grid[i, j] = 1
        else:
            idx22 = np.insert(idx2, 0, -1)
            idx22 = np.append(idx22, b_end)
            for b, beam in enumerate(idx22):
                b1 = idx22[b]
                if b < len(idx22)-1:
                    b2 = idx22[b + 1]
                else:
                    break
                hh = 0
                for oval in idx1:
                    if b1 < oval < b2:
                        # print(b, b1, b2, hh, oval)
                        grid[i, oval] = 0
                        grid[i, b1 + hh + 1] = 1
                        hh += 1
    fin_coord = np.where(grid.transpose() == 1)
    return fin_coord


def advent_a(arr):
    tot = 0

    input = list()
    for item in arr:
        input.append(list(item.replace("#", "2").replace(".", "0").replace("O", "1")))

    grid = np.array(input).astype(int)

    fin_coord = roll(grid)

    b_end = np.shape(grid)[0]
    for i in range(0, b_end):
        # print(fin_coord[0])
        num = (b_end - i) * np.shape(np.where(fin_coord[0] == i))[1]
        # print(num)
        tot += num
    return tot


def advent_b(arr):
    tot = 0
    for item in arr:
        pass
        # print(item)

    return tot


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = True
    if test:
        arr = ["O....#....",
               "O.OO#....#",
               ".....##...",
               "OO.#O....O",
               ".O.....O#.",
               "O.#..O.#.#",
               "..O..#O..O",
               ".......O..",
               "#....###..",
               "#OO..#...."]
        pass
    else:
        input = list()
        with open("inputs/input_14.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    print(advent_a(arr))
    print(advent_b(arr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
