#!/usr/bin/env python

import numpy as np
import pandas as pd


# # helpers in development, positive (p), negative (n)
# def one_space_pp():
#     space = np.zeros((10, 15))
#     c0 = [3, 2]
#     c1 = [4, 5]
#     cd0 = c1[0] - c0[0]
#     cd1 = c1[1] - c0[1]
#     min = compute_hcf(abs(cd0), abs(cd1))
#     print(min, cd0, cd1)
#     x = c1[0]
#     y = c1[1]
#     while x < 10 and y < 15:
#         print(x, y)
#         space[x, y] = 9
#         y += int(cd1 / min)
#         x += int(cd0 / min)
#     space[c0[0], c0[1]] = 1
#     space[c1[0], c1[1]] = 2
#     print(space)
#
#     return 1
#
# def one_space_nn():
#     space = np.zeros((10, 15))
#     c0 = [9, 9]
#     c1 = [7, 8]
#     cd0 = c1[0] - c0[0]
#     cd1 = c1[1] - c0[1]
#     min = compute_hcf(abs(cd0), abs(cd1))
#     print(min, cd0, cd1)
#     x = c1[0]
#     y = c1[1]
#     while x >= 0 and y >= 0:
#          print(x, y)
#          space[x, y] = 9
#          y -= int(abs(cd1) / min)
#          x -= int(abs(cd0) / min)
#     space[c0[0], c0[1]] = 1
#     space[c1[0], c1[1]] = 2
#     print(space)
#
#     return 1
#
#
# def one_space_np():
#     space = np.zeros((10, 15))
#     c0 = [9, 4]
#     c1 = [7, 6]
#     cd0 = c1[0] - c0[0]
#     cd1 = c1[1] - c0[1]
#     min = compute_hcf(abs(cd0), abs(cd1))
#     print(min, cd0, cd1)
#     x = c1[0]
#     y = c1[1]
#     while x >= 0 and y < 15:
#         print(x, y)
#         space[x, y] = 9
#         y += int(abs(cd1) / min)
#         x -= int(abs(cd0) / min)
#     space[c0[0], c0[1]] = 1
#     space[c1[0], c1[1]] = 2
#     print(space)
#
#     return 1
#
#
# def one_space_pn():
#     space = np.zeros((10, 15))
#     c0 = [0, 13]
#     c1 = [2, 10]
#     cd0 = c1[0] - c0[0]
#     cd1 = c1[1] - c0[1]
#     min = compute_hcf(abs(cd0), abs(cd1))
#     print(min, cd0, cd1)
#     x = c1[0]
#     y = c1[1]
#     while x < 10 and y >= 0:
#         print(x, y)
#         space[x, y] = 9
#         y -= int(abs(cd1) / min)
#         x += int(abs(cd0) / min)
#     space[c0[0], c0[1]] = 1
#     space[c1[0], c1[1]] = 2
#     print(space)
#
#     return 1


# Function to find HCF (highest common factor) the Using Euclidian algorithm
def compute_hcf(x, y):
    while (y):
        x, y = y, x % y
    return x


def one_space(space, idx, asters):
    yw = space.shape[0]
    xw = space.shape[1]
    stmp = np.zeros((xw, yw))
    c0 = asters[idx]

    aster_one = 0
    for aster in asters:
        c1 = aster
        if c0[0] == c1[0] and c0[1] == c1[1]:
            continue
        cd0 = c1[0] - c0[0]
        cd1 = c1[1] - c0[1]
        dirx = 1
        diry = 1
        if cd1 <= 0:
            diry = -1
        if cd0 <= 0:
            dirx = -1
        min = compute_hcf(abs(cd0), abs(cd1))
        x = c1[0]
        y = c1[1]
        while 0 <= x < xw and yw > y >= 0:
            if x == c1[0] and y == c1[1] and stmp[x, y] != 9:
                stmp[x, y] = 2
            else:
                stmp[x, y] = 9
            y += diry * int(abs(cd1) / min)
            x += dirx * int(abs(cd0) / min)

        if aster_one <= (np.sum(stmp == 2)):
            aster_one = np.sum(stmp == 2)
    return aster_one, stmp


def advent_10a(input):
    # pure coordinates manipulation - turned out to be BAD decision!!
    tmp_char = np.array(input)
    space = tmp_char.astype(np.int)
    space_fin = np.copy(space)

    # get coordinates
    asters = np.argwhere(space == 1)

    asteroids = np.zeros(asters.shape[0])
    for idx in range(asters.shape[0]):
        # print("new loop:", idx)
        aster_one, stmp = one_space(space, idx, asters)
        asteroids[idx] = aster_one
        c0 = asters[idx]
        space_fin[c0[0], c0[1]] = aster_one

    return int(np.amax(asteroids)), asters[np.argmax(asteroids)]


# recursion
def loop(space, k, corig, aster_vap, aster_no):
    print("Loop:", k)

    # get coordinates
    cord = np.argwhere(space == 1)

    # get index of the center asteroid from coordinates, remove the center
    kk = 0
    while kk < cord.shape[0]:
        if cord[kk][0] == corig[0] and cord[kk][1] == corig[1]:
            break
        kk += 1
    cord = np.delete(cord, kk, axis=0)

    # transfer to [0, 0]
    cord00 = cord - corig
    cord_t = np.transpose(cord00)
    # angles
    cord_arct = np.arctan2(cord_t[1], cord_t[0]) * 180 / np.pi
    # distances
    cord_dist = np.linalg.norm([0, 0] - cord00, axis=1)
    cord_t0 = np.transpose(cord)

    # pandas, really great for sorting by multiple axes, "clockwise" motion comes from
    # the proper sorting, in our coordinates (reverted from the puzzle) 180deg is top, <+180 left
    stmp = pd.DataFrame({"cordx": cord_t0[0],
                         "cordy": cord_t0[1],
                         "arct": cord_arct,
                         "dist": cord_dist})
    stmp = stmp.sort_values(by=["arct", "dist"], ascending=[False, True])
    # iloc is the row index, not the index carried from sorting
    cas = stmp.iloc[:, 2]

    # remove double angles
    cas = np.unique(cas)
    cas = np.flipud(cas)
    indcs = []
    # compare unique with doubles, if sorted properly it is enough to remove all
    # coordinates with shortest distance
    for i in range(cas.size):
        for idx in range(stmp.shape[0]):
            # print(stmp["arct"].iloc[idx], stmp["dist"].iloc[idx], cas[i], idx)
            if stmp["arct"].iloc[idx] == cas[i]:
                indcs.append(idx)
                if aster_vap == aster_no - 1:
                    return stmp.iloc[idx]
                aster_vap += 1
                break

    # drop all the unique coordinates
    stmp.drop(indcs)

    return loop(space, k + 1, corig, aster_vap, aster_no)


def advent_10b(input, corig, aster_no):
    tmp_char = np.array(input)
    space = tmp_char.astype(np.int)

    aster_vap = 0
    aster_fin = loop(space, 0, corig, aster_vap, aster_no)
    print(aster_fin)

    return space


if __name__ == "__main__":
    import time

    start_time = time.time()
    test = False

    if test:
        # input = list()
        # # replace to get 0,1 and change to list of individual char
        #
        # input.append(list(".#..#".replace("#","1").replace(".","0")))
        # input.append(list(".....".replace("#","1").replace(".","0")))
        # input.append(list("#####".replace("#","1").replace(".","0")))
        # input.append(list("....#".replace("#","1").replace(".","0")))
        # input.append(list("...##".replace("#","1").replace(".","0")))
        #
        # # position 4,3 with 8 other asteroids detected
        # output = advent_10a(input)
        #
        # # .7..7
        # # .....
        # # 67775
        # # ....7
        # # ...87
        #
        # input = list()
        # input.append(list("......#.#.".replace("#","1").replace(".","0")))
        # input.append(list("#..#.#....".replace("#","1").replace(".","0")))
        # input.append(list("..#######.".replace("#","1").replace(".","0")))
        # input.append(list(".#.#.###..".replace("#","1").replace(".","0")))
        # input.append(list(".#..#.....".replace("#","1").replace(".","0")))
        # input.append(list("..#....#.#".replace("#","1").replace(".","0")))
        # input.append(list("#..#....#.".replace("#","1").replace(".","0")))
        # input.append(list(".##.#..###".replace("#","1").replace(".","0")))
        # input.append(list("##...#..#.".replace("#","1").replace(".","0")))
        # input.append(list(".#....####".replace("#","1").replace(".","0")))
        #
        # # position 5,8 with 33 other asteroids detected
        # output = advent_10a(input)
        #
        # input = list()
        # input.append(list("#.#...#.#.".replace("#","1").replace(".","0")))
        # input.append(list(".###....#.".replace("#","1").replace(".","0")))
        # input.append(list(".#....#...".replace("#","1").replace(".","0")))
        # input.append(list("##.#.#.#.#".replace("#","1").replace(".","0")))
        # input.append(list("....#.#.#.".replace("#","1").replace(".","0")))
        # input.append(list(".##..###.#".replace("#","1").replace(".","0")))
        # input.append(list("..#...##..".replace("#","1").replace(".","0")))
        # input.append(list("..##....##".replace("#","1").replace(".","0")))
        # input.append(list("......#...".replace("#","1").replace(".","0")))
        # input.append(list(".####.###.".replace("#","1").replace(".","0")))
        #
        # # position 1,2 with 35 other asteroids detected
        # output = advent_10a(input)
        #
        # input = list()
        # input.append(list(".#..#..###".replace("#","1").replace(".","0")))
        # input.append(list("####.###.#".replace("#","1").replace(".","0")))
        # input.append(list("....###.#.".replace("#","1").replace(".","0")))
        # input.append(list("..###.##.#".replace("#","1").replace(".","0")))
        # input.append(list("##.##.#.#.".replace("#","1").replace(".","0")))
        # input.append(list("....###..#".replace("#","1").replace(".","0")))
        # input.append(list("..#.#..#.#".replace("#","1").replace(".","0")))
        # input.append(list("#..#.#.###".replace("#","1").replace(".","0")))
        # input.append(list(".##...##.#".replace("#","1").replace(".","0")))
        # input.append(list(".....#.#..".replace("#","1").replace(".","0")))
        #
        # # position 6,3 with 41 other asteroids detected
        # output = advent_10a(input)

        input = list()
        input.append(list(".#....#####...#..".replace("#", "1").replace(".", "0")))
        input.append(list("##...##.#####..##".replace("#", "1").replace(".", "0")))
        input.append(list("##...#...#.#####.".replace("#", "1").replace(".", "0")))
        input.append(list("..#.....#...###..".replace("#", "1").replace(".", "0")))
        input.append(list("..#.#.....#....##".replace("#", "1").replace(".", "0")))
        cord = [3, 8]
        aster_no = 27
        aster_fin = advent_10b(input, cord, aster_no)
        print("10:")
        print(aster_fin)

        input = list()
        input.append(list(".#..##.###...#######".replace("#", "1").replace(".", "0")))
        input.append(list("##.############..##.".replace("#", "1").replace(".", "0")))
        input.append(list(".#.######.########.#".replace("#", "1").replace(".", "0")))
        input.append(list(".###.#######.####.#.".replace("#", "1").replace(".", "0")))
        input.append(list("#####.##.#.##.###.##".replace("#", "1").replace(".", "0")))
        input.append(list("..#####..#.#########".replace("#", "1").replace(".", "0")))
        input.append(list("####################".replace("#", "1").replace(".", "0")))
        input.append(list("#.####....###.#.#.##".replace("#", "1").replace(".", "0")))
        input.append(list("##.#################".replace("#", "1").replace(".", "0")))
        input.append(list("#####.##.###..####..".replace("#", "1").replace(".", "0")))
        input.append(list("..######..##.#######".replace("#", "1").replace(".", "0")))
        input.append(list("####.##.####...##..#".replace("#", "1").replace(".", "0")))
        input.append(list(".#####..#.######.###".replace("#", "1").replace(".", "0")))
        input.append(list("##...#.##########...".replace("#", "1").replace(".", "0")))
        input.append(list("#.##########.#######".replace("#", "1").replace(".", "0")))
        input.append(list(".####.#.###.###.#.##".replace("#", "1").replace(".", "0")))
        input.append(list("....##.##.###..#####".replace("#", "1").replace(".", "0")))
        input.append(list(".#.#.###########.###".replace("#", "1").replace(".", "0")))
        input.append(list("#.#.#.#####.####.###".replace("#", "1").replace(".", "0")))
        input.append(list("###.##.####.##.#..##".replace("#", "1").replace(".", "0")))

        # # position 11,13 with 210 other asteroids detected:
        # output = advent_10a(input)
        # print("10a: ", output)

        cord = [13, 11]
        aster_no = 200
        aster_fin = advent_10b(input, cord, aster_no)
        print("10: ", aster_fin)

    else:
        input = list()
        with open("inputs/input_10.txt", "r") as f:
            for line in f:
                line = line.strip()
                input.append(list(line.replace("#", "1").replace(".", "0")))
        f.close()

        output = advent_10a(input)
        print("10a: ", output)

        cord = [29, 26]
        aster_no = 200
        output = advent_10b(input, cord, aster_no)
        print("10b: ", )
        print(output)

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")