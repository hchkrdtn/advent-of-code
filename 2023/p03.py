#!/usr/bin/env python3

import numpy as np
import re
import regex as rex

def advent_a(arr):
    symbols = []
    for item in arr:
        for ev in list(item):
            if (ev != "." and ev != "0" and ev != "1" and ev != "2" and
                ev != "3" and ev != "4" and ev != "5" and ev != "6" and
                ev != "7" and ev != "8" and ev != "9"):
                symbols.append(ev)
    symbols = sorted(set(symbols))
    # print(symbols)
    # symbols not used

    tot = 0
    chars_coor = []
    for row in range(len(arr)):
        for column in range(len(arr)):
            if arr[row][column] not in "01234566789.":
                chars_coor.append((row, column))
    # print(chars_coor)

    for rowno, item in enumerate(arr):
        for numbers in re.finditer(r"\d+", item):
            edge = set()
            for row in (rowno - 1, rowno, rowno + 1):
                for column in range(numbers.start() - 1, numbers.end() + 1):
                    edge.add((row, column))

            for com_coord in set(edge).intersection(chars_coor):
                # print(com_coord, int(numbers.group()))
                tot += int(numbers.group())
    return tot

def advent_b(arr):
    tot = 0

    stars = {}
    for row in range(len(arr)):
        for column in range(len(arr)):
            # only *
            if arr[row][column] not in "01234566789.#$%&+-=@/":
                stars[(row, column)] = []

    for rowno, item in enumerate(arr):
        for numbers in re.finditer(r"\d+", item):
            edge = set()
            for row in (rowno - 1, rowno, rowno + 1):
                for column in range(numbers.start() - 1, numbers.end() + 1):
                    edge.add((row, column))

            for com_coord in set(edge).intersection(stars.keys()):
                stars[com_coord].append(int(numbers.group()))
                # print(com_coord, int(numbers.group()))
    # print(stars)
    for star in stars.values():
        if len(star) == 2:
            tot += star[0] * star[1]
    return tot


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr_a = ["467..114..",
                 "...*......",
                 "..35...633",
                 "......#...",
                 "617*......",
                 ".....+.58.",
                 "..592.....",
                 "......755.",
                 "...$.*....",
                 ".664.598.."]
        arr = arr_a
        pass
    else:
        with open("inputs/input_03.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    print(advent_a(arr))
    print(advent_b(arr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
