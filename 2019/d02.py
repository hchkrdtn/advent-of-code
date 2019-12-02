#!/usr/bin/env python

import numpy as np


def advent_2a(input):
    last = np.where(input == 99)[0][-1]
    rules = input[0:last+1]
    for idx in range(0,int(np.floor(rules.size/4))):
        row = input[idx*4:(idx+1)*4]

        last = np.where(input == 99)[0][-1]
        last = max(last,row[3])

        if row[0] == 1:
            input[row[3]] = input[row[1]] + input[row[2]]
        elif row[0] == 2:
            input[row[3]] = input[row[1]] * input[row[2]]

    output = input[0:last+1]
    # print(output)
    return output[0]

def advent_2b(input):
    for noun in range(0, 100):
        for verb in range(0, 100):
            input_tmp = np.copy(input)
            input_tmp[1] = noun
            input_tmp[2] = verb

            output = advent_2a(input_tmp)
            if output == 19690720:
                print(str(100 * noun + verb) + ": " + str(output))
                return


if __name__ == "__main__":
    import time

    start_time = time.time()

    input = np.array([1,9,10,3,2,3,11,0,99,30,40,50])
    # 3500,9,10,70,2,3,11,0,99
    print(advent_2a(input))
    input = np.array([1,0,0,0,99])
    # 2,0,0,0,99
    print(advent_2a(input))
    input = np.array([2,3,0,3,99])
    # 2,3,0,6,99
    print(advent_2a(input))
    input = np.array([2,4,4,5,99,0])
    # 2,4,4,5,99,9801
    print(advent_2a(input))
    input = np.array([1,1,1,4,99,5,6,0,99])
    # 30,1,1,4,2,5,6,0,99
    print(advent_2a(input))

    input = np.array([1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,5,19,23,1,6,23,27,1,27,10,31,1,31,5,35,2,10,35,39,1,9,39,43,1,43,5,47,1,47,6,51,2,51,6,55,1,13,55,59,2,6,59,63,1,63,5,67,2,10,67,71,1,9,71,75,1,75,13,79,1,10,79,83,2,83,13,87,1,87,6,91,1,5,91,95,2,95,9,99,1,5,99,103,1,103,6,107,2,107,13,111,1,111,10,115,2,10,115,119,1,9,119,123,1,123,9,127,1,13,127,131,2,10,131,135,1,135,5,139,1,2,139,143,1,143,5,0,99,2,0,14,0])
    print(advent_2a(input))

    input = np.array([1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,5,19,23,1,6,23,27,1,27,10,31,1,31,5,35,2,10,35,39,1,9,39,43,1,43,5,47,1,47,6,51,2,51,6,55,1,13,55,59,2,6,59,63,1,63,5,67,2,10,67,71,1,9,71,75,1,75,13,79,1,10,79,83,2,83,13,87,1,87,6,91,1,5,91,95,2,95,9,99,1,5,99,103,1,103,6,107,2,107,13,111,1,111,10,115,2,10,115,119,1,9,119,123,1,123,9,127,1,13,127,131,2,10,131,135,1,135,5,139,1,2,139,143,1,143,5,0,99,2,0,14,0])
    advent_2b(input)

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
