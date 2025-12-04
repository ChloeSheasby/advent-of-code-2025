from aocd import get_data


def split_data_into_grid(data):
    grid = []
    for line in data.split("\n"):
        grid.append([d for d in line])
    return grid


def part_one(data):
    grid = split_data_into_grid(data)

    accessible_paper_coords = check_accessible_paper(grid)
    return len(accessible_paper_coords)


def check_accessible_paper(grid):
    accessible_paper_coords = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            adjacent_paper = 0
            if cell == "@":
                print(f"Checking cell at {i},{j}")
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                            if grid[ni][nj] == "@":
                                adjacent_paper += 1

                if adjacent_paper < 4:
                    accessible_paper_coords.append((i, j))
                            
    return accessible_paper_coords


def part_two(data):
    grid = split_data_into_grid(data)
    accessible_paper = 0

    while True:
        new_accessible_paper_coords = check_accessible_paper(grid)
        print(f"New accessible paper this round: {new_accessible_paper_coords}")
        if not new_accessible_paper_coords:
            break
        accessible_paper += len(new_accessible_paper_coords)
        for i, j in new_accessible_paper_coords:
            grid[i][j] = "."
    return accessible_paper


def main():
    data = get_data(day=4, year=2025)
    answer1 = part_one(data)
    print(f"The number of accessible rolls of paper is: {answer1}")
    answer2 = part_two(data)
    print(f"The sum of accessible rolls of paper is: {answer2}")


if __name__ == "__main__":
    main()
