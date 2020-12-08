#!/usr/bin/env python3

import numpy as np
import re


def get_recursively(search_dict, field, fields_found):
    for key, values in search_dict.items():
        if key == field:
            for value in values:
                fields_found.append(value)
                get_recursively(search_dict, value, fields_found)
    return list(set(fields_found))


def get_recursively_b(search_dict, field, fields_found):
    for key, values in search_dict.items():
        if key == field:
            # print(values)
            for value in values:
                fields_found.append(value)
                get_recursively_b(search_dict, value, fields_found)
    return fields_found


def advent_8a(inpt):
    my_bag = "shiny gold"
    bags_all = {}
    for bags in inpt:
        outer, inner = bags.split(" contain ")
        color = outer.split(" ")[0] + " " + outer.split(" ")[1]
        if "," in inner:
            inner_all = inner.split(", ")
            for inner_one in inner_all:
                key = inner_one.split(" ")[1] + " " + inner_one.split(" ")[2]
                if key in bags_all:
                    tmp = bags_all[key]
                    if color not in tmp:
                        tmp.append(color)
                    bags_all[key] = tmp
                else:
                    bags_all[key] = [color]
        else:
            if "other" not in inner:
                key = inner.split(" ")[1] + " " + inner.split(" ")[2]
                if key in bags_all:
                    tmp = bags_all[key]
                    if color not in tmp:
                        tmp.append(color)
                    bags_all[key] = tmp
                else:
                    bags_all[key] = [color]
    tmps = get_recursively(bags_all, my_bag, [])
    return len(tmps)


def advent_8b(inpt):
    my_bag = "shiny gold"
    bags_all = {}
    bags_all_no = {}
    for bags in inpt:
        outer, inner = bags.split(" contain ")
        key = outer.split(" ")[0] + " " + outer.split(" ")[1]

        if "," in inner:
            inner_all = inner.split(", ")
            for inner_one in inner_all:
                color = inner_one.split(" ")[1] + " " + inner_one.split(" ")[2]
                color_no = int(inner_one.split(" ")[0])
                if key in bags_all:
                    tmp = bags_all[key]
                    if color not in tmp:
                        for i in range (0, color_no):
                            tmp.append(color)
                    bags_all[key] = tmp
                else:
                    bags_all[key] = []
                    for i in range(0, color_no):
                        bags_all[key].append(color)
        else:
            if "other" not in inner:
                color = inner.split(" ")[1] + " " + inner.split(" ")[2]
                color_no = int(inner.split(" ")[0])
                if key in bags_all:
                    tmp = bags_all[key]
                    if color not in tmp:
                        for i in range (0, color_no):
                            tmp.append(color)
                    bags_all[key] = tmp
                else:
                    bags_all[key] = []
                    for i in range(0, color_no):
                        bags_all[key].append(color)
            else:
                bags_all[key] = []

    tmps = get_recursively_b(bags_all, my_bag, [])
    return len(tmps)


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        input_text = list()
        # input_text.append("light red bags contain 1 bright white bag, 2 muted yellow bags.")
        # input_text.append("dark orange bags contain 3 bright white bags, 4 muted yellow bags.")
        # input_text.append("bright white bags contain 1 shiny gold bag.")
        # input_text.append("muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.")
        # input_text.append("shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.")
        # input_text.append("dark olive bags contain 3 faded blue bags, 4 dotted black bags.")
        # input_text.append("vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.")
        # input_text.append("faded blue bags contain no other bags.")
        # input_text.append("dotted black bags contain no other bags.")
        # input_text.append("bright white bags contain 1 shiny gold bag.")
        # input_text.append("muted yellow bags contain 1 shiny gold bag.")
        # input_text.append("muted yellow bags contain other bags.")
        # input_text.append("dark orange bags contain 1 bright white bag, 1 muted yellow bag.")
        # input_text.append("muted yellow bags contain 1 shiny gold bag.")
        # input_text.append("bright white bags contain 1 shiny gold bag.")
        # input_text.append("bright white bags contain 1 shiny gold bag.")
        # input_text.append("muted yellow bags contain 1 shiny gold bag.")


        # input_text.append("shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.")
        # input_text.append("faded blue bags contain no other bags.")
        # input_text.append("dotted black bags contain no other bags.")
        # input_text.append("vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.")
        # input_text.append("dark olive bags contain 3 faded blue bags, 4 dotted black bags.")
        # print(input_text)

        input_text.append("shiny gold bags contain 2 dark red bags.")
        input_text.append("dark red bags contain 2 dark orange bags.")
        input_text.append("dark orange bags contain 2 dark yellow bags.")
        input_text.append("dark yellow bags contain 2 dark green bags.")
        input_text.append("dark green bags contain 2 dark blue bags.")
        input_text.append("dark blue bags contain 2 dark violet bags.")
        input_text.append("dark violet bags contain no other bags.")
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
