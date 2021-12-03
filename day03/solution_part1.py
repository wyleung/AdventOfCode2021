#!/usr/bin/env python3

import collections
import sys

input_file = sys.argv[1]
input_data = open(input_file)
input_dataset = input_data.readlines()

gamma_rate = ""
epsilon_rate = ""
power_consumption = 0

first_line = input_dataset[0]
transposed = [[c] for c in first_line.strip()]
for line in input_dataset[1:]:
    for i, char in enumerate(line.strip()):
        transposed[i].append(char)

for position in transposed:
    count = collections.Counter(position)
    mostcommon_bit = max(count, key=count.get)
    leastcommon_bit = min(count, key=count.get)

    gamma_rate += mostcommon_bit
    epsilon_rate += leastcommon_bit

power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
print(f"Gamma rate 0b{gamma_rate} = {int(gamma_rate,2)}")
print(f"Epsilon rate 0b{epsilon_rate} = {int(epsilon_rate,2)}")
print(
    f"Power consumption {int(gamma_rate,2)} * {int(epsilon_rate,2)} = {power_consumption}"
)
