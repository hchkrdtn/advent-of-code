#!/usr/bin/env python3

import numpy as np
import copy


def process_tickets(input):
    intervals = []
    fields = []
    your_ticket = []
    tickets = []

    flag = "fields"
    for idx, ipt in enumerate(input):
        if flag == "fields":
            if not ipt:
                flag = "your ticket"
                continue
            field, values = ipt.split(": ")
            v1, v2 = values.split(" or ")
            v1f, v1l = v1.split("-")
            v2f, v2l = v2.split("-")
            val_full = [*range(int(v1f), int(v1l)+1)] + [*range(int(v2f), int(v2l)+1)]
            fields.append(field)
            intervals.append(val_full)

        # your ticket
        if flag == "your ticket":
            if "your ticket" in ipt:
                continue
            if not ipt:
                flag = "nearby tickets"
                continue
            your_ticket = [int(i) for i in ipt.split(",")]

        # nearby tickets
        if flag == "nearby tickets":
            if "nearby tickets" in ipt:
                continue
            tickets.append([int(i) for i in ipt.split(",")])
    return fields, intervals, your_ticket, tickets


def wrong_tickets(intervals, tickets):
    res = []
    idx_wrong = []
    for idx, ticket in enumerate(tickets):
        flag = False
        for num in ticket:
            for interval in intervals:
                if num in interval:
                    flag = True
                    break
                else:
                    flag = False
            if not flag:
                res.append(num)
                idx_wrong.append(idx)
    tickets_valid = []
    # remove wrong tickets = add only good ones
    for pos, ticket in enumerate (tickets):
        if pos not in idx_wrong:
            tickets_valid.append(tickets[pos: pos+1][0])
    return res, tickets_valid


def advent_16a(input):
    fields, intervals, your_ticket, tickets = process_tickets(input)
    res, tickets = wrong_tickets(intervals, tickets)
    # print(len(res), len(tickets))

    return 0# np.sum(np.asarray(res))


def advent_16b(input):
    fields, intervals, your_ticket, tickets = process_tickets(input)
    res, tickets = wrong_tickets(intervals, tickets)
    # print(len(res), len(tickets))

    tickets = np.asarray(tickets, dtype=list)

    fields_fin = copy.deepcopy(fields)
    # outer loop
    for i in range(0, tickets.shape[1]):
        # loop through number positions (unknown fields)
        for j in range(0, tickets.shape[1]):
            tpos = tickets[:, j:j+1].flatten()
            # first, second ... ticket number fields in intervals allowed
            ft = []
            # loop through intervals of allowed numbers, intersect and compare it
            # with the original, inter is already sorted by intersect
            for k in range(0, len(intervals)):
                ipos = np.asarray(intervals[k])
                inter = np.intersect1d(tpos, ipos, assume_unique=True)
                if np.array_equal(np.sort(tpos), inter):
                    ft.append([j, k])
            # all cases when field numbers are in intervals. If the list has only
            # one element it is the field since the others are forbidden
            # print(ft)
            if len(ft) == 1:
                bg = ft[0][1]
                # get the correct field name
                fields_fin[j] = fields[bg]
                # set identified field to 0
                intervals[bg] = [0]
                break
    print(fields)
    print(fields_fin)
    # get multiplied "departure" fields
    departure_tot = 1
    for idx, field in enumerate(fields_fin):
        if "departure" in field:
            departure_tot *= your_ticket[idx]
    return departure_tot

if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        in_list = []





        # in_list.append("class: 1-3 or 5-7")
        # in_list.append("row: 6-11 or 33-44")
        # in_list.append("seat: 13-40 or 45-50")
        # in_list.append("")
        # in_list.append("your ticket:")
        # in_list.append("7,1,14")
        # in_list.append("")
        # in_list.append("nearby tickets:")
        # in_list.append("7,3,47")
        # in_list.append("40,4,50")
        # in_list.append("55,2,20")
        # in_list.append("38,6,12")

        in_list.append("class: 0-1 or 4-19")
        in_list.append("row: 0-5 or 8-19")
        in_list.append("seat: 0-13 or 16-19")
        in_list.append("")
        in_list.append("your ticket:")
        in_list.append("11,12,13")
        in_list.append("")
        in_list.append("nearby tickets:")
        in_list.append("3,9,18")
        in_list.append("15,1,5")
        in_list.append("5,14,9")
        pass
    else:
        in_list = list()
        with open("inputs/input_16.txt", "r") as f:
            for line in f:
                line = line.strip()
                in_list.append(line)
        f.close()
        # print(in_list)

    print(advent_16a(in_list))
    print(advent_16b(in_list))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
