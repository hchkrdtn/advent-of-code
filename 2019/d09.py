#!/usr/bin/env python

import numpy as np


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
            return self.p_ins[val]
        elif md == 1:
            return val
        elif md == 2:
            return self.p_ins[val + self.rb]

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
                self.p_ins = instr
                return

            self.rb = rb
            self.ip = ip
            self.p_ins = instr


def advent_9(p_instr, input):
    # expand array memory part
    more = 100000000
    p_instr = p_instr.split(",")
    p_instr = np.asarray([int(x) for x in p_instr])
    p_instr = np.concatenate((p_instr, np.zeros((more), dtype=p_instr.dtype)))

    vm = VM(p_instr)
    vm.set_input(input)
    vm.run()


if __name__ == "__main__":
    import time

    start_time = time.time()
    input = 2

    # p_instr = np.array([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])
    # # 109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99
    # print(advent_9(p_instr, input))
    # p_instr = np.array([104,1125899906842624,99])
    # # 1125899906842624
    # advent_9(p_instr, input)
    # p_instr = np.array([1102,34915192,34915192,7,4,7,99,0])
    # advent_9(p_instr, input)
    #
    # p_instr = np.array([109,-1,4,1,99])
    # # -1
    # advent_9(p_instr, input)
    # p_instr = np.array([109,-1,104,1,99])
    # # 1
    # advent_9(p_instr, input)
    # p_instr = np.array([109, -1, 204, 1, 99])
    # # 109
    # advent_9(p_instr, input)
    # p_instr = np.array([109, 1, 9, 2, 204, -6, 99])
    # # 204
    # advent_9(p_instr, input)
    # p_instr = np.array([109, 1, 109, 9, 204, -6, 99])
    # # 204
    # advent_9(p_instr, input)
    # p_instr = np.array([109, 1, 209, -1, 204, -106, 99])
    # # 204
    # advent_9(p_instr, input)
    # p_instr = np.array([109, 1, 3, 3, 204, 2, 99])
    # # the input value
    # advent_9(p_instr, input)
    # p_instr = np.array([109, 1, 203, 2, 204, 2, 99])
    # # outputs the input value
    # advent_9(p_instr, input)

    # input 1 for TEST
    # input 2 for BOOST (9b)
    with open("inputs/input_09.txt", "r") as f:
        for line in f:
            p_instr = line.strip()
    f.close()
    advent_9(p_instr, [input])

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
