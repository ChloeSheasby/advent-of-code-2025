import numpy as np
from aocd import get_data


def part_one(data):
    fresh_ingredient_array = []
    fresh_ingredients = 0

    for line in data.split("\n"):
        if "-" in line:
            start, end = line.split("-")
            fresh_ingredient_array.append([start, end])
        elif line == "":
            continue
        else:
            for val in fresh_ingredient_array:
                if int(line) >= int(val[0]) and int(line) <= int(val[1]):
                    fresh_ingredients += 1
                    break
        
    return fresh_ingredients


def merge_intervals(intervals):
    sorted_intervals = intervals[np.argsort(intervals[:, 0])]
    
    merged = [sorted_intervals[0]]
    
    for current in sorted_intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1] + 1:
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            merged.append(current)
    
    return np.array(merged)


def part_two(data):
    fresh_ingredient_array = []
    fresh_ingredients_possible = 0

    for line in data.split("\n"):
        if "-" in line:
            start, end = line.split("-")
            fresh_ingredient_array.append([start, end])
        elif line == "":
            break

    b = np.array(fresh_ingredient_array, dtype=int)

    merged = merge_intervals(b)
    print(merged)

    fresh_ingredients_possible = np.sum(merged[:, 1] - merged[:, 0] + 1)

    return fresh_ingredients_possible


def main():
    data = get_data(day=5, year=2025)
    answer1 = part_one(data)
    print(f"The number of fresh available ingredients is: {answer1}")
    answer2 = part_two(data)
    print(f"The number of possible fresh ingredients is: {answer2}")


if __name__ == "__main__":
    main()
