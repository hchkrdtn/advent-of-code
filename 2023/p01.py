#!/usr/bin/env python3

import re
import regex as rex

def advent_a(arr):
    tot = 0
    i = 0
    while i < len(arr):
        vals = re.findall(pattern=r"[+-]?\d", string=arr[i])
        # print(vals)
        if len(vals) == 0:
            val = 0
        elif len(vals) == 1:
            val = int(vals[0] + vals[0])
        else:
            val = int(vals[0] + vals[-1])
        tot += val
        # print(val, tot)

        i += 1
    return tot


def advent_b(arr):
    nums = {"1": "1", "one": "1",
            "2": "2", "two": "2",
            "3": "3", "three": "3",
            "4": "4", "four": "4",
            "5": "5", "five": "5",
            "6": "6", "six": "6",
            "7": "7", "seven": "7",
            "8": "8", "eight": "8",
            "9": "9", "nine": "9"}
    tot = 0
    i = 0
    while i < len(arr):
        # There are so-called overlapped words: "oneight", "threeight", "fiveight", "nineight",
        #                                       "twone", "sevenine", "eightwo", "eightwo, "eighthree"
        # which can be a problem at the end of the string
        # re module can't do it, we need to install and use regex module with overlapped flag
        # for example,  re + oneight at the end of the string gives ["one"]
        #               regex + oneight gives ["one", "eight"]
        vals = rex.findall(pattern=r"one|two|three|four|five|six|seven|eight|nine|\d", string=arr[i], overlapped=True)

        # overlap_vals = re.findall(pattern=r"oneight|threeight|fiveight|nineight|twone|sevenine|eightwo|eighthree", string=arr[i])
        # if overlap_vals:
        #     print(arr[i])
        #     print(overlap_vals)
        #     print(vals)

        # replace spelled digits ("one") with digit string ("1")
        vals = [v.replace(v, nums[v]) for v in vals]
        if len(vals) == 0:
            val = 0
        elif len(vals) == 1:
            val = int(vals[0] + vals[0])
        else:
            val = int(vals[0] + vals[-1])
        tot += val
        # print(val, tot)

        i += 1
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
