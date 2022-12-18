from aoc_helper.AoCHelper import *


class RockShape(object):
    def __init__(self, shape: list[Point]):
        self.shape = shape
        self.width = max([p.x for p in self.shape]) + 1
        self.height = max([p.y for p in self.shape]) + 1


rock_shapes = [RockShape([Point(x, y) for x, y in shape]) for shape in
               [[(0, 0), (1, 0), (2, 0), (3, 0)],
                [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
                [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
                [(0, 0), (0, 1), (0, 2), (0, 3)],
                [(0, 0), (1, 0), (0, 1), (1, 1)]]]

num_rock_shapes = len(rock_shapes)


class DaySolver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 17, None, None, True)

    def __simulate_rocks_falling(self, input, num_rocks):
        print()

        self.grid = Grid(".")
        for x in range(7):
            self.grid.set(Point(x, 0), "-")

        directions = input[0]
        num_directions = len(directions)
        current_direction_index = 0

        for rock_nr in range(num_rocks):
            print(f"{rock_nr+1:5}/{num_rocks}", end="\r")
            rock = rock_shapes[rock_nr % num_rock_shapes]
            position = Point(2, self.grid.max_y + 4)
            while True:
                #self.__print_transient(rock, position)
                direction = (-1, 0) if directions[current_direction_index % num_directions] == "<" else (1, 0)
                current_direction_index += 1
                position = self.__blow(rock, direction, position)
                #self.__print_transient(rock, position)
                if not self.__drop(rock, position):
                    self.__insert(rock, position)
                    break
                position += (0, -1)
        print()

    def __print_transient(self, rock, position):
        self.__insert(rock, position, "@")
        print()
        self.grid.print_grid()
        self.__insert(rock, position, self.grid.default_value)

    def __insert(self, rock: RockShape, position: Point, char="#"):
        for point in rock.shape:
            if char == self.grid.default_value:
                self.grid.reset(point + position)
            else:
                self.grid.set(point + position, char)

    def __blow(self, rock: RockShape, direction: tuple[int, int], position: Point):
        new_pos = position + direction
        if new_pos.x < 0 or new_pos.x + rock.width > 7:
            return position

        if self.__has_collision(rock, new_pos):
            return position
        return new_pos

    def __has_collision(self, rock: RockShape, position: Point):
        for point in rock.shape:
            if self.grid.get(point + position) != self.grid.default_value:
                return True
        return False

    def __drop(self, rock: RockShape, position: Point):
        return not self.__has_collision(rock, position + (0, -1))

    def solve_a(self, input: list[str]):
        self.__simulate_rocks_falling(input, 2022)
        return self.grid.max_y

    def solve_b(self, input: list[str]):
        self.__simulate_rocks_falling(input, 1000000000000)  # yeah, let's just pretend that this works without optimization...
        return self.grid.max_y


example_input1 = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""

example_input2 = """"""

if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test_with('a', example_input1.splitlines(), 3068)\
        .test_with('b', example_input1.splitlines(), 1514285714288)\
        .solve("b").submit()
