#!/usr/bin/env python3

import numpy as np
import copy


def pcounter(inpt):
    # for idx in range(0, len(instr)):
    #     if idx == 0:
    #         p = 0, instr[p] = 0, acc = 0, accum = 0
    #     elif idx == 1:
    #         p = 1, instr[p] = 1, acc = 1, accum = 1
    #     elif idx == 2:
    #         p = 2, instr[p] = 4, jmp = 4, accum = 1
    p_address = []
    p_accum = []
    seq = []
    accum = 0
    p = 0
    idx = 0
    repeat = False
    while 1:
        ds, ns = inpt[p].split()
        # print(ds, ns)
        if ds == "acc":
            accum += int(ns)
            p += 1
        elif ds == "jmp":
            p += int(ns)
        else:
            p += 1

        # find recurring pattern
        if p in p_address:
            if p in seq:
                result = find_sequens(np.array(seq), np.array(p_address))
                if result:
                    # print(p_address, p_accum, seq)
                    return [result-1, p_accum[result-1]]
            if repeat or len(seq) == 0:
                seq.append(p)
                repeat = True
            else:
                seq = []
                repeat = False
        p_address.append(p)
        p_accum.append(accum)

        if p == len(inpt):
            return [-99999, p_accum[-1]]
        idx += 1


def find_sequens(seq, full_arr):
    """ Find sequence in an array.

    Args:
        seq (np.array): Input 1D array with sequence pattern.
        full_arr (np.array): Input 1D array to be searched.

    Returns:
        int: starting index of the second occurrence or zero. It is an index from
        1D Array of indices in the input array that satisfy the
        matching of input sequence in the input array. In case of no match

    """
    # Store sizes of input array and sequence
    ns = seq.size
    na = full_arr.size

    # Range of sequence
    r_seq = np.arange(ns)

    # Create a 2D array of sliding indices across the entire length of input array.
    # Match up with the input sequence & get the matching starting indices.
    tmp = full_arr[np.arange(na - ns + 1)[:, None] + r_seq]
    mtx = (tmp == seq)
    mtx = np.all(mtx, axis=1)

    # Get the range of those indices as final output
    if mtx.any() > 0:
        mask = np.convolve(mtx, np.ones(ns, dtype=int))
        # only matches, and reshape to intervals of matching indeces,
        # -1 infers the size of the new dimension from the size of the input array.
        mm = np.reshape(np.where(mask > 0), (-1, ns))
        # starting index of the second occurrence
        return mm[1, 0]
    else:
        return 0         # no match


def advent_8a(inpt):
    return pcounter(inpt)


def advent_8b(inpt):
    nops = []
    jmps = []
    for i in range(0, len(inpt)):
        ds, ns = inpt[i].split()
        if ds == "nop":
            nops.append(i)
        elif ds == "jmp":
            jmps.append(i)

    # replace nop with jmp one by one
    print("nop->jmp")
    for idx in nops:
        inpt2 = copy.deepcopy(inpt)
        inpt2[idx] = inpt[idx].replace("nop", "jmp")
        if pcounter(inpt2)[0] < 0:
            print(pcounter(inpt2))

    # replace jmp with nop one by one
    print("jmp->nop")
    for idx in jmps:
        inpt2 = copy.deepcopy(inpt)
        inpt2[idx] = inpt[idx].replace("jmp", "nop")
        if pcounter(inpt2)[0] < 0:
            print(pcounter(inpt2))
    print("DONE")
    return 0


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        input_text = ["nop +0", "acc +1", "jmp +4", "acc +3", "jmp -3", "acc -99", "acc +1", "jmp -4", "acc +6"]
        # print(input_text)
        pass

    else:
        with open("inputs/input_08.txt", "r") as f:
            input_text = f.readlines()
            input_text = [x.strip() for x in input_text]
        f.close()
        # print(input_text)

    print(advent_8a(input_text))
    print(advent_8b(input_text))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
