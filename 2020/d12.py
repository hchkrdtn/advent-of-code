#!/usr/bin/env python3

import re


def advent_12a(input):
    ship = ["E", 0, 0]
    star = ["N", "E", "S", "W"]

    for inp in input:
        d, v = re.match(r"^(.)(\d+)$", inp).groups()
        v = int(v)
        if d == "L" or d == "R":
            idx = star.index(ship[0])
            if d == "L":
                v = -v
            ship[0] = star[(idx + int(v/90)) % 4]  # rotate index by multiple of 90
            continue
        elif d == "F":
            d = ship[0]

        if d == "N":
            ship[2] += - v
        elif d == "S":
            ship[2] += v
        elif d == "E":
            ship[1] += v
        elif d == "W":
            ship[1] += - v
    return abs(ship[1]) + abs(ship[2])


def advent_12b(input):
    ship = [0, 0]
    waypoint = [10, -1]
    for inp in input:
        d, v = re.match(r"^(.)(\d+)$", inp).groups()
        v = int(v)
        if d == "L" or d == "R":
            for i in range(0, int(v / 90)):
                if d == "L":
                    # 90deg: index +1 -> +0
                    waypoint = [waypoint[1], - waypoint[0]]
                else:
                    # 90deg: index +1 -> -0
                    waypoint = [- waypoint[1], waypoint[0]]
        elif d == "F":
            ship[0] += v * waypoint[0]
            ship[1] += v * waypoint[1]
            # print(ship, waypoint)
            continue

        if d == "N":
            waypoint[1] += - v
        elif d == "S":
            waypoint[1] += v
        elif d == "E":
            waypoint[0] += v
        elif d == "W":
            waypoint[0] += - v
        # print(ship, waypoint)
    return abs(ship[0]) + abs(ship[1])


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        in_list = ["F10", "N3", "F7", "R90", "F11"]
        pass
    else:
        with open("inputs/input_12.txt") as f:
            in_list = f.readlines()
        in_list = [x.strip() for x in in_list]

    print(advent_12a(in_list))
    print(advent_12b(in_list))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
