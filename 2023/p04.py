#!/usr/bin/env python3

import numpy as np
import re

def advent_a(arr):
    tot = 0
    for item in arr:
        cards = item.split(": ")

        win_num = re.findall(pattern=r"[+]?\d+", string=cards[1].split(" | ")[0])
        my_num = re.findall(pattern=r"[+]?\d+", string=cards[1].split(" | ")[1])

        win = np.asarray(win_num, dtype=int)
        my = np.asarray(my_num, dtype=int)
        mask = np.isin(my, win)

        if mask.sum():
            tot += 2**(mask.sum() - 1)
    return tot

def advent_b(arr):
    # list fill with ones
    result = [1] * len(arr)

    for i, item in enumerate(arr):
        cards = item.split(": ")

        win_num = re.findall(pattern=r"[+]?\d+", string=cards[1].split(" | ")[0])
        my_num = re.findall(pattern=r"[+]?\d+", string=cards[1].split(" | ")[1])

        win = np.asarray(win_num, dtype=int)
        my = np.asarray(my_num, dtype=int)

        mask = np.isin(my, win)
        num = mask.sum()

        # print(num)
        k = 1
        while k <= num:
            result[i + k] += result[i] * 1
            k += 1
        # print(result)

    return sum(result)


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr_a = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
                 "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
                 "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
                 "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
                 "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
                 "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]
        arr = arr_a
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
