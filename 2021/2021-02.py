import sys
sys.path.append('c:\\code\AoC_2022')
from aoc_helper.AoCHelper import PuzzleSolver, AoCHelper


class Day(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2021, 2, 150, 900, False)

    def solve_a(self, input: list[str]):
        course = self.__get_course(input)
        hor = 0
        dep = 0
        for item in course:
            op = self.__ops[item[0]]
            hor += op[0]*item[1]
            dep += op[1]*item[1]
        return hor*dep

    def __get_course(self, input):
        course = list(map(lambda y: (y[0], int(y[1])), list(
            map(lambda x: x.split(), input))))
        return course

    __ops = {
        'forward': (1, 0, 1),
        'down': (0, 1, 0),
        'up': (0, -1, 0)
    }

    def solve_b(self, input: list[str]):
        course = self.__get_course(input)
        aim = 0
        hor = 0
        dep = 0
        for item in course:
            op = self.__ops[item[0]]
            x = item[1]
            hor += op[0]*x
            aim += op[1]*x
            dep += op[2]*aim*x
        return hor*dep


if __name__ == "__main__":
    AoCHelper(Day()).test().solve().submit()
