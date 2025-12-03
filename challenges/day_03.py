from aocd import get_data


def part_one(data):
    joltage = 0

    for battery_bank in data.split("\n"):
        batteries = [int(d) for d in battery_bank]
        largest_battery = max(batteries[:len(batteries)-1])
        second_largest_battery = max(batteries[batteries.index(largest_battery)+1:])
        joltage += int(f"{largest_battery}{second_largest_battery}")

    return joltage


def part_two(data):
    joltage = 0

    for battery_bank in data.split("\n"):
        batteries = [int(d) for d in battery_bank]

        current_joltage = ""

        while len(current_joltage) < 12:
            testing_range = len(batteries) - (12 - len(current_joltage) % 12)

            next_largest = max(batteries[:testing_range + 1])
            current_joltage += str(next_largest)
            batteries = batteries[batteries.index(next_largest)+1:]

        print(current_joltage)
        joltage += int(current_joltage)

    return joltage


def main():
    data = get_data(day=3, year=2025)
    answer1 = part_one(data)
    print(f"The sum of the 2 digit joltage is: {answer1}")
    answer2 = part_two(data)
    print(f"The sum of the 12 digit joltage is: {answer2}")


if __name__ == "__main__":
    main()
