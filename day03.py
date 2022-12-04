from aoc_helper.AoCHelper import PuzzleSolver, AoCHelper


class Day(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 3, 157, 70, False)

    def solve_a(self, input: list[str]):
        answer = 0
        for rucksack in input:
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

    def solve_b(self, input: list[str]):
        answer = 0
        rucksacks = input
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
    AoCHelper(Day()).test().solve().submit()
