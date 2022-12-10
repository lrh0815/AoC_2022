from aoc_helper.AoCHelper import PuzzleSolver, AoCHelper
from advent_of_code_ocr import convert_6


class DaySolver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 10, None, None, True)

    def solve_a(self, input: list[str]):
        self.sum_signal_strength = 0
        self.execute_program(input, self.add_signal_strength)
        return self.sum_signal_strength

    def execute_program(self, input, operation_per_cycle):
        self.reg_x = 1
        self.cycle = 0
        for line in input:
            match line.split():
                case ["noop"]:
                    self.cycle += 1
                    operation_per_cycle()
                case ["addx", value]:
                    self.cycle += 1
                    operation_per_cycle()
                    self.cycle += 1
                    operation_per_cycle()
                    self.reg_x += int(value)

    def add_signal_strength(self):
        if self.cycle in [20, 60, 100, 140, 180, 220]:
            self.sum_signal_strength += self.cycle * self.reg_x

    def solve_b(self, input: list[str]):
        self.output = [""]
        self.max_line_length = 40
        self.execute_program(input, self.draw_pixel)
        self.print_output()
        return self.try_decode_output()

    def draw_pixel(self):
        if len(self.output[-1]) == self.max_line_length:
            self.output.append("")
        self.output[-1] += self.get_pixel()

    def get_pixel(self):
        current_horizontal_position = self.cycle % self.max_line_length
        delta = current_horizontal_position - self.reg_x
        if delta <= 2 and delta >= 0:
            return "#"
        return "."

    def try_decode_output(self):
        try:
            return convert_6("\n".join(self.output))
        except:
            return "dummy"

    def print_output(self):
        print()
        for line in self.output:
            print(line)


example_input1 = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

example_input2 = """"""

if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test_with('a', example_input1.splitlines(), 13140)\
        .test_with('b', example_input1.splitlines(), "dummy")\
        .solve().submit()
