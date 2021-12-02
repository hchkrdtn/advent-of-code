#!/usr/bin/env python3

import re

def advent_1a(inpt):
    horiz = 0
    depth = 0

    for item in inpt:
        move = int(re.findall(r"\d+", item)[0])
        if item[0] == "u":
            depth -= move
        elif item[0] == "d":
            depth += move
        elif item[0] == "f":
            horiz += move

    return horiz * depth


def advent_1b(inpt):
    horiz = 0
    depth = 0
    aim = 0

    for item in inpt:
        move = int(re.findall(r"\d+", item)[0])
        if item[0] == "u":
            aim -= move
        elif item[0] == "d":
            aim += move
        elif item[0] == "f":
            horiz += move
            depth += aim * move

    return horiz * depth


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
        pass
    else:
        # reading a file line by line into elements of an array
        with open("inputs/input_02.txt") as input:
            arr = input.readlines()

    print(advent_1a(arr))
    print(advent_1b(arr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
