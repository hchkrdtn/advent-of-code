#!/usr/bin/env python3

import numpy as np
import collections


def advent_15a(input, no):
    game = np.full((no), -1)
    game[0:len(input)] = input
    turn = len(input) - 1
    while True:
        prev = np.nonzero(game == game[turn:turn + 1])
        if prev[0].size == 0 or prev[0].size == 1:
            game[turn+1:turn+2] = 0
        else:
            game[turn+1:turn+2] = prev[0][-1:] - prev[0][-2:-1]
        if turn == game.size - 1:
            break
        turn += 1
    return game[-1]


def advent_15b(input, no):
    # too slow for large numbers
    game = collections.deque(input)
    game.reverse()
    turn = len(input) - 1
    while True:
        last_ch = game[0]
        try:
            prev = game.index(last_ch, 0, len(game))
            prev2 = game.index(last_ch, prev + 1, len(game))
            game.appendleft(prev2 - prev)
        except ValueError:
            game.appendleft(0)
        if len(game) == no:
            break
        turn += 1
    mylist = []
    for o in reversed(game):
        mylist.append(o)
    print(mylist)
    return game[0]


def advent_15b2(input, no):
    game = collections.deque(input)
    numbers = {}
    # populate first two
    for idx in range(0, len(game)-1):
        if game[idx] in numbers:
            numbers[game[idx]][0] = numbers[game[idx]][1]
            numbers[game[idx]][1] = game.index(game[idx], 0, len(input))
        else:
            numbers[game[idx]] = [-1, game.index(game[idx], 0, len(input))]
    # print(numbers)
    turn = len(input) - 1
    while True:
        last_ch = game[-1]
        if last_ch not in numbers:
            game.append(0)
            numbers[last_ch] = [-1, turn]
        else:
            numbers[last_ch][0] = numbers[last_ch][1]
            numbers[last_ch][1] = turn
            game.append(numbers[last_ch][1] - numbers[last_ch][0])
        # print(turn, last_ch, numbers)
        if len(game) == no:
            break
        turn += 1
    return game[-1]


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = True
    if test:
        in_list = [0,3,6] #436, 175594
        # in_list = [1,3,2] #1, 2578
        # in_list = [2,1,3] #10, 3544142
        # in_list = [1,2,3] #27, 261214
        # in_list = [2,3,1] #78, 6895259
        # in_list = [3,2,1] #438, 18
        in_list = [3,1,2] #1836, 362
        no = 2020
        pass
    else:
        in_list = [0,20,7,16,1,18,15]
        no = 30000000


    # print(advent_15a(in_list, no))
    # print(advent_15b(in_list, no))
    print(advent_15b2(in_list, no))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
