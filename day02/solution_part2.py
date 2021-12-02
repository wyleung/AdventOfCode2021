#!/usr/bin/env python3

import operator
import sys

input_file = sys.argv[1]
input_data = open(input_file)
input_dataset = input_data.readlines()

x = 0
y = 0
aim = 0

motions = {
    "up": operator.sub,
    "down": operator.add,
    "forward": operator.add,
}

for instruction in input_dataset:
    # tokenize
    tokens = instruction.strip().split(" ")
    motion, change = tokens[0], int(tokens[1])

    if motion in ["up", "down"]:
        aim = motions[motion](aim, change)
    elif motion in ["forward"]:
        x = motions[motion](x, change)
        y = y + aim * change

print(f"horizontal position of {x} and a depth of {y} = {x*y}")
