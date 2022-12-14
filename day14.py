from aoc_helper.AoCHelper import PuzzleSolver, AoCHelper

def sign(n): 
  if n<0: return -1 
  elif n>0: return 1 
  else: 0

class DaySolver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 14, 24, None, True)

    def solve_a(self, input: list[str]):
        print()
        paths = self.__get_paths(input)
        all_x_coords = [point[0] for point in [x for path in paths for x in path]]
        all_y_coords = [point[1] for point in [x for path in paths for x in path]]
        self.min_x = min(all_x_coords)
        self.max_x = max(all_x_coords)
        self.min_y = 0
        self.max_y = max(all_y_coords)
        self.grid = [["." for i in range(self.max_x - self.min_x + 1)] for i in range(self.max_y - self.min_y + 1)]
        self.__insert_paths(paths)

        for line in self.grid:
            print(line)

        count = 0
        while True:
            if self.__simulate_rock_fall():
                if self.__simulate_rock_fall():
                    break
                else:
                    count += 1
            else:
                count += 1
        return count

    def __simulate_rock_fall(self):
        pos = (500, 0)
        while True:
            sand_has_fallen = False
            for delta in [(0, 1), (-1, 1), (1, 1)]:
                next_pos = (pos[0] + delta[0], pos[1] + delta[1])
                if self.__is_out_of_bounds(next_pos):
                    return True
                if not self.__is_blocked(next_pos):
                    pos = next_pos
                    sand_has_fallen = True
                    break
            if not sand_has_fallen:
                self.__set(pos, "o")
                return False    

    def __is_out_of_bounds(self, pos):
        if pos[0] < self.min_x or pos[0] > self.max_x or pos[1] < self.min_y or pos[1] > self.max_y:
            return True
        return False

    def __is_blocked(self, pos):
        return self.__get(pos) != "."

    def __insert_paths(self, paths:list[list[tuple[int, int]]]):
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
    
    def __set(self, point, value):
        y = point[1] - self.min_y
        x = point[0] - self.min_x
        self.grid[y][x] = value

    def __get(self, point):
        return self.grid[point[1] - self.min_y][point[0] - self.min_x]


    def __get_paths(self, input: list[str]):
        paths = []
        for line in input:
            points = [(int(x), int(y)) for x, y in [z.strip().split(",") for z in line.split("->")]]
            paths.append(points)
        return paths

    def solve_b(self, input: list[str]):
        return None


example_input1 = """"""

example_input2 = """"""

if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test()\
        .solve().submit()
