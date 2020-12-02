#!/usr/bin/env python

import numpy as np


def advent_1a(inpt):
    # all combinations
    xv, yv = np.meshgrid(inpt, inpt, sparse=False)
    sum_all = xv + yv
    result = np.asarray(sum_all == 2020).nonzero()
    xy = result[0]
    # symmetrical
    first = xv[xy[0]][xy[1]]
    second = xv[xy[1]][xy[0]]
    return first * second


def advent_1b(inpt):
    xv, yv, zv = np.meshgrid(inpt, inpt, inpt, sparse=False)
    sum_all = xv + yv + zv
    result = np.asarray(sum_all == 2020).nonzero()
    xyz = result[0]
    # print(xyz)
    first = xv[xyz[0]][xyz[2]][xyz[4]]
    second = xv[xyz[2]][xyz[4]][xyz[0]]
    third = xv[xyz[4]][xyz[0]][xyz[2]]
    return first * second * third


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = True
    if test:
        arr = np.array([1721, 979, 366, 299, 675, 1456])
        pass
    else:
        arr = np.loadtxt("inputs/input_01.txt")
        arr = arr.astype(int)

    print(advent_1a(arr))
    print(advent_1b(arr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
