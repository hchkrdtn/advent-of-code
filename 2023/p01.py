#!/usr/bin/env python3

import re
import regex as rex

def advent_a(arr):
    tot = 0
    for item in arr:
        vals = re.findall(pattern=r"[+-]?\d", string=item)
        if len(vals) > 0:
            val = int(vals[0] + vals[-1])
            tot += val
    return tot


def advent_b(arr):
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    # pattern=r"one|two|three|four|five|six|seven|eight|nine|\d"
    pat = "|".join(nums) + "|\\d"

    tot = 0
    for item in arr:
        # There are so-called overlapped words: "oneight", "threeight", "fiveight", "nineight",
        #                                       "twone", "sevenine", "eightwo", "eightwo, "eighthree"
        # which can be a problem at the end of the string
        # default re module can't do it, we need to use regex module with overlapped flag
        # for example,  re + oneight at the end of the string gives ["one"]
        #               regex + oneight gives ["one", "eight"]
        # https://stackoverflow.com/questions/5616822/how-to-use-regex-to-find-all-overlapping-matches
        vals = rex.findall(pattern=pat, string=item, overlapped=True)

        # overlap_vals = re.findall(pattern=r"oneight|threeight|fiveight|nineight|twone|sevenine|eightwo|eighthree", string=arr[i])
        # if overlap_vals:
        #     print(item)
        #     print(overlap_vals)
        #     print(vals)

        if len(vals) > 0:
            for k, val in enumerate(vals):
                if val in nums:
                    vals[k] = val.replace(val, str(nums.index(val) + 1))
            val = int(vals[0] + vals[-1])
            tot += val
            # print(val, tot)
    return tot


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr_a = ["dd", "rkzlnmzgnk00zckqprrptnthreefourtwo", "1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
        arr_b = ["two1nine",
                 "eightwothree",
                 "abcone2threexyz",
                 "xtwone3four",
                 "4nineeightseven2",
                 "zoneight234",
                 "7pqrstsixteen"]
        arr = arr_b
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
