#!/usr/bin/env python3

import numpy as np
import scipy
from scipy import misc


def run_kernel(mtx, round):
    (dx, dy) = np.shape(mtx)
    mtx_n = np.array(mtx, copy=True)
    # print(round)
    # print(mtx_n)
    for i in range(1, dx - 1):  # the range starts from 1 to avoid the column and row of zeros, and ends before the last col and row of zeros
        for j in range(1, dy - 1):
            kern = mtx[i - 1:i + 2, j - 1:j + 2]
            if kern[1, 1] == 0:
                continue
            occup = np.count_nonzero(kern == 2)
            if kern[1, 1] != 2 and occup == 0:
                mtx_n[i, j] = 2
            elif kern[1, 1] == 2 and occup - 1 >= 4:
                mtx_n[i, j] = 1
    if np.all(np.equal(mtx_n, mtx)):
        print(mtx_n)
        print("DONE")
        return np.count_nonzero(mtx_n == 2)
    else:
        return run_kernel(mtx_n, round+1)

def advent_11a(input_seats):
    # print(input_seats)

    tmp_char = np.array(input_seats)
    grid = tmp_char.astype(np.int)
    print(grid)
    (x, y) = np.shape(grid)
    grid_n = np.zeros([x+2, y+2]).astype(int)
    grid_n[1:x+1, 1:y+1] = grid

    grid_res = run_kernel(grid_n, 0)
    return grid_res


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
        get_recursively(diff, results, comb, intr+1)
    return results

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


def advent_11b(input_seats):
    # add zero
    input_nums = np.asarray(input_seats)
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

    test = True
    if test:
        input_seats = []
        input_seats.append(list("L.LL.LL.LL".replace("L", "1").replace(".", "0")))
        input_seats.append(list("LLLLLLL.LL".replace("L", "1").replace(".", "0")))
        input_seats.append(list("L.L.L..L..".replace("L", "1").replace(".", "0")))
        input_seats.append(list("LLLL.LL.LL".replace("L", "1").replace(".", "0")))
        input_seats.append(list("L.LL.LL.LL".replace("L", "1").replace(".", "0")))
        input_seats.append(list("L.LLLLL.LL".replace("L", "1").replace(".", "0")))
        input_seats.append(list("..L.L.....".replace("L", "1").replace(".", "0")))
        input_seats.append(list("LLLLLLLLLL".replace("L", "1").replace(".", "0")))
        input_seats.append(list("L.LLLLLL.L".replace("L", "1").replace(".", "0")))
        input_seats.append(list("L.LLLLL.LL".replace("L", "1").replace(".", "0")))
        # rules
        # 000      000
        # 000  ->  010
        # 000      000
        #
        # 4 or more occupied
        # 111      111
        # 010  ->  000
        # 100      100
        pass
    else:
        input_seats = list()
        with open("inputs/input_11.txt", "r") as f:
            for line in f:
                line = line.strip()
                input_seats.append(list(line.replace("L", "1").replace(".", "0")))
        f.close()
        # print(input_seats)


    print(advent_11a(input_seats))
    # print(advent_11b(input_seats))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
