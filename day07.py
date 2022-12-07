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


class DirEntry(object):
    def __init__(self, path: str, parent: "DirEntry"):
        self.path = path
        self.parent = parent
        self.size = 0
        self.sub_dir_size = 0
        self.sub_dirs = set()

    @property
    def total_size(self):
        return self.size + self.sub_dir_size


class Day7Solver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 7, 95437, None, False)

    def solve_a(self, input: list[str]):
        self.__create_dirs(input)
        self.__update_subdir_size(self.dirs["/"])

        total_size = 0
        for dir in map(lambda x: x[1], self.dirs.items()):
            if dir.total_size <= 100000:
                total_size += dir.total_size

        return total_size

    def __create_dirs(self, input):
        self.dirs = {"/": DirEntry("/", None)}
        current_dir = None
        for line in map(lambda x: x.split(), input):
            if line[0] == "$":
                if line[1] == "cd":
                    if line[2] == "..":
                        if current_dir.parent != None:
                            current_dir = current_dir.parent
                    else:
                        if line[2] == "/":
                            current_dir = self.dirs["/"]
                        else:
                            current_dir = self.__get_or_add_entry(current_dir, line[2])
                elif line[1] == "ls":
                    current_dir.size = 0
            elif line[0] == "dir":
                self.__get_or_add_entry(current_dir, line[1])
            else:
                current_dir.size += int(line[0])

    def __get_or_add_entry(self, current_dir: DirEntry, dirname):
        path = current_dir.path + "/" + dirname
        if not path in self.dirs.keys():
            dir_entry = DirEntry(path, current_dir)
            current_dir.sub_dirs.add(dir_entry)
            self.dirs[path] = dir_entry
            return dir_entry
        else:
            return self.dirs[path]

    def __update_subdir_size(self, dir: DirEntry):
        for subdir in dir.sub_dirs:
            self.__update_subdir_size(subdir)
        if dir.parent != None:
            dir.parent.sub_dir_size += dir.total_size

    def solve_b(self, input: list[str]):
        self.__create_dirs(input)
        self.__update_subdir_size(self.dirs["/"])

        total_space = 70000000
        required_free = 30000000
        current_free = total_space - self.dirs["/"].total_size

        min_delete = None
        for dir in map(lambda x: x[1], self.dirs.items()):
            if current_free + dir.total_size > required_free:
                if min_delete == None or min_delete > dir.total_size:
                    min_delete = dir.total_size
        return min_delete


if __name__ == "__main__":
    AoCHelper(Day7Solver())\
        .test_with('a', example_input.splitlines(), 95437)\
        .test_with('b', example_input.splitlines(), 24933642)\
        .solve().submit()
