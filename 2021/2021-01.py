import sys
sys.path.append('c:\\code\AoC_2022')
from aoc_helper.AoCHelper import PuzzleSolver, AoCHelper


class Day(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2021, 1, 7, 5, False)

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
    AoCHelper(Day()).test().solve().submit()
