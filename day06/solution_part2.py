#!/usr/bin/env python3

import collections
import sys
import typing

input_file = sys.argv[1]
input_data = open(input_file)
input_dataset = "".join(input_data.read().split(","))

current_school = collections.Counter(input_dataset)


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


def spawn_new_lanternfish(current_school={}, days=0) -> typing.Dict:
    if days == 0:
        return current_school
    # print(current_school)
    new_school = {}
    for days_old, n_fish in sorted(current_school.items(), key=lambda item: item[0]):
        # print("old", days_old, n_fish)
        older_fish, new_fish = increase_day_with_spawn(int(days_old))
        # print("new", older_fish, new_fish)
        new_school[older_fish] = new_school.get(older_fish, 0) + n_fish
        if new_fish:
            new_school[8] = n_fish
    # print(new_school)
    return spawn_new_lanternfish(new_school, days - 1)


# --- Day 6: Lanternfish ---

# print("Initial state: " + ",".join(map(str, input_dataset)))
# for day in range(1, how_many_days + 1):
#     print(
#         f"After {day:-2} days: "
#         + ",".join(map(str, spawn_new_lanternfish(current_school, days=day).values()))
#     )

print(
    sum(spawn_new_lanternfish(current_school, days=how_many_days).values()),
    spawn_new_lanternfish(current_school, days=how_many_days),
    f"fish after {how_many_days} days",
)
