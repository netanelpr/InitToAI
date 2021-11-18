import numpy as np


def create_grid(grid_num=1):
    if grid_num == 1:
        with open("grid_1", "rt") as infile:
            return np.array(np.matrix([list(line.strip()) for line in infile.readlines()]))
    if grid_num == 2:
        with open("grid_2", "rt") as infile:
            return np.array(np.matrix([list(line.strip()) for line in infile.readlines()]))


def get_start_location():
    return tuple((0, 0))


