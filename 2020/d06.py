#!/usr/bin/env python3

import numpy as np
import re


def advent_6a(inpt):
    inpt = inpt.replace("\n\n", "#").replace("\n", "")
    qa_all = re.split("#", inpt)

    n_qa = 0
    for qa in qa_all:
        n_qa += len(set(qa))
    return n_qa


def advent_6b(inpt):
    inpt = inpt.replace("\n", " ").replace("  ", "\n")
    entries = re.split("\n", inpt)
    qa_all = [re.split(" ", entry) for entry in entries]

    n_qa = 0
    for qa in qa_all:
        # join all strings
        x = "".join(qa)
        labels, counts = np.unique(list(x), return_counts=True)
        idxs = np.where(counts == len(qa))

        # non empty array in tuple
        if idxs[0].size > 0:
            n_qa += idxs[0].size
    return n_qa


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        input_text = "abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb"
        pass
    else:
        with open("inputs/input_06.txt", "r") as f:
            input_text = f.read()
        f.close()
        # print(input_text)

    print(advent_6a(input_text))
    print(advent_6b(input_text))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
