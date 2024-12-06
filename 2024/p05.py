#!/usr/bin/env python3

import itertools
import math
import re


def advent(arr):
    tot_a = 0
    tot_b = 0
    flag = False

    rules = []
    final = []
    for item in arr:
        if item:
            if flag:
                final.append(item)
            else:
                rules.append(item)
        else:
            flag = True

    for item in final:
        vals = re.findall(r"\d+", string=item)
        perms = list(itertools.permutations(vals, 2)) # permutations('ABCD', 2)  AB, AC, ...
        fins = {}
        for perm in perms:
            rule = "|".join(perm)
            if rule in rules:
                if perm[0] in fins:
                    fins[perm[0]].append(perm[1])
                else:
                    fins[perm[0]] = [perm[1]]
                # print(rule)
        # print(fins)
        vals_fin = vals.copy()
        for val in fins:
            idx = len(vals_fin) - len(fins[val]) - 1
            vals_fin[idx] = val
            if len(fins[val]) == 1:
                vals_fin[-1] = fins[val][0]

        if vals_fin == vals:
            tot_a += int(vals[math.floor(len(vals) / 2)])
        else:
            tot_b += int(vals_fin[math.floor(len(vals_fin) / 2)])

    return tot_a, tot_b


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr_a = ["47|53",
                 "97|13",
                 "97|61",
                 "97|47",
                 "75|29",
                 "61|13",
                 "75|53",
                 "29|13",
                 "97|29",
                 "53|29",
                 "61|53",
                 "97|53",
                 "61|29",
                 "47|13",
                 "75|47",
                 "97|75",
                 "47|61",
                 "75|61",
                 "47|29",
                 "75|13",
                 "53|13",
                 "",
                 "75,47,61,53,29",
                 "97,61,53,29,13",
                 "75,29,13",
                 "75,97,47,61,53",
                 "61,13,29",
                 "97,13,75,29,47"]
        arr = arr_a
        pass
    else:
        with open("inputs/input_05.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    a, b = advent(arr)
    print("a:", a)
    print("b:", b)

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
