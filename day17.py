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

        grid = Grid(".")
        for x in range(7):
            grid.set(Point(x, 0), "-")

        directions = input[0]
        num_directions = len(directions)
        direction_index = -1

        hashes = {}
        height_offset = 0

        rock_nr = 0
        while rock_nr < num_rocks:
            print(f"{(remaining_rocks := num_rocks - rock_nr):14}", end="\r")

            rock = rock_shapes[(rock_shape_index := rock_nr % num_rock_shapes)]
            position = Point(2, grid.max_y + 4)
            while True:
                direction = (-1, 0) if directions[(direction_index := (direction_index + 1) % num_directions)] == "<" else (1, 0)
                position = self.__blow(rock, direction, position, grid)
                if not self.__drop(rock, position, grid):
                    self.__insert(rock, position, grid)
                    break
                position += (0, -1)

            hash_value = f"{rock_shape_index}{direction_index}{hash((Point(p.x, p.y - grid.max_y) for p in grid.all_set_points()))}"
            if hash_value in hashes:
                previous_rock_nr, previous_max_y = hashes[hash_value]
                cycle_length = rock_nr - previous_rock_nr
                if cycle_length < remaining_rocks:
                    remaining_cycles = remaining_rocks // cycle_length
                    rock_nr += remaining_cycles * cycle_length
                    height_offset = remaining_cycles * (grid.max_y - previous_max_y)
            else:
                hashes[hash_value] = (rock_nr, grid.max_y)

            rock_nr += 1
        print()
        return grid.max_y + height_offset

    def __insert(self, rock: RockShape, position: Point, grid: Grid, char="#"):
        for point in rock.shape:
            if char == grid.default_value:
                grid.reset(point + position)
            else:
                grid.set(point + position, char)

    def __blow(self, rock: RockShape, direction: tuple[int, int], position: Point, grid: Grid):
        new_pos = position + direction
        if new_pos.x < 0 or new_pos.x + rock.width > 7:
            return position

        if self.__has_collision(rock, new_pos, grid):
            return position
        return new_pos

    def __has_collision(self, rock: RockShape, position: Point, grid: Grid):
        for point in rock.shape:
            if grid.get(point + position) != grid.default_value:
                return True
        return False

    def __drop(self, rock: RockShape, position: Point, grid: Grid):
        return not self.__has_collision(rock, position + (0, -1), grid)

    def solve_a(self, input: list[str]):
        return self.__simulate_rocks_falling(input, 2022)

    def solve_b(self, input: list[str]):
        return self.__simulate_rocks_falling(input, 1000000000000)


example_input = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""

if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test_with('a', example_input.splitlines(), 3068)\
        .test_with('b', example_input.splitlines(), 1514285714288)\
        .solve("b").submit()
