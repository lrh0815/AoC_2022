import sys
sys.path.append('c:\\code\AoC_2022')
from puzzle_solver.PuzzleSolver import PuzzleSolver


class Day:
    def run(self):
        PuzzleSolver(2021, 1, self.solve_a, self.solve_b)\
            .with_expected_a(7)\
            .with_expected_b(5)\
            .test()\
            .solve()\
            .submit(do_submit=True)

    def solve_a(self, input: list[str]):
        depths = list(map(int, input))
        return self.__find_increases(depths)

    def __find_increases(self, depths):
        answer = 0
        for i in range(1, len(depths)):
            if depths[i] > depths[i-1]:
                answer += 1
        return answer

    def solve_b(self, input: list[str]):
        depths = list(map(int, input))
        groups = []
        for i in range(2, len(depths)):
            groups.append(depths[i] + depths[i-1] + depths[i-2])

        return self.__find_increases(groups)


if __name__ == "__main__":
    Day().run()
