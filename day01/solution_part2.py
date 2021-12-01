#!/usr/bin/env python3

import itertools
import sys

input_file = sys.argv[1]

input_data = open(input_file)
input_dataset = list(map(int, input_data.readlines()))
window_size = 3
input_dataset = [sum(input_dataset[i:i+window_size]) for i in range(len(input_dataset)-window_size+1)]

last_depth = None
increases = 0
for depth in input_dataset:
    if last_depth is not None:
        if depth > last_depth:
            print(f"{depth} (increased)")
            increases += 1
        elif depth < last_depth:
            print(f"{depth} (decreased)")
        else:
            print(f"{depth} (no change)")
    else:
        print(f"{depth} (N/A - no previous sum)")

    last_depth = depth

print(f"We found {increases} increases in {input_file}")