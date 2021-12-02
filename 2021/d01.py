#!/usr/bin/env python3

import numpy as np


def advent_1a(inpt):
    # roll one position and subtract
    arr_diff = np.array(inpt) - np.roll(arr, 1)
    # print(inpt, arr_diff)

    smaller = np.sum(arr_diff[1:] < 0)
    # print(smaller)
    larger = np.sum(arr_diff[1:] > 0)

    return larger


def advent_1b(inpt):
    arr = np.array(inpt)
    # roll one and two positions
    arr1 = np.roll(arr, -1)
    arr2 = np.roll(arr, -2)

    # sum three arrays (three rollong numbers)
    arr_three = arr + arr1 + arr2
    arr_three = arr_three[:-2]

    arr_diff = np.array(arr_three) - np.roll(arr_three, 1)

    smaller = np.sum(arr_diff[1:] < 0)
    # print(smaller)
    larger = np.sum(arr_diff[1:] > 0)

    return larger


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        pass
    else:
        arr = np.loadtxt("inputs/input_01.txt")
        arr = arr.astype(int)

    print(advent_1a(arr))
    print(advent_1b(arr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
