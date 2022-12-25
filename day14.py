from aoc_helper.AoCHelper import *


class DaySolver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 14, 24, 93, True)

    def __get_paths(self, input: list[str]):
        paths = []
        for line in input:
            points = [(int(x), int(y)) for x, y in [z.strip().split(",") for z in line.split("->")]]
            paths.append(points)
        return paths

    def __get_min_max_coords(self):
        self.min_x = min([k[0] for k in self.grid.keys()])
        self.max_x = max([k[0] for k in self.grid.keys()])
        self.max_y = max([k[1] for k in self.grid.keys()])

    def __create_grid(self, paths: list[list[tuple[int, int]]]):
        self.grid = {}
        for path in paths:
            rock = path.pop(0)
            self.__set((rock[0], rock[1]), "#")
            while len(path) > 0:
                next_rock = path.pop(0)
                delta_x = next_rock[0] - rock[0]
                delta_y = next_rock[1] - rock[1]
                while delta_x != 0:
                    self.__set((rock[0] + delta_x, rock[1]), "#")
                    delta_x -= sign(delta_x)
                while delta_y != 0:
                    self.__set((rock[0], rock[1] + delta_y), "#")
                    delta_y -= sign(delta_y)
                rock = next_rock

    def __simulate_sand(self, is_out_of_bounds=None):
        count = 0
        while True:
            if self.__simulate_sand_unit(is_out_of_bounds):
                if self.__simulate_sand_unit(is_out_of_bounds):
                    break
                else:
                    count += 1
            else:
                count += 1
        return count

    def __simulate_sand_unit(self, is_out_of_bounds=None):
        pos = (500, 0)
        while True:
            sand_has_fallen = False
            for delta in [(0, 1), (-1, 1), (1, 1)]:
                next_pos = (pos[0] + delta[0], pos[1] + delta[1])
                if is_out_of_bounds != None and is_out_of_bounds(next_pos):
                    return True
                if not self.__is_blocked(next_pos):
                    pos = next_pos
                    sand_has_fallen = True
                    break
            if not sand_has_fallen:
                self.__set(pos, "o")
                if pos == (500, 0):
                    return True
                return False

    def __is_out_of_bounds(self, pos):
        if pos[0] < self.min_x or pos[0] > self.max_x or pos[1] > self.max_y:
            return True
        return False

    def __is_blocked(self, pos):
        return self.__get(pos) != " "

    def __set(self, point, value):
        self.grid[point] = value

    def __get(self, point):
        if point[1] == self.max_y + 2:
            return "#"
        return self.grid.get(point, " ")

    def solve_a(self, input: list[str]):
        paths = self.__get_paths(input)
        self.__create_grid(paths)
        self.__get_min_max_coords()
        self.__print_grid()
        answer = self.__simulate_sand(self.__is_out_of_bounds)
        self.__print_grid()
        return answer

    def solve_b(self, input: list[str]):
        paths = self.__get_paths(input)
        self.__create_grid(paths)
        self.__print_grid()
        answer = self.__simulate_sand() + 1
        self.__print_grid()
        return answer

    def __print_grid(self):
        min_x = min([k[0] for k in self.grid.keys()])
        max_x = max([k[0] for k in self.grid.keys()])
        min_y = min([k[1] for k in self.grid.keys()])
        max_y = max([k[1] for k in self.grid.keys()])

        for y in range(min_y, max_y + 3):
            print()
            for x in range(min_x - 1, max_x + 2):
                print(self.__get((x, y)), end="")


if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test()\
        .solve().submit()
