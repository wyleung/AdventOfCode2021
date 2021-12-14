#!/usr/bin/env python3

import collections
import itertools
import sys

input_file = sys.argv[1]
input_data = open(input_file)
input_dataset = input_data.readlines()


def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


polymer_template = input_dataset[0].strip()

pair_insertion_rules = dict(
    tuple(rule.split(" -> ")) for rule in [line.strip() for line in input_dataset[2:]]
)
print()
print(polymer_template, pair_insertion_rules)
print()
polymer = polymer_template


def make_polymer(polymer):
    pieces = []
    for piece in pairwise(polymer):
        p = "".join(piece)
        new_piece = p
        rule = pair_insertion_rules.get(p)
        if rule:
            # apply rule
            new_piece = p[0] + rule + p[1]
        pieces.append(new_piece)

    # print(pieces)
    new_polymer = pieces[0]
    for p in pieces[1:]:
        new_polymer += p[1:]

    # print(new_polymer)
    return new_polymer


for step in range(1, 11):
    polymer = make_polymer(polymer)
    print(f"After step {step}: {polymer}")
    # print(f"After step {step}: {len(polymer)}")
    count = collections.Counter(polymer)
    c = count.items()
    # print(c)
    print(f"The sum is: {max(count.values()) - min(count.values())}")
