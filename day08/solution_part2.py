#!/usr/bin/env python3

import collections
import sys
from typing import OrderedDict

input_file = sys.argv[1]
input_data = open(input_file)
input_dataset = input_data.readlines()

new_wire_schema_translation = {
    "a": "d",
    "b": "e",
    "c": "a",
    "d": "f",
    "e": "g",
    "f": "b",
    "g": "c",
}


def pattern_from_wire_scheme(old_key, wireschema):
    # print(old_key, old_key.translate(wireschema), wireschema)
    trantab = str.maketrans("".join(wireschema.keys()), "".join(wireschema.values()))
    return old_key.translate(trantab)


def build_patterns(signal_patterns):
    """
    Make a mapping based on the patterns for
    signal 1: cf
    signal 4: bcdf
    signal 7: acf
    signal 8: abcdefg
    """
    patterns = signal_patterns.split(" ")
    # signal 8 is the one with the longest string
    signal_8 = ""
    for pattern in patterns:
        if len(pattern) == 7:
            signal_8 = pattern

    # print("--------")
    # find sortest and longest pattern
    probe_signals = {}
    # lenght=2 = 1
    # lenght=3 = 7
    # lenght=4 = 4
    # lenght=7 = 8
    for signal in signal_patterns.split(" "):
        if len(signal) in [2, 3, 4, 7]:
            # print(len(signal), signal)
            probe_signals[len(signal)] = signal
    # print(probe_signals)
    # print("--------")

    signal_freq = collections.Counter(signal_patterns)

    signal_N = set(probe_signals[3]) ^ set(probe_signals[2])
    signal_E = sorted(list(set(probe_signals[2])))

    fe1 = list(signal_E)[0]
    fe2 = list(signal_E)[1]
    if signal_freq[fe1] == 9 and signal_freq[fe2] == 8:
        signal_NE = fe2
        signal_SE = fe1
    else:
        signal_NE = fe1
        signal_SE = fe2

    NW_M = set(probe_signals[4]) - set(probe_signals[3])
    f1 = list(NW_M)[0]
    f2 = list(NW_M)[1]
    if signal_freq[f1] == 6 and signal_freq[f2] == 7:
        signal_NW = f1
        signal_M = f2
    else:
        signal_NW = f2
        signal_M = f1

    SW_S = set(probe_signals[7]) - set(probe_signals[4]) - set(probe_signals[3])
    f3 = list(SW_S)[0]
    f4 = list(SW_S)[1]
    if signal_freq[f3] == 4 and signal_freq[f4] == 7:
        signal_SW = f3
        signal_S = f4
    else:
        signal_SW = f4
        signal_S = f3

    wireschema = OrderedDict(
        {
            "a": list(signal_N)[0],  # N
            "b": signal_NW,  # NW
            "c": signal_NE,  # NE
            "d": signal_M,  # M
            "e": signal_SW,  # SW
            "f": signal_SE,  # SE
            "g": signal_S,  # S
        }
    )
    # print(wireschema)

    mapping = {
        "0": pattern_from_wire_scheme("abcefg", wireschema),
        "1": pattern_from_wire_scheme("cf", wireschema),
        "2": pattern_from_wire_scheme("acdeg", wireschema),
        "3": pattern_from_wire_scheme("acdfg", wireschema),
        "4": pattern_from_wire_scheme("bcdf", wireschema),
        "5": pattern_from_wire_scheme("abdfg", wireschema),
        "6": pattern_from_wire_scheme("abdefg", wireschema),
        "7": pattern_from_wire_scheme("acf", wireschema),
        "8": pattern_from_wire_scheme("abcdefg", wireschema),
        "9": pattern_from_wire_scheme("abcdfg", wireschema),
    }
    # print(mapping)
    return mapping


overall_res = []
for line in input_dataset:
    signal_patterns, four_digit_output_value = line.strip().split(" | ")
    signal_patterns_result = []
    line_result = []

    for ov in four_digit_output_value.split(" "):
        ov_value_digit = None
        uvalue = set(ov)
        patterns = build_patterns(signal_patterns).items()
        for k, v in patterns:
            # print(k, v)
            if uvalue == set(v):
                line_result.append(k)
                break
    line_sum = int("".join(map(str, line_result)))
    overall_res.append(line_sum)
    print(four_digit_output_value, line_sum)
print("Total sum:", sum(overall_res))
