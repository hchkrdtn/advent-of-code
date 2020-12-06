#!/usr/bin/env python3

import numpy as np


def advent_5a(input_codes):
    seat_max = 0
    for code in input_codes:
        row = code[0:7].replace("B", "1").replace("F", "0")
        seat = code[-3:].replace("R", "1").replace("L", "0")
        # binary to decimal
        row = int(row, 2)
        seat = int(seat, 2)
        seat_id = row * 8 + seat
        if seat_id > seat_max:
            seat_max = seat_id
    return seat_max


def advent_5b(input_codes):
    plane = np.zeros(len(input_codes))
    for idx, code in enumerate(input_codes):
        row = code[0:7].replace("B", "1").replace("F", "0")
        seat = code[-3:].replace("R", "1").replace("L", "0")
        seat_id = int(row, 2) * 8 + int(seat, 2)
        plane[idx] = seat_id
    plane.sort()
    # print(plane)

    # subtract adjacent numbers,
    # all numbers should be 1 except around the missing number (and first and last maybe)
    missing = np.subtract(plane, np.roll(plane, +1))
    # print(missing)
    my_seat = np.where(missing == 2)
    # print(my_seat, plane[my_seat[0]])
    return int(plane[my_seat[0]]-1)


# brute force
def get_id(code):
    # FBFBBFF RLR
    rows = list(code[:-3])
    seats = list(code[-3:])

    # adds = [64, 32, 16, 8, 4, 2, 1]
    # plane = np.ones((128, 8))
    # print(plane)
    # # 64                                                [0, 127]
    # # 32                                 F 0:63,                               B: 64:127
    # # 16                  F 0:31                         B 32:63           F: 64:91,  B: 92:127
    # # 8           F 0:15        B 16:31         F 32:47        B 48:63
    # # 4       F 0:7 B 8:15  F 16:23 B 24:31 F 32:39 B 40:47  F 48:55 B 56:63
    #
    # F is minus from R coord, L stays
    # B is plus to L coord, R stays
    #
    # binary 1111111

    row = [0, 127]
    seat = [0, 7]
    for idx, let in enumerate(rows):
        d = 2 ** (len(rows) - (idx + 1))
        # if let == "F":
        #     row[1] -= d
        if let == "B":
            row[0] += d

    for idx, dir in enumerate(seats):
        d = 2 ** (len(seats) - (idx + 1))
        # if dir == "L":
        #     seat[1] -= d
        if dir == "R":
            seat[0] += d
    seat_id = row[0] * 8 + seat[0]
    # print([row[0], seat[0]], seat_id)
    return seat_id


def advent_5a_brute(input_codes):
    seat_max = 0
    for code in input_codes:
        seat_id = get_id(code)
        if seat_id > seat_max:
            seat_max = seat_id
    return seat_max


def advent_5b_brute(input_codes):
    plane = np.zeros(len(input_codes))
    for idx, code in enumerate(input_codes):
        seat_id = get_id(code)
        plane[idx] = seat_id
    plane.sort()
    # subtract adjacent numbers,
    # all numbers should be 1 except around the missing number (and first and last maybe)
    missing = np.subtract(plane, np.roll(plane, +1))
    # print(missing)
    my_seat = np.where(missing == 2)
    # print(my_seat, plane[my_seat[0]])
    return int(plane[my_seat[0]]-1)


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        # test only for 5a
        input_codes = []
        input_codes.append("FBFBBFFRLR")
        input_codes.append("BFFFBBFRRR")
        input_codes.append("FFFBBBFRRR")
        input_codes.append("BBFFBBFRLL")
        # input_codes = ["BBBBBBBRRR"]
        pass
    else:
        with open("inputs/input_05.txt", "r") as f:
            input_codes = f.readlines()
            # remove whitespace characters like `\n` at the end of each line
            input_codes = [x.strip() for x in input_codes]
        f.close()
        # print(input_code)

    print("max BBBBBBBRRR:",str(127 * 8 + 7))

    print(advent_5a(input_codes))
    # print(advent_5a_brute(input_codes))
    print(advent_5b(input_codes))
    # print(advent_5b_brute(input_codes))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
