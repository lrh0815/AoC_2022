from puzzle_solver.PuzzleSolver import PuzzleSolver
from itertools import islice

class Day03:
    def __init__(self):
        self.puzzle_solver = PuzzleSolver(3, 157, self.solve_a, 70, self.solve_b)

    def test(self):
        self.puzzle_solver.test()
        return self
    
    def solve(self):
        self.puzzle_solver.solve()#('a', do_submit = False).solve('b', do_submit= False)
        return self

    def solve_a(self, input : str):
        answer = 0
        for rucksack in input.splitlines():
            comp1 = list(rucksack[0:len(rucksack)//2])
            comp2 = list(rucksack[len(rucksack)//2:])
            common = list(set([value for value in comp1 if value in comp2]))[0]
            prio = self._get_prio(common)
            answer += prio
        return answer

    def _get_prio(self, common):
        prio = ord(common)-ord('a')+1
        if prio < 1:
            prio += 58
        return prio

    def solve_b(self, input : str):
        answer = 0
        rucksacks = input.splitlines()
        groups = list(self._get_groups(rucksacks))
        for group in groups:
            common = list(set([value for value in group[0] if value in group[1] and value in group[2]]))[0]
            prio = self._get_prio(common)
            answer += prio

        return answer

    def _get_groups(self, rucksacks):
        for i in range(0, len(rucksacks), 3):
            yield rucksacks[i:i+3]


if __name__ == "__main__":
    Day03().solve()

    