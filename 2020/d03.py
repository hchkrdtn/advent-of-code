#!/usr/bin/env python

import numpy as np


def advent_3a(inpt, slp):
    origin = [0, 0]
    dx = slp[0]
    dy = slp[1]

    tmp_char = np.array(inpt)
    grid = tmp_char.astype(np.int)

    xsize, ysize = grid.shape
    # repeat pattern n-times, concatenate matrix
    conc_n = np.ceil(xsize / ysize * np.ceil(dx/dy))

    grids = list()
    i = 1
    # multiply array of grids
    while i <= conc_n:
        grids.append(grid)
        i += 1
    grid_fin = np.concatenate(grids, axis=1)

    k = 0
    result = np.zeros(xsize)
    while k * dy < xsize:
        # swap axes, np matrix has x down
        y = origin[0] + (k * dx)
        x = origin[1] + (k * dy)

        result[k] = grid_fin[x, y]
        k += 1

    return np.count_nonzero(result == 1)


def advent_3b(inpt):
    slopes = list()
    slopes.append([1, 1])
    slopes.append([3, 1])
    slopes.append([5, 1])
    slopes.append([7, 1])
    slopes.append([1, 2])

    trees = []
    for slp in slopes:
        trees.append(advent_3a(inpt, slp))
    # print(trees)
    return np.prod(np.array(trees))


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = True
    if test:
        in_list = list()
        in_list.append(list("..##.......".replace("#", "1").replace(".", "0")))
        in_list.append(list("#...#...#..".replace("#", "1").replace(".", "0")))
        in_list.append(list(".#....#..#.".replace("#", "1").replace(".", "0")))
        in_list.append(list("..#.#...#.#".replace("#", "1").replace(".", "0")))
        in_list.append(list(".#...##..#.".replace("#", "1").replace(".", "0")))
        in_list.append(list("..#.##.....".replace("#", "1").replace(".", "0")))
        in_list.append(list(".#.#.#....#".replace("#", "1").replace(".", "0")))
        in_list.append(list(".#........#".replace("#", "1").replace(".", "0")))
        in_list.append(list("#.##...#...".replace("#", "1").replace(".", "0")))
        in_list.append(list("#...##....#".replace("#", "1").replace(".", "0")))
        in_list.append(list(".#..#...#.#".replace("#", "1").replace(".", "0")))
        # print(in_list)
        pass
    else:
        in_list = list()
        with open("inputs/input_03.txt", "r") as f:
            for line in f:
                line = line.strip()
                in_list.append(list(line.replace("#", "1").replace(".", "0")))
        f.close()
        # print(in_list)

    slope = [3, 1]
    print(advent_3a(in_list, slope))
    print(advent_3b(in_list))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
