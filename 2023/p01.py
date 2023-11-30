#!/usr/bin/env python3

import numpy as np


def advent_a(arr):

    return np.amax(np.array(arr))


def advent_b(arr):
    arr = np.sort(arr, axis=None)

    return np.sum(arr[-3:])


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr = ["1000", "2000", "3000", "", "4000", "", "5000", "6000", "", "7000", "8000", "9000", "", "10000"]
        pass
    else:
        with open("inputs/input_01.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    narr = []
    nsum = 0
    i = 0
    while i < len(arr):
        if arr[i] == "":
            narr.append(nsum)
            nsum = 0
        else:
            nsum += int(arr[i])

        if i == len(arr) - 1:
            narr.append(nsum)
            break
        i += 1

    print(advent_a(narr))
    print(advent_b(narr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
