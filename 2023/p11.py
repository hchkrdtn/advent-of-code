#!/usr/bin/env python3

import numpy as np
import scipy as sp
from collections import deque


def advent_a(arr):
    tot = 0

    space = np.array(arr, dtype=int)
    space_fin = np.copy(space)

    # np.insert(a, 1, 5)
    # print(space)
    # print(space==0)
    # empty rows
    nul_row = np.all(space == 0, axis=0)
    # empty rows indices
    nul_row_idx = np.where(nul_row)
    # empty columns
    nul_col = np.all(space == 0, axis=1)
    # empty column indices
    nul_col_idx = np.where(nul_col)

    # print(nul_col_idx, nul_row_idx)

    idx = nul_row_idx[0] + 1
    # print(space)
    space = np.insert(space, idx, 0, axis=1)
    idx = nul_col_idx[0] + 1
    space = np.insert(space, idx, 0, axis=0)
    # print(space)

    # insert = 10
    # idx = nul_row_idx[0]
    # # print(space)
    # space = np.insert(space, slice(idx[0], idx[0]+insert), 0, axis=1)
    # space = np.insert(space, slice(idx[1]+insert, idx[1]+insert+insert), 0, axis=1)
    # space = np.insert(space, slice(idx[2]+2*insert, idx[2]+2*insert+insert), 0, axis=1)
    # # print(space)
    # idx = nul_col_idx[0]
    # space = np.insert(space, slice(idx[0], idx[0]+insert), 0, axis=0)
    # space = np.insert(space, slice(idx[1]+insert, idx[1]+insert+insert), 0, axis=0)


    idx_xy = np.nonzero(space == 1)
    # print(idx_xy)
    idx_xy = np.transpose(idx_xy)
    # print(idx_xy)
    full = sp.spatial.distance_matrix(idx_xy, idx_xy, p=1, threshold=1000000)
    # print(full)
    # print(sum(full))
    # print(sum(sum(full))/2)
    tot = sum(sum(full))/2

    # # p = 1, Manhattan Distance
    # # p = 2, Euclidean Distance
    # # p = ∞, Chebychev Distance
    # x = [[0,1,0],[0,0,0]]
    # print(x[0])
    # print(x[1])
    # # print(x[2])
    # y = [[0,0,0],[0,0,0]]
    # print(y[0])
    # print(y[1])
    # # print(y[2])
    # full = sp.spatial.distance_matrix(x, y, p=1, threshold=1000000)
    # # [[1. 1.]      [[x0 y0, x0 y1]
    # #  [0. 0.]]      [x1 y0, x1 y1]]
    # print(full)
    #
    # z = [[0,0,0,0,1,0,0,0,0,0],
    #      [0,0,0,0,0,0,0,0,0,1],
    #      [1,0,0,0,0,0,0,0,0,0]]
    # m, n = np.meshgrid(z, z)
    # # get the distance via the norm
    # out = abs(m - n)
    # print(out)
    #
    # full = sp.spatial.distance_matrix(space_full, space_full, p=1, threshold=1000000)
    # print(full)

    return tot


def advent_b(arr):
    space = np.array(arr, dtype=int)

    nul_row = np.all(space == 0, axis=0)
    # empty rows indices
    nul_row_idx = np.where(nul_row)
    # empty columns
    nul_col = np.all(space == 0, axis=1)
    # empty column indices
    nul_col_idx = np.where(nul_col)

    idx_xy = np.nonzero(space == 1)
    # print(idx_xy)

    insert = 1000000
    if insert != 1:
        insert -= 1
    # print(nul_col_idx, nul_row_idx)

    idx0 = idx_xy[0].copy()
    idx1 = idx_xy[1].copy()
    for idx in (nul_col_idx[0]):
        idx0[idx_xy[0] > idx] += insert
        # print(idx0)
    for idx in nul_row_idx[0]:
        idx1[idx_xy[1] > idx] += insert
        # print(idx1)
    idx_xy = np.transpose((idx0, idx1))
    # print(idx_xy)
    full = sp.spatial.distance_matrix(idx_xy, idx_xy, p=1, threshold=1000000)
    # print(full)
    # print(sum(full))
    # print(sum(sum(full))/2)
    tot = sum(sum(full))/2

    return tot


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr = ["...#......",
                ".......#..",
                "#.........",
                "..........",
                "......#...",
                ".#........",
                ".........#",
                "..........",
                ".......#..",
                "#...#....."]
        input = list()
        for item in arr:
            input.append(list(item.replace("#", "1").replace(".", "0")))
        pass
    else:
        input = list()
        with open("inputs/input_11.txt", "r") as f:
            for line in f:
                line = line.strip()
                input.append(list(line.replace("#", "1").replace(".", "0")))
        f.close()

    print(advent_a(input))
    print(advent_b(input))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
