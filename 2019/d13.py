#!/usr/bin/env python

import numpy as np
import pandas as pd
import sys
import pygame
import random

from pcounter import VM

# pygame did not installed on Python 3.8 on ElCapitan (10.11.6) of 12/13. Python 3.7 works.

# fill window with random colors defined by an array
def test_random():
    pygame.init()
    size = width, height = 320, 240
    # speed = [2, 2]

    arr = []
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    arr.append(red)
    #arr.append(green)
    arr.append(blue)
    arr.append(black)

    # Creates a new Surface object that represents the actual displayed graphics.
    # Any drawing you do to this Surface will become visible on the monitor.
    screen = pygame.display.set_mode(size)
    square = pygame.Surface((1, 1))

    for j in range(width):
        for i in range(height):
            num = random.randint(0, len(arr) - 1)
            square.fill(arr[num])
            draw_me = pygame.Rect((j + 1), (i + 1), 1, 1)
            screen.blit(square, draw_me)
    pygame.display.flip()

    # Pygame closes when window button x is pressed
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


def test_resize():
    screen_width, screen_height = 20, 20

    scale = 6

    x, y = 10, 10
    rect_width, rect_height = 2, 2
    vel = 2
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 255, 0)
    green = (0, 0, 255)
    pygame.init()
    window = pygame.display.set_mode((screen_width * scale, screen_height * scale))

    screen = pygame.Surface((screen_width, screen_height))

    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(black)
        pygame.draw.rect(screen, white, (x, y, rect_width, rect_height))
        pygame.draw.rect(screen, blue, (x+5, y+5, rect_width, rect_height))

        window.blit(pygame.transform.scale(screen, window.get_rect().size), (0, 0))
        pygame.display.update()
    pygame.quit()


def advent_13a(p_instr):
    elems = {0: list(), 1: list(), 2: list(), 3: list(), 4: list()}

    vm = VM(p_instr)
    vm.input = [1]

    triple = [0, 0, 0]
    state = []
    index = 0
    while True:
        if index > 0:
            vm.ip = state[0]
            vm.rb = state[1]
            vm.instr = state[2]
        output = vm.run(True)
        if index > 0 and index % 3 == 0:
            # print(triple)

            tmp = elems[triple[2]]
            # 13b, read the score
            if triple[0] == -1 and triple[1] == 0:
                print(triple[3])
            else:
                tmp.append([triple[0], triple[1]])
                elems[triple[2]] = tmp

        triple[index % 3] = output
        if output == 99:
            break
        state = [vm.ip, vm.rb, vm.instr]
        index += 1

    return elems


def advent_13b(p_instr):
    joystick = 0

    vm = VM(p_instr)
    vm.input = [joystick]

    triple = [0, 0, 0]
    paddle = []
    ball = []
    score = 0
    index = 0
    while True:
        output = vm.run(True)
        print(vm.input)
        if index > 0 and index % 3 == 0:
            print(triple)
            if triple[0] == -1 and triple[1] == 0:
                print(triple[2])
                score = triple[2]
            elif triple[2] == 3:
                paddle = [triple[0], triple[1]]
                joystick = jstick(paddle, ball)
            elif triple[2] == 4:
                ball = [triple[0], triple[1]]
                joystick = jstick(paddle, ball)
            vm.input = [joystick]
        triple[index % 3] = output
        if output == 99:
            break
        index += 1

    return score


def jstick(paddle, ball):
    if paddle and ball:
        if paddle[0] == ball[0]:
            return 0
        elif paddle[0] < ball[0]:
            return 1
        elif paddle[0] > ball[0]:
            return -1
        else:
            return 0
    else:
        return 0

def get_game_init(p_instr):
    elems = {0: list(), 1: list(), 2: list(), 3: list(), 4: list()}

    vm = VM(p_instr)
    vm.input = [1]

    triple = [0, 0, 0]
    state = []
    index = 0
    while True:
        if index > 0:
            vm.ip = state[0]
            vm.rb = state[1]
            vm.instr = state[2]
        output = vm.run(True)
        if index > 0 and index % 3 == 0:
            # print(triple)
            tmp = elems[triple[2]]
            tmp.append([triple[0], triple[1]])
            elems[triple[2]] = tmp

        triple[index % 3] = output
        if output == 99:
            break
        state = [vm.ip, vm.rb, vm.instr]
        index += 1

    return elems


def game_init(colors, elems, screen_size, scale, rect_size):
    # 0 is an empty tile. No game object appears in this tile. (white)
    # 1 is a wall tile. Walls are indestructible barriers. (red)
    # 2 is a block tile. Blocks can be broken by the ball. (green)
    # 3 is a horizontal paddle tile. The paddle is indestructible. (black)
    # 4 is a ball tile. The ball moves diagonally and bounces off objects. (blue)

    pygame.init()

    window = pygame.display.set_mode((screen_size[0] * scale, screen_size[1] * scale))
    screen = pygame.Surface((screen_size[0], screen_size[1]))

    screen.fill(white)

    for idx in range(len(elems)):
        # no need for white
        if elems[idx] and idx > 0:
            for cord in elems[idx]:
                pygame.draw.rect(screen, colors[idx], (cord[0], cord[1], rect_width, rect_height))

            window.blit(pygame.transform.scale(screen, window.get_rect().size), (0, 0))
    pygame.display.update()
    print(len(elems[2]))

    # pygame closes when window button x is pressed
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


def play_game(colors, elems, screen_size, scale, rect_size):
    # 0 is an empty tile. No game object appears in this tile. (white)
    # 1 is a wall tile. Walls are indestructible barriers. (red)
    # 2 is a block tile. Blocks can be broken by the ball. (green)
    # 3 is a horizontal paddle tile. The paddle is indestructible. (black)
    # 4 is a ball tile. The ball moves diagonally and bounces off objects. (blue)

    pygame.init()

    window = pygame.display.set_mode((screen_size[0] * scale, screen_size[1] * scale))
    screen = pygame.Surface((screen_size[0], screen_size[1]))

    screen.fill(white)

    for idx in range(len(elems)):
        # no need for white
        if elems[idx] and idx > 0:
            for cord in elems[idx]:
                pygame.draw.rect(screen, colors[idx], (cord[0], cord[1], rect_width, rect_height))

            window.blit(pygame.transform.scale(screen, window.get_rect().size), (0, 0))
    pygame.display.update()
    print(len(elems[2]))

    # update_game(elems)
    ballrect = pygame.draw.rect(screen, colors[4], (elems[4][0][0], elems[4][0][1], rect_width, rect_height))
    pygame.draw.rect(screen, colors[0], (ballrect[0], ballrect[1], rect_width, rect_height))
    speed = [1, 1]
    i = 0
    while i in range(10000):
        pygame.time.wait(0)
        ball_next = [ballrect.move(speed)[0], ballrect.move(speed)[1]]
        if  ball_next in elems[2] or ball_next in elems[1]:
            # case when the ball is stuck between the wall and block tile
            pass
        else:
            ballrect = ballrect.move(speed)

        hit_h = False
        hit_v = False
        hit_paddle = False
        if [ballrect[0]+1, ballrect[1]] in elems[1] or [ballrect[0]-1, ballrect[1]] in elems[1]:
            hit_h = True
        if [ballrect[0], ballrect[1]-1] in elems[1]:
            hit_v = True
        if ballrect.move(speed)[1] == elems[3][0][1] and ballrect[0] == elems[3][0][0]+speed[0]:
            hit_paddle = True

        if hit_paddle or hit_v or ballrect.top < 1:
            speed[1] = -speed[1]
        # width
        if hit_h or ballrect.left < 1 or ballrect.right > screen_size[0] - 1:
            speed[0] = -speed[0]

        vapor = []
        hit_block_v = False
        hit_block_h = False
        hit_block_c = False # corner
        if [ballrect.move(speed)[0]-speed[0], ballrect.move(speed)[1]] in elems[2]:
            vapor = [ballrect.move(speed)[0]-speed[0], ballrect.move(speed)[1]]
            hit_block_v = True
        elif [ballrect.move(speed)[0], ballrect.move(speed)[1]-speed[1]] in elems[2]:
            vapor = [ballrect.move(speed)[0], ballrect.move(speed)[1]-speed[1]]
            hit_block_h = True
        if [ballrect.move(speed)[0], ballrect.move(speed)[1]] in elems[2]:
            vapor = [ballrect.move(speed)[0], ballrect.move(speed)[1]]
            hit_block_c = True
        # print(vapor)

        if hit_block_v:
            speed[1] = -speed[1]
        elif hit_block_h:
            speed[0] = -speed[0]
        elif hit_block_c:
            speed[0] = -speed[0]
            speed[1] = -speed[1]

        pygame.draw.rect(screen, colors[0], (elems[4][0][0], elems[4][0][1], rect_width, rect_height))
        pygame.draw.rect(screen, colors[0], (elems[3][0][0], elems[3][0][1], rect_width, rect_height))
        elems[4][0][0] = ballrect[0]
        elems[4][0][1] = ballrect[1]
        elems[3][0][0] = ballrect[0]
        for idx in range(len(elems)):
            if elems[idx] and idx > 0:
                for cord in elems[idx]:
                    pygame.draw.rect(screen, colors[idx], (cord[0], cord[1], rect_width, rect_height))

                window.blit(pygame.transform.scale(screen, window.get_rect().size), (0, 0))
        pygame.display.update()

        if vapor:
            elems[2].remove(vapor)
            #if i < 714:
            pygame.draw.rect(screen, colors[0], (vapor[0], vapor[1], rect_width, rect_height))
            # else:
            #     pygame.draw.rect(screen, (128, 0, 0), (vapor[0], vapor[1], rect_width, rect_height))
        i += 1

    # pygame closes when window button x is pressed
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print(len(elems[2]))
                exit()


if __name__ == "__main__":
    import time

    start_time = time.time()
    test = False

    if test:
        # test_random()
        # test_resize()

        p_instr = [1,2,3,6,5,4]
        # vm = VM(p_instr)
        fin = advent_13a(p_instr)
        # print("13a: ", fin)

    else:
        input = list()
        with open("inputs/input_13.txt", "r") as f:
            for line in f:
                p_instr = line.strip()
        f.close()

        # expand array memory part
        more = 100000000
        p_instr = p_instr.split(",")
        p_instr = np.asarray([int(x) for x in p_instr])
        p_instr = np.concatenate((p_instr, np.zeros((more), dtype=p_instr.dtype)))

        elems = advent_13a(p_instr)
        print("13a: ", len(elems[2]))

        p_instr[0] = 2
        score = advent_13b(p_instr)
        print("13b: ", score)

        # elems = get_game_init(p_instr)
        #
        # colors = []
        # white = (255, 255, 255)
        # red = (255, 0, 0)
        # green = (0, 255, 0)
        # black = (0, 0, 0)
        # blue = (0, 0, 255)
        # colors.append(white)
        # colors.append(red)
        # colors.append(green)
        # colors.append(black)
        # colors.append(blue)
        #
        # screen_size = screen_width, screen_height = 42, 24
        # scale = 10
        # rect_size = rect_width, rect_height = 1, 1
        #
        # output = game_init(colors, elems, screen_size, scale, rect_size)
        #
        # play_game(colors, elems, screen_size, scale, rect_size)

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")