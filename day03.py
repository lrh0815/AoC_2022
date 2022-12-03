from puzzle_solver.PuzzleSolver import PuzzleSolver


class Day03:
    def run(self):
        PuzzleSolver(3, self.solve_a, self.solve_b, True)\
            .with_expected_a(157)\
            .with_expected_b(70)\
            .test()\
            .solve()\
            .submit(do_submit=True)

    def solve_a(self, input: str):
        answer = 0
        for rucksack in input.splitlines():
            comp1 = list(rucksack[0:len(rucksack)//2])
            comp2 = list(rucksack[len(rucksack)//2:])
            common = list(set([value for value in comp1 if value in comp2]))[0]
            prio = self.__get_prio(common)
            answer += prio
        return answer

    def __get_prio(self, common):
        prio = ord(common)-ord('a')+1
        if prio < 1:
            prio += 58
        return prio

    def solve_b(self, input: str):
        answer = 0
        rucksacks = input.splitlines()
        groups = list(self.__get_groups(rucksacks))
        for group in groups:
            common = list(set([value for value in group[0]
                          if value in group[1] and value in group[2]]))[0]
            prio = self.__get_prio(common)
            answer += prio

        return answer

    def __get_groups(self, rucksacks):
        for i in range(0, len(rucksacks), 3):
            yield rucksacks[i:i+3]


if __name__ == "__main__":
    Day03().run()
