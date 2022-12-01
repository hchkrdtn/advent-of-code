#!/usr/bin/env python3

import numpy as np


def advent_1a(arr):
    return len(arr)


def advent_1b(arr):
    return len(arr)


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

    print(advent_1a(arr))
    print(advent_1b(arr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
