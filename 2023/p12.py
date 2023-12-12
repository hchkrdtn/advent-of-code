#!/usr/bin/env python3

import numpy as np
import re
# import itertools package
import itertools
from itertools import product


def list_to_str(num_list):
    num_str = ""
    for i, num in enumerate(num_list):
        if i == 0:
            num_str = num * "#"
        else:
            num_str += "." + num * "#"
    return num_str


def str_to_list(num_str):
    num_list = []
    # num_list = re.split(pattern=r".+", string=num_str)
    nums = re.split(r"\.+", num_str)
    for num in nums:
        num_list.append(len(num))
    return num_list


def advent_a(arr):
    tot = 0

    # arr_solved = ["#.#.### 1,1,3",
    #               ".#...#....###. 1,1,3",
    #               ".#.###.#.###### 1,3,1,6",
    #               "####.#...#... 4,1,1",
    #               "#....######..#####. 1,6,5",
    #               ".###.##....# 3,2,1"]

    for item in arr:
        # print(item)
        springs = item.split(" ")
        br = re.findall(pattern=r"[+]?\d+", string=springs[1])
        br = [int(x) for x in br]
        br_str = list_to_str(br)
        # print(br, br_str)

        cnt = 0
        idx_all = []
        for qm in re.finditer(pattern=r"\?+", string=springs[0]):
            cnt += 1
            idx_all.append(list(range(qm.start(), qm.end())))
        #     print(cnt, "st match start index", qm.start(), "End index", qm.end())
        #     print(idx_all)
        # print(sum(idx_all, []))

        springs_comb = ""
        springs_comb1 = ""
        list_2 = [".", "#"]
        # flatten list
        list_1 = sum(idx_all, [])

        # create empty list to store the combinations
        unique_combinations = []
        # Extract Combination Mapping in two lists using zip() + product()
        unique_combinations = list(list(zip(list_1, element)) for element in product(list_2, repeat=len(list_1)))
        # print(unique_combinations)
        lu = 0
        for uk in unique_combinations:
            l = list(springs[0])
            for coord in uk:
                l[coord[0]] = coord[1]
            # print(l)
            res = []
            ps = 0
            for s in l:
                if s == ".":
                    if s not in res or res[ps - 1] == "#":
                        res.append(s)
                else:
                    res.append(s)
            ps += 1
            if res and res[0] == ".":
                res = res[1:]
            if res and res[-1] == ".":
                res = res[:-1]
            springs_comb = "".join(l)
            springs_comb1 = "".join(res)
            # print(springs_comb, springs_comb1, br_str)

            if springs_comb1 == br_str:
                lu += 1
                # print(springs_comb, springs_comb1, br_str)
        # print(lu)
        tot += lu

    return tot


def advent_b(arr):
    # try fuzzy string/list comparisons
    # difflib  https://docs.python.org/3/library/difflib.html
    # jellyfish https://pypi.org/project/jellyfish/
    tot = 0
    lu = 0

    # arr_solved = ["#.#.### 1,1,3",
    #               ".#...#....###. 1,1,3",
    #               ".#.###.#.###### 1,3,1,6",
    #               "####.#...#... 4,1,1",
    #               "#....######..#####. 1,6,5",
    #               ".###.##....# 3,2,1"]

    for item in arr:
        # print(item)
        springs = item.split(" ")
        # springs[0] = springs[0] + "?" + springs[0] + "?" + springs[0] + "?" + springs[0] + "?" + springs[0]
        # springs[1] = springs[1] + "," + springs[1] + "," + springs[1] + "," + springs[1] + "," + springs[1]
        print(springs)

        br = re.findall(pattern=r"[+]?\d+", string=springs[1])
        br = [int(x) for x in br]
        br_str = list_to_str(br)
        print(br_str, br)

        print("".join(br_str.rsplit(springs[1])))

        if len(springs[0]) == sum(br) + len(br) - 1:
            lu = 1
        print(lu)
        tot += lu

    return tot


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = True
    if test:
        arr = ["???.### 1,1,3",
               ".??..??...?##. 1,1,3",
               "?#?#?#?#?#?#?#? 1,3,1,6",
               "????.#...#... 4,1,1",
               "????.######..#####. 1,6,5",
               "?###???????? 3,2,1"]
        pass
    else:
        with open("inputs/input_12.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    # print("str_to_list", str_to_list("#.#.###"))
    # print("list_to_str", list_to_str([1,1,3]))

    print(advent_a(arr))
    print(advent_b(arr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
