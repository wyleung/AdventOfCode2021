#!/usr/bin/env python3

import collections
import sys

input_file = sys.argv[1]
input_data = open(input_file)
input_dataset = [line.strip() for line in input_data.readlines()]

pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

score_illegal_char = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def validate_syntax(line):
    stack = []
    char_start = pairs.keys()
    char_close = pairs.values()

    for idx, char in enumerate(line):
        # print(idx, char)
        error = False
        if len(stack) == 0:
            stack.append(char)
            continue
        last_char = stack[-1]
        expect = pairs.get(last_char)
        found = char

        current_is_start_char = char in char_start
        current_is_close_char = char in char_close
        if current_is_start_char:
            # print(f"adding {char} to {stack}")
            stack.append(char)
            continue
        elif current_is_close_char:
            if found == expect:
                # print(f"removing match for {char} = {last_char} from {stack}")
                _ = stack.pop()
                continue
            else:
                # char is not good
                error = True

        if error:
            warning = f"{line} - Expected {expect} but found {found} instead"
            return warning, found
    return None, 0


score = 0
for line in input_dataset:
    warning, illegal_char = validate_syntax(line)
    score += score_illegal_char.get(illegal_char, 0)

print(f"Sum of illegal char score: {score}")
