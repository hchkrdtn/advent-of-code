#!/usr/bin/env python3

import numpy as np


def advent_a(arr):
    labels = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9,
              "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}
    # strength = {"Five": [5],
    #             "Four": [4, 1],
    #             "Full": [3, 2],
    #             "Three": [3, 1, 1],
    #             "Two": [2, 2, 1],
    #             "One": [2,1,1,1],
    #             "High": [1, 1, 1, 1, 1]}
    strength = [[1, 1, 1, 1, 1], [2, 1, 1 ,1], [2, 2, 1], [3, 1, 1], [3, 2], [4, 1], [5]]

    res = []
    for i, game in enumerate(arr):
        game = game.split(" ")

        # [index_strength, n1, n2, n3, n4, n5, int(game[1]), i]
        # where 32T3K = 2 1 10 2 12 in numbers n1-n5, numbers are needed
        # for soring
        tmp = [0, 0, 0, 0, 0, 0, int(game[1]), i]
        cnt = {}
        for k in range(0, 5):
            let = game[0][k:k+1]
            if let in cnt:
                cnt[let] += 1
            else:
                cnt[let] = 1
            tmp[k+1] = labels[let]

        hand_idx = list(cnt.values())
        hand_idx.sort(reverse=True)

        idx = [ind for ind, ele in enumerate(strength) if ele == hand_idx]
        tmp[0] = idx[0]

        res.append(tmp)
    # print(res)
    # complex sorting by 1 + 5 digits
    res.sort(key=lambda res: (res[0], res[1], res[2], res[3], res[4], res[5]))
    # print(res)

    tot = 0
    for i, r in enumerate(res):
        tot += (i + 1) * r[-2]
    # 765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5 = 6440
    return tot


def advent_b(arr):
    labels = {"A": 13, "K": 12, "Q": 11, "J": 0, "T": 9,
              "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}
    strength = [[1, 1, 1, 1, 1], [2, 1, 1 ,1], [2, 2, 1], [3, 1, 1], [3, 2], [4, 1], [5]]

    res = []
    for i, game in enumerate(arr):
        game = game.split(" ")

        tmp = [0, 0, 0, 0, 0, 0, int(game[1]), i]
        cnt = {}
        for k in range(0, 5):
            let = game[0][k:k+1]
            if let in cnt:
                cnt[let] += 1
            else:
                cnt[let] = 1
            tmp[k+1] = labels[let]

        hand_idx = list(cnt.values())
        hand_idx.sort(reverse=True)

        # Look up table for replacing combinations with J
        # if "J" in cnt:
        #     print(cnt["J"])
        if "J" in cnt and cnt["J"] == 1:
            if hand_idx == [1, 1, 1, 1, 1]:
                hand_idx = [2, 1, 1, 1]
            elif hand_idx == [2, 1, 1, 1]:
                hand_idx = [3, 1, 1]
            elif hand_idx == [2, 2, 1]:
                hand_idx = [3, 2]
            elif hand_idx == [3, 1, 1]:
                hand_idx = [4, 1]
            elif hand_idx == [4, 1]:
                hand_idx = [5]
        elif "J" in cnt and cnt["J"] == 2:
            if hand_idx == [2, 1, 1, 1]:
                hand_idx = [3, 1, 1]
            elif hand_idx == [2, 2, 1]:
                hand_idx = [4, 1]
            elif hand_idx == [3, 2]:
                hand_idx = [5]
        elif "J" in cnt and cnt["J"] == 3:
            if hand_idx == [3, 1, 1]:
                hand_idx = [4, 1]
            elif hand_idx == [3, 2]:
                hand_idx = [5]
        elif "J" in cnt and cnt["J"] == 4:
            if hand_idx == [4, 1]:
                hand_idx = [5]

        idx = [ind for ind, ele in enumerate(strength) if ele == hand_idx]
        tmp[0] = idx[0]

        res.append(tmp)
    # print(res)
    res.sort(key=lambda res: (res[0], res[1], res[2], res[3], res[4], res[5]))
    # print(res)

    tot = 0
    for i, r in enumerate(res):
        tot += (i + 1) * r[-2]
    # 765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5 = 6440
    return tot


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = True
    if test:
        arr_a = ["32T3K 765",
                 "T55J5 684",
                 "KK677 28",
                 "KTJJT 220",
                 "QQQJA 483"]
        arr = arr_a
        pass
    else:
        with open("inputs/input_07.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    print(advent_a(arr))
    print(advent_b(arr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
