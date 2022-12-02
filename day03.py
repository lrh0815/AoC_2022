from puzzle_solver.PuzzleSolver import PuzzleSolver


class Day03:
    def __init__(self):
        self.puzzle_solver = PuzzleSolver(3, None, self.solve_a, None, self.solve_b)

    def test(self):
        self.puzzle_solver.test()
        return self
    
    def solve(self):
        self.puzzle_solver.solve()
        return self

    def solve_a(self, input):
        return None

    def solve_b(self, input):
        return None


if __name__ == "__main__":
    Day03().solve()

    