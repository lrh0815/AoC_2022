from aoc_helper.AoCHelper import *
import re
from dataclasses import dataclass
from icecream import ic


@dataclass
class Direction(object):
    symbol: str
    increment: Point


up = Direction("^", Point(0, -1))
right = Direction(">", Point(1, 0))
down = Direction("v", Point(0, 1))
left = Direction("<", Point(-1, 0))

directions = [right, down, left, up]


class DaySolver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 22, 6032, "dummy", True)

    def solve_a(self, input: list[str]):
        map, path = self.__read_input(input)
        pos, direction = self.__follow_path(map, path, self.__move_part_1)
        answer = 1000 * (pos.y + 1) + 4 * (pos.x + 1) + directions.index(direction)
        return answer

    def __follow_path(self, map: Grid, path: list, move_func, print_map = True):
        direction = directions[0]

        pos = self.__find_start(map)

        map.set(pos, direction.symbol)
        for entry in path:
            steps = int(entry[0])
            for _ in range(steps):
                new_pos, new_direction, blocked = move_func(map, pos, direction)
                if blocked:
                    break
                direction = new_direction
                pos = new_pos
                map.set(pos, direction.symbol)
            direction = self.__get_next_direction(direction, entry[1])
            map.set(pos, direction.symbol)

        if print_map: map.print_grid(reverse_y=True)
        return pos, direction

    def __find_start(self, map):
        pos = Point(0, 0)
        while not map.is_set(pos):
            pos += (1, 0)
        return pos

    def __move_part_1(self, map: Grid, pos: Point, direction: Direction):
        new_pos = pos + direction.increment
        if not map.is_set(new_pos):
            match direction.symbol:
                case ">":
                    new_pos = Point(0, pos.y)
                case "<":
                    new_pos = Point(map.max_x, pos.y)
                case "v":
                    new_pos = Point(pos.x, 0)
                case "^":
                    new_pos = Point(pos.x, map.max_y)
            while map.get(new_pos) == " ":
                new_pos += direction.increment

        blocked = map.get(new_pos) == "#"

        return new_pos, direction, blocked

    def __get_next_direction(self, direction: Direction, turn):
        dir_idx = directions.index(direction)
        if turn == "R":
            dir_idx += 1
            if dir_idx == len(directions):
                dir_idx = 0
        elif turn == "L":
            dir_idx -= 1
            if dir_idx < 0:
                dir_idx = len(directions) - 1
        return directions[dir_idx]

    def __read_input(self, input: list[str]):
        map = Grid(" ")
        for y, line in enumerate(input[:-2]):
            for x, tile in enumerate(line):
                if tile != " ":
                    map.set(Point(x, y), tile)

        path = re.findall(r"(\d\d?)([RL])?", input[-1])
        return map, path

    def solve_b(self, input: list[str]):
        if len(input) < 20:
            self.cs = 4
        else:
            self.cs = 50

        map, path = self.__read_input(input)
        map.print_grid(reverse_y=True)

        self.__test_movement(map)

        pos, direction = self.__follow_path(map, path, self.__move_part_2)
        answer = 1000 * ic(pos.y + 1) + 4 * ic(pos.x + 1) + ic(directions.index(direction))
        return answer

    def __test_movement(self, map: Grid):
        steps = 4 * self.cs
        start_pos = self.__find_start(map)

        map_copy = Grid(map.default_value)

        for i in range(4):
            for p in map.all_set_points():
                map_copy.set(p, ".")
            path = [[0, "R"]] * i + [[steps, ""]]
            pos, direction = self.__follow_path(map_copy, path, self.__move_part_2, False)
            assert pos == start_pos
            assert direction == directions[i]

    def __move_part_2(self, map: Grid, pos: Point, direction: Direction):
        new_pos = pos + direction.increment
        cs = self.cs
        if not map.is_set(new_pos):
            match pos:
                case p if p.x in range(1 * cs, 2 * cs) and p.y in range(0 * cs, 1 * cs):  # 1
                    if direction == up: # -> 6
                        new_direction = right
                        new_pos = Point(0, (p.x - cs) + 3 * cs)
                    if direction == left: # -> 5
                        new_direction = right
                        new_pos = Point(0, (3 * cs - 1) - p.y)

                case p if p.x in range(2 * cs, 3 * cs) and p.y in range(0 * cs, 1 * cs):  # 2
                    if direction == right: # -> 4
                        new_direction = left
                        new_pos = Point(2 * cs - 1, (3 * cs - 1) - p.y)
                    if direction == up: # -> 6
                        new_direction = up
                        new_pos = Point((p.x - 2 * cs), 4 * cs - 1)
                    if direction == down: # -> 3
                        new_direction = left
                        new_pos = Point(2 * cs - 1, (p.x - 2 * cs) + cs)

                case p if p.x in range(1 * cs, 2 * cs) and p.y in range(1 * cs, 2 * cs):  # 3
                    if direction == left: # -> 5
                        new_direction = down
                        new_pos = Point((p.y - cs), 2 * cs)
                    if direction == right: # -> 2
                        new_direction = up
                        new_pos = Point((p.y - cs) + 2 * cs, cs - 1)

                case p if p.x in range(1 * cs, 2 * cs) and p.y in range(2 * cs, 3 * cs):  # 4
                    if direction == right: # -> 2
                        new_direction = left
                        new_pos = Point(3 * cs - 1, cs - 1 - (p.y - 2 * cs))
                    if direction == down: # -> 6
                        new_direction = left
                        new_pos = Point(cs - 1, (p.x - cs) + 3 * cs)
                
                case p if p.x in range(0 * cs, 1 * cs) and p.y in range(2 * cs, 3 * cs):  # 5
                    if direction == up: # -> 3
                        new_direction = right
                        new_pos = Point(cs, p.x + cs)
                    if direction == left: # -> 1
                        new_direction = right
                        new_pos = Point(cs, cs - 1 - (p.y - 2 * cs))

                case p if p.x in range(0 * cs, 1 * cs) and p.y in range(3 * cs, 4 * cs):  # 6
                    if direction == right: # -> 4
                        new_direction = up
                        new_pos = Point((p.y - 3 * cs) + cs, 3 * cs - 1)
                    if direction == left: # -> 1
                        new_direction = down
                        new_pos = Point((p.y - 3 * cs) + cs, 0)
                    if direction == down: # -> 2
                        new_direction = down
                        new_pos = Point(p.x + 2 * cs, 0)
        else:
            new_direction = direction

        if direction != new_direction:
            ic(pos, direction, new_pos, new_direction)

        if map.get(new_pos) == "#":
            return None, None, True

        return new_pos, new_direction, False


example_input1 = """"""

example_input2 = """    ...#.#..
    .#......
    #.....#.
    ........
    ...#
    #...
    ....
    ..#.
..#....#
........
.....#..
........
#...
..#.
....
....

10R5L5R10L4R5L5"""

if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test("a")\
        .test_with('b', example_input2.splitlines(), 10 * 1000 + 1 * 4 + 2)\
        .solve().submit()


