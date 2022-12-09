from aoc_helper.AoCHelper import PuzzleSolver, AoCHelper


class Day9Solver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 9, None, None, True)

    def solve_a(self, input: list[str]):
        return self.simulate_rope(input, 2)

    def simulate_rope(self, input, num_knots):
        self.x = [0 for i in range(0, num_knots)]
        self.y = [0 for i in range(0, num_knots)]
        self.tail_positions = {(0, 0)}

        for line in input:
            match line.split(" "):
                case "U", d:
                    self.move(int(d), 0, 1)
                case "L", d:
                    self.move(int(d), -1, 0)
                case "R", d:
                    self.move(int(d), 1, 0)
                case "D", d:
                    self.move(int(d), 0, -1)
        return len(self.tail_positions)

    def move(self, distance, dx, dy):
        while distance > 0:
            self.move_step(dx, dy)
            distance -= 1

    def move_step(self, dx, dy):
        self.x[0] += dx
        self.y[0] += dy
        for i in range(1, len(self.x)):
            self.adjust_tail(i)
        self.tail_positions.add((self.x[-1], self.y[-1]))

    def adjust_tail(self, t):
        match (self.x[t] - self.x[t-1], self.y[t] - self.y[t-1]):
            case (-2, -2):
                self.y[t] += 1
                self.x[t] += 1
            case (-1, -2):
                self.y[t] += 1
                self.x[t] += 1
            case (0, -2):
                self.y[t] += 1
            case (1, -2):
                self.y[t] += 1
                self.x[t] -= 1
            case (2, -2):
                self.y[t] += 1
                self.x[t] -= 1
            case (-2, -1):
                self.y[t] += 1
                self.x[t] += 1
            case (2, -1):
                self.y[t] += 1
                self.x[t] -= 1
            case (-2, 0):
                self.x[t] += 1
            case (2, 0):
                self.x[t] -= 1
            case (-2, 1):
                self.y[t] -= 1
                self.x[t] += 1
            case (2, 1):
                self.y[t] -= 1
                self.x[t] -= 1
            case (-2, 2):
                self.y[t] -= 1
                self.x[t] += 1
            case (-1, 2):
                self.y[t] -= 1
                self.x[t] += 1
            case (0, 2):
                self.y[t] -= 1
            case (1, 2):
                self.y[t] -= 1
                self.x[t] -= 1
            case (2, 2):
                self.y[t] -= 1
                self.x[t] -= 1

    def solve_b(self, input: list[str]):
        return self.simulate_rope(input, 10)


example_input1 = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

example_input2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

if __name__ == "__main__":
    AoCHelper(Day9Solver())\
        .test_with('a', example_input1.splitlines(), 13)\
        .test_with('b', example_input2.splitlines(), 36)\
        .solve().submit()
