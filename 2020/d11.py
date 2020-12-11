#!/usr/bin/env python3

import numpy as np


def get_directions(mtx, i, j):
    kern = np.array([[0,0,0],[0,0,0],[0,0,0]])
    # print(mtx[i - 1:i + 2, j - 1:j + 2])
    kern[1, 1] = mtx[i, j]
    # print("down i+")
    for idx in range(1, mtx.shape[0]-i-1):
        cell = mtx[i+idx:i+idx+1, j:j+1]
        # print(cell[0][0])
        if cell[0][0] == 2:
            kern[2, 1] = 2
            break
        if cell[0][0] == 1:
            kern[2, 1] = 1
            break
        if len(cell) == 0:
            break
    # print("up i-")
    for idx in range(0, i):
        cell = mtx[i-idx-1:i-idx, j:j+1]
        # print(cell[0][0])
        if cell[0][0] == 2:
            kern[0, 1] = 2
            break
        if cell[0][0] == 1:
            kern[0, 1] = 1
            break
        if len(cell) == 0:
            break
    # print("right j+")
    for idx in range(1, mtx.shape[1]-j-1):
        cell = mtx[i:i+1, j+idx:j+idx+1]
        # print(cell[0][0])
        if cell[0][0] == 2:
            kern[1, 2] = 2
            break
        if cell[0][0] == 1:
            kern[1, 2] = 1
            break
        if len(cell) == 0:
            break
    # print("left j-")
    for idx in range(0, j):
        cell = mtx[i:i+1, j-idx-1:j-idx]
        # print(cell[0][0])
        if cell[0][0] == 2:
            kern[1, 0] = 2
            break
        if cell[0][0] == 1:
            kern[1, 0] = 1
            break
        if len(cell) == 0:
            break
    # print("diagonal down right i+j+")
    for idx in range(1, np.min([mtx.shape[0]-i-1, mtx.shape[1]-j-1])):
        cell = mtx[i+idx:i+idx+1, j+idx:j+idx+1]
        # print(cell[0][0])
        if cell[0][0] == 2:
            kern[2, 2] = 2
            break
        if cell[0][0] == 1:
            kern[2, 2] = 1
            break
        if len(cell) == 0:
            break
    # print("diagonal down left i+j-")
    for idx in range(0, np.min([mtx.shape[0]-i-1, j])):
        cell = mtx[i+idx+1:i+idx+2, j-idx-1:j-idx]
        # print(cell[0][0])
        if cell[0][0] == 2:
            kern[2, 0] = 2
            break
        if cell[0][0] == 1:
            kern[2, 0] = 1
            break
        if len(cell) == 0:
            break
    # print("diagonal top right i-j+")
    for idx in range(0, np.min([i, mtx.shape[1]-j-1])):
        cell = mtx[i-idx-1:i-idx, j+idx+1:j+idx+2]
        # print(cell[0][0])
        if cell[0][0] == 2:
            kern[0, 2] = 2
            break
        if cell[0][0] == 1:
            kern[0, 2] = 1
            break
        if len(cell) == 0:
            break
    # print("diagonal top left i-j-")
    for idx in range(0, np.min([i, j])):
        cell = mtx[i-idx-1:i-idx, j-idx-1:j-idx]
        # print(cell[0][0])
        if cell[0][0] == 2:
            kern[0, 0] = 2
            break
        if cell[0][0] == 1:
            kern[0, 0] = 1
            break
        if len(cell) == 0:
            break
    return kern


def run_kernel_a(mtx, round):
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
        return np.count_nonzero(mtx_n == 2)
    else:
        return run_kernel_a(mtx_n, round+1)


def run_kernel_b(mtx, round):
    (dx, dy) = np.shape(mtx)
    mtx_n = np.array(mtx, copy=True)
    print(round)
    # print(mtx_n)
    for i in range(1, dx - 1):  # the range starts from 1 to avoid the column and row of zeros, and ends before the last col and row of zeros
        for j in range(1, dy - 1):
            if mtx[i:i+1, j:j+1] == 0:
                continue
            kern = get_directions(mtx, i, j)
            # if i == 2 and j == 1:
            #     print(kern)
            occup = np.count_nonzero(kern == 2)
            if kern[1, 1] != 2 and occup == 0:
                mtx_n[i, j] = 2
            elif kern[1, 1] == 2 and occup - 1 >= 5:
                mtx_n[i, j] = 1
    if np.all(np.equal(mtx_n, mtx)):
        print(mtx_n)
        return np.count_nonzero(mtx_n == 2)
    else:
        return run_kernel_b(mtx_n, round+1)


def advent_11a(input_seats):
    # print(input_seats)

    tmp_char = np.array(input_seats)
    grid = tmp_char.astype(np.int)
    # print(grid)
    (x, y) = np.shape(grid)
    grid_n = np.zeros([x+2, y+2]).astype(int)
    grid_n[1:x+1, 1:y+1] = grid

    grid_res = run_kernel_a(grid_n, 0)
    return grid_res


def advent_11b(input_seats):
    # print(input_seats)
    tmp_char = np.array(input_seats)
    grid = tmp_char.astype(np.int)
    # print(grid)
    (x, y) = np.shape(grid)
    grid_n = np.zeros([x+2, y+2]).astype(int)
    grid_n[1:x+1, 1:y+1] = grid

    # print(get_directions(grid_n, 2, 1))
    grid_res = run_kernel_b(grid_n, 0)
    return grid_res


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
    print(advent_11b(input_seats))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
