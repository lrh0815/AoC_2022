from aoc_helper.AoCHelper import *
import re
from dataclasses import dataclass
from icecream import ic
from collections import deque
from rich import print
from rich.progress import Progress
from itertools import cycle

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
        PuzzleSolver.__init__(self, 2022, 22, 6032, None, True)

    def solve_a(self, input: list[str]):
        map, path = self.__read_input(input)
        pos, direction = self.__folow_path(map, path, self.__traverse_edge_part1)
        answer = 1000 * pos.y + 4 * pos.x + directions.index(direction)
        return answer

    def __folow_path(self, map: Grid, path: list, traverse_edge_func):
        pos = Point(1, 1)
        direction = directions[(dir_idx := 0)]

        while map.get(pos) == " ":
            pos += (1, 0)

        for entry in path:
            steps = int(entry[0])
            for _ in range(steps):
                new_pos = pos + direction.increment
                if map.get(new_pos) == "#":
                    break
                if map.get(new_pos) == " ":
                    new_pos, new_direction, blocked = traverse_edge_func(map, new_pos, direction)
                    if blocked:
                        break
                    direction = new_direction
                pos = new_pos
                map.set(pos, direction.symbol)
            direction, dir_idx = self.__get_next_direction(dir_idx, entry[1])

        map.print_grid(reverse_y=True)
        return pos, direction

    def __traverse_edge_part1(self, map: Grid, pos: Point, direction : Direction):
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


    def __get_next_direction(self, dir_idx, turn):
        if turn == "R": 
            dir_idx += 1
            if dir_idx == len(directions): dir_idx = 0
        elif turn == "L": 
            dir_idx -= 1
            if dir_idx < 0: dir_idx = len(directions) - 1
        return directions[dir_idx], dir_idx

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
        map, path = self.__read_input(input)
        pos, direction = self.__folow_path(map, path, self.__traverse_edge_part2)
        answer = 1000 * pos.y + 4 * pos.x + directions.index(direction)
        return answer

    def __traverse_edge_part1(self, map: Grid, pos: Point, direction : Direction):
        return pos, direction, True


example_input1 = """"""

example_input2 = """"""

if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test()\
        .solve().submit()
