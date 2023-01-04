#!/usr/bin/env python3

import re
import copy
import math


def advent_a(ms, my):
    m_yell = copy.deepcopy(my)
    mos = copy.deepcopy(ms)
    while True:
        del_key = []
        for key in mos:
            if mos[key][0] in m_yell.keys():
                mos[key][0] = int(m_yell[mos[key][0]])
            if mos[key][1] in m_yell.keys():
                mos[key][1] = int(m_yell[mos[key][1]])
            if all(isinstance(k, int) for k in mos[key][0:2]):
                del_key.append(key)
                if mos[key][2] == "+":
                    m_yell[key] = mos[key][0] + mos[key][1]
                elif mos[key][2] == "-":
                    m_yell[key] = mos[key][0] - mos[key][1]
                elif mos[key][2] == "/":
                    m_yell[key] = mos[key][0] / mos[key][1]
                elif mos[key][2] == "*":
                    m_yell[key] = mos[key][0] * mos[key][1]
        for it in del_key:
            del mos[it]
        if len(mos.keys()) == 0:
            break

    return m_yell["root"]


def advent_b(ms, my):
    ms["root"][2] = "-"
    my["humn"] = 0
    while True:
        m_yell = copy.deepcopy(my)
        mos = copy.deepcopy(ms)
        # print(m_yell)
        # print(mos)
        while True:
            del_key = []
            for key in mos:
                if mos[key][0] in m_yell.keys():
                    mos[key][0] = int(m_yell[mos[key][0]])
                if mos[key][1] in m_yell.keys():
                    mos[key][1] = int(m_yell[mos[key][1]])
                if all(isinstance(k, int) for k in mos[key][0:2]):
                    del_key.append(key)
                    if mos[key][2] == "+":
                        m_yell[key] = mos[key][0] + mos[key][1]
                    elif mos[key][2] == "-":
                        m_yell[key] = mos[key][0] - mos[key][1]
                    elif mos[key][2] == "/":
                        m_yell[key] = mos[key][0] / mos[key][1]
                    elif mos[key][2] == "*":
                        m_yell[key] = mos[key][0] * mos[key][1]
            for it in del_key:
                # print(mos)
                del mos[it]
            if len(mos.keys()) == 0:
                break

        if m_yell["root"] == 0:
            return my["humn"]
        n = m_yell["root"]
        if n > 0:
            digits = int(math.log10(n)) + 1
        elif n == 0:
            digits = 1
        else:
            digits = int(math.log10(-n)) + 1
        # print(digits, n)
        if digits-2 == 0:
            my["humn"] += 1
        else:
            my["humn"] += 10**(digits-2)

    return -1


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr = ["root: pppw + sjmn",
               "dbpl: 5",
               "cczh: sllz + lgvd",
               "zczc: 2",
               "ptdq: humn - dvpt",
               "dvpt: 3",
               "lfqf: 4",
               "humn: 5",
               "ljgn: 2",
               "sjmn: drzm * dbpl",
               "sllz: 4",
               "pppw: cczh / lfqf",
               "lgvd: ljgn * ptdq",
               "drzm: hmdt - zczc",
               "hmdt: 32"]
        arr = [x.strip() for x in arr]
        pass
    else:
        with open("inputs/input_21.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    # get the sensor and beacon positions
    monkeys = {}
    monkeys_yell = {}

    i = 0
    for i in range(len(arr)):
        lines = arr[i].split(":")
        num = re.findall(pattern=r"[+-]?\d+", string=lines[1])
        if not num:
            m1, oper, m2 = lines[1].split()
            monkeys[lines[0]] = [m1, m2, oper]
        else:
            monkeys_yell[lines[0]] = num[0]

    print(advent_a(monkeys, monkeys_yell))
    print(advent_b(monkeys, monkeys_yell))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
