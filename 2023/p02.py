#!/usr/bin/env python3

import numpy as np
import re
import regex as rex

def advent_a(arr):
    tot = 0

    # red <= 12, green <= 13, blue <= 14
    draw_max = (12, 13, 14)
    for i, item in enumerate(arr):
        flag = True
        games = item.split(":")
        game = int(re.findall(pattern=r"[+-]?\d+", string=games[0])[0])

        draws = games[1].split(";")
        for draw in draws:
            red = 0
            blue = 0
            green = 0
            redex = re.findall(r"(\d+)(?=\s*red)", draw)
            if redex:
                red = int(redex[0])
            blueex = re.findall(r"(\d+)(?=\s*blue)", draw)
            if blueex:
                blue = int(blueex[0])
            greenex = re.findall(r"(\d+)(?=\s*green)", draw)
            if greenex:
                green = int(greenex[0])
            if (red > draw_max[0]) or green > draw_max[1] or blue > draw_max[2]:
                flag = False
                break
        if flag:
            tot += game
    return tot

def advent_b(arr):
    tot = 0

    # red <= 12, green <= 13, blue <= 14
    draw_max = (12, 13, 14)
    for item in arr:
        games = item.split(": ")
        game_id = int(re.findall(pattern=r"\d+", string=games[0])[0])

        draws = games[1].split(";")
        red = 0
        blue = 0
        green = 0
        for draw in draws:
            redex = re.findall(r"(\d+)(?=\s*red)", draw)
            if redex:
                red = max(red, int(redex[0]))
            blueex = re.findall(r"(\d+)(?=\s*blue)", draw)
            if blueex:
                blue = max(blue, int(blueex[0]))
            greenex = re.findall(r"(\d+)(?=\s*green)", draw)
            if greenex:
                green = max(green, int(greenex[0]))
        # rgb = (red, green, blue)
        tot += (red * green * blue)
    return tot


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr_a = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
                 "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
                 "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
                 "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
                 "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
        arr = arr_a
        pass
    else:
        with open("inputs/input_02.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    print(advent_a(arr))
    print(advent_b(arr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
