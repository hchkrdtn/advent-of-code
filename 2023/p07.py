#!/usr/bin/env python3

import numpy as np
import re


def advent_a(arr):
    race_ts = re.findall(pattern=r"\d+", string=arr[0])
    distances = re.findall(pattern=r"\d+", string=arr[1])
    # print(race_ts)
    # print(distances)

    tot = 1
    for i in range (0, len(race_ts)):
        race_t = int(race_ts[i])
        dist = int(distances[i])

        race = np.zeros((race_t+1, 3), dtype=int)
        race[:,0] = np.arange(race_t + 1)
        race[:, 1] = np.flip(race[:, 0])
        race[:, 2] = np.array((race[:, 0] * race[:, 1]))
        # race[:, 3] = race[:, 2] - dist

        record = (sum(race[:, 2] > dist))
        tot *= record
    return tot


def advent_b(arr):
    race_ts = re.findall(pattern=r"\d+", string=arr[0])
    distances = re.findall(pattern=r"\d+", string=arr[1])
    # print(race_ts)
    # print(distances)
    tot = 1

    race_t = ""
    dist = ""
    for i in range (0, len(race_ts)):
        race_t += race_ts[i]
        dist += distances[i]

    race_t = int(race_t)
    dist = int(dist)

    race = np.zeros((race_t+1, 3), dtype=int)
    race[:,0] = np.arange(race_t + 1)
    race[:, 1] = np.flip(race[:, 0])
    race[:, 2] = np.array((race[:, 0] * race[:, 1]))
    # race[:, 3] = race[:, 2] - dist

    record = (sum(race[:, 2] > dist))
    tot *= record
    return tot


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr_a = ["seeds"]
        arr = arr_a
        pass
    else:
        with open("inputs/input_07.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    print(advent_a(arr))
    print(advent_b(arr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
