#!/usr/bin/env python

import numpy as np
from itertools import permutations


def acs_value(p_instr, p, input):
    ins = np.copy(p_instr)
    while True:
        opc1 = int(ins[p:p+1])
        opc5 = "{0:05d}".format(opc1)
        opcode = opc5[3:5]
        m1 = int(opc5[2:3])
        m2 = int(opc5[1:2])
        m3 = int(opc5[0:1])

        if opcode == "03":
            # print(p, input[p])
            ins[ins[p+1:p+2]] = input[0]
            if len(input) > 1:
                input.pop(0)
            p += 2
        elif opcode == "04":
            prm1 = int(ins[p+1:p+2])
            if not m1:
                prm1 = int(ins[ins[p+1:p+2]])
            output = prm1
            p += 2
            return output, p, ins
        elif opcode == "99":
            return 99, p, ins
        else:
            prm1 = int(ins[p+1:p+2])
            prm2 = int(ins[p+2:p+3])
            if not m1:
                prm1 = int(ins[ins[p+1:p+2]])
            if not m2:
                prm2 = int(ins[ins[p+2:p+3]])

            if opcode == "01":
                ins[ins[p+3:p+4]] = prm1 + prm2
                p += 4
            elif opcode == "02":
                ins[ins[p+3:p+4]] = prm1 * prm2
                p += 4
            elif opcode == "05":
                if prm1 != 0:
                    p = prm2
                else:
                    p += 3
            elif opcode == "06":
                if prm1 == 0:
                    p = prm2
                else:
                    p += 3
            elif opcode == "07":
                ins[ins[p+3:p+4]] = 0
                if prm1 < prm2:
                    ins[ins[p+3:p+4]] = 1
                p += 4
            elif opcode == "08":
                ins[ins[p+3:p+4]] = 0
                if prm1 == prm2:
                    ins[ins[p+3:p+4]] = 1
                p += 4


def advent_7a(p_instr, phs, idx, value):

    input = [phs[idx], value]
    output, p, ins = acs_value(p_instr, 0, input)
    if idx == len(phs) - 1:
        return output

    return advent_7a(p_instr, phs, idx+1, output)


# recursive, keep state after each 5 runs
def advent_7b(p_all, idx, amp, val_prev):

    value = p_all[amp][0]
    if idx < 5:
        value_init = [value, val_prev]
    else:
        value_init = [val_prev]
    point = p_all[amp][1]
    instr = p_all[amp][2]
    value, point, instr = acs_value(instr, point, value_init)
    # print(idx, amp, " ", point, value, instr[len(instr) - 3:len(instr)])
    p_all[amp][0] = value
    p_all[amp][1] = point
    p_all[amp][2] = instr

    if idx == 1000 or value == 99:
        return val_prev
    val_prev = value

    amp += 1
    if amp == 5:
        amp = 0

    return advent_7b(p_all, idx + 1, amp, val_prev)


if __name__ == "__main__":
    import time

    start_time = time.time()

    p_input = np.array([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0])
    phs = [4, 3, 2, 1, 0]
    output = advent_7a(p_input, phs, 0, 0)
    print(output)

    p_input = np.array([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0])
    phs = [0, 1, 2, 3, 4]
    output = advent_7a(p_input, phs, 0, 0)
    print(output)

    p_input = np.array([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0])
    phs = [0, 1, 2, 3, 4]
    output = advent_7a(p_input, phs, 0, 0)
    print(output)

    p_input = np.array([3,8,1001,8,10,8,105,1,0,0,21,46,63,76,97,118,199,280,361,442,99999,3,9,102,4,9,9,101,2,9,9,1002,9,5,9,101,4,9,9,102,2,9,9,4,9,99,3,9,101,5,9,9,102,3,9,9,101,3,9,9,4,9,99,3,9,1001,9,2,9,102,3,9,9,4,9,99,3,9,1002,9,5,9,101,4,9,9,1002,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,5,9,101,3,9,9,1002,9,5,9,1001,9,5,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99])
    phs = [0, 1, 2, 3, 4]
    perms = set(permutations(phs))
    maxval = 0
    for perm in perms:
        output = advent_7a(p_input, perm, 0, 0)
        if maxval < output:
            maxval = output
    print("7a: ", maxval)

    p_input = np.array([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5])
    phs = [9, 8, 7, 6, 5]

    p_all = {}
    p_all[0] = {[phs[0], 0, p_input], [phs[1], 0, p_input], [phs[2], 0, p_input], [phs[3], 0, p_input], [phs[4], 0, p_input]}
    output = advent_7b(p_all, 0, 0, 0)
    # 139629729
    print(output)

    p_input = np.array([3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10])
    phs = [9, 7, 8, 5, 6]
    
    p_all[0] = {[phs[0], 0, p_input], [phs[1], 0, p_input], [phs[2], 0, p_input], [phs[3], 0, p_input], [phs[4], 0, p_input]}
    output = advent_7b(p_all, 0, 0, 0)
    # 18216
    print(output)

    p_input = np.array([3,8,1001,8,10,8,105,1,0,0,21,46,63,76,97,118,199,280,361,442,99999,3,9,102,4,9,9,101,2,9,9,1002,9,5,9,101,4,9,9,102,2,9,9,4,9,99,3,9,101,5,9,9,102,3,9,9,101,3,9,9,4,9,99,3,9,1001,9,2,9,102,3,9,9,4,9,99,3,9,1002,9,5,9,101,4,9,9,1002,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,5,9,101,3,9,9,1002,9,5,9,1001,9,5,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99])
    phs = [5, 6, 7, 8, 9]
    perms = set(permutations(phs))
    maxval = 0
    for perm in perms:
        p_all = {}
        p_all[0] = [perm[0], 0, p_input]
        p_all[1] = [perm[1], 0, p_input]
        p_all[2] = [perm[2], 0, p_input]
        p_all[3] = [perm[3], 0, p_input]
        p_all[4] = [perm[4], 0, p_input]
        output = advent_7b(p_all, 0, 0, 0)

        if maxval < output:
            maxval = output
    print("7b: ", maxval)

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")

