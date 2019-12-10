#!/usr/bin/env python

import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def advent_8a(input, sizes):
    nx = size[1]
    ny = size[0]
    # np array
    dg_1d = np.asarray([int(x) for x in input])
    nz = int(dg_1d.size/(nx * ny))
    # print(nx, ny, nz)

    # 3d np array with last axis being number of layers
    mx = dg_1d.reshape((nz, ny, nx))

    # zeros True, rest False
    mx0 = mx == 0

    # number of zeros "along" the z axis (in each layer), 1d array
    zeros = np.sum(mx0, axis=(1,2))

    # index of the min in the array, multiple occurrences - the first is returned
    # zero minimum value
    min = np.min(zeros)
    # index of zero  minimum value
    minpos = np.argmin(zeros)

    # # non-zero minimum value
    # min = np.min(ma.masked_where(zeros == 0, zeros))
    # # index of non-zero minimum value
    # minpos = np.argmin(ma.masked_where(zeros == 0, zeros))

    # get the layer based on args
    lay0 = mx[minpos, :, :]

    # 1d array of ones, twos
    mx1 = lay0[lay0 == 1]
    mx2 = lay0[lay0 == 2]
    # 1 digits multiplied by the number of 2 digits
    return mx1.size * mx2.size


def advent_8b(input, sizes):
    nx = size[1]
    ny = size[0]
    # np array
    dg_1d = np.asarray([int(x) for x in input])
    nz = int(dg_1d.size / (nx * ny))

    # 3d np array with last axis being number of layers
    mx = dg_1d.reshape((nz, ny, nx))
    # transpose to have the values along the layers
    mx = np.transpose(mx)
    # non 2 indeces
    indices = np.argmax(mx < 2, axis=2)
    values = np.copy(indices)
    # loop in 2 dimensions
    for i in np.ndindex(mx.shape[:2]):
        values[i] = mx[i][indices[i]]

    imgplot = plt.imshow(values)
    plt.show()

    return values


if __name__ == "__main__":
    import time

    start_time = time.time()
    test = False

    if test:
        input = "123456719012012012"
        size = [2, 3]

        # 0: 0,1,2
        # 1: 1,2,2
        # 2: 1,1,2
        # t: 1,2,4
        output = advent_8a(input, size)
        print("8a: ", output)

        input = "0222112222120000"
        size = [2, 2]
        output = advent_8b(input, size)
        print("8b:")
        print(output)

    else:
        with open("inputs/input_08.txt", "r") as f:
            for line in f:
                line = line.strip()
        f.close()

        size = [6, 25]
        output = advent_8a(line, size)
        print("8a: ", output)
        output = advent_8b(line, size)
        print("8b:")
        print(output)

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")