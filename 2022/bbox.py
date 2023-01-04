#!/usr/bin/env python3


class BoundingBox:
    """ Find bounding box from coordinates or moving directions. """

    def __init__(self, input, coord_orient=True, origin=True):
        """ Get parameters for the Bounding box calculator.

            Args:
                input (list): Points defined by moving direction and distance, snake-like or by coordinates
                coord_orient (bool): True: x -> right, y -> bottom,
                                     False: x -> bottom, y -> right
                origin (bool):       True re-scales the coordinates to [0, 0] of the new box from all points.
                                     False leaves coordinates with [0, 0] being the first incoming point

        """
        self.input = input
        self.coord_orient = coord_orient
        self.origin = origin

    def get_bbox_direction(self):
        """ Get sizes of the bounding box based on the points positions and directions, such as points moving
        in some snake motion.
        Coordinate orientation and box zero origin are also set. Returns three lists of x, y values, 1) the size of
        the box - delta x and delta y, 2) coordinates of the starting point, 3) coordinates of the end point

        Tests:
        Input: ["R 4", "U 4", "L 6", "D 1", "R 4", "D 5", "L 5", "R 2"]
               0  1  2  3  4  5  6  7
            0  . x3  x  x  x  x  x x2
            1  . x4  x  x  x x5  .  x
            2  .  .  .  .  .  x  .  x
            3  .  .  .  .  .  x  .  x
            4  .  .  .  S  x  x  x x1
            5  .  .  .  .  .  x  .  .
            6 x7  x  E  x  x  x6 .  .

            True, True: ([8, 7], [3, 4], [2, 6])
            True, False: ([8, 7], [0, 0], [-1, 2])
            False, True: ([7, 8], [4, 3], [6, 2])
            False, False: ([7, 8], [0, 0], [2, -1])

        Return:
            delta_xy: list
            xy_start: list
            xy_end: list

        """
        input = self.input
        d1 = 0
        d2 = 0
        d1_min = 0
        d1_max = 0
        d2_min = 0
        d2_max = 0

        for leg in input:
            dirc = leg.split(" ")[0]
            dist = int(leg.split(" ")[1])
            if dirc == "L" or dirc == "U":
                dist = dist * (-1)

            if dirc == "R" or dirc == "L":
                d1 += dist
                d1_min = min(d1_min, d1)
                d1_max = max(d1_max, d1)
            elif dirc == "U" or dirc == "D":
                d2 += dist
                d2_min = min(d2_min, d2)
                d2_max = max(d2_max, d2)

        if self.coord_orient:
            x = d1
            y = d2
            x_min = d1_min
            x_max = d1_max
            y_min = d2_min
            y_max = d2_max
        else:
            x = d2
            y = d1
            x_min = d2_min
            x_max = d2_max
            y_min = d1_min
            y_max = d1_max

        delta_xy = [abs(x_min) + abs(x_max) + 1, abs(y_min) + abs(y_max) + 1]
        if self.origin:
            xy_start = [abs(x_min), abs(y_min)]
            xy_end = [x + abs(x_min), y + abs(y_min)]
        else:
            xy_start = [0, 0]
            xy_end = [x, y]

        return delta_xy, xy_start, xy_end

    def get_bbox_coord(self):
        """ Get sizes of the bounding box based on the points coordinates, such as points moving in some snake motion.
        Box zero origin are also set. Returns two lists of x, y values, 1) the size of
        the box - delta x and delta y, 2) coordinates of the points re-scaled to [0, 0] of the new box.

        Tests:
        Input: [[0, 0], [4, 0], [4, -4], [-2, -4], [-2, -3], [2, -3], [2, 2], [-3, 2], [-1, 2]]
            Coordinate orientation: x -> right          Coordinate orientation: x -> down
               0  1  2  3  4  5  6  7                      0  1  2  3  4  5  6
            0  . x3  x  x  x  x  x x2                   0  .  .  .  .  .  . x7
            1  . x4  x  x  x x5  .  x                   1 x3 x4  .  .  .  .  x
            2  .  .  .  .  .  x  .  x                   2  x  x  .  .  .  .  E
            3  .  .  .  .  .  x  .  x                   3  x  x  .  .  S  .  x
            4  .  .  .  S  x  x  x x1                   4  x  x  .  .  x  .  x
            5  .  .  .  .  .  x  .  .                   5  x x5  x  x  x  x x6
            6 x7  x  E  x  x  x6 .  .                   6  x  .  .  .  x  .  .
                                                        7 x2  x  x  x x1  .  .
        Output: ([8, 7], [[3, 4], [7, 4], [7, 0], [1, 0], [1, 1], [5, 1], [5, 6], [0, 6], [2, 6]])

        Return:
            delta_xy: list
            xy: list

        """
        input = self.input
        x_min = 0
        x_max = 0
        y_min = 0
        y_max = 0

        i = 0
        while i < len(input):
            x = input[i][0]
            y = input[i][1]

            x_min = min(x_min, x)
            x_max = max(x_max, x)
            y_min = min(y_min, y)
            y_max = max(y_max, y)
            i += 1

        xy = []
        for point in input:
            xy.append([point[0] + x_min * (-1), point[1] + y_min * (-1)])
        delta_xy = [abs(x_min) + abs(x_max) + 1, abs(y_min) + abs(y_max) + 1]

        return delta_xy, xy

    def direct_to_coord(self):
        """ Convert points directions, such as points moving in some snake motion to coordinates.
        Coordinate orientation is also set. Returns t lists of x, y values

        Tests:
        Input:  ["R 4", "U 4", "L 6", "D 1", "R 4", "D 5", "L 5", "R 2"]
        Output: [[0,0], [4,0], [4,-4], [-2,-4], [-2,-3], [2,-3], [2,2], [-3,2], [-1,2]]

        Return:
            coords: list

        """
        input = self.input
        d1 = 0
        d2 = 0
        coords = [[d1, d2]]
        for leg in input:
            dirc = leg.split(" ")[0]
            dist = int(leg.split(" ")[1])
            if dirc == "L" or dirc == "U":
                dist = dist * (-1)

            if dirc == "R" or dirc == "L":
                d1 += dist
            elif dirc == "U" or dirc == "D":
                d2 += dist

            if self.coord_orient:
                x = d1
                y = d2
            else:
                x = d2
                y = d1
            coords.append([x, y])

        return coords
