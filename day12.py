from aoc_helper.AoCHelper import PuzzleSolver, AoCHelper


class DaySolver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 12, 31, 29, True)

    def solve_a(self, input: list[str]):
        self.grid = input
        start = list(self.__find("S"))
        self.dest = list(self.__find("E"))[0]
        return self.__find_paths(start[0], None)

    def __find(self, char):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] == char:
                    yield (x, y)

    def __height_at(self, pos):
        match self.grid[pos[1]][pos[0]]:
            case "S":
                return 0
            case "E":
                return ord("z") - ord("a")
            case c:
                return ord(c) - ord("a")

    def __find_paths(self, start, min_path_len):
        queue = [(start, [])]
        visited = {}

        while True:
            if len(queue) == 0:
                break

            item = queue.pop()
            pos = item[0]

            if pos == start:
                continue

            path = item[1]
            path_len = len(path)
            if min_path_len != None and path_len >= min_path_len:
                continue

            if pos == self.dest:
                if min_path_len == None or path_len < min_path_len:
                    min_path_len = path_len
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
        return min_path_len

    def solve_b(self, input: list[str]):
        self.grid = [line.replace("S", "a") for line in input]
        self.dest = list(self.__find("E"))[0]
        min_path_len = None
        starts = list(self.__find("a"))
        print(len(starts))
        i = 0
        for start in starts:
            path_len = self.__find_paths(start, min_path_len)
            if min_path_len == None or path_len < min_path_len:
                min_path_len = path_len
            i += 1
            print(f"{i}/{len(starts)}: {start} = {min_path_len}")
        return min_path_len


example_input1 = """"""

example_input2 = """"""

if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test("b")\
        .solve("b").submit()
