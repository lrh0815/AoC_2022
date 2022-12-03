import sys
sys.path.append('c:\\code\AoC_2022')
from puzzle_solver.PuzzleSolver import PuzzleSolver


class Day:
    def run(self):
        PuzzleSolver(2021, 3, self.solve_a, self.solve_b, True)\
            .with_expected_a(198)\
            .with_expected_b(None)\
            .test()\
            .solve()\
            .submit(do_submit=True)

    def solve_a(self, input: str):
        print(input)
        return None

    def solve_b(self, input: str):
        return None


if __name__ == "__main__":
    Day().run()
