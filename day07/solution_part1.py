#!/usr/bin/env python3

# import pprint
import sys

input_file = sys.argv[1]
input_data = open(input_file)
input_dataset = list(map(int, input_data.read().split(",")))

cost_table = {}

for final_position in range(min(input_dataset), max(input_dataset)):
    total_cost = 0
    for crab in input_dataset:
        cost = abs(crab - final_position)
        total_cost += cost
    cost_table[final_position] = total_cost


# pprint.pprint(cost_table)

lowest_fuel = min(cost_table.values())
lowest_fuel_pos = list(filter(lambda x: x[1] == lowest_fuel, cost_table.items()))[0]

print(f"Lowest fuel cost: {lowest_fuel} at position {lowest_fuel_pos[0]}")
