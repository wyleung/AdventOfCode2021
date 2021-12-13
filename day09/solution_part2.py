#!/usr/bin/env python3

import math
import typing
import sys

input_file = sys.argv[1]
input_data = open(input_file)
input_grid = input_data.readlines()

grid = [[int(val) for val in line.strip()] for line in input_grid]

map_bounds = [len(grid) - 1, len(grid[0]) - 1]


def get_neighbors(pos_y, pos_x, map_bounds):
    neighbours = [
        (pos_y + 1, pos_x),
        (pos_y - 1, pos_x),
        (pos_y, pos_x + 1),
        (pos_y, pos_x - 1),
    ]
    max_y, max_x = map_bounds
    # filter out points out of bounds
    neighbours = filter(
        lambda x: x[1] <= max_x and x[1] >= 0,
        filter(lambda y: y[0] <= max_y and y[0] >= 0, neighbours),
    )

    return list(neighbours)


def is_lowest_point(grid, pos_x, pos_y, map_bounds):
    # is this position the lowest point in N/E/S/W ?
    this_height = grid[pos_y][pos_x]

    neighbours = get_neighbors(pos_y, pos_x, map_bounds)
    for neighbour_y, neighbour_x in neighbours:
        if this_height > grid[neighbour_y][neighbour_x]:
            return False
    return True


def get_low_points(grid, map_bounds) -> typing.List:
    """
    Find low points in grid
    A low point is a "local" lowest point
    """
    low_coords = []

    for pos_y, line in enumerate(grid):
        for pos_x, value in enumerate(line):
            if is_lowest_point(grid, pos_x, pos_y, map_bounds):
                low_coords.append((pos_y, pos_x))
    return low_coords


def get_basin(pos_x, pos_y, grid, map_bounds):
    to_evaluate = [(pos_y, pos_x)]
    basin_points = []

    while len(to_evaluate) > 0:
        pos_y, pos_x = to_evaluate.pop()
        basin_points.append((pos_y, pos_x))

        for neighbour_y, neighbour_x in get_neighbors(pos_y, pos_x, map_bounds):
            # skip ones already defined in the current basin
            if (neighbour_y, neighbour_x) in basin_points:
                continue
            # skip 9
            if grid[neighbour_y][neighbour_x] == 9:
                # print(f"skipping 9 at {pos_y}, {pos_x}")
                continue
            # preconditions passed
            # see whether we can extend fromt the neighbour point
            to_evaluate.append((neighbour_y, neighbour_x))
    return sorted(set(basin_points))


low_points = get_low_points(grid, map_bounds)
basins = []
for low_point in low_points:
    basin = get_basin(low_point[1], low_point[0], grid, map_bounds)
    # print(low_point, basin, len(basin))
    basins.append(basin)

sorted_basins = sorted(basins, key=lambda x: len(x), reverse=True)
sorted_basin_sizes = [len(x) for x in sorted_basins][:3]
print(
    f"Find the three largest basins and multiply their sizes together. This is {sorted_basin_sizes[0]} * {sorted_basin_sizes[1]} * {sorted_basin_sizes[2]} = {math.prod(sorted_basin_sizes)}"
)
