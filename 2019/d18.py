#!/usr/bin/env python

import numpy as np


def action2():
    pass

def advent_18a(input):
    tmp_char = np.array(input)
    it = np.nditer(tmp_char, flags=['multi_index'])

    at_x = 0
    at_y = 0
    keys = []
    while not it.finished:
        char = str(it[0])
        if char.islower():
            keys.append(char)
        if char == "@":
            at_x = it.multi_index[0]
            at_y = it.multi_index[1]
        # print((it[0], it.multi_index), end=' ')
        it.iternext()
    # print(at_x, at_y)

    collect = []
    steps = 0
    dir = "right"

    while True:
        print(at_x, at_y)
        print(tmp_char)
        if len(keys) == len(collect):
            break

        if dir == "right":
            tmp_char, at_x, at_y, dir, collect, steps = action_dir(tmp_char, at_x, at_y,
                                                                        dir, "left", collect, steps)
        elif dir == "left":
            tmp_char, at_x, at_y, dir, collect, steps = action_dir(tmp_char, at_x, at_y,
                                                                        dir, "up", collect, steps)
        elif dir == "up":
            tmp_char, at_x, at_y, dir, collect, steps = action_dir(tmp_char, at_x, at_y,
                                                                        dir, "down", collect, steps)
        elif dir == "down":
            tmp_char, at_x, at_y, dir, collect, steps = action_dir(tmp_char, at_x, at_y,
                                                                        dir, "right", collect, steps)
        #
        #
        # if dir == "right":
        #     x = at_x
        #     y = at_y + diridx
        #     action, collect = check_pos(tmp_char, x, y, collect)
        #     if action == 0:
        #         dir = "left"
        #     elif action == 1:
        #         tmp_char[at_x, at_y] = "."
        #         tmp_char[x, y] = "@"
        #         at_x = x
        #         at_y = y
        #         steps += 1
        #     # # decision 2: where to go next
        #     elif action == 2:
        #         tmp_char[at_x, at_y] = "."
        #         tmp_char[x, y] = "@"
        #         at_x = x
        #         at_y = y
        #         dir = "left"
        #         steps += 1
        # elif dir == "left":
        #     x = at_x
        #     y = at_y - diridx
        #     action, collect = check_pos(tmp_char, x, y, collect)
        #     if action == 0:
        #         dir = "up"
        #     elif action == 1:
        #         tmp_char[at_x, at_y] = "."
        #         tmp_char[x, y] = "@"
        #         at_x = x
        #         at_y = y
        #         steps += 1
        #     # # decision 2: where to go next
        #     elif action == 2:
        #         tmp_char[at_x, at_y] = "."
        #         tmp_char[x, y] = "@"
        #         at_x = x
        #         at_y = y
        #         dir = "up"
        #         steps += 1
        # elif dir == "up":
        #     x = at_x + diridx
        #     y = at_y
        #     action, collect = check_pos(tmp_char, x, y, collect)
        #     if action == 0:
        #         dir = "down"
        #     elif action == 1:
        #         tmp_char[at_x, at_y] = "."
        #         tmp_char[x, y] = "@"
        #         at_x = x
        #         at_y = y
        #         steps += 1
        #     # # decision 2: where to go next
        #     elif action == 2:
        #         tmp_char[at_x, at_y] = "."
        #         tmp_char[x, y] = "@"
        #         at_x = x
        #         at_y = y
        #         dir = "down"
        #         steps += 1
        # elif dir == "down":
        #     x = at_x - diridx
        #     y = at_y
        #     action, collect = check_pos(tmp_char, x, y, collect)
        #     if action == 0:
        #         dir = "up"
        #     elif action == 1:
        #         tmp_char[at_x, at_y] = "."
        #         tmp_char[x, y] = "@"
        #         at_x = x
        #         at_y = y
        #         steps += 1
        #     # # decision 2: where to go next
        #     elif action == 2:
        #         tmp_char[at_x, at_y] = "."
        #         tmp_char[x, y] = "@"
        #         at_x = x
        #         at_y = y
        #         dir = "right"
        #         steps += 1
    # print(collect)
    # print(tmp_char)
    return steps


def check_pos(tmp_char, x, y, collect):
    char = tmp_char[x, y]
    print(char)
    if char == ".":
        return 1, collect
    elif char == "#":
        return 0, collect
    elif char.isupper():
        if char.lower() in collect:
            return 1, collect
        else:
            return 0, collect
    else:
        collect.append(char)
        # decision where to go next
        return 2, collect


def action_dir(tmp_char, at_x, at_y, dir, dir_new, collect, steps):
    dir_next = dir
    diridx = 1
    x = 0
    y = 0
    if dir == "right":
        x = at_x
        y = at_y + diridx
    elif dir == "left":
        x = at_x
        y = at_y - diridx
    elif dir == "up":
        x = at_x + diridx
        y = at_y
    elif dir == "down":
        x = at_x - diridx
        y = at_y

    action, collect = check_pos(tmp_char, x, y, collect)
    if action == 0:
        dir_next = dir_new
    elif action == 1:
        tmp_char[at_x, at_y] = "."
        tmp_char[x, y] = "@"
        at_x = x
        at_y = y
        steps += 1
    # # decision 2: where to go next
    elif action == 2:
        tmp_char[at_x, at_y] = "."
        tmp_char[x, y] = "@"
        at_x = x
        at_y = y
        dir_next = dir_new
        steps += 1
    return(tmp_char, at_x, at_y, dir_next, collect, steps)


if __name__ == "__main__":
    import time

    start_time = time.time()
    test = True

    if test:
        input = list()
        input.append(list("#########"))
        input.append(list("#b.A.@.a#"))
        input.append(list("#########"))

        output = advent_18a(input)

        # input = list()
        # input.append(list("########################"))
        # input.append(list("#f.D.E.e.C.b.A.@.a.B.c.#"))
        # input.append(list("######################.#"))
        # input.append(list("#d.....................#"))
        # input.append(list("########################"))
        #
        # output = advent_18a(input)

        #
        # input = list()
        # input.append(list("#################")))
        # input.append(list("#i.G..c...e..H.p#"))
        # input.append(list("########.########"))
        # input.append(list("#j.A..b...f..D.o#"))
        # input.append(list("########@########"))
        # input.append(list("#k.E..a...g..B.n#"))
        # input.append(list("########.########"))
        # input.append(list("#l.F..d...h..C.m#"))
        # input.append(list("#################"))
        #
        # input = list()
        # input.append(list("########################"))
        # input.append(list("#@..............ac.GI.b#))
        # input.append(list("###d#e#f################"))
        # input.append(list("###A#B#C################"))
        # input.append(list("###g#h#i################"))
        # input.append(list("########################"))

        print("18a: ", output)
        print("18b: ", )
    else:
        input = dict()
        with open("inputs/input_06.txt", "r") as f:
            for line in f:
                planet = line.split(")")
                input[planet[1].strip("\n")] = [planet[0]]
        f.close()

        orbits, transf = advent_18a(input)
        print("6a: ", )
        print("6b: ", )

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
