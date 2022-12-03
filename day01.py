from puzzle_solver.PuzzleSolver import PuzzleSolver


class Day:
    def run(self):
        PuzzleSolver(1, self.solve_a, self.solve_b)\
            .with_expected_a(24000)\
            .with_expected_b(45000)\
            .test()\
            .solve()\
            .submit()

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
        for calories in input.splitlines():
            if calories == "":
                calories_per_elf.append(0)
            else:
                calories_per_elf[-1] += int(calories)

        calories_per_elf.sort(reverse=True)

        return calories_per_elf


if __name__ == "__main__":
    Day().run()