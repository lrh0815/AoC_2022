from aocd.models import Puzzle


def read_elves(puzzle: Puzzle):
    i = 0
    elves = []
    elves.append(0)
    for cal in puzzle.input_data.splitlines():
        if cal == "":
            i += 1
            elves.append(0)
        else:
            x = int(cal)
            elves[i] += x

    return elves

def solve_a(elves: list):
    sortedElves = elves.copy()
    sortedElves.sort(reverse=True)

    answer = sortedElves[0]

    print(answer)
    return answer


def solve_b(elves: list):
    sortedElves = elves.copy()
    sortedElves.sort(reverse=True)

    print(sortedElves[:3])

    answer = sum(sortedElves[:3])
    print(answer)

    return answer


if __name__ == "__main__":
    submitAnswers = False

    puzzle = Puzzle(year=2022, day=1)

    elves = read_elves(puzzle)

    answer_a = solve_a(elves)
    answer_b = solve_b(elves)

    print()
    if submitAnswers:
        print("Submitting answers...")
        puzzle.answer_a = answer_a
        puzzle.answer_b = answer_b
    else:
        print("Answers not submitted:")
        print(answer_a)
        print(answer_b)

