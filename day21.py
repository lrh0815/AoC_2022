from aoc_helper.AoCHelper import *


class Monkey(object):
    def __init__(self, monkeys: dict[str, "Monkey"], number: int = None, operation: tuple[str, str, str] = None):
        self.__monkeys = monkeys
        self.__number = number
        self.__operation = operation

    @property
    def listening_to(self) -> tuple["Monkey", "Monkey"]:
        if self.__operation:
            return (self.__monkeys[self.__operation[0]], self.__monkeys[self.__operation[2]])

    @property
    def number(self):
        if self.__number == None:
            return self.__evaluate()
        return self.__number

    def __evaluate(self):
        return int(eval(f"{self.listening_to[0].number} {self.__operation[1]} {self.listening_to[1].number}"))


class DaySolver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 21, 152, 301, True)

    def solve_a(self, input: list[str]):
        monkeys = self.__read_monkeys(input)
        return monkeys["root"].number

    def __read_monkeys(self, input):
        monkeys: dict[str, Monkey] = {}
        for line in input:
            match line.split():
                case m, m1, op, m2:
                    monkeys[m[:-1]] = Monkey(monkeys, operation=(m1, op, m2))
                case m, n:
                    monkeys[m[:-1]] = Monkey(monkeys, number=int(n))
        return monkeys

    def solve_b(self, input: list[str]):
        monkeys = self.__read_monkeys(input)
        root_monkey = monkeys["root"]

        monkey_1_number = root_monkey.listening_to[1].number
        monkey_2_number = self.__monkey_2_number_with_my_number(monkeys, root_monkey, (my_number := 0))
        was_greater = (monkey_2_number > monkey_1_number)

        increment = 10000000000
        while True:
            print(f"[{increment:20,}] {my_number:20,}: {monkey_2_number:20,} == {monkey_1_number:20,}                    ", end="\r")

            if monkey_2_number == monkey_1_number:
                break

            if monkey_2_number > monkey_1_number:
                if was_greater:
                    my_number += increment
                else:
                    increment = int(increment / -10)
                    my_number += increment
                    was_greater = True
            else:
                if not was_greater:
                    my_number += increment
                else:
                    increment = int(increment / -10)
                    my_number += increment
                    was_greater = False

            monkey_2_number = self.__monkey_2_number_with_my_number(monkeys, root_monkey, my_number)

        print()
        return my_number

    def __monkey_2_number_with_my_number(self, monkeys, root_monkey: Monkey, my_number):
        monkeys["humn"] = Monkey(monkeys, number=my_number)
        return root_monkey.listening_to[0].number


if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test()\
        .solve().submit()
