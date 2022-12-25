from aoc_helper.AoCHelper import *
import re
from dataclasses import dataclass
from icecream import ic
from collections import deque
from rich import print
from rich.progress import track
from rich.status import Status
import copy

WAIT = (0, 0)
UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)

BU = 2**0
BR = 2**1
BD = 2**2
BL = 2**3
WALL = 2**4


class DaySolver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 24, 18, None, True)

    def solve_a(self, input: list[str]):
        start = Point(1, 0)
        target = Point(len(input[0])-2,  len(input)-1)
        map = self.__create_map(input)

        positions: set[Point] = {start}
        minutes = 0
        status = Status(f"Minutes {minutes}")
        status.start()
        while not target in positions:
            minutes += 1
            status.update(f"Minutes {minutes}")
            new_map = self.__move_blizzards(map)
            new_positions: set[Point] = set()
            for pos in positions:
                for dir in [UP, RIGHT, DOWN, LEFT, WAIT]:
                    new_pos = pos + dir
                    if new_pos.y < 0:
                        continue
                    if new_map[new_pos.y][new_pos.x] == 0:
                        new_positions.add(new_pos)
            positions = new_positions
            map = new_map
        status.stop()
        return minutes

    def __create_map(self, input):
        map = []
        self.map_proto = []
        for line in input:
            map.append([])
            self.map_proto.append([])
            for tile in line:
                match tile:
                    case "#":
                        map[-1].append(WALL)
                        self.map_proto[-1].append(WALL)
                    case "^":
                        map[-1].append(BU)
                        self.map_proto[-1].append(0)
                    case ">":
                        map[-1].append(BR)
                        self.map_proto[-1].append(0)
                    case "v":
                        map[-1].append(BD)
                        self.map_proto[-1].append(0)
                    case "<":
                        map[-1].append(BL)
                        self.map_proto[-1].append(0)
                    case _:
                        map[-1].append(0)
                        self.map_proto[-1].append(0)

        return tuple([tuple(row) for row in map])

    def __move_blizzards(self, map: list[list[int]]) -> list[list[int]]:
        new_map = copy.deepcopy(self.map_proto)
        for y in range(1, len(map)-1):
            for x in range(1, len(map[y])-1):
                if map[y][x] == 0 or map[y][x] == WALL:
                    continue
                if map[y][x] & BU:
                    if map[y-1][x] & WALL:
                        new_map[-2][x] |= BU
                    else:
                        new_map[y-1][x] |= BU
                if map[y][x] & BR:
                    if map[y][x+1] & WALL:
                        new_map[y][1] |= BR
                    else:
                        new_map[y][x+1] |= BR
                if map[y][x] & BD:
                    if map[y+1][x] & WALL:
                        new_map[1][x] |= BD
                    else:
                        new_map[y+1][x] |= BD
                if map[y][x] & BL:
                    if map[y][x-1] & WALL:
                        new_map[y][-2] |= BL
                    else:
                        new_map[y][x-1] |= BL
        return tuple([tuple(row) for row in new_map])

    def solve_b(self, input: list[str]):
        return None


example_input1 = """""".splitlines()

example_input2 = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#""".splitlines()

if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test_with('a', example_input2, 18)\
        .solve().submit()
