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
