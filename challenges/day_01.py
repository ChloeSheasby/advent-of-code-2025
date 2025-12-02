from aocd import get_data


def part_one(data):
    zero_counter = 0
    starting_position = 50

    for line in data.split("\n"):
        direction, steps = line[0], int(line[1:])
        print(direction, steps)
        if direction == "R":
            starting_position += steps
        elif direction == "L":
            starting_position -= steps

        starting_position = starting_position % 100

        if starting_position == 0:
            zero_counter += 1

    return zero_counter


def part_two(data):
    pass_zero_counter = 0
    starting_position = 50

    for line in data.split("\n"):
        direction, steps = line[0], int(line[1:])
        if direction == "R":
            for _ in range(steps):
                starting_position += 1
                starting_position = starting_position % 100
                if starting_position == 0:
                    pass_zero_counter += 1
        elif direction == "L":
            for _ in range(steps):
                starting_position -= 1
                starting_position = starting_position % 100
                if starting_position == 0:
                    pass_zero_counter += 1

    return pass_zero_counter


def main():
    data = get_data(day=1, year=2025)
    answer1 = part_one(data)
    print(f"The password is: {answer1}")
    answer2 = part_two(data)
    print(f"The password for part two is: {answer2}")


if __name__ == "__main__":
    main()
