#!/usr/bin/env python3

import numpy as np


def advent_a(in_list):
    trees = 0
    forest = np.array(in_list).astype(np.int32)
    print(forest)
    lx = forest.shape[0]
    ly = forest.shape[1]
    tree_edges = 2 * (lx + ly - 2)
    print(lx, ly, tree_edges)

    # left to right
    fmx_left = np.zeros((lx, ly), dtype=np.int32)
    for i in range(0, lx-1):
        if i == 0:
            fmx_left[:, 0] = forest[:, 0]
        else:
            # print(fmx_left[:, i-1])
            # print(forest[:, i])
            fmx_left[:, i] = np.maximum(forest[:, i], fmx_left[:, i-1])
        # print(fmx_left)
    # print(fmx_left)
    fmx_left = fmx_left[:, :-2] < fmx_left[:, 1:-1]
    # print(fmx_left)
    fmx_left = fmx_left[1:-1, :]
    # print(fmx_left)
    tree_left = np.count_nonzero(fmx_left)
    # print(tree_left)

    # right to left
    fmx_right = np.zeros((lx, ly), dtype=np.int32)
    for i in range(0, lx-1):
        if i == 0:
            fmx_right[:, -1 - i] = forest[:, -1 - i]
        else:
            # print(fmx_right[:, - i])
            # print(forest[:, -1 - i])
            fmx_right[:, -1-i] = np.maximum(forest[:, -1-i], fmx_right[:, -i])
        # print(fmx_right)
    # print(fmx_right)
    # print(fmx_right[:, 2:])
    # print(fmx_right[:, 1:-1])
    fmx_right = fmx_right[:, 2:] < fmx_right[:, 1:-1]
    # print(fmx_right)
    fmx_right = fmx_right[1:-1, :]
    # print(fmx_right)
    tree_right = np.count_nonzero(fmx_right)
    # print(tree_right)

    # top to bottom
    fmx_top = np.zeros((lx, ly), dtype=np.int32)
    for i in range(0, ly-1):
        if i == 0:
            fmx_top[i, :] = forest[i, :]
        else:
            # print(fmx_top[i - 1, :])
            # print(forest[i, :])
            fmx_top[i, :] = np.maximum(forest[i, :], fmx_top[i-1, :])
        # print(fmx_top)
    # print(fmx_top)
    # print(fmx_top[0:3, :])
    # print(fmx_top[1:-1, :])
    fmx_top = fmx_top[:-2, :] < fmx_top[1:-1, :]
    # print(fmx_top)
    fmx_top = fmx_top[:, 1:-1]
    # print(fmx_top)
    tree_top = np.count_nonzero(fmx_top)
    # print(tree_top)

    # bottom to top
    fmx_bottom = np.zeros((lx, ly), dtype=np.int32)
    for i in range(0, ly-1):
        if i == 0:
            fmx_bottom[-1, :] = forest[-1, :]
        else:
            # print(fmx_bottom[- i, :])
            # print(forest[-1 - i, :])
            fmx_bottom[-1-i, :] = np.maximum(forest[-1-i, :], fmx_bottom[-i, :])
        # print(fmx_bottom)
    # print(fmx_bottom)
    # print(fmx_bottom[2:, :])
    # print(fmx_bottom[1:-1, :])
    fmx_bottom = fmx_bottom[2:, :] < fmx_bottom[1:-1, :]
    # print(fmx_bottom)
    fmx_bottom = fmx_bottom[:, 1:-1]
    # print(fmx_bottom)
    tree_bottom = np.count_nonzero(fmx_bottom)
    # print(tree_bottom)

    # trees = tree_left + tree_right + tree_top + tree_bottom
    # print(tree_edges, trees)
    # trees = tree_edges + trees
    # print(trees)

    fin_lr = np.logical_or(fmx_left, fmx_right)
    # print(fin_lr)
    # print(np.count_nonzero(fin_lr))

    fin_tb = np.logical_or(fmx_top, fmx_bottom)
    # print(fin_tb)
    # print(np.count_nonzero(fin_tb))

    fin = np.logical_or(fin_lr, fin_tb)
    # print(fin)
    trees = np.count_nonzero(fin)
    print(tree_edges, trees)
    trees = tree_edges + trees
    # print(trees)

    # TEST one line
    # print(forest[:,-3])
    # print(fmx_top[:,-2])
    # print(np.count_nonzero(fmx_top[:,-2]))
    # print(fmx_bottom[:,-2])
    # print(np.count_nonzero(fmx_bottom[:,-2]))
    #
    # fin_test = np.logical_or(fmx_top, fmx_bottom)
    # print(fin_test[:, -2])
    # print(np.count_nonzero(fin_test[:, -2]))

    return trees


def advent_b(in_list):
    forest = np.array(in_list).astype(np.int32)
    print(forest)

    i = 0
    while i < len(in_list):
        if len(in_list) == 1:
            return i
        i += 1
    return -1

if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr = ["30373","25512","65332","33549","35390"]

        in_list = list()
        # in_list = list()
        # in_list.append(list("25512"))
        # in_list.append(list("65332"))
        # in_list.append(list("33549"))
        # in_list.append(list("35390"))
        for line in arr:
            in_list.append(list(line))
        # print(in_list)
        pass
    else:
        in_list = list()
        with open("inputs/input_08.txt", "r") as f:
            for line in f:
                line = line.strip()
                in_list.append(list(line))
        f.close()

    print(advent_a(in_list))
    # print(advent_b(in_list))


    # print(np.max(forest, axis=1))
    # print(np.max(sliding_window_view(forest, window_shape=[1,5]), axis=0))
    # print(np.count_nonzero((forest[:, 0:1] < forest[:, 1:-3])[1:lx - 1, :]))

    # x = np.arange(6)
    # print(x)
    # v = np.lib.stride_tricks.sliding_window_view(x, 3)
    # print(v)
    # # array([[0, 1, 2],[1, 2, 3],[2, 3, 4],[3, 4, 5]])
    # moving_average = v.mean(axis=1)
    # print(moving_average)

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
