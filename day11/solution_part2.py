#!/usr/bin/env python3

import math
import sys

input_file = sys.argv[1]
input_data = open(input_file)
input_dataset = input_data.readlines()

grid = [[int(x) for x in row.strip()] for row in input_dataset]
for row in grid:
    print("".join(map(str, row)))
print()
# print(octo_grid)
map_bounds = [len(grid) - 1, len(grid[0]) - 1]


def get_neighbors(pos_x, pos_y, map_bounds):
    neighbours = [
        (pos_x, pos_y + 1),  # S
        (pos_x, pos_y - 1),  # N
        (pos_x + 1, pos_y),  # E
        (pos_x - 1, pos_y),  # W
        (pos_x - 1, pos_y - 1),  # NW
        (pos_x - 1, pos_y + 1),  # SW
        (pos_x + 1, pos_y - 1),  # NE
        (pos_x + 1, pos_y + 1),  # SE
    ]
    max_y, max_x = map_bounds
    # filter out points out of bounds
    neighbours = filter(
        lambda x: x[0] <= max_x and x[0] >= 0,
        filter(lambda y: y[1] <= max_y and y[1] >= 0, neighbours),
    )
    return list(neighbours)


def increase_energy(grid):
    # this is increasing energy for one step
    # keep track of which octo had flashed, reset to energy 0 before returning grid
    flashes = []
    new_grid = grid.copy()
    collateral_increases = []

    # # first increase
    for y, row in enumerate(new_grid):
        for x, val in enumerate(row):
            collateral_increases.append((x, y))
    while len(collateral_increases) > 0:
        point = collateral_increases.pop()
        # print(point)
        if point in flashes:
            # don't do this point, this octo already has flashed
            continue
        # increase energy level of the point
        x, y = point
        new_grid[y][x] += 1
        if new_grid[y][x] == 10:
            if (x, y) not in flashes:
                flashes.append((x, y))
            collateral_increases.extend(get_neighbors(x, y, map_bounds))

    # any position that had flashed is reset to 0
    for point in flashes:
        x, y = point
        new_grid[y][x] = 0

    return new_grid, len(flashes)


flashes = 0
step = 0

while flashes < (math.prod([len(grid), len(grid)])):
    step += 1
    print(f"After step {step}:")
    grid, flashes = increase_energy(grid)
    for row in grid:
        print("".join(map(str, row)))
    print(flashes)
