#!/usr/bin/env python3

import collections
import sys

input_file = sys.argv[1]
input_data = open(input_file)
input_dataset = [line.strip().split("-") for line in input_data.readlines()]


class Node:
    def __init__(self, name, graph):
        self.name = name
        self.graph = graph
        self.neighbours = set()

    def add_neighbour(self, target):
        # print("in", self.neighbours)
        self.neighbours.add(target)
        # print("out", self.neighbours)

    @property
    def is_small_cave(self):
        return len(self.name) == 1 and self.name == self.name.lower()

    @property
    def is_large_cave(self):
        return len(self.name) == 1 and self.name == self.name.upper()

    def __repr__(self):
        return self.name


class Graph:
    def __init__(self):
        self.nodes = {}
        self.visited = set()
        self.paths = []

    def __create_node(self, name):
        self.nodes[name] = Node(name, graph=self)
        return self.nodes[name]

    def get_or_create_node(self, name):
        node = self.nodes.get(name)
        if not node:
            node = self.__create_node(name)
        return node

    def add_vertex(self, a, b):
        node_a = self.get_or_create_node(a)
        node_b = self.get_or_create_node(b)
        node_a.add_neighbour(node_b)
        node_b.add_neighbour(node_a)

    def build_path_for(self, current_path, visited_small_caves=[]):
        last_cave = current_path[-1]  # index to last cave
        # print(current_path)
        # print(visited_small_caves)
        if last_cave.name == "end":
            self.paths.append(current_path)
            return

        if last_cave.is_small_cave:
            visit_counter = collections.Counter(visited_small_caves)
            visited_earlier = last_cave in visited_small_caves
            visited_twice = visit_counter.get(last_cave.name) is not None

            if visited_earlier and not visited_twice:
                visited_small_caves.append(last_cave)

        # print(f"{last_cave} neighbours", self.nodes[last_cave.name].neighbours)
        for neighbour in self.nodes[last_cave.name].neighbours:
            if neighbour.name == "start":
                continue
            # print(f"n({last_cave}):", neighbour)
            if neighbour in visited_small_caves:
                continue
            self.build_path_for(current_path + [neighbour], visited_small_caves.copy())

    def show_paths(self, start_node="start"):
        self.build_path_for(
            [self.nodes.get(start_node)],
        )
        self.paths = sorted(
            list(set([tuple(path) for path in self.paths])),
            key=lambda x: len(x),
        )
        return self.paths


graph = Graph()

print(input_dataset)

for vertex in input_dataset:
    # print(vertex)
    graph.add_vertex(*vertex)

print(graph.show_paths())
for path in graph.paths:
    print(path)

print(len(graph.paths))
