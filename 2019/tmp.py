#!/usr/bin/env python

import numpy as np


class VM:
    # interpreted and literal frame/modes for passing and getting values, not used
    INTERPRETED = 1
    LITERAL = 1

    def __init__(self, p_instr):
        # instruction set
        # instruction pointer

        # self.instr = np.copy(p_instr)
        self.instr = p_instr

        self.ip = 0
        self.rb = 0
        self.input = []

    def __str__(self):
        ps = "VM({0}".format(self.instr)
        return ps

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

    def run(self, output):
        while True:
            instr = self.instr
            ip = self.ip
            rb = self.rb

            opc, m = self.get_opcmod()
            v = self.get_val(opc)

            if not self.input:
                print("You might need to set input values!")

            if opc == 1:
                instr[self.liter(m[2], v[2])] = self.inter(m[0], v[0]) + self.inter(m[1], v[1])
                ip += 4
            if opc == 2:
                instr[self.liter(m[2], v[2])] = self.inter(m[0], v[0]) * self.inter(m[1], v[1])
                ip += 4
            if opc == 3:
                print("input", self.input[0])
                instr[self.liter(m[0], v[0])] = self.input[0]
                self.next_inp()
                ip += 2
            if opc == 4:
                out = self.inter(m[0], v[0])
                ip += 2
                if output:
                    self.rb = rb
                    self.ip = ip
                    self.instr = instr
                    return out
                else:
                    print(out)
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
                return 99

            self.rb = rb
            self.ip = ip
            self.instr = instr
