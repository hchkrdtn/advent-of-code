#!/usr/bin/env python3

def hashing(str):
    tot = 0
    for ch in list(str):
        tot += ord(ch)
        tot *= 17
        tot = tot%256
    return tot


def advent_a(str):
    steps = str.split(",")
    tot = 0
    for step in steps:
        tot += hashing(step)
    return tot


def advent_b(str):
    test = hashing("HASH")
    print(test)

    steps = str.split(",")
    tot = 0
    hashmap = {}
    for step in steps:
        op = "="
        eq = step.find(op)
        if eq > 0:
            label = step[0: eq]
            focus = step[eq + 1: len(step)]
            hl = hashing(label)
            lens = "[" + step.replace(step[eq], " ") + "]"
            if hl not in hashmap.keys():
                hashmap[hl] = [lens]
            else:
                labels = hashmap[hl]
                flag = False
                for h, lb in enumerate(labels):
                    if label == lb[1: eq+1]:
                        labels[h] = lb.replace(lb[eq+2: eq+3], focus)
                        flag = True
                        break
                if not flag:
                    labels.append(lens)
                hashmap[hl] = labels
        else:
            op = "-"
            eq = step.find(op)
            label = step[0: eq]
            hl = hashing(label)
            # print(step, label, hl)
            if hl in hashmap.keys():
                for i, ls in enumerate(hashmap[hl]):
                    if label in ls[1: eq+1]:
                        hashmap[hl].pop(i)
    # print(hashmap)

    sorted_hashmap = dict(sorted(hashmap.items()))
    for box in sorted_hashmap:
        focus = 0
        for k, slot in enumerate(hashmap[box]):
            eq = slot.find(" ")
            focus = int(slot[eq+1: len(slot)-1])
            slot_num = (1 + int(box)) * (k + 1) * focus
            tot += slot_num
            print(1 + int(box), slot, k+1, focus, slot_num, tot)
    return tot


if __name__ == "__main__":
    import time

    start_time = time.time()
    # Production part b is wrong after refactoring
    test = False
    if test:
        str = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
        pass
    else:
        with open("inputs/input_15.txt", "r") as f:
            str = f.readlines()
            str = str[0]
        f.close()

    print(advent_a(str))
    print(advent_b(str))

    # from https://github.com/hugseverycat/aoc2023/blob/master/day15.py
    # import re
    # from dataclasses import dataclass
    #
    # with open('inputs/input_15.txt') as f:
    #     lines = [line.rstrip() for line in f]
    #
    #
    # @dataclass
    # class LensBox:
    #     number: int
    #     lens_labels: list
    #     focal_lengths: list
    #
    #
    # def run_hash(sequence: str):
    #     hash_value = 0
    #     for c in sequence:
    #         hash_value += ord(c)
    #         hash_value *= 17
    #         hash_value = hash_value % 256
    #     return hash_value
    #
    #
    # lens_boxes = dict()
    # verification_sum = 0
    # init_seq = lines[0].split(',')
    # for this_seq in init_seq:
    #     verification_sum += run_hash(this_seq)
    #
    # for i in range(256):  # Generate our list of LensBoxes
    #     lens_boxes[i] = LensBox(i, [], [])
    #
    # for counter, this_seq in enumerate(init_seq):
    #     label, focal_length = re.split('-|=', this_seq)
    #     box_num = run_hash(label)
    #     if '-' in this_seq:
    #         # Using a janky try-except to find out whether the label is already in the box
    #         try:
    #             remove_index = lens_boxes[box_num].lens_labels.index(label)
    #         except ValueError:
    #             # It's not in the box, do nothing
    #             pass
    #         else:
    #             # It's in the box, delete it and its focal length
    #             del lens_boxes[box_num].lens_labels[remove_index]
    #             del lens_boxes[box_num].focal_lengths[remove_index]
    #     elif '=' in this_seq:
    #         try:
    #             replace_index = lens_boxes[box_num].lens_labels.index(label)
    #         except ValueError:
    #             # It's not in the box, append it to the end of the list
    #             lens_boxes[box_num].lens_labels.append(label)
    #             lens_boxes[box_num].focal_lengths.append(int(focal_length))
    #         else:
    #             # A lens with this label is already in the box, replace it with new lens
    #             lens_boxes[box_num].lens_labels[replace_index] = label
    #             lens_boxes[box_num].focal_lengths[replace_index] = int(focal_length)
    #
    # total_power = 0
    # for box in lens_boxes:
    #     for i, fl in enumerate(lens_boxes[box].focal_lengths):
    #         print(lens_boxes[box])
    #         lens_power = (1 + box) * (i + 1) * fl
    #         total_power += lens_power
    #         print(1 + int(box), fl, i+1, lens_power, total_power)
    #
    # print(f"Part 1: {verification_sum}")
    # print(f"Part 2: {total_power}")

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
