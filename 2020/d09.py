#!/usr/bin/env python3

import numpy as np
import copy
import random


def xmas(inum, input_nums):
    # all combinations
    xv, yv = np.meshgrid(input_nums, input_nums, sparse=False)
    sum_all = xv + yv
    # get the upper triangular part of this matrix
    m = sum_all[np.triu_indices(sum_all.shape[0], k=1)] # offset
    # print(np.unique(m))
    if inum in np.unique(m):
        return True
    else:
        return False


def advent_9a(preamble, previous, input_nums):
    first = 0
    last = preamble

    # test_numbers = [26, 49, 100, 50]
    # test_result = []
    # for inum in test_numbers:
    #     is_valid = xmas(inum, input_nums[first:last])
    #     test_result.append(is_valid)
    # print(test_numbers)
    # print(test_result)
    #
    # test_numbers = [26, 65, 64, 66]
    # test_result = []
    # for inum in test_numbers:
    #     is_valid = xmas(inum, input_nums[first:last])
    #     test_result.append(is_valid)
    # print(test_numbers)
    # print(test_result)

    # print(xmas(55, [15, 25, 47, 40, 62]))
    # print(xmas(65, [25, 47, 40, 62, 55]))

    # print(input_nums)
    # print(preamble, previous, len(input_nums))

    XMAS_weakness = 0
    for i in range(0, len(input_nums) - preamble):
        inum = input_nums[preamble + i: preamble + i + 1][0]
        nums = input_nums[i:preamble + i]
        is_valid = xmas(inum, nums)
        # print(inum, is_valid)
        if not is_valid:
            XMAS_weakness = inum
            break
    return XMAS_weakness


def advent_9b(preamble, previous, input_nums):
    XMAS_weakness = 0
    for i in range(0, len(input_nums) - preamble):
        inum = input_nums[preamble + i: preamble + i + 1][0]
        nums = input_nums[i:preamble + i]
        is_valid = xmas(inum, nums)
        # print(inum, is_valid)
        if not is_valid:
            XMAS_weakness = inum
            break

    encryption_weak = -1
    # remove all numbers > XMAS_weakness
    seq = np.asarray(input_nums)[np.asarray(input_nums) < XMAS_weakness]
    # print(seq)
    # print(np.cumsum(seq))
    for k in range(0, seq.shape[0]):
        seqroll = np.roll(seq, k)
        is_xmas = np.where(np.cumsum(seqroll) == XMAS_weakness)[0]
        if len(is_xmas) > 0:
            consnum = seqroll[0: is_xmas[0] + 1]
            encryption_weak = np.min(consnum) + np.max(consnum)
            break
    return encryption_weak


if __name__ == "__main__":
    import time

    start_time = time.time()

    preamble = 0
    previous = 0

    test = False
    if test:
        # the numbers 1 through 25
        # input_nums = list(range(1, 6))
        # print(input_nums)

        # the numbers 1 through 25 in a random order, no repeat
        input_nums = []
        while len(input_nums) < 25:
            n = random.randint(1, 25)
            if n not in input_nums:
                input_nums.append(n)
        # print(input_nums)

        # swap number 20 with the first one, drop new first (20) and add 46
        if input_nums[0] != 20:
            index = input_nums.index(20)
            first = input_nums[0]
            input_nums[index] = first
        input_nums.append(45)
        input_nums = input_nums[1:]
        # print(input_nums)

        preamble = 25
        previous = 25

        input_nums = []
        input_nums.append(35)
        input_nums.append(20)
        input_nums.append(15)
        input_nums.append(25)
        input_nums.append(47)
        input_nums.append(40)
        input_nums.append(62)
        input_nums.append(55)
        input_nums.append(65)
        input_nums.append(95)
        input_nums.append(102)
        input_nums.append(117)
        input_nums.append(150)
        input_nums.append(182)
        input_nums.append(127)
        input_nums.append(219)
        input_nums.append(299)
        input_nums.append(277)
        input_nums.append(309)
        input_nums.append(576)
        preamble = 5
        previous = 5
        pass

    else:
        with open("inputs/input_09.txt", "r") as f:
            input_nums = f.readlines()
            input_nums = [x.strip() for x in input_nums]
            input_nums = list(map(int, input_nums))
            preamble = 25
            previous = 25
        f.close()
        # print(input_nums)

    print(advent_9a(preamble, previous, input_nums))
    print(advent_9b(preamble, previous, input_nums))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
