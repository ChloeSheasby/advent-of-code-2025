from math import prod

import networkx as nx
from aocd import get_data


def part_one(data, connections=1000):
    nodes = []

    for line in data.split("\n"):
        x, y, z = map(int, line.split(","))
        nodes.append((x, y, z))

    graph = nx.Graph()

    for i, (x1, y1, z1) in enumerate(nodes):
        for j in range(i + 1, len(nodes)):
            x2, y2, z2 = nodes[j]
            distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5
            graph.add_edge((x1, y1, z1), (x2, y2, z2), weight=distance)

    edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])[:connections]

    print(edges)

    circuits = []

    for edge in edges:
        start, end, data = edge
        starts_circuit = None
        ends_circuit = None
        for circuit in circuits:
            if start in circuit:
                starts_circuit = circuit
            if end in circuit:
                ends_circuit = circuit

        if starts_circuit and not ends_circuit:
            starts_circuit.append(end)
        elif not starts_circuit and ends_circuit:
            ends_circuit.append(start)
        elif starts_circuit and ends_circuit and starts_circuit != ends_circuit:
            starts_circuit.extend(ends_circuit)
            circuits.remove(ends_circuit)
        elif not starts_circuit and not ends_circuit:
            circuits.append([start, end])

    circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
        
    return prod(len(circuit) for circuit in circuits[:3])


def part_two(data):
    nodes = []

    for line in data.split("\n"):
        x, y, z = map(int, line.split(","))
        nodes.append((x, y, z))

    graph = nx.Graph()

    for i, (x1, y1, z1) in enumerate(nodes):
        for j in range(i + 1, len(nodes)):
            x2, y2, z2 = nodes[j]
            distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5
            graph.add_edge((x1, y1, z1), (x2, y2, z2), weight=distance)

    edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])

    circuits = []
    final_edge = edges[0]

    while (len(circuits) > 1 or len(circuits) == 0) and not all(node in sum(circuits, []) for node in nodes):
        for edge in edges:
            final_edge = edge
            start, end, data = edge
            starts_circuit = None
            ends_circuit = None
            for circuit in circuits:
                if start in circuit:
                    starts_circuit = circuit
                if end in circuit:
                    ends_circuit = circuit

            if starts_circuit and not ends_circuit:
                starts_circuit.append(end)
            elif not starts_circuit and ends_circuit:
                ends_circuit.append(start)
            elif starts_circuit and ends_circuit and starts_circuit != ends_circuit:
                starts_circuit.extend(ends_circuit)
                circuits.remove(ends_circuit)
            elif not starts_circuit and not ends_circuit:
                circuits.append([start, end])

            if len(circuits) == 1 and all(node in sum(circuits, []) for node in nodes):
                break

    return final_edge[0][0] * final_edge[1][0]


def main():
    data = get_data(day=8, year=2025)
    answer1 = part_one(data, 1000)
    print(f"The product of the sizes of the 3 largest circuits is: {answer1}")
    answer2 = part_two(data)
    print(f"The product of the x-values of the final connection is: {answer2}")


if __name__ == "__main__":
    main()
