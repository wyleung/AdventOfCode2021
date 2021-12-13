#!/usr/bin/env python3

import collections
import sys

input_file = sys.argv[1]
input_data = open(input_file)
input_dataset = input_data.readlines()


def visualize_grid(grid):
    # print the grid
    max_x, max_y = max([x[0] for x in grid]), max([y[1] for y in grid])
    print()
    print(f"Grid with size {max_x}x{max_y} and {len(grid)} dots")
    print()
    # print(grid)
    for y in range(0, max_y + 1):
        line = []
        for x in range(0, max_x + 1):
            if [x, y] in grid:
                line.append("#")
            else:
                line.append(".")
        print("".join(line))
    print()


grid = []
instructions = []

for line in input_dataset:
    if line.startswith("fold along"):
        instructions.append(line.strip())
    elif line.strip() != "":
        grid.append(list(map(int, line.strip().split(","))))

# print(sorted(grid), instructions)
# print(grid, len(grid))

fold_coordinate_mapping = {
    "y": 1,
    "x": 0,
}

for instruction in instructions:
    _, instruction = instruction.split("fold along ")
    fold_type, position = instruction.split("=")
    position = int(position)
    # print(fold_type, position)

    coord = fold_coordinate_mapping.get(fold_type)

    new_grid = []
    for point in sorted(grid):
        if point[coord] < position:
            # print(f"not transforming {point}")
            new_grid.append(point)
        else:
            distance_to_fold = abs(position - point[coord])
            new_point = point.copy()
            new_point[coord] = point[coord] - (2 * distance_to_fold)
            new_grid.append(new_point)
    grid = new_grid.copy()
    # visualize_grid(grid)


visualize_grid(grid)
