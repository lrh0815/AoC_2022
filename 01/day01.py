from aocd.models import Puzzle


def read_calories_per_elf(puzzle: Puzzle):
    calories_per_elf = [0]
    for calories in puzzle.input_data.splitlines():
        if calories == "":
            calories_per_elf.append(0)
        else:
            calories_per_elf[-1] += int(calories)

    calories_per_elf.sort(reverse=True)

    return calories_per_elf

def solve_a(calories_per_elf: list):
    answer = calories_per_elf[0]

    print(answer)
    return answer


def solve_b(calories_per_elf: list):

    print(calories_per_elf[:3])

    answer = sum(calories_per_elf[:3])
    print(answer)

    return answer


if __name__ == "__main__":
    submit_answers = False

    puzzle = Puzzle(year=2022, day=1)

    calories_per_elf = read_calories_per_elf(puzzle)

    answer_a = solve_a(calories_per_elf)
    answer_b = solve_b(calories_per_elf)

    print()
    if submit_answers:
        print("Submitting answers...")
        puzzle.answer_a = answer_a
        puzzle.answer_b = answer_b
    else:
        print("Answers not submitted:")
        print(answer_a)
        print(answer_b)

