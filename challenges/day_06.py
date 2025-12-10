
import numpy as np
from aocd import get_data


def part_one(data):
    digits = {}
    operation = {}
    sum_of_homework = 0

    for line in data.split("\n"):
        for i, digit in enumerate(line.split()):
            print(i, digit)
            if '*' in line:
                operation[i] = digit
            else:
                if i not in digits:
                    digits[i] = []
                digits[i].append(int(digit))

    print(digits)

    for i, values in digits.items():
        if operation.get(i) == '*':
            sum_of_homework += np.prod(values)
        else:
            sum_of_homework += sum(values)

    return sum_of_homework


def part_two(data):
    sum_of_homework = 0

    all_chars = list(zip(*[line for line in data.split("\n")]))
    columns = [[char for char in col if char not in ['*', '+']] for col in all_chars]
    operations = [[char for char in col if char in ['*', '+']] for col in all_chars if any(char in ['*', '+'] for char in col)]

    current_problem = 0

    op = operations.pop(0)[0]

    while True:
        for col in columns:
            if all(c == ' ' for c in col):
                if operations:
                    op = operations.pop(0)[0]
                print(op)
                print(current_problem)
                sum_of_homework += current_problem
                current_problem = 0
                continue
            num = int(''.join(col).strip())
            print(num)
            if op == '*':
                if current_problem == 0:
                    current_problem = 1
                current_problem *= num
            else:
                current_problem += num

            col.clear()
            col.extend([' ' for _ in range(len(col))])
        
        sum_of_homework += current_problem
        break
        
    return sum_of_homework


def main():
    data = get_data(day=6, year=2025)
    answer1 = part_one(data)
    print(f"The sum of the homework problems is: {answer1}")
    answer2 = part_two(data)
    print(f"The sum of cephalopod homework problems is: {answer2}")


if __name__ == "__main__":
    main()
