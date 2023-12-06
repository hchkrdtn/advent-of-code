#!/usr/bin/env python3

import numpy as np
import re


def calc_prod(prods, seed_nums, intervals):
    results = []
    for k, seed_num in enumerate(seed_nums):
        seed_num_end = seed_num + intervals[k]

        while seed_num < seed_num_end:
            res = [seed_num]
            p = seed_num
            for i, key in enumerate(prods.keys()):
                for item in prods[key]:
                    rows = item.split(" ")
                    r1 = int(rows[0])
                    r2 = int(rows[1])
                    d = int(rows[2])
                    # trial and error:
                    # not if r2 < res[i] and res[i] <= r2 + d:
                    if r2 <= res[i] and res[i] < r2 + d:
                        p = res[i] + (r1 - r2)
                    # print(r1, r2, d, p, res[i])
                res.append(p)
                i += 1
            # print(res)
            results.append(res)
            if seed_num % 1000000 == 0:
                print(seed_num, res[-1])
                end_time = time.time()
                elapsed = end_time - start_time
                print("Time: {:.2f}".format(elapsed) + "s")
            seed_num += 1
    return results


def advent_a(arr):
    groups = ["seed-to-soil",
              "soil-to-fertilizer", "fertilizer-to-water",
              "water-to-light", "light-to-temperature",
              "temperature-to-humidity", "humidity-to-location"]

    sublist = re.findall(pattern=r"\d+", string=arr[0])
    seed_nums = [int(val) for val in sublist]
    # print(len(seed_nums))

    prods = {}
    for i, group in enumerate(groups):
        start_idx = arr.index(group + " map:")
        if i == len(groups) - 1:
            end_idx = len(arr)
        else:
            end_idx = arr.index(groups[i + 1] + " map:")
        sublist = arr[start_idx + 1: end_idx - 1]
        prods[group] = sublist
    # print(prods)

    # single number, intervals = 1
    intervals = [1 for i in range(len(seed_nums))]
    results = calc_prod(prods, seed_nums, intervals)
    # print(results)

    tot = min([r[-1] for r in results])
    return tot


def advent_b(arr):
    groups = ["seed-to-soil",
              "soil-to-fertilizer", "fertilizer-to-water",
              "water-to-light", "light-to-temperature",
              "temperature-to-humidity", "humidity-to-location"]

    sublist = re.findall(pattern=r"\d+", string=arr[0])
    seed_nums = [int(val) for val in sublist]
    # print(len(seed_nums))

    prods = {}
    for i, group in enumerate(groups):
        start_idx = arr.index(group + " map:")
        if i == len(groups) - 1:
            end_idx = len(arr)
        else:
            end_idx = arr.index(groups[i + 1] + " map:")
        sublist = arr[start_idx + 1: end_idx - 1]
        prods[group] = sublist
    # print(prods)

    # odd numbers: seed_nums_odd[1::2]
    # even numbers: seed_nums_even[::2]
    seed_nums_odd = seed_nums[::2]
    intervals = seed_nums[1::2]

    # x1 = 3169137700
    # x2 = 271717609
    # d = 1e3
    # # 3300650700 213844930 Execution time: 33.41s
    # x1 = 3522125441
    # x2 = 23376095
    # d = 1e3
    # # 3523913441 2334237362
    # x1 = 1233948799
    # x2 = 811833837
    # d = 1e3
    # # 1848532799 517683912
    # x1 = 280549587
    # x2 = 703867355
    # d = 1e3
    # 360119587 114138365
    # x1 = 166086528
    # x2 = 44766996
    # d = 1e3
    # # 205771528 1164454361
    # x1 = 2326968141
    # x2 = 69162222
    # d = 1e3
    # # 2392582141 219974839
    # x1 = 2698492851
    # x2 = 14603069
    # d = 1e3
    # # 2698492851 3756578039
    # x1 = 2755327667
    # x2 = 348999531
    # d = 1e3
    # # 2762480667 218729070
    x1 = 2604900000 # 2600461189
    x2 = 100000 # 92332846
    d = 1
    # 2604983879 !!!! 84206669 !!!!! Execution time: 11.86s
    # x1 = 1054656969
    # x2 = 169099767
    # d = 1e3
    # # 1060711969 386981576 Execution time: 20.80s

    x = x1
    seed_nums_odd = []
    print(x1, x1+x2, x2, int(d))
    while x < x1 + x2:
        seed_nums_odd.append(int(x))
        x += int(d)
    # single number, intervals = 1
    intervals = [1 for i in range(len(seed_nums_odd))]

    results = calc_prod(prods, seed_nums_odd, intervals)

    # for r in results:
    #     # print(r)
    #     print(r[0], r[-1])
    tot = min([r[-1] for r in results])
    index = [r[-1] for r in results].index(tot)
    print("\n")
    print(results[index][0], tot)

    return tot


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr_a = ["seeds: 79 14 55 13",
                 "",
                 "seed-to-soil map:",
                 "50 98 2",
                 "52 50 48",
                 "",
                 "soil-to-fertilizer map:",
                 "0 15 37",
                 "37 52 2",
                 "39 0 15",
                 "",
                 "fertilizer-to-water map:",
                 "49 53 8",
                 "0 11 42",
                 "42 0 7",
                 "57 7 4",
                 "",
                 "water-to-light map:",
                 "88 18 7",
                 "18 25 70",
                 "",
                 "light-to-temperature map:",
                 "45 77 23",
                 "81 45 19",
                 "68 64 13",
                 "",
                 "temperature-to-humidity map:",
                 "0 69 1",
                 "1 0 69",
                 "",
                 "humidity-to-location map:",
                 "60 56 37",
                 "56 93 4"]
        arr = arr_a
        pass
    else:
        with open("inputs/input_05.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    print(advent_a(arr))
    print(advent_b(arr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
