from aocd.models import Puzzle
from aocd import numbers

puzzle = Puzzle(year=2022, day=1)

i = 0
elves = []
elves.append(0)
for cal in puzzle.input_data.splitlines():
    if cal == "":
        i += 1
        elves.append(0)
    else:
        x = int(cal)
        elves[i] += x

elves.sort(reverse = True)

answer_a = elves[0]
print(answer_a)
puzzle.answer_a = answer_a

print(elves[:3])

answer_b = sum(elves[:3])
print(answer_b)

puzzle.answer_b = answer_b

