
import networkx as nx
from aocd import get_data
from shapely.geometry import Point, Polygon


def part_one(data):
    nodes = []

    for line in data.split("\n"):
        x, y = map(int, line.split(","))
        nodes.append((x, y))

    graph = nx.Graph()

    for i, (x1, y1) in enumerate(nodes):
        for j in range(i + 1, len(nodes)):
            x2, y2 = nodes[j]
            real_point = (x1, y2)
            width = abs(real_point[0] - x2) + 1
            height = abs(real_point[1] - y1) + 1
            area = width * height
            graph.add_edge((x1, y1), (x2, y2), weight=area)
    
    edges = sorted(
        graph.edges(data=True),
        key=lambda x: x[2]['weight'],
        reverse=True
    )

    return edges[0][2]['weight']


def part_two(data):
    nodes = []

    for line in data.split("\n"):
        x, y = map(int, line.split(","))
        nodes.append((x, y))

    poly = Polygon(nodes)

    graph = nx.Graph()

    for i, (x1, y1) in enumerate(nodes):
        for j in range(i + 1, len(nodes)):
            x2, y2 = nodes[j]
            real_point = (x1, y2)
            width = abs(real_point[0] - x2) + 1
            height = abs(real_point[1] - y1) + 1
            area = width * height
            graph.add_edge((x1, y1), (x2, y2), weight=area)

    edges = sorted(
        graph.edges(data=True),
        key=lambda x: x[2]['weight'],
        reverse=True
    )

    for interior in poly.interiors:
        print("Interior:", interior)

    for edge in edges:
        x1, y1 = edge[0]
        x2, y2 = edge[1]
        third_point = Point(x1, y2)
        fourth_point = Point(x2, y1)

        interior_polygon = Polygon([
            (x1, y1),
            (x1, y2),
            (x2, y2),
            (x2, y1)
        ])

        if poly.covers(interior_polygon):
            return edge[2]['weight']
        

def main():
    data = get_data(day=9, year=2025)
    answer1 = part_one(data)
    print(f"The largest possible area is: {answer1}")
    answer2 = part_two(data)
    print(f"The largest possible area using only red and green tiles is: {answer2}")


if __name__ == "__main__":
    main()
