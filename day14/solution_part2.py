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
polymer: collections.Counter = collections.Counter(
    [polymer_template[i : i + 2] for i in range(len(polymer_template) - 1)]
)

pair_insertion_rules = dict(line.strip().split(" -> ") for line in input_dataset[2:])


def make_polymer(polymer: collections.Counter):
    # track new polymer pairs
    new_polymer = collections.Counter()
    insert_count = collections.Counter()

    for pair, n in polymer.items():
        insert = pair_insertion_rules.get(pair)
        new_polymer[pair[0] + insert] += n
        new_polymer[insert + pair[1]] += n
        insert_count[insert] += n
    return new_polymer, insert_count


element_counts = collections.Counter(polymer_template)
for step in range(1, 41):
    polymer, insert_count = make_polymer(polymer)
    # update how many new inserts there are
    element_counts.update(insert_count)
    # print(f"After step {step}: {polymer}")

# print(element_counts)
most_common_elements = element_counts.most_common()
most_common_element = most_common_elements[0]
least_common_element = most_common_elements[::-1][0]
print(f"Most common element: {most_common_element[0]} with {most_common_element[1]}")
print(f"Least common element: {least_common_element[0]} with {least_common_element[1]}")
print(
    f"{most_common_element[1]} - {least_common_element[1]} = {most_common_element[1]-least_common_element[1]}"
)
