from aoc_helper.AoCHelper import PuzzleSolver, AoCHelper


class Day(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 1, 24000, 45000, False)

    def solve_a(self, input):
        calories_per_elf = self.__read_calories_per_elf(input)
        answer = calories_per_elf[0]
        return answer

    def solve_b(self, input):
        calories_per_elf = self.__read_calories_per_elf(input)
        answer = sum(calories_per_elf[:3])
        return answer

    def __read_calories_per_elf(self, input):
        calories_per_elf = [0]
        for calories in input:
            if calories == "":
                calories_per_elf.append(0)
            else:
                calories_per_elf[-1] += int(calories)

        calories_per_elf.sort(reverse=True)

        return calories_per_elf


if __name__ == "__main__":
    AoCHelper(Day()).test().solve().submit()
