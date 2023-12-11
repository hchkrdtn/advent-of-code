#!/usr/bin/env python3

import numpy as np
from collections import deque

def rotation(all):
    line = np.asarray(all[-1])
    de = deque(line.copy())
    de.rotate(1)
    line2 = np.asarray(de)
    dif = line - line2
    # number of list elements = number of iterations
    iter = len(all)

    all.append(list(dif))
    if np.all(dif[iter:] == 0):
        return np.asarray(all)
    else:
        return rotation(all)


def advent_a(arr):
    tot = 0

    for i, item in enumerate(arr):
        line = [int(x) for x in list(item.split(" "))]
        all = [line]
        all_fin = rotation(all)
        # print(all_fin)

        tot += np.sum(all_fin[:,-1], axis=0)
    return tot


def advent_b(arr):
    tot = 0

    for i, item in enumerate(arr):
        line = [int(x) for x in list(item.split(" "))]
        all = [line]
        all_fin = rotation(all)

        dim0 = np.shape(all_fin)[0]
        first = np.zeros(dim0)
        for i in range(0, dim0 + 1):
            first_r = all_fin[i:i+1,i:i+1]
            first[i:i+1] = first_r.flatten()

        # print(first)
        # 10.  3.  0.  2.  0.]
        # to
        # [ 5.  5. -2.  2.  0.]
        # start from back and subtract last from second last (2-0)
        # then subtract result from third (0-2)
        first2 = np.zeros(dim0)
        for  i in range(0, len(first)):
            lst = len(first)
            if i == 0:
                first2[lst-1] = int(first2[lst-1])
            else:
                first2[lst-i-1] = int(first[lst-i-1] - first2[lst-i])
        # print(first2)
        tot += int(first2[0])
    return tot


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr = ["0 3 6 9 12 15",
               "1 3 6 10 15 21",
               "10 13 16 21 30 45"]
        pass
    else:
        with open("inputs/input_09.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    print(advent_a(arr))
    print(advent_b(arr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
