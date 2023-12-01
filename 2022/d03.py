#!/usr/bin/env python3

import string


def advent_a(arr):
    alphabet_a = string.ascii_lowercase
    alphabet_A = string.ascii_uppercase

    com_type = 0
    i = 0
    while i < len(arr):
        comp12 = arr[i]

        full = len(comp12)
        half = int(full/2)

        comp1 = comp12[0:half]
        comp2 = comp12[half:full]

        # using set() + intersection() to get string intersection
        res = set(comp1).intersection(comp2)

        pos_a = alphabet_a.rfind(list(res)[0]) + 1
        pos_A = alphabet_A.rfind(list(res)[0]) + 1
        if pos_a:
            com_type += pos_a
        elif pos_A:
            com_type += (26 + pos_A)

        # print(alphabet_a.rfind("p"))
        # print(comp1, comp2)
        i += 1

    return com_type


def advent_b(arr):
    alphabet_a = string.ascii_lowercase
    alphabet_A = string.ascii_uppercase

    com_type = 0
    carr = []

    i = 0
    while i < len(arr):
        carr.append(arr[i])

        if len(carr) % 3 == 0:
            res = set(carr[0]).intersection(carr[1], carr[2])

            pos_a = alphabet_a.rfind(list(res)[0]) + 1
            pos_A = alphabet_A.rfind(list(res)[0]) + 1
            if pos_a:
                com_type += pos_a
            elif pos_A:
                com_type += (26 + pos_A)
            carr = []
        i += 1

    return com_type


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr = ["vJrwpWtwJgWrhcsFMMfFFhFp",
               "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
               "PmmdzqPrVvPwwTWBwg",
               "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
               "ttgJtRGJQctTZtZT",
               "CrZsJsPPZsGzwwsLwLmpwMDw"]
        pass
    else:
        with open("inputs/input_03.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    print(advent_a(arr))
    print(advent_b(arr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
