#!/usr/bin/env python3
from typing import Optional

import numpy as np
np.set_printoptions(threshold=np.inf)
from collections import deque


def move_piece(p: np.array, ds: str) -> np.array:
    """ Get a new position based on the move.

    Args:
        p (np.array): Piece coordinates.
        ds (str): direction, > or <

    Returns:
        np.array: Shifted position of the piece.


    """
    if (ds == ">" and not np.any(p[:, -1])) or (ds == "<" and not np.any(p[:, 0])):
        d = int(ds.replace(">", "1").replace("<", "-1"))

        return np.roll(p, d, axis=1)
    return p


def move_piece_1d(p: np.array, ds: str) -> np.array:
    """ Get a new position based on the move.

    Args:
        p (np.array): Piece coordinates.
        ds (str): direction, > or <

    Returns:
        np.array: Shifted position of the piece.


    """
    if (ds == ">" and not np.any(p[-1])) or (ds == "<" and not np.any(p[0])):
        d = int(ds.replace(">", "1").replace("<", "-1"))

        return np.roll(p, d)
    return p


def move_piece_1d2(b: np.array, pd: np.array, pt: np.array, ds: str, flags: list) -> np.array:
    """ Get a new position based on the move.

    Args:
        b (np.array): Bottom box coordinates.
        p (np.array): Piece coordinates.
        ds (str): direction, > or <

    Returns:
        np.array: Shifted position of the piece.

    """
    if ds == ">":
        d = int(ds.replace(">", "1"))
        pidx = np.where(pd > 0)
        if not pd[-1]:
            try:
                last = pidx[0][-1]
                print("compare", pd[last], b[last + 1], flags[0])
                if pd[last] <= b[last + 1] or flags[0]:
                    if pt[last] == b[last + 1]:
                        flags[0] = False
                    else:
                        flags[0] = True
                    print("no right", pd[last], b[last + 1])
                    return pd, pt, flags
            except:
                print("no")
                return pd, pt, flags
            print(ds)
            return np.roll(pd, d), np.roll(pt, d), flags

    elif ds == "<":
        d = int(ds.replace("<", "-1"))
        pidx = np.where(pd > 0)
        if not pd[0]:
            try:
                first = pidx[0][0]
                print("compare", pd[first], b[first - 1], flags[0])
                if pd[first] <= b[first - 1] or flags[1]:
                    if pt[first] == b[first - 1]:
                        flags[1] = False
                    else:
                        flags[1] = True
                    print("no left")
                    # print("first", first, pd, pd[first], b, b[first - 1])
                    return pd, pt, flags
            except:
                print("no")
                return pd, pt, flags
            print(ds)
            return np.roll(pd, d), np.roll(pt, d), flags
    print(ds, "no")
    return pd, pt, flags


def move_piece_bt(p: list, ds: str) -> Optional[list]:
    """ Get a new position based on the move.

    Args:
        p (list): Piece bottom coordinates.
        ds (str): direction, > or <

    Returns:
        list: Shifted position of the piece.

    """
    if (ds == ">" and not p[-1]) or (ds == "<" and not p[0]):
        dp = deque(p)
        d = int(ds.replace(">", "1").replace("<", "-1"))
        dp.rotate(d)

        return list(dp)
    return p


def drop(bottom, p_bt, dir_all):
    # Each rock appears so that its left edge is two units away from the left wall
    # and its bottom edge is three units above the highest rock in the room
    # (or the floor, if there isn't one).
    top_max = np.max(bottom)
    drop_max = 3

    pba = np.array(p_bt[0])
    pta = np.array(p_bt[1])

    pba_drop = np.where(pba > 0, pba + top_max + drop_max, pba)
    pta_drop = np.where(pta > 0, pta + top_max + drop_max, pta)

    # i = 0
    # while i < 10:
    #     p = move_piece(p, dirall[i])
    #     print(p)
    #     i += 1

    # i = 0
    # while i < 10:
    #     pb = move_piece_bt(pb, dirall[i])
    #     pt = move_piece_bt(pt, dirall[i])
    #     print([pb, pt])
    #     i += 1

    i = 0
    while i < 1000:
        # print(i)
        # shift piece coordinates
        if i == 0:
            flags = [False, False]
            print("new piece", bottom, pba, pta, pba_drop, pta_drop, top_max, )
            pba_drop, pta_drop, flags = move_piece_1d2(bottom, pba_drop, pta_drop, dir_all[0], flags)
        else:
            dir_all.rotate(-1)

            # pba_drop = move_piece_1d(pba_drop, dir_all[0])
            # pta_drop = move_piece_1d(pta_drop, dir_all[0])

            # check for adjacent pieces blocking movement sideways
            pba_drop, pta_drop, flags = move_piece_1d2(bottom, pba_drop, pta_drop, dir_all[0], flags)

        tmp = pba_drop - (bottom + 1)
        print(tmp)
        tmp = tmp[np.where(pba_drop > 0)]
        print(pba_drop, tmp, bottom[np.where(pba_drop > 0)], bottom, i)
        if tmp[0] < 0:
            break
        # tmp = np.array([1,1,0,0,0,0,1])
        # only the pieces
        print(np.array_equal(tmp, bottom[np.where(pba_drop > 0)]))
        if np.any(tmp == 0):
            bottom = np.where(pba_drop > 0, pta_drop, bottom)
    #         print(bottom)
    #         bottom = np.where(np.array([0,0,3,4,3,0,0]) > 0, [0,0,3,4,3,0,0], [0,0,1,1,1,1,0])
            print(bottom)
    #         print(i, bottom, pta_drop, np.max(bottom))
            dir_all.rotate(-1)
            return bottom, dir_all
        else:
            pba_drop = np.where(pba_drop > 0, pba_drop - 1, pba_drop)
            pta_drop = np.where(pta_drop > 0, pta_drop - 1, pta_drop)
        i += 1

    # full   =      .......
    # bottom =  [0, 0, 0, 0, 0, 0, 0]       top_max = 0

    # p1b    = [[n, n, 1, 1, 1, 1, n], [n, n, 1, 1, 1, 1, n]]
    #               ..xxxx.
    # bottom =  [0, 0, 1, 1, 1, 1, 0]       top_max = 1

    # p1b    = [[n, n, 2, 2, 2, 2, n], [n, n, 2, 2, 2, 2, n]]   add top_max to p1b
    #               ..xxxx.
    #               ..xxxx.
    # bottom =  [0, 0, 2, 2, 2, 2, 0]       top_max = 2

    # p1b    = [[n, n, 3, 3, 3, 3, n], [n, n, 3, 3, 3, 3, n]]   add top_max to p1b
    #               ..xxxx.
    #               ..xxxx.
    #               ..xxxx.
    # bottom =  [0, 0, 3, 3, 3, 3, 0]       top_max = 3

    # ########### p2b ################
    # full   =      .......
    # bottom =  [0, 0, 0, 0, 0, 0, 0]       top_max = 0

    # p2b    = [[n, n, 2, 1, 2, n, n], [n, n, 2, 3, 2, n, n]]
    #               ...x...
    #               ..xxx..
    #               ...x...
    # bottom =  [0, 0, 2, 3, 2, 0, 0]       top_max = 3

    # p2b    = [[n, n, 5, 4, 5, n, n], [n, n, 5, 6, 5, n, n]]   add top_max to p2b
    #               ...x...
    #               ..xxx..
    #               ...x...
    #               ...x...
    #               ..xxx..
    #               ...x...
    # p2b-bot+1 [n, n, 2, 0, 2, n, n],  # hit zero, stop
    # bottom =  [0, 0, 5, 6, 5, 0, 0]       top_max = 6
    # bottom =                         [0, 0, 5, 6, 5, 0, 0] # add with old bottom where my piece non zero

    # ########### p2b shift #########
    # full   =      .......
    # bottom =  [0, 0, 0, 0, 0, 0, 0]       top_max = 0

    # p2b    = [[n, n, 2, 1, 2, n, n], [n, n, 2, 3, 2, n, n]]
    #               ...x...
    #               ..xxx..
    #               ...x...
    # bottom =  [0, 0, 2, 3, 2, 0, 0]       top_max = 3

    # shift
    # p2b    = [[n, 5, 4, 5, n, n, n], [n, 5, 6, 5, n, n, n]]   add top_max to p2b
    #               ..x....
    #               .xxx...
    #               ..x....
    #               ...x...
    #               ..xxx..
    #               ...x...
    # p2b-bot+1 [n, 4, 1, 1, n, n, n],  # not zero, drop
    # p2b    = [[n, 4, 3, 4, n, n, n], [n, 4, 5, 4, n, n, n]]
    #               ..x....
    #               .xxx...
    #               ..xx...
    #               ..xxx..
    #               ...x...
    # p2b-bot+1 [n, 3, 0, 0, n, n, n], # hit zero, drop
    # bottom =  [0, 4, 5, 4, 2, 0, 0]

    ##################   Example  #####################
    #            .......
    # bottom =  [0, 0, 0, 0, 0, 0, 0]       top_max = 0

    #######  piece 1  ######
    # p1b    = [[n, n, 1, 1, 1, 1, n], [n, n, 1, 1, 1, 1, n]]
    #               ..xxxx.
    # bottom =  [0, 0, 1, 1, 1, 1, 0]       top_max = 1

    #######  piece 2  ######
    # p2b    = [[n, n, 2, 1, 2, n, n], [n, n, 2, 3, 2, n, n]]
    # p2b    = [[n, n, 3, 2, 3, n, n], [n, n, 3, 4, 3, n, n]]
    #               ...x...
    #               ..xxx..
    #               ...x...
    #               ..xxxx.
    # bottom =  [0, 0, 3, 4, 3, 1, 0]       top_max = 4

    #######  piece 3  ######
    # p3b =    [[n, n, 1, 1, 1, n, n], [n, n, 1, 1, 3, n, n]]
    # p3b =    [[n, n, 5, 5, 5, n, n], [n, n, 5, 5, 7, n, n]]
    #               ....x..
    #               ....x..
    #               ..xxx..
    #               ...x...
    #               ..xxx..
    #               ...x...
    #               ..xxxx.
    # bottom =  [0, 0, 5, 5, 7, 1, 0]       top_max = 7

    #######  piece 4  ######
    # p4b    = [[n, n, 1, n, n, n, n], [n, n, 4, n, n, n, n]]
    #               ..x....
    #               ..x....
    #               ..x.x..
    #               ..x.x..
    #               ..xxx..
    #               ...x...
    #               ..xxx..
    #               ...x...
    #               ..xxxx.
    # bottom =  [0, 0, 9, 5, 7, 1, 0]       top_max = 9

    #######  piece 5  ######
    # p5b    = [[n, n, 1, 1, n, n, n], [n, n, 2, 2, n, n, n]]
    #               ..xx...
    #               ..xx...
    #               ..x....
    #               ..x....
    #               ..x.x..
    #               ..x.x..
    #               ..xxx..
    #               ...x...
    #               ..xxx..
    #               ...x...
    #               ..xxxx.
    # bottom =  [0, 0, 11, 11, 7, 1, 0]       top_max = 11

    return [-1]


def advent_a(pieces, p_bottom_top, direction_all):
    bottom = np.array([0, 0, 0, 0, 0, 0, 0])
    # p = pieces[1]

    dir_all = deque(direction_all)

    k = 0
    # while k < 10:
    while k < 2022:
    #     print(p_bottom_top[k%5])
    #     print(dir_all)
        bottom, dir_all = drop(bottom, p_bottom_top[k%5], dir_all)
        k += 1

    return np.max(bottom)


def advent_b(pieces, p_bottom_top, dirall):

    return -1


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = True
    if test:
        str = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
        pass
    else:
        with open("inputs/input_17.txt", "r") as f:
            str = f.readlines()
        f.close()

    dirall = [*str]    # unpack into list of char

    p1 = np.array([[0, 0, 1, 1, 1, 1, 0]])
    p2 = np.array([[0, 0, 0, 1, 0, 0, 0],
                   [0, 0, 1, 1, 1, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0]])
    p3 = np.array([[0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 1, 1, 1, 0, 0]])
    p4 = np.array([[0, 0, 1, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0, 0]])
    p5 = np.array([[0, 0, 1, 1, 0, 0, 0],
                   [0, 0, 1, 1, 0, 0, 0]])

    # bottom, top piece coordinates
    p1b = [[0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 1, 0]]
    p2b = [[0, 0, 2, 1, 2, 0, 0], [0, 0, 2, 3, 2, 0, 0]]
    p3b = [[0, 0, 1, 1, 1, 0, 0], [0, 0, 1, 1, 3, 0, 0]]
    p4b = [[0, 0, 1, 0, 0, 0, 0], [0, 0, 4, 0, 0, 0, 0]]
    p5b = [[0, 0, 1, 1, 0, 0, 0], [0, 0, 2, 2, 0, 0, 0]]

    pieces = [p1, p2, p3,p4, p5]
    p_bottom_top = [p1b, p2b, p3b, p4b, p5b]

    print(advent_a(pieces, p_bottom_top, dirall))
    print(advent_b(pieces, p_bottom_top, dirall))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
