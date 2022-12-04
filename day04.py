from puzzle_solver.PuzzleSolver import PuzzleSolver


class Day:
    def run(self):
        PuzzleSolver(2022, 4, self.solve_a, self.solve_b)\
            .with_expected_a(2)\
            .with_expected_b(4)\
            .test()\
            .solve()\
            .submit(do_submit=False)

    def solve_a(self, input: list[str]):
        answer = 0
        for line in input:
            pair = line.split(',')
            assignment1 = self.__get_assignment(pair[0])
            assignment2 = self.__get_assignment(pair[1])
            intersection = [val for val in assignment1 if val in assignment2]
            if intersection == assignment1 or intersection == assignment2:
                answer += 1
        return answer

    def __get_assignment(self, asstr : str):
        assignment = list(map(lambda x: int(x), asstr.split('-')))
        return [x for x in range(assignment[0], assignment[1] + 1)]

    def solve_b(self, input: list[str]):
        answer = 0
        for line in input:
            pair = line.split(',')
            assignment1 = self.__get_assignment(pair[0])
            assignment2 = self.__get_assignment(pair[1])
            intersection = [val for val in assignment1 if val in assignment2]
            if intersection != []:
                answer += 1
        return answer


if __name__ == "__main__":
    Day().run()
