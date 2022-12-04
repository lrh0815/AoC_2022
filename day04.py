from aoc_helper.AoCHelper import PuzzleSolver, AoCHelper


class Day(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 4, 2, 4, False)

    def solve_a(self, input: list[str]):
        answer = 0
        for assignments in self.__get_all_assignments(input):
            intersection = self.__get_intersection(assignments)
            if intersection == assignments[0] or intersection == assignments[1]:
                answer += 1
        return answer

    def __get_intersection(self, assignments: list[int]):
        intersection = [val for val in assignments[0] if val in assignments[1]]
        return intersection

    def __get_all_assignments(self, input: list[str]):
        return list(map(self.__get_assignments, input))

    def __get_assignments(self, line: str):
        return list(map(self.__get_assignment, line.split(',')))

    def __get_assignment(self, assignment_string: str):
        assignment_range = list(
            map(lambda x: int(x), assignment_string.split('-')))
        return [x for x in range(assignment_range[0], assignment_range[1] + 1)]

    def solve_b(self, input: list[str]):
        answer = 0
        for assignments in self.__get_all_assignments(input):
            intersection = self.__get_intersection(assignments)
            if intersection != []:
                answer += 1
        return answer


if __name__ == "__main__":
    AoCHelper(Day()).test().solve().submit()
