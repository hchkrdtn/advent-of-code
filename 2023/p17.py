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
    # Production part b is wrong after refactoring
    test = True
    if test:
        arr = ["2413432311323",
               "3215453535623",
               "3255245654254",
               "3446585845452",
               "4546657867536",
               "1438598798454",
               "4457876987766",
               "3637877979653",
               "4654967986887",
               "4564679986453",
               "1224686865563",
               "2546548887735",
               "4322674655533"]
        pass
    else:
        input = list()
        with open("inputs/input_17.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    print(advent_a(arr))
    print(advent_b(arr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
