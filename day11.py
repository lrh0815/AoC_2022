from aoc_helper.AoCHelper import PuzzleSolver, AoCHelper
from math import trunc


def chunk_input(input, size):
    for i in range(0, len(input), size):
        yield input[i:i+size]


class Monkey(object):
    def __init__(self, items: list[int], operation: list[str], test_value: int, true_target: int, false_target: int):
        self.items = items
        self.operation = operation
        self.test_value = test_value
        self.true_target = true_target
        self.false_target = false_target
        self.num_inspections = 0

    def __str__(self):
        return f"{self.items}, {self.operation}, {self.test_value}, {self.true_target}, {self.false_target}, {self.num_inspections}"

    def receive(self, item):
        self.items.append(item)

    def inspect_and_throw(self, targets: list["Monkey"], worry_divider: int, common_factor: int):
        for item in self.items:
            inspected_item = self.__inspect(item, worry_divider, common_factor)
            self.__throw(inspected_item, targets)
        self.items.clear()

    def __inspect(self, item: int, worry_divider: int, common_factor: int):
        self.num_inspections += 1
        if self.operation[2] == "old":
            x = item
        else:
            x = int(self.operation[2])

        if self.operation[1] == "+":
            item = item + x
        else:
            item = item * x

        item = trunc(item / worry_divider)
        item = item - (trunc(item / common_factor) * common_factor)
        return item

    def __throw(self, item: int, targets: list["Monkey"]):
        if item % self.test_value == 0:
            targets[self.true_target].receive(item)
        else:
            targets[self.false_target].receive(item)


class DaySolver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 11, 10605, 2713310158, True)

    def solve_a(self, input: list[str]):
        return self.__solve(input, 20, 3)

    def solve_b(self, input: list[str]):
        return self.__solve(input, 10000, 1)

    def __solve(self, input, rounds: int, worry_divider: int):
        self.monkeys: list[Monkey] = []
        for monkey_input in chunk_input(input, 7):
            self.__parse_monkey(monkey_input)

        common_factor = 1
        for monkey in self.monkeys:
            common_factor *= monkey.test_value

        for _ in range(rounds):
            for monkey in self.monkeys:
                monkey.inspect_and_throw(self.monkeys, worry_divider, common_factor)
        inspections = [x.num_inspections for x in self.monkeys]
        inspections.sort()

        answer = inspections[-1] * inspections[-2]
        return answer

    def __parse_monkey(self, input: list[str]):
        items = [int(x) for x in input[1].split(":")[1].split(", ")]
        operation = input[2].split("=")[1].split()
        test_value = int(input[3].split()[3])
        true_target = int(input[4].split()[5])
        false_target = int(input[5].split()[5])
        monkey = Monkey(items, operation, test_value, true_target, false_target)
        self.monkeys.append(monkey)


example_input1 = """"""

example_input2 = """"""

if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test().solve().submit()
