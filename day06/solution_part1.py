#!/usr/bin/env python3

import collections
import sys
import typing

input_file = sys.argv[1]
input_data = open(input_file)
input_dataset = list(map(int, input_data.read().split(",")))

how_many_days = int(sys.argv[2])


def increase_day_with_spawn(
    day,
) -> typing.Union[int, typing.Union[None, int]]:
    new_day = day - 1
    spawned = None

    if new_day < 0:
        new_day = 6
        spawned = 8

    return new_day, spawned


def spawn_new_lanternfish(current_school=[], days=0) -> typing.List:
    if days == 0:
        return current_school
    # print(current_school)
    new_school = []
    new_fishschool = []
    for fish in current_school:
        # print(fish)
        older_fish, new_fish = increase_day_with_spawn(fish)
        new_school.append(older_fish)
        new_fishschool.append(new_fish)
    new_fishschool = list(filter(lambda x: x is not None, new_fishschool))
    return spawn_new_lanternfish(new_school + new_fishschool, days - 1)


# --- Day 6: Lanternfish ---

print("Initial state: " + ",".join(map(str, input_dataset)))
for day in range(1, how_many_days + 1):
    print(
        f"After {day:-2} days: "
        + ",".join(map(str, spawn_new_lanternfish(input_dataset, days=day)))
    )

print(
    len(spawn_new_lanternfish(input_dataset, days=how_many_days)),
    f"fish after {how_many_days} days",
)
