#!/usr/bin/env python

import numpy as np


def advent_3():
    input = list()
    test = False
    if test:
        # input.append("Before: [3, 2, 1, 1]")
        # input.append("9 2 1 2")
        # input.append("After:  [3, 2, 2, 1]")
        # input.append("")
        pass
    else:
        with open("input_00.txt", "r") as f:
            for line in f:
                input.append(line)
        f.close()

def advent_3a(input):
    input_tmp = np.copy(input)
    # print(input_tmp)
    return input_tmp[0]

def advent_3b(input):
    input_tmp = np.copy(input)
    print(input_tmp[0])


if __name__ == "__main__":
    import time

    start_time = time.time()

    input = np.array([1,1,1,1,1])
    print(advent_3a(input))

    input = np.array([1,1,1,1,1])
    advent_3b(input)

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")