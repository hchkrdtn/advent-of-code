#!/usr/bin/env python3

import numpy as np


def advent_a(arr):
    intersections = 0

    i = 0
    while i < len(arr):
        sec12 = arr[i].split(",")

        sec1 = sec12[0].split("-")
        sec2 = sec12[1].split("-")

        sec1_arr = np.array([range(int(sec1[0]), int(sec1[1])+1)], np.int32)
        sec2_arr = np.array([range(int(sec2[0]), int(sec2[1])+1)], np.int32)

        inter12 = np.intersect1d(sec1_arr, sec2_arr)

        if inter12.size == sec1_arr.size or inter12.size == sec2_arr.size:
            intersections += 1
            # print(sec1_arr, sec2_arr)

        i += 1

    return intersections


def advent_b(arr):
    intersections = 0

    i = 0
    while i < len(arr):
        sec12 = arr[i].split(",")

        sec1 = sec12[0].split("-")
        sec2 = sec12[1].split("-")

        sec1_arr = np.array([range(int(sec1[0]), int(sec1[1])+1)], np.int32)
        sec2_arr = np.array([range(int(sec2[0]), int(sec2[1])+1)], np.int32)

        inter12 = np.in1d(sec1_arr, sec2_arr)

        if inter12.any():
            intersections += 1
            # print(sec1_arr, sec2_arr)

        i += 1

    return intersections


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr = ["2-4,6-8",
               "2-3,4-5",
               "5-7,7-9",
               "2-8,3-7",
               "6-6,4-6",
               "2-6,4-8"]
        pass
    else:
        with open("inputs/input_04.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    print(advent_a(arr))
    print(advent_b(arr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
