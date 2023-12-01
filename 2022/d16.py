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

# full matrix, too big for memory
def advent_a0(sensors, beacons):
    print(sensors)
    print(beacons)

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
    # print(md_all[6])
    # print(scoord_all[6])

    bb = BoundingBox(scoord_for_bbox)
    bbs_size, bbs_new = bb.get_bbox_coord()
    print(bbs_size)

    coord_shift = [bbs_new[0][0] - sensors[0][0], bbs_new[0][1] - sensors[0][1]]
    print(coord_shift)

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
    # print(sensors)
    # print(beacons)
    # print(line)

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
    climit = coord_shift[0] + line_max

    start_time = time.time()
    for line in range(0, line_max):
        if line % 1000 == 0:
            end_time = time.time()
            elapsed = end_time - start_time
            print(line, "{:.2f}".format(elapsed) + "s")
        line_new = line + coord_shift[1]

        sm_fin = np.zeros((1, climit+1)).astype(np.int32)

        k = 0
        while k < len(sensors):
            x0 = sensors[k][0] + coord_shift[0]
            y0 = sensors[k][1] + coord_shift[1]
            md = md_all[k]

            if y0 - md < line_new < y0 + md:
                sm = np.zeros((1, climit+1)).astype(np.int32)
                # print(k, line_new, y0, y0 - md, y0 + md, line_new - y0)

                d = line_new - y0
                dd = md - abs(d)
                sm[0: 1, x0 - dd: x0 + dd + 1] = 1
                # if yb0 == line_new:
                #     sm[0: 1, xb0: xb0 + 1] = 3
                sm_fin = np.logical_or(sm_fin, sm == 1)
            k += 1

        fin = np.count_nonzero(sm_fin[0:1, coord_shift[0]:climit+1])
        if fin != line_max+1:
            x_empty = np.argwhere(sm_fin[0:1, coord_shift[0]:climit + 1] == 0)
            print(x_empty[0][1], line)
            return ((x_empty[0][1] * 4000000)+line)

    return -1


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = True
    if test:
        arr = ["Valve AA has flow rate=0; tunnels lead to valves DD, II, BB",
               "Valve BB has flow rate=13; tunnels lead to valves CC, AA",
               "Valve CC has flow rate=2; tunnels lead to valves DD, BB",
               "Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE",
               "Valve EE has flow rate=3; tunnels lead to valves FF, DD",
               "Valve FF has flow rate=0; tunnels lead to valves EE, GG",
               "Valve GG has flow rate=0; tunnels lead to valves FF, HH",
               "Valve HH has flow rate=22; tunnel leads to valve GG",
               "Valve II has flow rate=0; tunnels lead to valves AA, JJ",
               "Valve JJ has flow rate=21; tunnel leads to valve II"]
        pass
    else:
        with open("inputs/input_16.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    # get the sensor and beacon positions
    flows = {}
    valves = {}
    tunnels = {}

    i = 0
    while i < len(arr):
        line = arr[i].split(";")
        # Find all coordinates (integers)
        flow = re.findall(pattern=r"[+-]?\d+", string=line[0])
        valve = re.findall(pattern=r"[A-Z]+", string=line[0])
        tunnel = re.findall(pattern=r"[A-Z]+", string=line[1])
        valves[valve[1]] = int(flow[0])
        tunnels[valve[1]] = tunnel

        # flows.append([int(flows[0]), int(flows[1])])
        # valves.append([int(valves[2]), int(valves[3])])
        i += 1
    print(valves)
    print(tunnels, tunnels.keys(), sorted(tunnels.keys()))

    tunnels_sort = sorted(tunnels.keys())

    # print(advent_a(flows, valves))
    # print(advent_a(sensors, beacons, 2000000))
    # print(advent_b(sensors, beacons, 20))
    # print(advent_b(sensors, beacons, 4000000))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
