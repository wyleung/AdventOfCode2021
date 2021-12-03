#!/usr/bin/env python3

import collections
import sys

input_file = sys.argv[1]
input_data = open(input_file)
input_dataset = input_data.readlines()

gamma_rate = ""
epsilon_rate = ""
power_consumption = 0
life_support_rating = 0
oxygen_generator_rating = 0
CO2_scrubber_rating = 0


def transpose_report(lines):
    first_line = lines[0]
    transposed = [[c] for c in first_line.strip()]
    for line in lines[1:]:
        for i, char in enumerate(line.strip()):
            transposed[i].append(char)
    return transposed


def filter_bits(transposed, position, filter_func, fallback_num):
    count = collections.Counter(transposed[position])
    if len(set(count.values())) == 1:
        return fallback_num
    return filter_func(count, key=count.get)


def find_oxygen_generator_rating(dataset, position=0):
    if len(dataset) == 1:
        return dataset[0].strip()
    transposed = transpose_report(dataset)

    common_bit = filter_bits(transposed, position, max, "1")

    return find_oxygen_generator_rating(
        list(filter(lambda x: x[position] == common_bit, dataset)), position + 1
    )


def find_CO2_scrubber_rating(dataset, position=0):
    if len(dataset) == 1:
        return dataset[0].strip()
    transposed = transpose_report(dataset)

    common_bit = filter_bits(transposed, position, min, "0")

    return find_CO2_scrubber_rating(
        list(filter(lambda x: x[position] == common_bit, dataset)), position + 1
    )


oxygen_generator_rating = find_oxygen_generator_rating(input_dataset)
CO2_scrubber_rating = find_CO2_scrubber_rating(input_dataset)
life_support_rating = int(oxygen_generator_rating, 2) * int(CO2_scrubber_rating, 2)
print(
    f"oxygen_generator_rating 0b{oxygen_generator_rating} = {int(oxygen_generator_rating, 2)}"
)
print(f"CO2_scrubber_rating 0b{CO2_scrubber_rating} = {int(CO2_scrubber_rating, 2)}")
print(f"life_support_rating = {life_support_rating}")
