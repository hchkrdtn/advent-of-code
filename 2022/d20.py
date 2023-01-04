#!/usr/bin/env python3

from collections import deque


def mix_grove(input, dpi, dpv):
    size = len(input)

    for k in range(size):
        # index of values of indices
        idx = dpi.index(k)

        del dpi[idx] # can't use remove, needs del by index
        del dpv[idx]
        # rotate, -1 to reverse the rotation
        dpi.rotate(input[k] * -1)
        dpv.rotate(input[k] * -1)

        dpi.insert(idx, k)
        dpv.insert(idx, input[k])
    return dpi, dpv


def advent_a(input):
    size = len(input)
    dpv = deque(input.copy())
    dpi = deque([*range(size)])

    dpi, dpv = mix_grove(input, dpi, dpv)

    idx0 = dpi.index(0)

    dpi.rotate(idx0 * -1)
    dpv.rotate(idx0 * -1)
    # print(dpi, dpv)

    idv0 = dpv.index(0)  # test zero = 5, input zero = 4449

    p1 = 1000
    p2 = 2000
    p3 = 3000
    return dpv[(idv0 + p1) % size] + dpv[(idv0 + p2) % size] + dpv[(idv0 + p3) % size]


def advent_b(input):
    decryption_key = 811589153

    input = [int(item) * decryption_key for item in input]
    size = len(input)

    dpv = deque(input.copy())
    dpi = deque([*range(size)])

    for num in range(10):
        dpi, dpv = mix_grove(input, dpi, dpv)

    idv0 = dpv.index(0)  # test zero = 5, input zero = 4449

    p1 = 1000
    p2 = 2000
    p3 = 3000
    return dpv[(idv0 + p1) % size] + dpv[(idv0 + p2) % size] + dpv[(idv0 + p3) % size]


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr = ["1", "2", "-3", "3", "-2", "0", "4"]
        arr = [int(x.strip()) for x in arr]
        pass
    else:
        with open("inputs/input_20.txt", "r") as f:
            arr = f.readlines()
            arr = [int(x.strip()) for x in arr]
        f.close()

    print(advent_a(arr))
    print(advent_b(arr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
