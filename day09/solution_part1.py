#!/usr/bin/env python3

import collections
import sys

input_file = sys.argv[1]
input_data = open(input_file)
input_dataset = input_data.readlines()

dataset = [line.strip() for line in input_dataset]

low_map = []
low_values = []


for line_no, line in enumerate(dataset):
    lowest_points_on_line = []
    for position, value in enumerate(line):
        # is this position the lowest point in N/E/S/W ?
        value = int(value)
        # print(position, value)
        if line_no > 0:
            N = int(dataset[line_no - 1][position])
        else:
            N = 9

        if position < len(line) - 1:
            E = int(dataset[line_no][position + 1])
        else:
            E = 9

        if line_no < len(dataset) - 1:
            S = int(dataset[line_no + 1][position])
        else:
            S = 9

        if position > 0:
            W = int(dataset[line_no][position - 1])
        else:
            W = 9

        is_lowest_point = all([value < N, value < E, value < S, value < W])
        lowest_points_on_line.append(is_lowest_point)
        if is_lowest_point:
            low_values.append(value)
    # print()
    low_map.append(lowest_points_on_line)

print(low_map)
print(sum(map(lambda x: x + 1, low_values)))
