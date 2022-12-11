from aoc_helper.AoCHelper import PuzzleSolver, AoCHelper
from math import trunc


def chunk_input(input, size):
    for i in range(0, len(input), size):
        yield input[i:i+size]


class Monkey(object):
    def __init__(self, monkey_spec: list[str]):
        self.items = [int(x) for x in monkey_spec[1].split(":")[1].split(", ")]
        self.operation = Monkey.__convert_operation(monkey_spec[2].split("=")[1].split())
        self.test_value = int(monkey_spec[3].split()[3])
        self.true_target = int(monkey_spec[4].split()[5])
        self.false_target = int(monkey_spec[5].split()[5])
        self.num_inspections = 0

    def __convert_operation(op: list[str]):
        if op[1] == "+":
            operation = Monkey.__add
        else:
            operation = Monkey.__multiply

        if op[2] != "old":
            second_operand_value = int(op[2])
            return lambda x: operation(x, second_operand_value)
        else:
            return lambda x: operation(x, x)

    def __add(x, y):
        return x + y

    def __multiply(x, y):
        return x * y

    def inspect_and_throw(self, targets: list["Monkey"], worry_divider: int, common_factor: int):
        for item in self.items:
            inspected_item = self.__inspect(item, worry_divider, common_factor)
            self.__throw(inspected_item, targets)
        self.items.clear()

    def __inspect(self, item: int, worry_divider: int, common_factor: int):
        self.num_inspections += 1
        item = self.operation(item)
        item = trunc(item / worry_divider)
        item = item - (trunc(item / common_factor) * common_factor)
        return item

    def __throw(self, item: int, targets: list["Monkey"]):
        if item % self.test_value == 0:
            targets[self.true_target].__catch(item)
        else:
            targets[self.false_target].__catch(item)

    def __catch(self, item):
        self.items.append(item)


class DaySolver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 11, 10605, 2713310158, True)

    def solve_a(self, input: list[str]):
        return self.__solve(input, 20, 3)

    def solve_b(self, input: list[str]):
        return self.__solve(input, 10000, 1)

    def __solve(self, input, rounds: int, worry_divider: int):
        monkeys = [Monkey(monkey_spec) for monkey_spec in chunk_input(input, 7)]

        common_factor = 1
        for monkey in monkeys:
            common_factor *= monkey.test_value

        for _ in range(rounds):
            for monkey in monkeys:
                monkey.inspect_and_throw(monkeys, worry_divider, common_factor)

        inspections = [x.num_inspections for x in monkeys]
        inspections.sort()

        answer = inspections[-1] * inspections[-2]
        return answer


example_input1 = """"""

example_input2 = """"""

if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test().solve().submit()
