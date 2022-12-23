from aoc_helper.AoCHelper import *
import re
from dataclasses import dataclass
from icecream import ic
from collections import deque
from rich import print
from rich.progress import Progress


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
        pos, direction = self.__folow_path(map, path, self.__traverse_edge_part1)
        answer = 1000 * pos.y + 4 * pos.x + directions.index(direction)
        return answer

    def __folow_path(self, map: Grid, path: list, traverse_edge_func):
        pos = Point(1, 1)
        direction = directions[0]

        while map.get(pos) == " ":
            pos += (1, 0)

        map.set(pos, direction.symbol)
        for entry in path:
            steps = int(entry[0])
            for _ in range(steps):
                new_pos = pos + direction.increment
                if map.get(new_pos) == "#":
                    break
                if map.get(new_pos) == " ":
                    traversed_pos, traversed_direction, blocked = traverse_edge_func(map, new_pos, direction)
                    if blocked:
                        break
                    direction = traversed_direction
                    new_pos = traversed_pos
                pos = new_pos
                map.set(pos, direction.symbol)
            direction = self.__get_next_direction(direction, entry[1])
            map.set(pos, direction.symbol)

        map.print_grid(reverse_y=True)
        return pos, direction

    def __traverse_edge_part1(self, map: Grid, pos: Point, direction: Direction):
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
        for y, line in enumerate(input):
            if line.strip() == "":
                break

            for x, tile in enumerate(line):
                if tile != " ":
                    map.set(Point(x + 1, y + 1), tile)

        path = re.findall(r"(\d\d?)([RL])?", input[-1])
        return map, path

    def solve_b(self, input: list[str]):
        if len(input) < 20:
            self.cs = 4
        else:
            self.cs = 50

        map, path = self.__read_input(input)
        map.print_grid(reverse_y=True)
        pos, direction = self.__folow_path(map, path, self.__traverse_edge_part2)
        answer = 1000 * ic(pos.y) + 4 * ic(pos.x) + ic(directions.index(direction))
        return answer

    def __traverse_edge_part2(self, map: Grid, pos: Point, direction: Direction):
        cs = self.cs
        ic(pos)
        match pos:
            case p if p.x in range(cs + 1, 2 * cs + 1) and p.y == 0:       # 1 -> 6
                new_direction = right
                new_pos = Point(1, (pos.x - cs) + 3 * cs)

            case p if p.x == cs and p.y in range(1, cs + 1):        # 1 -> 5
                new_direction = right
                new_pos = Point(1, (3 * cs + 1) - pos.y)

            case p if p.x == 3 * cs + 1 and p.y in range(1, cs + 1):       # 2 -> 4
                new_direction = left
                new_pos = Point(2 * cs, (3 * cs + 1) - pos.y)

            case p if p.x in range(2 * cs + 1, 3 * cs + 1) and p.y == 0:      # 2 -> 6
                new_direction = up
                new_pos = Point((pos.x - 2 * cs), 4 * cs)

            case p if p.x in range(2 * cs + 1, 3 * cs + 1) and p.y == cs + 1:     # 2 -> 3
                new_direction = left
                new_pos = Point(2 * cs, (pos.x - 2 * cs) + cs)

            case p if p.x == cs and p.y in range(cs + 1, 2 * cs + 1):      # 3 -> 5
                new_direction = down
                new_pos = Point((pos.y - cs), 2 * cs + 1)

            case p if p.x == 2 * cs + 1 and p.y in range(cs + 1, 2 * cs + 1):     # 3 -> 2
                new_direction = up
                new_pos = Point((pos.y - cs) + 2 * cs, cs)

            case p if p.x == 2 * cs + 1 and p.y in range(2 * cs + 1, 3 * cs + 1):    # 4 -> 2
                new_direction = left
                new_pos = Point(3 * cs, (cs + 1) - (pos.y - 2 * cs))

            case p if p.x in range(cs + 1, 2 * cs + 1) and p.y == 3 * cs + 1:     # 4 -> 6
                new_direction = left
                new_pos = Point(cs, (pos.x - cs) + 3 * cs)

            case p if p.x in range(1, cs + 1) and p.y == 2 * cs:       # 5 -> 3
                new_direction = right
                new_pos = Point(cs + 1, pos.x + cs)

            case p if p.x == 0 and pos.y in range(2 * cs + 1, 3 * cs + 1):    # 5 -> 1
                new_direction = right
                new_pos = Point(cs + 1, (cs + 1) - (pos.y - 2 * cs))

            case p if p.x == cs + 1 and p.y in range(3 * cs + 1, 4 * cs + 1):     # 6 -> 4
                new_direction = up
                new_pos = Point((pos.y - 3 * cs) + cs, 3 * cs)

            case p if p.x == 0 and p.y in range(3 * cs + 1, 4 * cs + 1):      # 6 -> 1
                new_direction = down
                new_pos = Point((pos.y - 3 * cs) + cs, 1)

            case p if p.x in range(1, cs + 1) and p.y == 4 * cs + 1:       # 6 -> 2
                new_direction = down
                new_pos = Point(pos.x + 2 * cs, 1)

        ic(new_pos)
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
        .test_with('b', example_input2.splitlines(), 10 * 1000 + 1 * 4 + 2)\
        .solve("b").submit()
