#!/usr/bin/env python

import numpy as np


def advent_2a(inpt):
    n_pswd = 0
    for item in inpt:
        rule, char, pswd = item.split()
        first, second = rule.split("-")

        # list of chars and count of unique chars
        lets, counts = np.unique(list(pswd), return_counts=True)
        # find letter/char
        idxs = np.where(lets == char[0:1])

        # non empty array in tuple
        if idxs[0].size > 0:
            idx = idxs[0].item()
            # print(counts[idx])
            if int(first) <= counts[idx] <= int(second):
                n_pswd += 1
    return n_pswd


def advent_2b(inpt):
    n_pswd = 0
    for item in inpt:
        rule, char, pswd = item.split()
        first, second = rule.split("-")
        idxs = np.where(np.asarray(list(pswd)) == char[0:1])
        if idxs[0].size > 0:
            idx = idxs[0]
            # print(idx)
            # logical XOR of two variables
            if bool(int(first)-1 in idx) ^ bool(int(second)-1 in idx):
                n_pswd += 1
    return n_pswd


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = True
    if test:
        in_list = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
        pass
    else:
        with open("inputs/input_02.txt") as f:
            in_list = f.readlines()
        # remove whitespace characters like `\n` at the end of each line
        in_list = [x.strip() for x in in_list]

    print(advent_2a(in_list))
    print(advent_2b(in_list))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
