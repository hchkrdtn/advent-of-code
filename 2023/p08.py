#!/usr/bin/env python3

import numpy as np
from collections import deque
from multiprocessing import Pool


def f(x):
    return x*x


def parsing(arr):
    directions = arr[0]
    # Declaring deque
    de = deque(list(directions))

    arr = arr[2:]
    node_dirs = {}
    for i, item in enumerate(arr):
        nodes = item.split(" = ")
        node_dirs[nodes[0]] = nodes[1][1:-1].split(", ")
    # print(node_dirs)
    return de, node_dirs


def compute1(de, node_start, node_end, slicer, node_path):
    i = 0
    while True:
        direction = 0 # left
        first = de[0]
        if first == "R":
            direction = 1   # right
        node_start = node_path[node_start][direction]

        if node_start[slicer] == node_end[slicer]:
            return i, node_start
        de.rotate(-1)
        i += 1

def advent_a(arr):
    node_start = "AAA"
    node_end = "ZZZ"

    de, node_dirs = parsing(arr)

    idx, node = compute1(de, node_start, node_end, slice(len(node_start)), node_dirs)
    # idx, node = compute_a(de, node_start, node_end, slice(-1,None), node_dirs)
    return idx + 1


def advent_b(arr):
    node_start = "xxA"
    node_end = "ZZZ"

    de, node_dirs = parsing(arr)

    node_starts = []
    for ndk in node_dirs.keys():
        if ndk[-1] == node_start[-1]:
            node_starts.append(ndk)
    # print(node_starts)

    node_starts_new = []
    idx_first = []
    for node_start in node_starts:
        idx, node = compute1(de.copy(), node_start, node_end, slice(-1,None), node_dirs)
        # print(idx, node_start, node)
        node_starts_new.append(node)
        idx_first.append(idx + 1)
    # print(idx_first)

    # wow, it took me the whole afternoon to realize the indices are periodical
    # and I can use lcm (lowest common multiple)
    idx_first = np.asarray(idx_first)
    lcm = np.lcm.reduce(idx_first)

    return lcm


    # with Pool(5) as p:
    #     print(p.map(compute_a(de, node_start, node_end, slicer, node_path), [1, 2, 3]))
    # pool = Pool()
    # result1 = pool.apply_async(solve1, [A])  # evaluate "solve1(A)" asynchronously
    # result2 = pool.apply_async(solve2, [B])  # evaluate "solve2(B)" asynchronously
    # answer1 = result1.get(timeout=10)
    # answer2 = result2.get(timeout=10)
    # args = [A, B]
    # results = pool.map(solve1, args)


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr_a1 = ["RL",
                  "",
                  "AAA = (BBB, CCC)",
                  "BBB = (DDD, EEE)",
                  "CCC = (ZZZ, GGG)",
                  "DDD = (DDD, DDD)",
                  "EEE = (EEE, EEE)",
                  "GGG = (GGG, GGG)",
                  "ZZZ = (ZZZ, ZZZ)"]
        arr_a2 = ["LLR",
                  "",
                  "AAA = (BBB, BBB)",
                  "BBB = (AAA, ZZZ)",
                  "ZZZ = (ZZZ, ZZZ)"]
        arr_b = ["LR",
                 "",
                 "11A = (11B, XXX)",
                 "11B = (XXX, 11Z)",
                 "11Z = (11B, XXX)",
                 "22A = (22B, XXX)",
                 "22B = (22C, 22C)",
                 "22C = (22Z, 22Z)",
                 "22Z = (22B, 22B)",
                 "XXX = (XXX, XXX)"]
        arr = arr_b
        pass
    else:
        with open("inputs/input_08.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    # with Pool(5) as p:
    #     print(p.map(f, [1, 2, 3]))

    print(advent_a(arr))
    print(advent_b(arr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
