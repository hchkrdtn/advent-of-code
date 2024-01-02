#!/usr/bin/env python3

import numpy as np
import math
import collections as cs


def is_valid(mtx, nx, ny, x, y, prev, new):
    if x < 0 or x >= nx or y < 0 or y >= ny or mtx[x][y] != prev or mtx[x][y] == new:
        return False
    return True


def flood_fill_bfs(mtx, nx, ny, x, y, prev, new):
    queue = []

    # Append the position of starting pixel of the component
    queue.append([x, y])

    # Color the pixel with the new color
    mtx[x][y] = new

    # While the queue is not empty i.e. the whole component having prev color is not colored with new color
    while queue:
        # Dequeue the front node
        currPixel = queue.pop()

        posX = currPixel[0]
        posY = currPixel[1]

        # Check if the adjacent pixels are valid
        if is_valid(mtx, nx, ny, posX + 1, posY, prev, new):
            # Color with newC if valid and enqueue
            mtx[posX + 1][posY] = new
            queue.append([posX + 1, posY])

        if is_valid(mtx, nx, ny, posX - 1, posY, prev, new):
            mtx[posX - 1][posY] = new
            queue.append([posX - 1, posY])

        if is_valid(mtx, nx, ny, posX, posY + 1, prev, new):
            mtx[posX][posY + 1] = new
            queue.append([posX, posY + 1])

        if is_valid(mtx, nx, ny, posX, posY - 1, prev, new):
            mtx[posX][posY - 1] = new
            queue.append([posX, posY - 1])

def flood_fill_dsf(mtx, nx, ny, x, y, prev, new):
    # Condition for checking out of bounds
    if x < 0 or x >= nx or y < 0 or y >= ny:
        return

    if mtx[x][y] != prev:
        return

    mtx[x][y] = new
    flood_fill_dsf(mtx, nx, ny, x - 1, y, prev, new)  # left
    flood_fill_dsf(mtx, nx, ny, x + 1, y, prev, new)  # right
    flood_fill_dsf(mtx, nx, ny, x, y + 1, prev, new)  # top
    flood_fill_dsf(mtx, nx, ny, x, y - 1, prev, new)  # bottom


def parse_coord(arr, puzz, all):
    cs = [(0, 0)]
    cs_all = [(0, 0)]

    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0
    for item in arr:
        # print(item)
        dc = item.split(" ")
        if puzz == "b":
            dc[1] = int(dc[2][2:7], 16)
            if dc[2][7:8] == 0:
                dc[0] = "R"
            elif dc[2][7:8] == 1:
                dc[0] = "D"
            elif dc[2][7:8] == 2:
                dc[0] = "L"
            elif dc[2][7:8] == 3:
                dc[0] = "U"

        for i in range(1, int(dc[1]) + 1):
            max_x = max(max_x, cs[-1][0])
            max_y = max(max_y, cs[-1][1])
            min_x = min(min_x, cs[-1][0])
            min_y = min(min_y, cs[-1][1])
            if dc[0] == "R":
                if all:
                    cs_all.append((cs[-1][0], cs[-1][1] + i))
                if i == int(dc[1]):
                    cs.append((cs[-1][0], cs[-1][1] + int(dc[1])))
            elif dc[0] == "L":
                if all:
                    cs_all.append((cs[-1][0], cs[-1][1] - i))
                if i == int(dc[1]):
                    cs.append((cs[-1][0], cs[-1][1] - int(dc[1])))
            elif dc[0] == "D":
                if all:
                    cs_all.append((cs[-1][0] + i, cs[-1][1]))
                if i == int(dc[1]):
                    cs.append((cs[-1][0] + int(dc[1]), cs[-1][1]))
            elif dc[0] == "U":
                if all:
                    cs_all.append((cs[-1][0] - i, cs[-1][1]))
                if i == int(dc[1]):
                    cs.append((cs[-1][0] - int(dc[1]), cs[-1][1]))
    nx = abs(min_x) + abs(max_x)
    ny = abs(min_y) + abs(max_y)

    # print(nx, ny, min_x, max_x, min_y, max_y)
    # print(coords)

    cs_fin = []
    for c in cs:
        cs_fin.append((c[0] - min_x, c[1] - min_y))

    cs_all_fin = []
    if all:
        for c in cs_all:
            cs_all_fin.append((c[0] - min_x, c[1] - min_y))

    return cs_fin, cs_all_fin, nx, ny


def parse_coord_b(arr):
    area = 0
    cs = [(0, 0)]

    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0
    for item in arr:
        dc = item.split(" ")
        hex = int(dc[2][2:7], 16)
        hex_last = int(dc[2][7:8])

        max_x = max(max_x, cs[-1][0])
        max_y = max(max_y, cs[-1][1])
        min_x = min(min_x, cs[-1][0])
        min_y = min(min_y, cs[-1][1])
        if hex_last == 0:   # "R"
            cs.append((cs[-1][0], cs[-1][1] + int(hex)))
        elif hex_last == 1: # "D"
            cs.append((cs[-1][0] + int(hex), cs[-1][1]))
        elif hex_last == 2: # "L"
            cs.append((cs[-1][0], cs[-1][1] - int(hex)))
        elif hex_last == 3: # "U"
            cs.append((cs[-1][0] - int(hex), cs[-1][1]))

    nx = abs(min_x) + abs(max_x)
    ny = abs(min_y) + abs(max_y)

    print(nx, ny, min_x, max_x, min_y, max_y)
    print(cs)

    cs_fin = []
    for i,c in enumerate(cs):
        cs_fin.append((c[0] - min_x, c[1] - min_y))

        if i > 0:
            dc = arr[i-1].split(" ")
            hex = int(dc[2][2:7], 16)
            hex_last = int(dc[2][7:8])

            # wrong
            if hex_last == 0:
                # dir = "R"
                area += int(hex) * (nx - cs_fin[-1][0])
                area -= int(hex)
            elif hex_last == 1:
                # dir = "D"
                area += int(hex)
            elif hex_last == 2:
                # dir = "L"
                area -= int(hex) * (nx - cs_fin[-1][0])
                area += int(hex)
            elif hex_last == 3:
                # dir = "U"
                area += int(hex)


    return cs_fin, nx, ny, area


def advent_a(arr):
    tot = 0
    line = 0

    cs_fin, cs_all_fin, nx, ny = parse_coord(arr, "a", True)

    n = len(cs_fin)
    for i in range(0, n):
        qx = cs_fin[i][0]
        qy = cs_fin[i][1]
        if i == 0:
            px = cs_fin[0][0]
            py = cs_fin[0][1]
        else:
            px = cs_fin[i-1][0]
            py = cs_fin[i-1][1]
        line += math.dist([px, py], [qx, qy])

    # print(line)
    grid = []
    # print(nx, ny)
    for i in range(nx + 1):
        grid.append(["."] * (ny + 1))

    for c in cs_all_fin:
        # print(coord)
        wh = grid[c[0]]
        wh[c[1]] = "#"
        # grid[c[0], c[1]] = "#"

    for i in range(nx + 1):
        pass
        # print(grid[i])

    # flood_fill_dsf(grid, nx, ny, 1, 1, ".", "o")
    # I don't know which one is in and which out, half and half starting was a nice compromise, turned out to be correct :-)
    flood_fill_bfs(grid, nx, ny, int(nx/2), int(ny/2), ".", "o")

    fill = 0
    for i in range(nx + 1):
        # print(grid[i])
        for j in grid[i]:
            if j == "o":
                fill += 1

    print(tot, line, fill)
    tot = int(line + fill)

    return tot


def advent_b(arr):
    tot = 0

    cs_fin, nx, ny, area = parse_coord_b(arr)
    print(cs_fin, nx, ny, area)

    return tot


if __name__ == "__main__":
    import time

    start_time = time.time()
    # Production part b is wrong after refactoring
    test = True
    if test:
        arr = ["R 6 (#70c710)",
               "D 5 (#0dc571)",
               "L 2 (#5713f0)",
               "D 2 (#d2c081)",
               "R 2 (#59c680)",
               "D 2 (#411b91)",
               "L 5 (#8ceee2)",
               "U 2 (#caa173)",
               "L 1 (#1b58a2)",
               "U 2 (#caa171)",
               "R 2 (#7807d2)",
               "U 3 (#a77fa3)",
               "L 2 (#015232)",
               "U 2 (#7a21e3)"]
        pass
    else:
        input = list()
        with open("inputs/input_18.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    print(advent_a(arr))
    # b is wrong
    print(advent_b(arr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
