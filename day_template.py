from aoc_helper.AoCHelper import *
import re
from dataclasses import dataclass
from icecream import ic
from collections import deque
from rich import print
from rich.progress import Progress


class DaySolver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, x, None, None, True)

    def solve_a(self, input: list[str]):
        return None

    def solve_b(self, input: list[str]):
        return None


example_input1 = """"""

example_input2 = """"""

if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test_with('a', example_input1.splitlines(), None)\
        .test_with('b', example_input2.splitlines(), None)\
        .solve().submit()
