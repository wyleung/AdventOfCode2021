#!/usr/bin/env python3

import collections
import copy
import sys

input_file = sys.argv[1]
input_data = open(input_file)
input_dataset = input_data.readlines()

# move into individual points
grid = [[x for x in row.strip()] for row in input_dataset]
# print(grid)


def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()


def in_bound(pos, map_bounds):
    return pos[0] < map_bounds[0] and pos[1] < map_bounds[1]


def move_sea_cucumbers(grid):
    # print(grid)
    # python 0-index based bounds for the grid
    map_bounds = (len(grid), len(grid[0]))

    new_grid = copy.deepcopy(grid)
    # move east
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == ">":
                # try to move right
                next_pos = (y, x + 1)
                # is next_pos in bounds?
                if not in_bound(next_pos, map_bounds):
                    # print(f"{map_bounds}, {next_pos},  {y}, {x} {col} not in bound")
                    next_pos = (y, 0)
                ny, nx = next_pos
                if grid[ny][nx] == ".":
                    new_grid[y][x] = "."
                    new_grid[ny][nx] = col
            # print(grid, new_grid)

    # # move south
    vnew_grid = copy.deepcopy(new_grid)
    for y, row in enumerate(new_grid):
        for x, col in enumerate(row):
            if col == "v":
                # try to move right
                next_pos = (y + 1, x)
                # is next_pos in bounds?
                if not in_bound(next_pos, map_bounds):
                    # print(f"{map_bounds}, {next_pos},  {y}, {x} {col} not in bound")
                    next_pos = (0, x)
                ny, nx = next_pos
                if new_grid[ny][nx] == ".":
                    vnew_grid[y][x] = "."
                    vnew_grid[ny][nx] = col
    return vnew_grid


for step in range(1, 1_001):
    print(f"Step {step}")
    old_grid = copy.deepcopy(grid)
    grid = move_sea_cucumbers(grid)
    if grid == old_grid:
        print(f"After {step} the grid didn't change")
        break
    print_grid(grid)

# print(move_sea_cucumbers([[">", ".", ">", "."], [">", ".", ">", "."]]))
# print(move_sea_cucumbers([[">", ".", ".", "."], [">", ".", ".", "."]]))
# print(move_sea_cucumbers([[">", ".", "v", "."], [">", "v", ".", "."]]))
# print(move_sea_cucumbers([[".", ".", "v", "."], [".", "v", ".", "."]]))
