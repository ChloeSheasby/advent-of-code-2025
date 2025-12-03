from aocd import get_data


def part_one(data):
    invalid_ids_sum = 0

    for line in data.split(","):
        starting_number, ending_number = map(int, line.split("-"))

        for number in range(starting_number, ending_number + 1):
            if len(str(number)) % 2 != 0:
                continue

            digits = [int(d) for d in str(number)]
            mid = len(digits) // 2
            first_half = digits[:mid]
            second_half = digits[mid:]

            if first_half == second_half:
                invalid_ids_sum += number

    return invalid_ids_sum


def part_two(data):
    invalid_ids_sum = 0

    for line in data.split(","):
        starting_number, ending_number = map(int, line.split("-"))

        for number in range(starting_number, ending_number + 1):
            s = str(number)
            if s in (s + s)[1:-1]:
                print(s)
                invalid_ids_sum += number

    return invalid_ids_sum


def main():
    data = get_data(day=2, year=2025)
    answer1 = part_one(data)
    print(f"The sum of invalid ids is: {answer1}")
    answer2 = part_two(data)
    print(f"The number of valid ids is: {answer2}")


if __name__ == "__main__":
    main()
