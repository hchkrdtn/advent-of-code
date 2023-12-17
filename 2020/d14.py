#!/usr/bin/env python3

import numpy as np
from itertools import *
import re

def advent_14a(input):
    mask = 0
    memory = {}
    memory_masked = {}
    for inp in input:
        key, value = inp.split(" = ")
        if "mask" in key:
            mask = value
        elif "mem" in key:
            npm = re.match(r"^mem\[(\d+)]$", key).groups()

            valst = str(bin(int(value))[2:].zfill(len(mask)))

            pos_zer = [pos for pos, char in enumerate(mask) if char == "0"]
            pos_one = [pos for pos, char in enumerate(mask) if char == "1"]
            for posz in pos_zer:
                valst = valst[:posz] + "0" + valst[posz + 1:]
            for posz in pos_one:
                valst = valst[:posz] + "1" + valst[posz + 1:]
            print(valst)
            
            memory[npm[0]] = int(value)
            memory_masked[npm[0]] = int(valst, 2)
    print(memory)
    print(memory_masked)

    tot = 0
    for key in memory_masked:
        if memory_masked[key]:
            tot += memory_masked[key]
    return tot


def advent_14b(input):
    mask = 0
    memory = {}
    memory_masked = {}
    for inp in input:
        key, value = inp.split(" = ")
        if "mask" in key:
            mask = value
            print(value)
        elif "mem" in key:
            npm = re.match(r"^mem\[(\d+)]$", key).groups()
            npmst = str(bin(int(npm[0]))[2:].zfill(len(mask)))

            print(npm)
            posX = []
            for pos, char in enumerate(mask):
                if char == "1":
                    npmst = npmst[:pos] + "1" + npmst[pos + 1:]
                elif char == "X":
                    posX.append(pos)

            permuts = list(product([0, 1], repeat=len(posX)))  # the list with all the 64 combinations
            for permut in permuts:
                for idx, posn in enumerate(posX):
                    npmst = npmst[:posn] + str(permut[idx]) + npmst[posn + 1:]
                    memory_masked[int(npmst, 2)] = int(value)
    tot = 0
    for key in memory_masked:
        if memory_masked[key]:
            tot += np.sum(np.asarray(memory_masked[key]))
    return tot


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        in_list = []
        in_list.append("mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        in_list.append("mem[8] = 11")
        in_list.append("mem[7] = 101")
        in_list.append("mem[8] = 0")

        in_list = []
        in_list.append("mask = 000000000000000000000000000000X1001X")
        in_list.append("mem[42] = 100")
        in_list.append("mask = 00000000000000000000000000000000X0XX")
        in_list.append("mem[26] = 1")
        pass
    else:
        in_list = list()
        with open("inputs/input_14.txt", "r") as f:
            for line in f:
                line = line.strip()
                in_list.append(line)
        f.close()
        # print(in_list)

    # print(advent_14a(in_list))
    print(advent_14b(in_list))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
