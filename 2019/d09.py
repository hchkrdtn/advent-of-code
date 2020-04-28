#!/usr/bin/env python

import numpy as np
from itertools import permutations


class VM:
    # interpreted and literal frame/modes for passing and getting values, not used
    INTERPRETED = 1
    LITERAL = 1

    def __init__(self, p_instr):
        # instruction set
        # instruction pointer

        self.instr = np.copy(p_instr)

        self.ip = 0
        self.rb = 0
        self.input = []

    def __str__(self):
        ps = "VM({0}".format(self.instr)
        return ps

    def set_input(self, input):
        # value input
        self.input = input
        if not isinstance(input, list):
            self.input = [input]

    def get_ip(self):
        return self.ip

    def set_ip(self, pointer):
        self.ip = pointer

    def get_rb(self):
        # relative base
        return self.rb

    def get_instr(self):
        return self.instr

    def next_inp(self):
        if len(self.input) > 1:
            self.input.pop(0)

    def inter(self, md, val):
        if md == 0:
            return self.instr[val]
        elif md == 1:
            return val
        elif md == 2:
            return self.instr[val + self.rb]

    def liter(self, md, val):
        if md == 0:
            return val
        elif md == 1:
            print("Illegal operation!")
            exit()
        elif md == 2:
            return val + self.rb

    def get_opcmod(self):
        # parameter mode 0
        # immediate mode 1
        # relative mode  2
        opc1 = int(self.instr[self.ip])
        opc = opc1 % 100

        # The // does integer division by a power of ten to move the digit to the ones position,
        # then the % gets the remainder after division by 10.
        m0 = opc1 // 10**2 % 10
        m1 = opc1 // 10**3 % 10
        m2 = opc1 // 10**4 % 10
        return opc, [m0, m1, m2]

    def get_val(self, opc):
        instr = self.instr
        ip = self.ip

        v0 = instr[ip + 1]
        if opc == 5 or opc == 6:
            v1 = instr[ip + 2]
            return [v0, v1]
        elif opc == 1 or opc == 2 or opc == 7 or opc == 8:
            v0 = instr[ip + 1]
            v1 = instr[ip + 2]
            v2 = instr[ip + 3]
            return [v0, v1, v2]
        # opc 3, 4, 9
        return [v0]

    def run(self):

        while True:
            instr = self.instr
            ip = self.ip
            rb = self.rb

            opc, m = self.get_opcmod()
            v = self.get_val(opc)
            # print(opc, m, v)

            if not self.input:
                print("You might need to set input values!")

            if opc == 1:
                instr[self.liter(m[2], v[2])] = self.inter(m[0], v[0]) + self.inter(m[1], v[1])
                ip += 4
            if opc == 2:
                instr[self.liter(m[2], v[2])] = self.inter(m[0], v[0]) * self.inter(m[1], v[1])
                ip += 4
            if opc == 3:
                instr[self.liter(m[0], v[0])] = self.input[0]
                self.next_inp()
                ip += 2
            if opc == 4:
                out = self.inter(m[0], v[0])
                print(out)
                ip += 2
            if opc == 5:
                if self.inter(m[0], v[0]) != 0:
                    ip = self.inter(m[1], v[1])
                else:
                    ip += 3
            if opc == 6:
                if self.inter(m[0], v[0]) == 0:
                    ip = self.inter(m[1], v[1])
                else:
                    ip += 3
            if opc == 7:
                if self.inter(m[0], v[0]) < self.inter(m[1], v[1]):
                    instr[self.liter(m[2], v[2])] = 1
                else:
                    instr[self.liter(m[2], v[2])] = 0
                ip += 4
            if opc == 8:
                if self.inter(m[0], v[0]) == self.inter(m[1], v[1]):
                    instr[self.liter(m[2], v[2])] = 1
                else:
                    instr[self.liter(m[2], v[2])] = 0
                ip += 4
            if opc == 9:
                rb += self.inter(m[0], v[0])
                ip += 2
            if opc == 99:
                self.rb = rb
                self.ip = ip
                self.instr = instr
                return

            self.rb = rb
            self.ip = ip
            self.instr = instr


def acs_value(p_instr, p, input):
    ins = np.copy(p_instr)
    rb = 0
    while True:
        opc1 = int(ins[p:p + 1])
        opc5 = "{0:05d}".format(opc1)
        opcode = opc5[3:5]
        m1 = int(opc5[2:3])     # position and relative mode
        m2 = int(opc5[1:2])
        m3 = int(opc5[0:1])
        # print(p, rb, opcode, m1, m2)

        if opcode == "03":
            if m1 == 0:
                ins[p + 1:p + 2] = input[0]
            elif m1 == 1:
                pass
            elif m1 == 2:
                tmp = rb + int(ins[p + 1:p + 2])
                ins[tmp:tmp + 1] = input[0]
            if len(input) > 1:
                input.pop(0)
            p += 2
        elif opcode == "04":
            if m1 == 0:
                prm1 = int(ins[int(ins[p + 1:p + 2])])
            elif m1 == 1:
                prm1 = int(ins[p + 1:p + 2])
            elif m1 == 2:
                tmp = rb + int(ins[p + 1:p + 2])
                prm1 = int(ins[tmp:tmp + 1])
            output = prm1
            p += 2
            print(output)
        elif opcode == "09":
            if m1 == 0:
                rbase = int(ins[int(ins[p + 1:p + 2])])
            elif m1 == 1:
                rbase = int(ins[p + 1:p + 2])
            elif m1 == 2:
                tmp = rb + int(ins[p + 1:p + 2])
                rbase = int(ins[tmp:tmp + 1])
            rb += rbase
            print(opcode, p, rb, m1, ins[p + 1:p + 2], ins[int(ins[p + 1:p + 2])], rbase)
            p += 2
        elif opcode == "99":
            return
        else:
            if m1 == 0:
                prm1 = int(ins[int(ins[p + 1:p + 2])])
            elif m1 == 1:
                prm1 = int(ins[p + 1:p + 2])
            elif m1 == 2:
                tmp = rb + int(ins[p + 1:p + 2])
                prm1 = int(ins[tmp:tmp + 1])

            if m2 == 0:
                prm2 = int(ins[int(ins[p + 2:p + 3])])
            elif m2 == 1:
                prm2 = int(ins[p + 2:p + 3])
            elif m2 == 2:
                tmp = rb + int(ins[p + 2:p + 3])
                prm2 = int(ins[tmp:tmp + 1])
            try:
                print(opcode, p, rb, m1, ins[p + 1:p + 2], ins[int(ins[p + 1:p + 2])], prm1)
                print(opcode, p, rb, m2, ins[p + 2:p + 3], ins[int(ins[p + 2:p + 3])], prm2)
            except:
                print(opcode, p, rb, m1, ins[p + 1:p + 2], "out", prm1)
                print(opcode, p, rb, m2, ins[p + 2:p + 3], "out", prm2)

            # write
            if opcode == "01":
                if m2 == 0:
                    ins[p + 3:p + 4] = prm1 + prm2
                elif m2 == 1:
                    pass
                elif m2 == 2:
                    tmp = rb + int(ins[p + 3:p + 4])
                    ins[tmp:tmp + 1] = prm1 + prm2
                p += 4
            elif opcode == "02":
                if m2 == 0:
                    ins[p + 3:p + 4] = prm1 * prm2
                elif m2 == 1:
                    pass
                elif m2 == 2:
                    tmp = rb + int(ins[p + 3:p + 4])
                    ins[tmp:tmp + 1] = prm1 * prm2
                p += 4
            elif opcode == "05":
                if prm1 != 0:
                    p = prm2
                else:
                    p += 3
            #1005, 63, 65
            elif opcode == "06":
                if prm1 == 0:
                    p = prm2
                else:
                    p += 3
            elif opcode == "07":
                if m2 == 0:
                    ins[p + 3:p + 4] = 0
                elif m2 == 1:
                    pass
                elif m2 == 2:
                    tmp = rb + int(ins[p + 3:p + 4])
                    ins[tmp:tmp + 1] = 0

                if prm1 < prm2:
                    if m2 == 0:
                        ins[p + 3:p + 4] = 1
                    elif m2 == 1:
                        pass
                    elif m2 == 2:
                        tmp = rb + int(ins[p + 3:p + 4])
                        ins[tmp:tmp + 1] = 1
                p += 4
            elif opcode == "08":
                if m2 == 0:
                    ins[p + 3:p + 4] = 0
                elif m2 == 1:
                    pass
                elif m2 == 2:
                    tmp = rb + int(ins[p + 3:p + 4])
                    ins[tmp:tmp + 1] = 0

                if prm1 == prm2:
                    if m2 == 0:
                        ins[p + 3:p + 4] = 1
                    elif m2 == 1:
                        pass
                    elif m2 == 2:
                        tmp = rb + int(ins[p + 3:p + 4])
                        ins[tmp:tmp + 1] = 1
                p += 4


def advent_9a(p_instr, input):
    # expand array memory part
    more = 100000000
    p_instr = p_instr.split(",")
    p_instr = np.asarray([int(x) for x in p_instr])
    p_instr = np.concatenate((p_instr, np.zeros((more), dtype=p_instr.dtype)))

    vm = VM(p_instr)
    vm.set_input(input)
    vm.run()

    # acs_value(p_instr, 0, input)


def advent_9b(p_instr, input):

    return 1


if __name__ == "__main__":
    import time

    start_time = time.time()
    input = 2

    # p_instr = np.array([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])
    # # 109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99
    # print(advent_9a(p_instr, input))
    # p_instr = np.array([104,1125899906842624,99])
    # # 1125899906842624
    # advent_9a(p_instr, input)
    # p_instr = np.array([1102,34915192,34915192,7,4,7,99,0])
    # advent_9a(p_instr, input)
    #
    # p_instr = np.array([109,-1,4,1,99])
    # # -1
    # advent_9a(p_instr, input)
    # p_instr = np.array([109,-1,104,1,99])
    # # 1
    # advent_9a(p_instr, input)
    # p_instr = np.array([109, -1, 204, 1, 99])
    # # 109
    # advent_9a(p_instr, input)
    # p_instr = np.array([109, 1, 9, 2, 204, -6, 99])
    # # 204
    # advent_9a(p_instr, input)
    # p_instr = np.array([109, 1, 109, 9, 204, -6, 99])
    # # 204
    # advent_9a(p_instr, input)
    # p_instr = np.array([109, 1, 209, -1, 204, -106, 99])
    # # 204
    # advent_9a(p_instr, input)
    # p_instr = np.array([109, 1, 3, 3, 204, 2, 99])
    # # the input value
    # advent_9a(p_instr, input)
    # p_instr = np.array([109, 1, 203, 2, 204, 2, 99])
    # # outputs the input value
    # advent_9a(p_instr, input)

    # append 3,1 for TEST
    with open("inputs/input_09.txt", "r") as f:
        for line in f:
            p_instr = line.strip()
    f.close()
    advent_9a(p_instr, [input])
    #
    # p_instr = np.array([1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,5,19,23,1,6,23,27,1,27,10,31,1,31,5,35,2,10,35,39,1,9,39,43,1,43,5,47,1,47,6,51,2,51,6,55,1,13,55,59,2,6,59,63,1,63,5,67,2,10,67,71,1,9,71,75,1,75,13,79,1,10,79,83,2,83,13,87,1,87,6,91,1,5,91,95,2,95,9,99,1,5,99,103,1,103,6,107,2,107,13,111,1,111,10,115,2,10,115,119,1,9,119,123,1,123,9,127,1,13,127,131,2,10,131,135,1,135,5,139,1,2,139,143,1,143,5,0,99,2,0,14,0])
    # advent_9b(p_instr, input)


    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")