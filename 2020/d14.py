#!/usr/bin/env python3

import numpy as np
from itertools import *
import re


class MemoryPoint:
    """ Memory pointer with mask """

    def __init__(self):
        """ Initialize 36-bit mask for the memory pointers. """
        self.memory = np.zeros(36, dtype=np.bool)
        self.mask = np.zeros(36, dtype=np.int)
        self.mask.fill(-1)

    def get_mask(self):
        """ Validate passport entries.

        Args:

        Returns:
            bool: Valid or not.

        """
        return self.mask

    def set_mask(self, index, mask):
        """ Set mask.

        Args:
            index (int): Position.
            memory (int): Memory.

        Returns:
            bool: Valid or not.

        """
        self.mask[-index] = mask
        return self.mask

    def set_mask_all(self, mask):
        """ Set mask.

        Args:
            mask (str): The whole memory..

        Returns:
            bool: Valid or not.

        """
        self.mask = mask
        return 1

    def get_memory(self):
        """ Validate passport entries.

        Args:

        Returns:
            bool: Valid or not.

        """
        return self.memory

    def set_memory(self, index, decnum):
        """ Set memory.

        Args:
            index (int): Position.
            decnum (int): Decimal number.

        Returns:
            bool: Valid or not.

        """
        a = np.array([[2]], dtype=np.uint8)
        binum = np.unpackbits(a, bitorder="big")
        print("dd", binum)
        # self.memory[-index] = memory


def advent_14a(input):
    # mask ="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    # maskp = mask.replace("X", "0")
    # maskn = mask.replace("X", "1")
    # memory = np.zeros(36).astype(np.int)

    # mp = MemoryPoint()
    # print(mp.get_mask())
    # print(mp.get_memory())
    # numpy.binary_repr¶
    # Return the binary representation of the input number as a string.
    # a = np.array([[0]], dtype=np.uint8)
    # binum = np.unpackbits(a, bitorder="big")
    # print("dd", binum)
    mask = 0
    memory = {}
    memory_masked = {}
    for inp in input:
        key, value = inp.split(" = ")
        if "mask" in key:
            # maskp = value.replace("X", "0")
            # maskn = value.replace("1", "X").replace("0", "2")
            # maskn = maskn.replace("X", "1").replace("2", "0")
            mask = value
            print(value)
            # print(maskp)
            # print(maskn)
        elif "mem" in key:
            npm = re.match(r"^mem\[(\d+)]$", key).groups()

            valst = str(bin(int(value))[2:].zfill(len(mask)))
            print(valst)

            pos_zer = [pos for pos, char in enumerate(mask) if char == "0"]
            pos_one = [pos for pos, char in enumerate(mask) if char == "1"]
            for posz in pos_zer:
                valst = valst[:posz] + "0" + valst[posz + 1:]
            for posz in pos_one:
                valst = valst[:posz] + "1" + valst[posz + 1:]
            print(valst)

            # print(npm[0], value)
            memory[npm[0]] = int(value)
            memory_masked[npm[0]] = int(valst, 2)
    print(memory)
    print(memory_masked)

    tot = 0
    for key in memory_masked:
        if memory_masked[key]:
            tot += memory_masked[key]

            # print(bin(int(value))[2:].zfill(len(maskp)))
            # print(maskp)
            # y = int(maskp, 2) ^ int(value, 2)
            # y = bin(y)[2:].zfill(len(maskp))
            # print(y)
            # print(maskn)
            # y = int(maskn, 2) & int(y, 2)
            # print(bin(y)[2:].zfill(len(maskp)))

# x & y  Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
# x | y  Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
# ~ x    Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
# x ^ y  Each bit of the output is the same as the corresponding bit in x if that bit in y is 0,
    #    and it's the complement of the bit in x if that bit in y is 1.
    # a = "11011111101100110110011001011101000"
    # b = "11001011101100111000011100001100001"
    # y = int(a, 2) ^ int(b, 2)
    # print(bin(y)[2:].zfill(len(a)))

        # [output: 00010100000000001110000101010001001]

        # mp.set_memory(int(npm[0]), value)
        # print(mp.get_mask())

        # print(mp.get_memory())


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
            print(npmst)

            permuts = list(product([0, 1], repeat=len(posX)))  # the list with all the 64 combinations
            for permut in permuts:
                for idx, posn in enumerate(posX):
                    npmst = npmst[:posn] + str(permut[idx]) + npmst[posn + 1:]
                    memory_masked[int(npmst, 2)] = int(value)
    print(memory)
    print(memory_masked)

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
