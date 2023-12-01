#!/usr/bin/env python3

import re


def advent_a(arr, init, crates):
    col_crate = crates.copy()

    i = init + 1
    while i < len(arr):
        line = arr[i]
        if not line:
            break

        moves = line.split(" ")
        ncrates = int(moves[1])
        pos_from = int(moves[3])
        pos_to = int(moves[5])

        no_crates = col_crate[pos_from][0:ncrates]
        if no_crates:
            no_crates.reverse()
        col_crate[pos_from] = col_crate[pos_from][ncrates:]

        no_crates += col_crate[pos_to]
        col_crate[pos_to] = no_crates
        i += 1

    top = ""
    for k in range(1, len(col_crate)+1):
        top = top + col_crate[k][0]

    return top


def advent_b(arr, init, crates):
    col_crate = crates.copy()

    i = init + 1
    while i < len(arr):
        line = arr[i]
        if not line:
            break

        moves = line.split(" ")
        ncrates = int(moves[1])
        pos_from = int(moves[3])
        pos_to = int(moves[5])

        no_crates = col_crate[pos_from][0:ncrates]
        # if no_crates:
        #     no_crates.reverse()
        col_crate[pos_from] = col_crate[pos_from][ncrates:]

        no_crates += col_crate[pos_to]
        col_crate[pos_to] = no_crates
        i += 1

    top = ""
    for k in range(1, len(col_crate)+1):
        top = top + col_crate[k][0]

    return top


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr = ["    [D]",
               "[N] [C]",
               "[Z] [M] [P]",
               " 1   2   3 ",
               "",
               "move 1 from 2 to 1",
               "move 3 from 1 to 3",
               "move 2 from 2 to 1",
               "move 1 from 1 to 2"]
        pass
    else:
        with open("inputs/input_05.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    # get the crate stacks
    crates = {}
    # find the line with number of columns
    columns = []

    i = 0
    moves_i = 0
    while i < len(arr):
        line = arr[i]
        if not line:
            moves_i = i
            break
        # Find all indices of A, B ... Z
        idxs = re.finditer(pattern="[A-Z]", string=line)
        crate_idxs = [idx.start() for idx in idxs]
        # print(crate_idxs)
        # brute force to get rid of all empty spaces and [ ] for 1, 2, 3, .... crate letter
        # from this "[A] [B] [D]" through substring indices
        # [1, 5, 9]
        # to column number
        # [1, 2, 3]
        # there are 4 characters per crate letter: [A]space
        for index in crate_idxs:
            pos = int((index - 1) / 4) + 1
            if pos in crates:
                crates[pos].append(line[index])
            else:
                crates[pos] = [line[index]]

        # number of columns (positions) from line (before empty - moves_i), can be used as a check/test
        # p = re.compile(r"\d+")
        # columns = p.findall(line.strip())
        i += 1
    # print(col_crate)

    print(advent_a(arr, moves_i, crates))
    print(advent_b(arr, moves_i, crates))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
