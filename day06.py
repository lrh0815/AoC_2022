from aoc_helper.AoCHelper import PuzzleSolver, AoCHelper


class Day06Solver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 6, 7, 19, False)

    def solve_a(self, input: list[str]):
        datastream = input[0]
        return self.__find_unique_char_sequence(4, datastream)

    def __find_unique_char_sequence(self, number_of_unique_characters, datastream):
        for i in range(number_of_unique_characters, len(datastream)):
            unique_characters = set(datastream[i-number_of_unique_characters:i])
            if len(unique_characters) == number_of_unique_characters:
                break
        return i

    def solve_b(self, input: list[str]):
        line = input[0]
        return self.__find_unique_char_sequence(14, line)


if __name__ == "__main__":
    AoCHelper(Day06Solver()).test_with('a', ["bvwbjplbgvbhsrlpgdmjqwftvncz"], 5)\
        .test_with('b', ["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"], 26)\
        .test().solve().submit()
