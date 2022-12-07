from aoc_helper.AoCHelper import PuzzleSolver, AoCHelper


example_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


class Day7Solver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 7, 95437, None, False)

    def solve_a(self, input: list[str]):
        self.__create_dirs(input)
        self.__update_subsize(self.dirs["/"])

        total = 0
        for dir in map(lambda x: x[1], self.dirs.items()):
            total_dir_size = dir[2] + dir[4]
            if total_dir_size <= 100000:
                total += total_dir_size

        return total

    def __create_dirs(self, input):
        self.dirs = {"/" : ["/", None, 0, set(), 0]}
        current_dir = None
        for line in map(lambda x: x.split(), input):
            if line[0] == "$":
                if line[1] == "cd":
                    if line[2] == "..":
                        if current_dir[1] != None:
                            current_dir = self.dirs[current_dir[1]]
                    else:
                        if line[2] != "/":
                            dirname = current_dir[0] + "/" + line[2]
                        else:
                            dirname = line[2]
                        if not dirname in self.dirs.keys():
                            self.dirs[dirname] = [dirname, current_dir[0], 0, set(), 0]
                        current_dir = self.dirs[dirname]
                elif line[1] == "ls":
                    current_dir[2] = 0
            elif line[0] == "dir":
                current_dir[3].add(current_dir[0] + "/" + line[1])
            else:
                current_dir[2] += int(line[0])

    def __update_subsize(self, dir):
        for subdir in dir[3]:
            self.__update_subsize(self.dirs[subdir])
        if dir[1] != None:
            self.dirs[dir[1]][4] += dir[2] + dir[4]

    def solve_b(self, input: list[str]):
        self.__create_dirs(input)
        self.__update_subsize(self.dirs["/"])

        total_space = 70000000
        required_free = 30000000
        current_free = total_space - (self.dirs["/"][2] + self.dirs["/"][4])

        min_delete = None
        for dir in map(lambda x: x[1], self.dirs.items()):
            total_dir_size = dir[2] + dir[4]
            if current_free + total_dir_size > required_free:
                if min_delete == None or min_delete > total_dir_size:
                    min_delete = total_dir_size
        return min_delete


if __name__ == "__main__":
    AoCHelper(Day7Solver())\
        .test_with('a', example_input.splitlines(), 95437)\
        .test_with('b', example_input.splitlines(), 24933642)\
        .solve().submit()
