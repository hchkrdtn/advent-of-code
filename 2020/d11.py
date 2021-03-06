#!/usr/bin/env python3

import numpy as np


def get_kernel(part, mtx, i, j):
    if part == "a":
        return mtx[i-1:i+2, j-1:j+2]

    kern = np.array([[0,0,0],[0,0,0],[0,0,0]])
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


def run(mtx, round, *argv):
    # argv [part "a"/"b", n of occupied seats] e.g ["a", 4]
    (dx, dy) = np.shape(mtx)
    mtx_n = np.array(mtx, copy=True)
    # print(round)
    # print(mtx_n)
    # the range starts from 1 because we added 0 pads # to all sides af a matrix
    for i in range(1, dx-1):
        for j in range(1, dy-1):
            if mtx[i:i+1, j:j+1] == 0:
                continue
            kern = get_kernel(argv[0], mtx, i, j)
            occup = np.count_nonzero(kern == 2)
            if kern[1, 1] != 2 and occup == 0:
                mtx_n[i, j] = 2
            elif kern[1, 1] == 2 and occup - 1 >= argv[1]:
                mtx_n[i, j] = 1
    if np.array_equal(mtx_n, mtx):
        # print(mtx_n)
        return np.count_nonzero(mtx_n == 2)
    else:
        return run(mtx_n, round+1, *argv)


def advent_11a(input_seats):
    grid = np.array(input_seats).astype(np.int)
    (x, y) = np.shape(grid)
    grid_n = np.zeros([x+2, y+2]).astype(np.int)
    grid_n[1:x+1, 1:y+1] = grid

    grid_res = run(grid_n, 0, "a", 4)
    return grid_res


def advent_11b(input_seats):
    grid = np.array(input_seats).astype(np.int)
    (x, y) = np.shape(grid)
    grid_n = np.zeros([x+2, y+2]).astype(np.int)
    grid_n[1:x+1, 1:y+1] = grid

    # print(get_directions(grid_n, 2, 1))
    grid_res = run(grid_n, 0, "b", 5)
    return grid_res


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
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
        with open("inputs/input_12.txt", "r") as f:
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
