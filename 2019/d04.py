#!/usr/bin/env python

def valid_a(input):
    digits = [int(x) for x in str(input)]

    isvalid = False
    for idx in range(len(digits) - 1):
        res = digits[idx + 1] - digits[idx]
        # The digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
        if res < 0:
            return False
        # Two adjacent digits are the same (like 22 in 122345).
        if res == 0:
            isvalid = True
    return isvalid


def valid_b(input):
    # The two adjacent matching digits are not part of a larger group of matching digits (like 22 in 122245)
    #   however the 2 adjacent digits have priority (111122 meets the criteria (even though 1 is repeated more
    #   than twice, it still contains a double 22. So does 112223.
    digits = [int(x) for x in str(input)]

    zeros = 0
    isvalid = False
    for idx in range(len(digits) - 1):
        res = digits[idx + 1] - digits[idx]
        if res < 0:
            return False
        if res == 0:
            zeros += 1
        if res > 0:
            if zeros == 1:
                isvalid = True
            zeros = 0
    if zeros == 1 or isvalid:
        return True
    else:
        return False


def advent_4(input):
    interval = input.split("-")
    start = int(interval[0])
    stop = int(interval[1])

    total = 0
    for idx in range(start, stop + 1):
        if valid_a(idx):
            total += 1
    print("4a: ", total)

    total = 0
    for idx in range(start, stop + 1):
        if valid_b(idx):
            total += 1
    print("4b: ", total)


if __name__ == "__main__":
    import time

    start_time = time.time()

    input = 111111
    print(valid_a(input))
    input = 223450
    print(valid_a(input))
    input = 123789
    print(valid_a(input))

    input = 112233
    print(valid_b(input))
    input = 123444
    print(valid_b(input))
    input = 111122
    print(valid_b(input))
    input = 112223
    print(valid_b(input))

    input = "171309 - 643603"
    advent_4(input)

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
