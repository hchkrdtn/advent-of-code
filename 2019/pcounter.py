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
            pass
        elif md == 2:
            return val + self.rb

    def get_opc(self):
        opc1 = int(self.p_ins[self.ip])
        opc = opc1 % 100
        return opc

    def get_mod(self, opc1):
        m0 = np.floor(opc1 / 100) % 10
        m1 = np.floor(opc1 / 1000) % 10
        m2 = np.floor(opc1 / 10000) % 10
        return [m0, m1, m2]

    def get_val(self, opc):
        instr = self.p_ins
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
        opc = self.get_opc()
        m = self.get_mod(opc)
        v = self.get_val(opc)

        if not self.input:
            print("You might need to set input values!")

        instr = self.p_ins
        ip = self.ip
        rb = self.rb

        if opc == 1:
            instr[self.liter(m[2], m[2])] = self.inter(m[0], v[0]) + self.inter(m[1], v[1])
            ip += 4
        if opc == 2:
            instr[self.liter(m[2], v[2])] = self.inter(m[0], v[0]) * self.inter(m[1], v[1])
            ip += 4
        if opc == 3:
            instr[self.liter(m[0], v[0])] = self.input
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
            rb += self.liter(m[0], v[0])
            ip += 2
        if opc == 99:
            self.rb = rb
            self.ip = ip
            self.p_ins = instr
            return

        self.rb = rb
        self.ip = ip
        self.p_ins = instr