from puzzle_solver.PuzzleSolver import PuzzleSolver


class Day:
    def run(self):
        PuzzleSolver(2022, 0, self.solve_a, self.solve_b, True)\
            .with_expected_a(None)\
            .with_expected_b(None)\
            .test()\
            .solve()\
            .submit(do_submit=True)

    def solve_a(self, input: str):
        return None

    def solve_b(self, input: str):
        return None


if __name__ == "__main__":
    Day().run()
