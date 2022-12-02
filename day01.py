from puzzle_solver.PuzzleSolver import PuzzleSolver

def read_calories_per_elf(input):
    calories_per_elf = [0]
    for calories in input.splitlines():
        if calories == "":
            calories_per_elf.append(0)
        else:
            calories_per_elf[-1] += int(calories)

    calories_per_elf.sort(reverse=True)

    return calories_per_elf

def solve_a(input):
    calories_per_elf = read_calories_per_elf(input)
    answer = calories_per_elf[0]
    return answer


def solve_b(input):
    calories_per_elf = read_calories_per_elf(input)
    answer = sum(calories_per_elf[:3])
    return answer


if __name__ == "__main__":
    PuzzleSolver(1, 24000, solve_a, 45000, solve_b).solve()
