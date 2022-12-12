from aoc_helper.AoCHelper import PuzzleSolver, AoCHelper


class DaySolver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 12, 31, None, True)

    def solve_a(self, input: list[str]):
        self.grid = input
        self.start = self.__find_start()
        self.dest = self.__find_dest()
        return self.__find_paths()

    def __find_start(self):
        return self.__find("S")

    def __find_dest(self):
        return self.__find("E")

    def __find(self, char):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] == char:
                    return (x, y)

    def __height_at(self, pos):
        match self.grid[pos[1]][pos[0]]:
            case "S":
                return 0
            case "E":
                return ord("z") - ord("a")
            case c:
                return ord(c) - ord("a")

    def __find_paths(self):
        queue = [(self.start, [])]
        min_path_len = None
        visited = {}

        while True:
            if len(queue) == 0:
                break

            item = queue.pop()
            pos = item[0]
            path = item[1]
            path_len = len(path)
            if pos == self.dest:
                if min_path_len == None or path_len < min_path_len:
                    min_path_len = path_len
                    min_path = path
                continue

            if min_path_len != None and path_len >= min_path_len:
                continue

            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_pos = (pos[0] + direction[0], pos[1] + direction[1])
                if next_pos[0] > -1 and next_pos[0] < len(self.grid[0]) and next_pos[1] > -1 and next_pos[1] < len(self.grid):
                    next_height = self.__height_at(next_pos)
                    current_height = self.__height_at(pos)
                    if next_height <= current_height + 1:
                        if next_pos not in visited.keys():
                            visited[next_pos] = path_len + 1
                            queue.append((next_pos, path + [(next_pos, next_height)]))
                        elif visited[next_pos] > path_len + 1:
                            visited[next_pos] = path_len + 1
                            queue.append((next_pos, path + [(next_pos, next_height)]))

        print(min_path)
        return min_path_len

    def solve_b(self, input: list[str]):
        return None


example_input1 = """"""

example_input2 = """"""

if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test()\
        .solve().submit()
