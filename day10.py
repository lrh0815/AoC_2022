from aoc_helper.AoCHelper import PuzzleSolver, AoCHelper


class Day10Solver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 10, None, None, True)

    def solve_a(self, input: list[str]):
        return None

    def solve_b(self, input: list[str]):
        return None


example_input1 = """"""

example_input2 = """"""

if __name__ == "__main__":
    AoCHelper(Day10Solver())\
        .test_with('a', example_input1.splitlines(), None)\
        .test_with('b', example_input2.splitlines(), None)\
        .solve().submit()
