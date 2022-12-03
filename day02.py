from puzzle_solver.PuzzleSolver import PuzzleSolver


class Day:
    def run(self):
        PuzzleSolver(2, self.solve_a, self.solve_b)\
            .with_expected_a(15)\
            .with_expected_b(12)\
            .test()\
            .solve()\
            .submit()

    def solve_a(self, input):
        return self.__solve(input, self.__get_own_shape_a)

    def solve_b(self, input):
        return self.__solve(input, self.__get_own_shape_b)

    __shape_scores = {
        "A": 1,
        "B": 2,
        "C": 3
    }

    __result_scores = {
        "A A": 3,
        "B B": 3,
        "C C": 3,
        "A B": 6,
        "B C": 6,
        "C A": 6,
        "A C": 0,
        "B A": 0,
        "C B": 0,
    }

    def __get_own_shape_a(self, round):
        own_shape_dict = {
            "X": "A",
            "Y": "B",
            "Z": "C"
        }
        return own_shape_dict[round[1]]

    def __get_own_shape_b(self, round):
        own_shape_dict = {
            "X": {"A": "C", "B": "A", "C": "B"},
            "Y": {"A": "A", "B": "B", "C": "C"},
            "Z": {"A": "B", "B": "C", "C": "A"}
        }
        return own_shape_dict[round[1]][round[0]]

    def __calculate_score(self, round, own_shape_getter):
        opponent_shape = round[0]
        own_shape = own_shape_getter(round)

        shape_score = self.__shape_scores[own_shape]
        result_score = self.__result_scores[f"{opponent_shape} {own_shape}"]

        return shape_score + result_score

    def __solve(self, input, own_shape_getter):
        total_score = 0
        for line in input.splitlines():
            score = self.__calculate_score(line.split(), own_shape_getter)
            total_score += score

        return total_score


if __name__ == "__main__":
    Day().run()
