#!/usr/bin/env python3

import collections
import sys

input_file = sys.argv[1]
input_data = open(input_file)
input_dataset = input_data.readlines()

grid = []
instructions = []

for line in input_dataset:
    if line.startswith("fold along"):
        instructions.append(line.strip())
    elif line.strip() != "":
        grid.append(list(map(int, line.strip().split(","))))

# print(sorted(grid), instructions)
# print(grid, len(grid))

for instruction in instructions[:1]:
    _, instruction = instruction.split("fold along ")
    fold_type, position = instruction.split("=")
    position = int(position)
    # print(fold_type, position)

    if fold_type == "y":
        # the fold is horizontal so "mirror" from point=y
        new_grid = []
        for point in sorted(grid):
            if point[1] < position:
                # print(f"not transforming {point}")
                new_grid.append(point)
            else:
                distance_to_fold = abs(position - point[1])
                new_point = point.copy()
                new_point[1] = point[1] - (2 * distance_to_fold)
                # print(f"folding point {point} to {new_point}")
                new_grid.append(new_point)
        grid = new_grid.copy()
    if fold_type == "x":
        # the fold is vertical so "mirror" from point=x
        new_grid = []
        for point in sorted(grid):
            if point[0] < position:
                # print(f"not transforming {point}")
                new_grid.append(point)
            else:
                distance_to_fold = abs(position - point[0])
                new_point = point.copy()
                new_point[0] = point[0] - (2 * distance_to_fold)
                # print(f"folding point {point} to {new_point}")
                new_grid.append(new_point)
        grid = new_grid.copy()

dedup_grid = sorted(list(set(tuple(g) for g in grid)))
print(f"We count {len(dedup_grid)} dots")
