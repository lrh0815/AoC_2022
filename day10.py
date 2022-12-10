from aoc_helper.AoCHelper import PuzzleSolver, AoCHelper


class DaySolver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 10, None, None, True)

    def solve_a(self, input: list[str]):
        self.execute_program(input, self.add_signal_strength)
        return self.sum_signal_strength

    def execute_program(self, input, operation_per_cycle):
        self.X = 1
        self.cycle = 0
        self.sum_signal_strength = 0
        for line in [x.split() for x in input]:
            if line[0] == "noop":
                self.cycle += 1
                operation_per_cycle()
            elif line[0] == "addx":
                self.cycle += 1
                operation_per_cycle()
                self.cycle += 1
                operation_per_cycle()
                self.X += int(line[1])

    def add_signal_strength(self):
        if self.cycle in [20, 60, 100, 140, 180, 220]:
            self.sum_signal_strength += self.cycle * self.X

    def solve_b(self, input: list[str]):
        self.output = [[]]
        self.output_line = 0
        self.execute_program(input, self.draw_pixel)
        print()
        for line in self.output:
            print("".join(line))
        return "dummy"

    def draw_pixel(self):
        line_len = len(self.output[self.output_line])
        if line_len == 40:
            self.output.append([])
            self.output_line += 1
        pos = self.cycle % 40
        delta = pos - self.X
        if delta <= 2 and delta >= 0:
            pixel = "#"
        else:
            pixel = "."
        self.output[self.output_line].append(pixel)


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
        .solve().submit('a')
