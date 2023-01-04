#!/usr/bin/env python3

import numpy as np


def opponent(oplist):
    rock = 1
    paper = 2
    scissors = 3

    opp = rock  # A
    if oplist == "B":
        opp = paper
    elif oplist == "C":
        opp = scissors
    return opp


def advent_a(arr, games):
    rock = 1
    paper = 2
    scissors = 3

    garr = []  # game
    marr = []  # myself

    i = 0
    while i < len(arr):
        opmy = arr[i].split(" ")

        # assign opponent's move
        opp = opponent(opmy[0])

        my = rock
        if opmy[1] == "Y":
            my = paper
        elif opmy[1] == "Z":
            my = scissors
        marr.append(my)

        garr.append(games[opp-1, my-1]) # indices
        i += 1
    return np.sum(garr) + np.sum(marr)


def advent_b(arr, games):
    loss = 0
    draw = 3
    win = 6

    garr = []  # game array
    marr = []  # myself

    i = 0
    while i < len(arr):
        opmy = arr[i].split(" ")

        # assign opponent's move
        opp = opponent(opmy[0])

        myg = loss
        if opmy[1] == "Y":
            myg = draw
        elif opmy[1] == "Z":
            myg = win
        garr.append(myg)

        index = np.where(games[opp - 1,:] == myg)   # find index of myg row with draw, loss, win points (3, 0, 6)

        marr.append(index[0][0] + 1)    # index +1
        i += 1
    return np.sum(garr) + np.sum(marr)


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr = ["A Y", "B X", "C Z"]
        pass
    else:
        with open("inputs/input_02.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    # myself = columns (rock, paper, scissors), opponent = rows (rock, paper, scissors)
    # draw = 3 (diagonal), my win = 6, my loss = 0
    # [[3 6 0]
    #  [0 3 6]
    #  [6 0 3]]
    games = np.array([[3, 6, 0], [0, 3, 6], [6, 0, 3]], np.int32)

    print(advent_a(arr, games))
    print(advent_b(arr, games))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
