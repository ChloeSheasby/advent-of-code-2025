
from itertools import combinations

import cvxpy as cp
import numpy as np
from aocd import get_data


def part_one(data):
    button_presses = 0
    for line in data.split("\n"):
        expected_indicator_lights = []
        buttons = []
        for block in line.split(" "):
            if block.startswith("[") and block.endswith("]"):
                indicator_light_str = block[1:-1]
                expected_indicator_lights = [
                    1 if char == "#" else 0 for char in indicator_light_str
                ]
            elif block.startswith("(") and block.endswith(")"):
                button_str = block[1:-1]
                button_positions = list(map(int, button_str.split(",")))
                buttons.append(button_positions)
        
        min_presses = float('inf')
        best_combination = None

        for r in range(len(buttons) + 1):
            for combo in combinations(range(len(buttons)), r):
                test_lights = [0] * len(expected_indicator_lights)
                for button_idx in combo:
                    for light_idx in buttons[button_idx]:
                        test_lights[light_idx] ^= 1 
                
                if test_lights == expected_indicator_lights:
                    if len(combo) < min_presses:
                        min_presses = len(combo)
                        best_combination = combo

        if best_combination is not None:
            button_presses += min_presses
        else:
            print("No solution found")

    return button_presses


def part_two(data):
    print(cp.installed_solvers())
    button_presses = 0
    for line in data.split("\n"):
        expected_voltages = []
        buttons = []
        for block in line.split(" "):
            if block.startswith("(") and block.endswith(")"):
                button_str = block[1:-1]
                button_positions = list(map(int, button_str.split(",")))
                buttons.append(button_positions)
            elif block.startswith("{") and block.endswith("}"):
                voltage_str = block[1:-1]
                expected_voltages = list(map(int, voltage_str.split(",")))

        button_effect_matrix = []
        for button in buttons:
            effect_row = [0] * len(expected_voltages)
            for light_idx in button:
                effect_row[light_idx] = 1
            button_effect_matrix.append(effect_row)

        A = np.array(button_effect_matrix).T
        b = np.array(expected_voltages)

        print("A:", A)
        print("b:", b)

        min_presses = minimal_presses(
            A,
            b
        )

        button_presses += sum(min_presses)

    return button_presses
        

# Integer Linear Program - fascinating to learn about
def minimal_presses(button_effects, expected_vector):    
    print(f"✓ Shapes validated: matrix {button_effects.shape} × target {expected_vector.shape}")
    
    n = button_effects.shape[1]
    x = cp.Variable(n, integer=True)
    constraints = [button_effects @ x == expected_vector, x >= 0]
    problem = cp.Problem(cp.Minimize(cp.sum(x)), constraints)
    
    problem.solve(solver=cp.GUROBI)
    solver_used = "GUROBI"
    
    if problem.status == "optimal":
        print(f"Solver used: {solver_used}")
        return x.value.round().astype(int)
    raise ValueError("No feasible solution exists for given expected passes.")


def main():
    data = get_data(day=10, year=2025)
    answer1 = part_one(data)
    print(f"The smallest required button presses is: {answer1}")
    answer2 = part_two(data)
    print(f"The smallest required button presses for joltage is: {answer2}")


if __name__ == "__main__":
    main()
