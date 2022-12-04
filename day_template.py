from aoc_helper.AoCHelper import PuzzleSolver, AoCHelper


class Day(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 0, None, None, True)

    def solve_a(self, input: list[str]):
        print(input)
        return 1

    def solve_b(self, input: list[str]):
        return None


if __name__ == "__main__":
    AoCHelper(Day()).test().solve().submit()
