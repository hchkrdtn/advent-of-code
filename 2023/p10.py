#!/usr/bin/env python3

import numpy as np
import shapely.geometry


def start(arr):
    x1 = []
    y1 = []
    # find S
    for i, item in enumerate(arr):
        # print(item)
        if "S" in item:
            x1.append(i)
            y1.append(item.index("S"))
            # print(x1, y1)
            break
    x2 = x1.copy()
    y2 = y1.copy()
    # print(x2, y2)

    east = "-LF"
    west = "-J7"
    north = "|7F"
    south = "|LJ"

    first = False
    second = False

    px1 = x1[-1]
    py1 = y1[-1]
    px2 = x2[-1]
    py2 = y2[-1]

    d1 = ["S"]
    d2 = ["S"]

    left = arr[px1][py1 - 1]
    right = arr[px1][py1 + 1]
    top = arr[px1 - 1][py1]
    bottom = arr[px1 + 1][py1]

    # print(top, north))
    if top in north:
        x1.append(px1 - 1)
        y1.append(py1)
        d1.append(top)
        first = True
    # print(right, west)
    if right in west:
        if first:
            x2.append(px2)
            y2.append(py2 + 1)
            d2.append(right)
            second = True
        else:
            x1.append(px1)
            y1.append(py1 + 1)
            d1.append(right)
            first = True
    # print(bottom, south)
    if bottom in south:
        if first:
            x2.append(px2 + 1)
            y2.append(py2)
            d2.append(bottom)
            second = True
        else:
            x1.append(px1 + 1)
            y1.append(py1)
            d1.append(bottom)
            first = True
    # print(right, east)
    if left in east:
        x2.append(px2)
        y2.append(py2 - 1)
        d2.append(left)
        second = True
    return d1, x1, y1, d2, x2, y2


def full_path(x, y, d, east, west, north, south):
    px = x[-1]
    py = y[-1]
    pd = d[-1]
    if px - 1 >= 0:
        top = arr[px - 1][py]
    else:
        top = ""
    if py + 1 < len(arr[0]):
        right = arr[px][py + 1]
    else:
        right = ""
    if px + 1 < len(arr):
        bottom = arr[px + 1][py]
    else:
        bottom = ""
    if py - 1 >= 0:
        left = arr[px][py - 1]
    else:
        left = ""
    # print(pd, x, y, top, right, bottom, left)
    if pd == "|":
        if len(bottom) > 0 and bottom in south and x[-2] < px:
            # print("|", "bottom", bottom, south)
            d.append(bottom)
            x.append(px + 1)
            y.append(py)
        elif len(top) > 0 and top in north and x[-2] > px:
            # print("|", "top", top, north)
            d.append(top)
            x.append(px - 1)
            y.append(py)
    elif pd == "-":
        if len(left) > 0 and left in east and y[-2] > py:
            # print("-", "left", left, east)
            d.append(left)
            x.append(px)
            y.append(py - 1)
        elif len(right) > 0 and right in west and y[-2] < py:
            # print("-", "right", right, west)
            d.append(right)
            x.append(px)
            y.append(py + 1)
    elif pd == "L":
        if len(top) > 0 and top in north and x[-2] == px:
            # print("L", "top", top, north)
            d.append(top)
            x.append(px - 1)
            y.append(py)
        elif len(right) > 0 and right in west and y[-2] == py:
            # print("L", "right", right, west)
            d.append(right)
            x.append(px)
            y.append(py + 1)
    elif pd == "J":
        if len(top) > 0 and top in north and x[-2] == px:
            # print("J", "top", top, north)
            d.append(top)
            x.append(px - 1)
            y.append(py)
        elif len(left) > 0 and left in east and y[-2] == py:
            # print("J", "left", left, east)
            d.append(left)
            x.append(px)
            y.append(py - 1)
    elif pd == "7":
        if len(bottom) > 0 and bottom in south and x[-2] == px:
            # print("7", "bottom", bottom, south)
            d.append(bottom)
            x.append(px + 1)
            y.append(py)
        elif len(left) > 0 and left in east and y[-2] == py:
            # print("7", "left", left, east)
            d.append(left)
            x.append(px)
            y.append(py - 1)
    elif pd == "F":
        if len(bottom) > 0 and bottom in south and x[-2] == px:
            # print("F", "bottom", bottom, south)
            d.append(bottom)
            x.append(px + 1)
            y.append(py)
        elif len(right) > 0 and right in west and y[-2] == py:
            # print("F", "right", right, east)
            d.append(right)
            x.append(px)
            y.append(py + 1)
    return x, y, d


def advent_a(arr):
    d1, x1, y1, d2, x2, y2 = start(arr)
    # print(d1, x1, y1)
    # print(d2, x2, y2)

    east = "-LF"
    west = "-J7"
    north = "|7F"
    south = "|LJ"
    # S: left/east -LF, right/west -J7, top/north |7F, bottom/south |LJ
    # |: top/north |7F, bottom/south |LJ
    # -: left/east -LF, right/west -J7
    # L: right/west -J7, top/north |7F
    # J: left/east -LF, top/north |7F
    # 7: left/east -LF, bottom/south |LJ
    # F: right/west -J7, bottom/south |LJ

    k = 1
    while True:
        x1, y1, d1 = full_path(x1, y1, d1, east, west, north, south)
        x2, y2, d2 = full_path(x2, y2, d2, east, west, north, south)
        if x1[-1] == x2[-1] and y1[-1] == y2[-1]:
            tot = k + 1
            break
        k += 1
    return tot


def advent_b(arr):
    tot = 0
    d1, x1, y1, d2, x2, y2 = start(arr)
    # print(d1, x1, y1)
    # print(d2, x2, y2)

    east = "-LF"
    west = "-J7"
    north = "|7F"
    south = "|LJ"

    k = 1
    while True:
        x1, y1, d1 = full_path(x1, y1, d1, east, west, north, south)
        if x1[-1] == x2[1] and y1[-1] == y2[1]:
            tot = k + 1
            break
        k += 1

    x1.append(x2[0])
    y1.append(y2[0])
    # x1 = [0, 0, 1, 1, 0]
    # y1 = [0, 1, 1, 0, 0]
    x1 = [1, 1, 2, 7, 7, 6, 5, 5, 2, 2, 3, 4, 5, 5, 7, 7, 7, 1]
    y1 = [1, 9, 9, 9, 6, 6, 6, 8, 8, 2, 2, 2, 2, 4, 4, 3, 1, 1]
    print(x1, y1)
    coords = zip(x1, y1)
    print(coords)

    polygon = shapely.geometry.Polygon(coords)
    print(polygon)
    print(polygon.area)

    # Example polygon with two holes
    inputPolygon = shapely.geometry.Polygon(((0, 0), (10, 0), (10, 10), (0, 10)),
                           (((1, 3), (5, 3), (5, 1), (1, 1)), ((9, 9), (9, 8), (8, 8), (8, 9))))

    polygonExterior = inputPolygon.exterior
    polygonInteriors = []
    for i in range(len(inputPolygon.interiors)):
        # do the stuff with your polygons
        polygonInteriors.append(inputPolygon.interiors[i])

    newPolygon = shapely.geometry.Polygon(polygonExterior, [[pt for pt in inner.coords] for inner in polygonInteriors])
    print(newPolygon)
    print(newPolygon.area)

    return tot


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = True
    if test:
        arr1 = ["-L|F7",
               "7S-7|",
               "L|7||",
               "-L-J|",
               "L|-JF"]
        arr2 = ["7-F7-",
               ".FJ|7",
               "SJLL7",
               "|F--J",
               "LJ.LJ"]
        arr3 = ["...........",
                ".S-------7.",
                ".|F-----7|.",
                ".||.....||.",
                ".||.....||.",
                ".|L-7.F-J|.",
                ".|..|.|..|.",
                ".L--J.L--J.",
                "..........."]
        arr4 = ["..........",
                ".S------7.",
                ".|F----7|.",
                ".||....||.",
                ".||....||.",
                ".|L-7F-J|.",
                ".|..||..|.",
                ".L--JL--J.",
                ".........."]
        arr5 = [".F----7F7F7F7F-7....",
                ".|F--7||||||||FJ....",
                ".||.FJ||||||||L7....",
                "FJL7L7LJLJ||LJ.L-7..",
                "L--J.L7...LJS7F-7L7.",
                "....F-J..F7FJ|L7L7L7",
                "....L7.F7||L7|.L7L7|",
                ".....|FJLJ|FJ|F7|.LJ",
                "....FJL-7.||.||||...",
                "....L---J.LJ.LJLJ..."]
        arr6 = ["FF7FSF7F7F7F7F7F---7",
                "L|LJ||||||||||||F--J",
                "FL-7LJLJ||||||LJL-77",
                "F--JF--7||LJLJ7F7FJ-",
                "L---JF-JLJ.||-FJLJJ7",
                "|F|F-JF---7F7-L7L|7|",
                "|FFJF7L7F-JF7|JL---7",
                "7-L-JL7||F7|L7F-7F7|",
                "L.L7LFJ|||||FJL7||LJ",
                "L7JLJL-JLJLJL--JLJ.L"]
        arr = arr3
        pass
    else:
        with open("inputs/input_10.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    print(advent_a(arr))
    print(advent_b(arr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
