

from functools import lru_cache

import networkx as nx
from aocd import get_data
from shapely import Polygon, box
from shapely.affinity import translate
from shapely.ops import unary_union


def part_one(data):
    present_shapes = []
    cells = []
    row_index = 0
    regions = []

    for line in data.split("\n"):
        if "#" in line or "." in line:
            # Process a row of the shape
            for col_index, char in enumerate(line):
                if char == "#":
                    # Create a 2x2 box for each cell
                    cell = box(col_index*2, row_index*2, col_index*2+2, row_index*2+2)
                    cells.append(cell)
            row_index += 1
        elif line == "" and len(cells) > 0:
            # End of a shape definition
            shape = unary_union(cells)
            present_shapes.append(shape)
            cells = []
            row_index = 0
        elif line and ":" in line and "#" not in line:
            # Either a shape number (e.g., "0:") or a region definition
            if "x" in line:
                # Region definition like "4x4: 0 0 0 0 2 0"
                width, length = line.split(":")[0].split("x")
                quantities = line.split(":")[1].strip().split(" ")
                regions.append({
                    "width": int(width),
                    "length": int(length),
                    "quantities": list(map(int, quantities))
                })
            # else: it's a shape number marker like "0:", just skip it



    working_regions = 0

    for region in regions:
        # Region dimensions are in grid cells, each cell is 2x2 in our coordinate system
        # So the actual area should be (width * length) * 4 (since each cell is 2x2 = 4 square units)
        region_area = region["width"] * region["length"] * 4
        
        # Check if total area of shapes fits in region
        total_shape_area = 0
        for quantity_idx, quantity in enumerate(region["quantities"]):
            if quantity_idx < len(present_shapes):
                total_shape_area += present_shapes[quantity_idx].area * quantity
        
        # Check if shapes fit by area with reasonable packing efficiency
        # Irregular shapes typically need some slack space to pack efficiently
        if total_shape_area > region_area:
            continue
        elif total_shape_area / region_area > 0.85:
            # More than 85% utilization - shapes likely won't pack
            continue
        else:
            working_regions += 1

    return working_regions


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
    data = get_data(day=12, year=2025)
    answer1 = part_one(data)
    print(f"The number of regions that can fit the presents is: {answer1}")
    # answer2 = part_two(data)
    # print(f"The paths from svr to out with passing through "
    #       f"dac and fft is: {answer2}")


if __name__ == "__main__":
    main()
