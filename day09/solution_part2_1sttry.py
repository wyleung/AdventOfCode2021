#!/usr/bin/env python3

import collections
import typing
import sys

input_file = sys.argv[1]
input_data = open(input_file)
input_dataset = input_data.readlines()

dataset = [line.strip() for line in input_dataset]

low_map = []
low_values = []


for line_no, line in enumerate(dataset):
    lowest_points_on_line = []
    for position, value in enumerate(line):
        # is this position the lowest point in N/E/S/W ?
        value = int(value)
        # print(position, value)
        if line_no > 0:
            N = int(dataset[line_no - 1][position])
        else:
            N = 9

        if position < len(line) - 1:
            E = int(dataset[line_no][position + 1])
        else:
            E = 9

        if line_no < len(dataset) - 1:
            S = int(dataset[line_no + 1][position])
        else:
            S = 9

        if position > 0:
            W = int(dataset[line_no][position - 1])
        else:
            W = 9

        is_lowest_point = all([value < N, value < E, value < S, value < W])
        lowest_points_on_line.append(is_lowest_point)
        if is_lowest_point:
            low_values.append(value)
    # print()
    low_map.append(lowest_points_on_line)

# print(low_map)
# print(sum(map(lambda x: x + 1, low_values)))
# print()
# Find the basins
basin_map = []
basin_values = []

for line_no, line in enumerate(dataset):
    basin_on_line = []
    lowest_points_on_line = low_map[line_no]

    for position, value in enumerate(line):
        is_lowest_point = lowest_points_on_line[position]
        value = int(value)
        if value == 9:
            # we cannot add this 9 position to the basin
            # proceed with next position
            continue

        # was there a previous line with basin points?
        if line_no > 0:
            # is N point part of basin?
            basin_N = position in basin_map[line_no - 1]
            basin_on_line.append(position)
            continue

        # scan current line for adjacent basin points
        if position > 0:
            W = int(dataset[line_no][position - 1])
        else:
            W = 9

        if position < len(line) - 1:
            E = int(dataset[line_no][position + 1])
        else:
            E = 9

        if any([E < 9, W < 9]):
            basin_on_line.append(position)

    basin_on_line = list(set(basin_on_line))
    basin_map.append(basin_on_line)

# for line in basin_map:
#     print(line)


def find_basin_neighbor(pos_y, pos_x, max_x, max_y, basin_map) -> typing.List:
    if pos_x > max_x:
        return []
    if pos_y > max_y:
        return []

    if pos_x < 0:
        return []
    if pos_y < 0:
        return []

    E = pos_x + 1 in basin_map[pos_y]
    W = pos_x - 1 in basin_map[pos_y]
    N = pos_x in basin_map[pos_y - 1]
    S = pos_x in basin_map[pos_y + 1]

    res = []
    if E:
        res.append((pos_y, pos_x + 1))
        res.extend(find_basin_neighbor(pos_y, pos_x + 1, max_x, max_y, basin_map))
    if W:
        res.append((pos_y, pos_x - 1))
        res.extend(find_basin_neighbor(pos_y, pos_x - 1, max_x, max_y, basin_map))
    if N:
        res.append((pos_y - 1, pos_x))
        res.extend(find_basin_neighbor(pos_y - 1, pos_x, max_x, max_y, basin_map))
    if S:
        res.append((pos_y + 1, pos_x))
        res.extend(find_basin_neighbor(pos_y + 1, pos_x, max_x, max_y, basin_map))
    return res


def find_cluster(pos_y, pos_x, basin_map) -> typing.List:
    # grow the basin from the initial pos_y, pos_x
    basin_locations = []

    # grow left
    for x in range(pos_x, -1, -1):
        is_basin_point = x in basin_map[pos_y]
        if is_basin_point:
            basin_locations.append((pos_y, x))
        else:
            break
    # grow right
    for x in range(pos_x, len(basin_map[pos_y]) + 1):
        is_basin_point = x in basin_map[pos_y]
        if is_basin_point:
            basin_locations.append((pos_y, x))
        else:
            break

    return basin_locations


clusters = {}
# find clusters of basin points belonging to the lowest point from part 1
for line_no, line in enumerate(low_map):
    all_cluster_start_points = [i for i, x in enumerate(line) if x is True]

    for cluster_start in all_cluster_start_points:
        clusters[f"{line_no}_{cluster_start}"] = find_cluster(
            line_no, cluster_start, basin_map
        )

# find clusters of basin points belonging to the lowest point from part 1
for line_no, line in enumerate(low_map):
    # extend clusters with basin points found on this line
    # print(basin_map[line_no])
    for point in basin_map[line_no]:
        # for each found cluster find whether this is adjacent to an existing cluster point
        N = (line_no - 1, point)
        for cluster_name in clusters.keys():
            if N in clusters[cluster_name]:
                clusters[cluster_name].append((line_no, point))
        # then find eventual neightbours we neglected earlier
        S = (line_no + 1, point)
        for cluster_name in clusters.keys():
            if S in clusters[cluster_name]:
                clusters[cluster_name].append((line_no, point))

        # then find eventual neightbours we neglected earlier
        W = (line_no, point - 1)
        for cluster_name in clusters.keys():
            if W in clusters[cluster_name]:
                clusters[cluster_name].append((line_no, point))

        # then find eventual neightbours we neglected earlier
        E = (line_no, point + 1)
        for cluster_name in clusters.keys():
            if E in clusters[cluster_name]:
                clusters[cluster_name].append((line_no, point))

# run (phase 2) second time to complete map
for line_no, line in enumerate(low_map):
    # extend clusters with basin points found on this line
    # print(basin_map[line_no])
    for point in basin_map[line_no]:
        # for each found cluster find whether this is adjacent to an existing cluster point
        N = (line_no - 1, point)
        for cluster_name in clusters.keys():
            if N in clusters[cluster_name]:
                clusters[cluster_name].append((line_no, point))
        # then find eventual neightbours we neglected earlier
        S = (line_no + 1, point)
        for cluster_name in clusters.keys():
            if S in clusters[cluster_name]:
                clusters[cluster_name].append((line_no, point))

        # then find eventual neightbours we neglected earlier
        W = (line_no, point - 1)
        for cluster_name in clusters.keys():
            if W in clusters[cluster_name]:
                clusters[cluster_name].append((line_no, point))

        # then find eventual neightbours we neglected earlier
        E = (line_no, point + 1)
        for cluster_name in clusters.keys():
            if E in clusters[cluster_name]:
                clusters[cluster_name].append((line_no, point))

# run (phase 3) to complete map
for line_no, line in enumerate(low_map):
    # extend clusters with basin points found on this line
    # print(basin_map[line_no])
    for point in basin_map[line_no]:
        # for each found cluster find whether this is adjacent to an existing cluster point
        N = (line_no - 1, point)
        for cluster_name in clusters.keys():
            if N in clusters[cluster_name]:
                clusters[cluster_name].append((line_no, point))
        # then find eventual neightbours we neglected earlier
        S = (line_no + 1, point)
        for cluster_name in clusters.keys():
            if S in clusters[cluster_name]:
                clusters[cluster_name].append((line_no, point))

        # then find eventual neightbours we neglected earlier
        W = (line_no, point - 1)
        for cluster_name in clusters.keys():
            if W in clusters[cluster_name]:
                clusters[cluster_name].append((line_no, point))

        # then find eventual neightbours we neglected earlier
        E = (line_no, point + 1)
        for cluster_name in clusters.keys():
            if E in clusters[cluster_name]:
                clusters[cluster_name].append((line_no, point))

# run (phase 4) to complete map
for line_no, line in enumerate(low_map):
    # extend clusters with basin points found on this line
    # print(basin_map[line_no])
    for point in basin_map[line_no]:
        # for each found cluster find whether this is adjacent to an existing cluster point
        N = (line_no - 1, point)
        for cluster_name in clusters.keys():
            if N in clusters[cluster_name]:
                clusters[cluster_name].append((line_no, point))
        # then find eventual neightbours we neglected earlier
        S = (line_no + 1, point)
        for cluster_name in clusters.keys():
            if S in clusters[cluster_name]:
                clusters[cluster_name].append((line_no, point))

        # then find eventual neightbours we neglected earlier
        W = (line_no, point - 1)
        for cluster_name in clusters.keys():
            if W in clusters[cluster_name]:
                clusters[cluster_name].append((line_no, point))

        # then find eventual neightbours we neglected earlier
        E = (line_no, point + 1)
        for cluster_name in clusters.keys():
            if E in clusters[cluster_name]:
                clusters[cluster_name].append((line_no, point))


# draw full basin map
for line_no, line in enumerate(dataset):
    draw_line = []
    for position, value in enumerate(line):
        if position in basin_map[line_no]:
            draw_line.append(value)
        else:
            draw_line.append(".")
    print("".join(draw_line))


# draw cluster basin map
cluster_sizes = []
for cluster_name, values in clusters.items():
    print(cluster_name)
    cluster_values = []
    for line_no, line in enumerate(dataset):
        draw_line = []
        for position, value in enumerate(line):
            if (line_no, position) in values:
                draw_line.append(value)
                cluster_values.append(value)
            else:
                draw_line.append(".")
        print("".join(draw_line))
    print()
    print("Cluster size", len(cluster_values))
    cluster_sizes.append(len(cluster_values))
    print()

size_of_top_3 = sorted(cluster_sizes)[::-1][:3]
print(size_of_top_3, "=", size_of_top_3[0] * size_of_top_3[1] * size_of_top_3[2])
