#!/usr/bin/env python3

import numpy as np


def advent_a(arr):
    tot = 0
    for item in arr:
        print(item)

    return tot


def advent_b(arr):
    tot = 0
    for item in arr:
        print(item)

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
