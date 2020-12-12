#!/usr/bin/env python3

import numpy as np


def advent_10a(input_nums):
    # add zero
    input_nums.insert(0, 0)
    input_nums = np.asarray(input_nums)
    nums = np.sort(input_nums)
    num_roll = np.roll(nums, 1)
    diff = nums - num_roll
    # results = [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
    #         # {1:7, 3:5}
    # [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
    # 1, 3, 2, 1, 1, 2, 1, 1, 1, 1
    # 1, 3, 2, 1, 1, 2, 1, 1, 1, 1
    results = {}
    results[1] = np.count_nonzero(diff == 1)
    results[2] = np.count_nonzero(diff == 2)
    # the last plus 3
    results[3] = np.count_nonzero(diff == 3) + 1
    print(results)
    return results[1] * results[3]


def get_recursively(diff, results, comb, intr):
    for j in range(0, len(diff)-intr):
        dd = np.asarray(diff[len(diff) - j - intr - 1:len(diff) - j])
        patt = np.repeat(1, intr-1)
        if np.all(np.equal(dd[1:intr], patt)) and dd[0:1][0] != 1 and dd[intr:intr+1][0] != 1:
            if comb in results:
                results[comb] += 1
            else:
                results[comb] = 1
    if intr >= len(diff):
        return results
    else:
        comb += intr - 1
        return get_recursively(diff, results, comb, intr+1)

    # for j in range(0, len(diff)-4):
    #     dd = np.asarray(diff[len(diff) - j - 5:len(diff) - j])
    #     print(dd)
    #     if np.all(np.equal(dd[1:4], np.asarray([1, 1, 1]))) and dd[0:1][0] != 1 and dd[4:5][0] != 1:
    #         if 4 in results:
    #             results[4] += 1
    #         else:
    #             results[4] = 1
    #
    # for j in range(0, len(diff)-5):
    #     dd = np.asarray(diff[len(diff) - j - 6:len(diff) - j])
    #     print(dd)
    #     if np.all(np.equal(dd[1:5], np.asarray([1, 1, 1, 1]))) and dd[0:1][0] != 1 and dd[5:6][0] != 1:
    #         if 7 in results:
    #             results[7] += 1
    #         else:
    #             results[7] = 1


def advent_10b(input_nums):
    # add zero
    input_nums = np.asarray(input_nums)
    nums = np.sort(input_nums)
    nums = np.insert(nums, 0, 0)
    nums = np.append(nums, nums[-1] + 3)
    print(nums)
    results = {}
    num_roll = np.roll(nums, 1)
    diff = nums - num_roll
    print(diff)
    tt = get_recursively(diff, results, 2, 3)
    print(tt)
    tot = 1
    for key in tt:
        tot *= key ** tt[key]
    return tot


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        input_nums = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        # 10a {1:7, 3:5}

        input_nums = []
        input_nums.append(28)
        input_nums.append(33)
        input_nums.append(18)
        input_nums.append(42)
        input_nums.append(31)
        input_nums.append(14)
        input_nums.append(46)
        input_nums.append(20)
        input_nums.append(48)
        input_nums.append(47)
        input_nums.append(24)
        input_nums.append(23)
        input_nums.append(49)
        input_nums.append(45)
        input_nums.append(19)
        input_nums.append(38)
        input_nums.append(39)
        input_nums.append(11)
        input_nums.append(1)
        input_nums.append(32)
        input_nums.append(25)
        input_nums.append(35)
        input_nums.append(8)
        input_nums.append(17)
        input_nums.append(7)
        input_nums.append(9)
        input_nums.append(4)
        input_nums.append(2)
        input_nums.append(34)
        input_nums.append(10)
        input_nums.append(3)
        # 10a {1:22, 3:10}
        pass

    else:
        with open("inputs/input_10.txt", "r") as f:
            input_nums = f.readlines()
            input_nums = [x.strip() for x in input_nums]
            input_nums = list(map(int, input_nums))
        f.close()
        # print(input_nums)

    print(advent_10a(input_nums))
    print(advent_10b(input_nums))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
