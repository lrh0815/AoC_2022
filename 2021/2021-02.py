import sys
sys.path.append('c:\\code\AoC_2022')
from puzzle_solver.PuzzleSolver import PuzzleSolver


class Day:
    def run(self):
        PuzzleSolver(2021, 2, self.solve_a, self.solve_b)\
            .with_expected_a(150)\
            .with_expected_b(900)\
            .test()\
            .solve()\
            .submit(do_submit=True)

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
    Day().run()
