#!/usr/bin/env python3

import re
import numpy as np
np.set_printoptions(threshold=np.inf)

from bbox import BoundingBox

# Calculating Manhattan Distance
def manhattan_distance(p1, p2):
    md = 0
    for x1, x2 in zip(p1, p2):
        diff = x2 - x1
        md += abs(diff)
    return md


def bbox_shift(sensors, beacons):
    scoord_all = []
    scoord_for_bbox = []
    md_all = []
    i = 0
    while i < len(sensors):
        s = sensors[i]
        b = beacons[i]

        smd = manhattan_distance(s, b)
        md_all.append(smd)

        smx = [s[0] - smd, s[1]]
        spx = [s[0] + smd, s[1]]
        smy = [s[0], s[1] - smd]
        spy = [s[0], s[1] + smd]

        scoord_all.append([smx, spx, smy, spy])
        scoord_for_bbox.append(s)
        scoord_for_bbox.append(b)
        scoord_for_bbox.append(smx)
        scoord_for_bbox.append(spx)
        scoord_for_bbox.append(smy)
        scoord_for_bbox.append(spy)
        i += 1

    bb = BoundingBox(scoord_for_bbox)
    bbs_size, bbs_new = bb.get_bbox_coord()
    # print(bbs_size)
    coord_shift = [bbs_new[0][0] - sensors[0][0], bbs_new[0][1] - sensors[0][1]]
    # print(coord_shift)

    return coord_shift, bbs_size, md_all


def sites(climit, line_new, sensors, coord_shift, md_all):
    sm_fin = np.zeros((1, climit + 1)).astype(np.int32)

    k = 0
    while k < len(sensors):
        x0 = sensors[k][0] + coord_shift[0]
        y0 = sensors[k][1] + coord_shift[1]
        md = md_all[k]

        d = line_new - y0
        dd = md - abs(d)
        sm_fin[0: 1, x0 - dd: x0 + dd + 1] = 1

        k += 1
    return sm_fin


# full matrix, too big for memory
def advent_a0(sensors, beacons):
    coord_shift, bbs_size, md_all = bbox_shift(sensors, beacons)

    sm_fin = np.zeros((bbs_size)).astype(np.int32)

    k = 0
    while k < len(sensors):
        x0 = sensors[k][0] + coord_shift[0]
        y0 = sensors[k][1] + coord_shift[1]
        sm = np.zeros((bbs_size)).astype(np.int32)

        xb0 = beacons[k][0] + coord_shift[0]
        yb0 = beacons[k][1] + coord_shift[1]

        md = md_all[k]
        for d in range(0, md + 1):
            sm[x0 - (md - d): x0 + (md - d)+1, y0 - d: (y0 - d)+1] = 1
            sm[x0 - (md - d): x0 + (md - d)+1, y0 + d: y0 + d+1] = 1
            sm[x0 - d: x0 - d+1, y0 - (md - d): y0 + (md - d)+1] = 1
            sm[x0 + d: x0 + d+1, y0 - (md - d): y0 + (md - d)+1] = 1

            # sm[1: 2, 2: 3] = 7
            # sm[x0: x0+1, y0: y0+1] = 2
            sm[xb0: xb0+1, yb0: yb0+1] = 3
        if k == 6:
            print(sensors[k])
            print([x0, y0])
            print(beacons[k])
            print([xb0, yb0])
            print(md)
            print(sm)
            print(np.count_nonzero(sm[10+coord_shift[0], :]))
            sm_fin = np.logical_or(sm_fin, sm==1)
            # print(sm_fin)
            print(np.count_nonzero(sm_fin[10+coord_shift[0]]))

        sm_fin = np.logical_or(sm_fin, sm == 1)
        k += 1

    print(sm_fin)
    print(sm_fin[10 + coord_shift[0], :])
    print(np.count_nonzero(sm_fin[10 + coord_shift[0], :]))

    return -1

def advent_a(sensors, beacons, line):
    coord_shift, bbs_size, md_all = bbox_shift(sensors.copy(), beacons.copy())

    line_new = line + coord_shift[1]
    sm_fin = np.zeros((3, bbs_size[0])).astype(np.int32)

    k = 0
    while k < len(sensors):
        x0 = sensors[k][0] + coord_shift[0]
        y0 = sensors[k][1] + coord_shift[1]
        xb0 = beacons[k][0] + coord_shift[0]
        yb0 = beacons[k][1] + coord_shift[1]
        md = md_all[k]

        if y0 - md < line_new < y0 + md:
            sm = np.zeros((3, bbs_size[0])).astype(np.int32)
            # print(k, line_new, y0, y0 - md, y0 + md, line_new - y0)

            d = line_new - y0
            dd = md - abs(d)

            sm[1: 2, x0 - dd: x0 + dd + 1] = 1
            if d > 0:
                sm[0: 1, x0 - dd - 1: x0 + dd + 1 + 1] = 1
                sm[2: 3, x0 - dd + 1: x0 + dd - 1 + 1] = 1
            elif d < 0:
                sm[0: 1, x0 - dd + 1: x0 + dd - 1 + 1] = 1
                sm[2: 3, x0 - dd - 1: x0 + dd + 1 + 1] = 1
            else:
                sm[0: 1, x0 - dd + 1: x0 + dd - 1 + 1] = 1
                sm[2: 3, x0 - dd + 1: x0 + dd - 1 + 1] = 1

            if yb0 == line_new:
                sm[1: 2, xb0: xb0 + 1] = 3
            elif yb0 == line_new + 1:
                sm[2: 3, xb0: xb0 + 1] = 3
            elif yb0 == line_new - 1:
                sm[0: 1, xb0: xb0 + 1] = 3

            # print(np.count_nonzero(sm[1: 2, :]))
            # print(sm)
            sm_fin = np.logical_or(sm_fin, sm == 1)
        k += 1

    # print(sm_fin)
    fin = np.count_nonzero(sm_fin[1:2, :])

    return fin


def advent_b(sensors, beacons, line_max):
    coord_shift, bbs_size, md_all = bbox_shift(sensors, beacons)

    climit = coord_shift[0] + line_max

    start_time = time.time()
    i_init = 0
    i_init = 2767500 # 2767556 it is
    for line in range(i_init, line_max + 1):
        if line % 10000 == 0:
            end_time = time.time()
            elapsed = end_time - start_time
            print(line, "{:.2f}".format(elapsed) + "s")
        line_new = line + coord_shift[1]

        sm_fin = sites(climit, line_new, sensors, coord_shift, md_all)

        fin = np.count_nonzero(sm_fin[0:1, coord_shift[0]:climit+1])
        if fin != line_max+1:
            x_empty = np.argwhere(sm_fin[0:1, coord_shift[0]:climit + 1] == 0)
            # print(x_empty[0][1], line)
            return ((x_empty[0][1] * 4000000)+line)
    return -1


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr = ["Sensor at x=2, y=18: closest beacon is at x=-2, y=15",
               "Sensor at x=9, y=16: closest beacon is at x=10, y=16",
               "Sensor at x=13, y=2: closest beacon is at x=15, y=3",
               "Sensor at x=12, y=14: closest beacon is at x=10, y=16",
               "Sensor at x=10, y=20: closest beacon is at x=10, y=16",
               "Sensor at x=14, y=17: closest beacon is at x=10, y=16",
               "Sensor at x=8, y=7: closest beacon is at x=2, y=10",
               "Sensor at x=2, y=0: closest beacon is at x=2, y=10",
               "Sensor at x=0, y=11: closest beacon is at x=2, y=10",
               "Sensor at x=20, y=14: closest beacon is at x=25, y=17",
               "Sensor at x=17, y=20: closest beacon is at x=21, y=22",
               "Sensor at x=16, y=7: closest beacon is at x=15, y=3",
               "Sensor at x=14, y=3: closest beacon is at x=15, y=3",
               "Sensor at x=20, y=1: closest beacon is at x=15, y=3"]
        pass
    else:
        with open("inputs/input_15.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    # get the sensor and beacon positions
    sensors = []
    beacons = []

    i = 0
    while i < len(arr):
        line = arr[i]
        # Find all coordinates (integers)
        idxs = re.findall(pattern=r"[+-]?\d+", string=line)

        sensors.append([int(idxs[0]), int(idxs[1])])
        beacons.append([int(idxs[2]), int(idxs[3])])
        i += 1

    if test:
        line_new = 10
        limit_max = 20
    else:
        line_new = 2000000
        limit_max = 4000000
    print(advent_a(sensors, beacons, line_new))
    print(advent_b(sensors, beacons, limit_max))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
