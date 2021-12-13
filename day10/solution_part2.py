#!/usr/bin/env python3

import math
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

score_completing_char = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def score_completion_string(completion_string) -> int:
    score = 0
    for char in completion_string:
        score = score * 5
        score += score_completing_char.get(char, 0)
    return score


def validate_syntax(line):
    stack = []
    missing = []
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
            return warning, found, missing

    # fill out the missing chars when the stack is not empty
    if len(stack):
        for char in stack[::-1]:
            missing.append(pairs.get(char))

    return None, 0, "".join(missing)


score = 0
completion_score = []
for line in input_dataset:
    warning, illegal_char, missing = validate_syntax(line)
    score += score_illegal_char.get(illegal_char, 0)
    if not warning and len(missing):
        points = score_completion_string(missing)
        completion_score.append(points)
        print(f"{line} - Complete by adding {missing}. - {points}")

middlescore = sorted(completion_score)[math.floor(len(completion_score) / 2)]

print(f"Sum of illegal char score: {score}")
print(f"Middle score of completion: {middlescore}")
