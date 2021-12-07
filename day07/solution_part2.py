#!/usr/bin/env python3

import sys

input_file = sys.argv[1]
input_data = open(input_file)
input_dataset = list(map(int, input_data.read().split(",")))

cost_table = {}


def build_step_cost_table(end):
    step_cost_table = {}
    cost = 0
    for step in range(0, end + 1):
        cost += step
        step_cost_table[step] = cost
    return step_cost_table


step_cost_table = build_step_cost_table(max(input_dataset))


def movement_to_cost(steps) -> int:
    return step_cost_table.get(steps)


for final_position in range(min(input_dataset), max(input_dataset)):
    total_cost = 0
    for crab in input_dataset:
        cost = movement_to_cost(abs(crab - final_position))
        total_cost += cost
    cost_table[final_position] = total_cost

lowest_fuel = min(cost_table.values())
lowest_fuel_pos = list(filter(lambda x: x[1] == lowest_fuel, cost_table.items()))[0]

print(f"Lowest fuel cost: {lowest_fuel} at position {lowest_fuel_pos[0]}")
