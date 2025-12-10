from functools import lru_cache

import networkx as nx
from aocd import get_data


def part_one(data):
    beam_map = []
    splitter_locations = []

    for y, line in enumerate(data.split("\n")):
        line_map = []
        for x, char in enumerate(line):
            if char == "^":
                splitter_locations.append((x, y, False))
            line_map.append(char)
        beam_map.append(line_map)

    print(splitter_locations)

    for i, (x1, y1, has_split) in enumerate(splitter_locations):
        if i == 0:
            splitter_locations[i] = (x1, y1, True)

        if has_split or i == 0:
            left_split = None
            right_split = None
            for j in range(i + 1, len(splitter_locations)):
                x2, y2, has_split2 = splitter_locations[j]
                if x2 == x1 + 1 and right_split is None:
                    right_split = (x2, y2)
                    if not has_split2:
                        splitter_locations[j] = (x2, y2, True)
                elif x2 == x1 - 1 and left_split is None:
                    left_split = (x2, y2)
                    if not has_split2:
                        splitter_locations[j] = (x2, y2, True)

                if left_split and right_split:
                    break
            continue

    return sum(1 for x, y, has_split in splitter_locations if has_split)


def part_two(data):
    beam_map = []
    splitter_locations = []

    for y, line in enumerate(data.split("\n")):
        line_map = []
        for x, char in enumerate(line):
            if char == "^":
                splitter_locations.append((x, y))
            line_map.append(char)
        beam_map.append(line_map)

    graph = nx.DiGraph()

    for i, (x1, y1) in enumerate(splitter_locations):
        left_split = None
        right_split = None
        for j in range(i + 1, len(splitter_locations)):
            x2, y2 = splitter_locations[j]
            if x2 == x1 + 1 and right_split is None:
                print("Adding edge", (x1, y1), "->", (x2, y2))
                right_split = (x2, y2)
                graph.add_edge((x1, y1), (x2, y2))
            elif x2 == x1 - 1 and left_split is None:
                print("Adding edge", (x1, y1), "->", (x2, y2))
                left_split = (x2, y2)
                graph.add_edge((x1, y1), (x2, y2))

            if left_split and right_split:
                break

        if left_split is None:
            graph.add_edge((x1, y1), (x1-1, y1+1))  # self-loop to represent end of path
        if right_split is None:
            graph.add_edge((x1, y1), (x1+1, y1+1))  # self-loop to represent end of path

        continue

    count = 0

    @lru_cache(maxsize=None)
    def count_paths_from_node(node):
        if graph.out_degree(node) == 0:
            return 1
        
        total = 0
        for neighbor in graph.neighbors(node):
            total += count_paths_from_node(neighbor)
        
        return total
    
    count = count_paths_from_node(splitter_locations[0])

    return count


def main():
    data = get_data(day=7, year=2025)
    answer1 = part_one(data)
    print(f"The number of times the beam has split is: {answer1}")
    answer2 = part_two(data)
    print(f"The number of timelines is: {answer2}")


if __name__ == "__main__":
    main()
