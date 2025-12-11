

from functools import lru_cache

import networkx as nx
from aocd import get_data


def part_one(data):
    graph = nx.DiGraph()

    for line in data.split("\n"):
        parent, children_str = line.split(": ")
        children = children_str.split(" ")
        for child in children:
            graph.add_edge(parent, child)

    return len(list(nx.all_simple_paths(graph, source="you", target="out")))


def part_two(data):
    graph = nx.DiGraph()

    for line in data.split("\n"):
        parent, children_str = line.split(": ")
        children = children_str.split(" ")
        for child in children:
            graph.add_edge(parent, child)

    if not nx.is_directed_acyclic_graph(graph):
        print("Warning: Graph has cycles, using slower path enumeration")
        all_paths = []
        for path in nx.all_simple_paths(graph, source="svr", target="out"):
            if "fft" in path and "dac" in path:
                all_paths.append(path)
        return len(all_paths)
        
    @lru_cache(maxsize=None)
    def count_paths(current, target, remaining_waypoints):
        next_waypoints = remaining_waypoints
        if current in remaining_waypoints:
            next_waypoints = tuple(w for w in remaining_waypoints if w != current)
        
        if current == target:
            return 1 if not next_waypoints else 0

        total = 0
        for neighbor in graph[current]:
            total += count_paths(neighbor, target, next_waypoints)

        return total

    return count_paths("svr", "out", ("fft", "dac"))


def main():
    data = get_data(day=11, year=2025)
    answer1 = part_one(data)
    print(f"The paths from you to out is: {answer1}")
    answer2 = part_two(data)
    print(f"The paths from svr to out with passing through "
          f"dac and fft is: {answer2}")


if __name__ == "__main__":
    main()
