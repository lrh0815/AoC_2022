from aoc_helper.AoCHelper import *
from collections import deque
from rich.progress import track
from rich.status import Status

N = (0, -1)
NE = (1, -1)
E = (1, 0)
SE = (1, 1)
S = (0, 1)
SW = (-1, 1)
W = (-1, 0)
NW = (-1, -1)


class DaySolver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 23, 110, 20, True)

    def solve_a(self, input: list[str]):
        map = self.__create_map(input)
        num_elves = len(map.all_set_points())

        directions = deque([(N, NE, NW), (S, SE, SW), (W, NW, SW), (E, NE, SE)])
        for _ in track(range(1, 11)):
            self.__move_elves(map, directions)
            directions.rotate(-1)

        num_tiles = (map.max_x - map.min_x + 1) * (map.max_y - map.min_y + 1)
        empty_tiles = num_tiles - num_elves
        return empty_tiles

    def __create_map(self, input):
        map = Grid(".")
        for y, line in enumerate(input):
            for x, tile in enumerate(line):
                if tile == "#":
                    map.set(Point(x, y), "#")
        return map

    def __move_elves(self, map: Grid, directions):
        proposed_moves = self.__propose_moves(map, directions)
        if len(proposed_moves) == 0:
            return False

        for move in proposed_moves.items():
            if len(move[1]) > 1:
                continue
            map.reset(move[1][0])
            map.set(move[0], "#")
        return True

    def __propose_moves(self, map: Grid, directions):
        proposed_moves = {}
        for elf in map.all_set_points():
            if self.__all_free(map, elf, (N, NW, W, SW, S, SE, E, NE)):
                continue
            for direction in directions:
                if self.__all_free(map, elf, direction):
                    new_pos = elf + direction[0]
                    elves = proposed_moves.get(new_pos, [])
                    elves.append(elf)
                    proposed_moves[new_pos] = elves
                    break
        return proposed_moves

    def __all_free(self, map: Grid, position: Point, directions):
        for delta in directions:
            if map.is_set(position + delta):
                return False
        return True

    def solve_b(self, input: list[str]):
        map = self.__create_map(input)

        directions = deque([(N, NE, NW), (S, SE, SW), (W, NW, SW), (E, NE, SE)])

        rounds = 1
        status = Status(f"Moving elves: {rounds}")
        status.start()
        while self.__move_elves(map, directions):
            rounds += 1
            directions.rotate(-1)
            status.update(f"Moving elves: {rounds}")

        status.stop()
        return rounds


example_input1 = """.....
..##.
..#..
.....
..##.
....."""

example_input2 = """"""

if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test()\
        .solve().submit()
