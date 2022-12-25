from aoc_helper.AoCHelper import *


class DaySolver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 18, 64, 58, True)

    def solve_a(self, input: list[str]):
        print()

        cubes, grid = self.__read_input(input)

        count = 0
        for index, cube in enumerate(cubes):
            print(f"{index + 1:4}/{len(cubes)}", end="\r")
            for neighbor in self.__get_neighbors(cube):
                if grid.get(neighbor) == grid.default_value:
                    count += 1
        print()
        return count

    def solve_b(self, input: list[str]):
        print()

        cubes, grid = self.__read_input(input)

        queue = [Point(x, y, z) for x in [grid.min_x-1, grid.max_x+1] for y in [grid.min_y-1, grid.max_y+1] for z in [grid.min_z-1, grid.max_z+1]]
        while len(queue) > 0:
            print(f"{len(queue):5}", end="\r")
            point = queue.pop()
            if grid.get(point) == grid.default_value:
                grid.set(point, "*")
                for neighbor in self.__get_neighbors(point):
                    if grid.contains(neighbor) and grid.get(neighbor) == grid.default_value and neighbor not in queue:
                        queue.append(neighbor)

        print()
        count = 0
        for index, cube in enumerate(cubes):
            print(f"{index + 1:4}/{len(cubes)}", end="\r")
            for neighbor in self.__get_neighbors(cube):
                if grid.get(neighbor) == "*":
                    count += 1
        print()
        return count

    def __read_input(self, input):
        cubes = [Point(int(coords[0]), int(coords[1]), int(coords[2])) for coords in [line.split(",") for line in input]]
        grid = Grid(".")
        for cube in cubes:
            grid.set(cube, "#")
        return cubes, grid

    def __get_neighbors(self, point):
        for dir in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            yield point + dir


if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test()\
        .solve()
