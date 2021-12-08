#!/usr/bin/env python3

import collections
import sys

input_file = sys.argv[1]
input_data = open(input_file)
input_dataset = input_data.readlines()

patterns = {
    "0": ["abcefg", "d"],
    "1": ["cf", "abdeg"],
    "2": ["acdeg", "bf"],
    "3": ["acdfg", "be"],
    "4": ["bcdf", "aeg"],
    "5": ["abdfg", "ce"],
    "6": ["abdefg", "c"],
    "7": ["acf", "bdeg"],
    "8": ["abcdefg", ""],
    "9": ["abcdfg", "e"],
}

overall_res = []
for line in input_dataset:
    signal_patterns, four_digit_output_value = line.strip().split(" | ")
    line_result = []
    # print(four_digit_output_value)
    for ov in four_digit_output_value.split(" "):
        ov_value_digit = None
        uvalue = set(ov)
        # print(uvalue, len(uvalue))
        if len(uvalue) in [2, 4, 3, 7]:
            for k, v in patterns.items():
                if uvalue <= set(v[0]) and uvalue.isdisjoint(v[1]):
                    # print(ov, k, set(v[0]), uvalue)
                    if k in ["1", "4", "7", "8"] and not ov_value_digit:
                        line_result.append(k)
                        overall_res.append(k)
                        ov_value_digit = k

    print(line_result)

print(overall_res, len(overall_res))
