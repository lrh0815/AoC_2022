from puzzle_solver.PuzzleSolver import PuzzleSolver


class Day:
    def run(self):
        PuzzleSolver(2022, 0, self.solve_a, self.solve_b)\
            .with_expected_a(None)\
            .with_expected_b(None)\
            .test()\
            .solve()\
            .submit(do_submit=True)

    def solve_a(self, input: list[str]):
        answer = None
        return answer

    def solve_b(self, input: list[str]):
        answer = None
        return answer


if __name__ == "__main__":
    Day().run()
