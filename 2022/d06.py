#!/usr/bin/env python3

from collections import deque


def advent_ab(signal, n):
    i = 0
    while i < len(signal)-n:
        items = deque(signal)
        items.rotate(-i)

        # print(len(set(list(items)[0:n])))
        if len(set(list(items)[0:n])) == n:
            return i+n
        i += 1
    return -1


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb",
               "bvwbjplbgvbhsrlpgdmjqwftvncz",
               "nppdvjthqldpwncqszvftbrmjlhg",
               "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
               "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]
        pass
    else:
        with open("inputs/input_06.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    for signal in arr:
        print(advent_ab(signal, 4))
    for signal in arr:
        print(advent_ab(signal, 14))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
