#!/usr/bin/env python3

import numpy as np
import re


def advent_a(input, dirs):
    space = np.array(input)
    space_fin = np.copy(space.astype(np.int8))

    # print(space_fin)
    pidx = np.where(space_fin[0, :] == 1)
    print(pidx)

    space_fin[0, np.min(pidx)] = 3

    moves = re.findall(pattern=r"[RL]?\d+", string=dirs)
    d = ""
    for i in range(0, len(moves)):
        move = moves[i]
        if i == 0:
            l = re.findall(pattern=r"\d+", string=dirs)[0]
        else:
            arr = re.findall(pattern=r"([RL])(\d+)", string=move)
            d = arr[0][0]
            l = int(arr[0][1])
        # # for k in range(0, )
        print(d, l)

    print(space_fin)
    return -1


def advent_b(input, dir):

    return -1


if __name__ == "__main__":
    import time

    start_time = time.time()

    input = list()

    test = True
    if test:
        input.append(list("        ...#    ".replace(" ", "0").replace(".", "1").replace("#", "2")))
        input.append(list("        .#..    ".replace(" ", "0").replace(".", "1").replace("#", "2")))
        input.append(list("        #...    ".replace(" ", "0").replace(".", "1").replace("#", "2")))
        input.append(list("        ....    ".replace(" ", "0").replace(".", "1").replace("#", "2")))
        input.append(list("...#.......#    ".replace(" ", "0").replace(".", "1").replace("#", "2")))
        input.append(list("........#...    ".replace(" ", "0").replace(".", "1").replace("#", "2")))
        input.append(list("..#....#....    ".replace(" ", "0").replace(".", "1").replace("#", "2")))
        input.append(list("..........#.    ".replace(" ", "0").replace(".", "1").replace("#", "2")))
        input.append(list("        ...#....".replace(" ", "0").replace(".", "1").replace("#", "2")))
        input.append(list("        .....#..".replace(" ", "0").replace(".", "1").replace("#", "2")))
        input.append(list("        .#......".replace(" ", "0").replace(".", "1").replace("#", "2")))
        input.append(list("        ......#.".replace(" ", "0").replace(".", "1").replace("#", "2")))
        dir = "10R5L5R10L4R5L5"

        pass
    else:
        dir = ""
        flag = True
        with open("inputs/input_22.txt", "r") as f:
            for line in f:
                if line.strip():
                    if flag:
                        mx = list(line.replace(" ", "0").replace(".", "1").replace("#", "2"))
                        input.append(mx[0:-1])
                    else:
                        dir = line
                else:
                    print("line", line)
                    flag = False
        f.close()

    # print(input)
    # print(dir)

    print(advent_a(input, dir))
    print(advent_b(input, dir))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
