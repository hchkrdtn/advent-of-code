#!/usr/bin/env python3

import numpy as np


def advent_13a(input):
    depart = int(input[0])
    buses = np.array(input[1].split(","))

    buses = buses[buses != "x"].astype(np.int)
    bd = buses - depart % buses
    return np.min(bd) * buses[np.argmin(bd)]


def advent_13b(input):
    # basic, works for all tests but not the file
    buses = np.array(input[1].split(","))
    inter = np.arange(buses.size)

    nox = np.flatnonzero(buses != "x")
    buses = buses[nox].astype(np.int)
    inter = inter[nox].astype(np.int)

    idx = 0
    while True:
        indices = np.full(buses.size, idx * np.max(buses))
        indices = indices - inter[np.flatnonzero(buses == np.max(buses))] + inter

        if np.all(indices % buses == 0):
            return indices[0]
        idx += 1


def advent_13b2(input):
    # Adjust [0, 1, 0 ....] array to turn on and off the corresponding reduced numbers
    # for example [7,13,x,x,59,x,31,19] is reduced to [7,13,59,31,19]. Start with the highest number
    # [1,1,0,1,1]. write down index difference, put it in idx +=, and idx = use the highest index.
    # Repeat for other numbers "turned on" [1,1,0,0,0], go from highest to lowest
    # You have to repeat it several times for the file input values where the total number (index * highest)
    # is too high for single run (or even few runs)
    buses = np.array(input[1].split(","))
    inter = np.arange(buses.size)

    nox = np.flatnonzero(buses != "x")
    buses = buses[nox].astype(np.int)
    inter = inter[nox].astype(np.int)
    print(inter, buses)

    # test
    # idx = 17526
    # idx = 163
    # idx = 7655
    # idx = 11203
    # idx = 18401
    # idx = 115802

    # file
    idx = 10844453793
    while True:
        indices = np.full(buses.size, idx * np.max(buses))
        indices = indices - inter[np.flatnonzero(buses == np.max(buses))] + inter

        wes = indices % buses == 0

        # test
        # if np.array_equal((wes == 0), np.asarray([1, 1, 0, 0, 0])):
        # if np.array_equal((wes == 0), np.asarray([0, 1, 0])):
        # if np.array_equal((wes == 0), np.asarray([0, 1, 0, 0])):
        # if np.array_equal((wes == 0), np.asarray([0, 0, 1, 0])):
        # if np.array_equal((wes == 0), np.asarray([0, 1, 1, 1])):
        # if np.array_equal((wes == 0), np.asarray([0, 1, 1, 0])):

        # file
        if np.array_equal((wes == 0), np.asarray([0, 0, 0, 1, 1, 1, 0, 0, 0])):
            print(idx, indices, indices % buses)

        if np.all(indices % buses == 0):
            # print(indices[0])
            return indices[0]
        if idx % (np.max(buses) * 100000) == 0:
            print(idx)

        # test
        # idx += 589
        # idx += 17
        # idx += 3599
        # idx += 427
        # idx += 427
        # idx += 1789

        # file
        idx += 413842151


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        # no spaces, no strip
        in_list = ["939", "7,13,x,x,59,x,31,19"] # b: 1068781
        in_list = ["-1", "17,x,13,19"] # 3417
        in_list = ["-1", "67,7,59,61"] # 754018
        in_list = ["-1", "67,x,7,59,61"] # 779210
        in_list = ["-1", "67,7,x,59,61"] # 1261476.
        in_list = ["-1", "1789,37,47,1889"] # 1202161486
        pass
    else:
        with open("inputs/input_13.txt") as f:
            in_list = f.readlines()
        in_list = [x.strip() for x in in_list]

    print(advent_13a(in_list))
    # print(advent_13b(in_list))
    print(advent_13b2(in_list))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
