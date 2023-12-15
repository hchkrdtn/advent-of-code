#!/usr/bin/env python3

import re
import regex as rex

def advent_a(arr):
    tot = 0

    return tot


def advent_b(arr):
    tot = 0

    return tot


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr = ["dd", "rkzlnmzgnk00zckqprrptnthreefourtwo", "1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
        arr = ["two1nine",
               "eightwothree",
               "abcone2threexyz",
               "xtwone3four",
               "4nineeightseven2",
               "zoneight234",
               "7pqrstsixteen"]
        pass
    else:
        with open("inputs/input_01.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    print(advent_a(arr))
    print(advent_b(arr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
