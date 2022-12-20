from aoc_helper.AoCHelper import *


class DaySolver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 20, 3, 1623178306, True)

    def solve_a(self, input: list[str]):
        return self.decrypt(input, 1, 1)

    def decrypt(self, input, dec_key, times_to_mix):
        orig_file = list((i + 1, dec_key * v) for i, v in enumerate(map(int, input)))
        file = orig_file.copy()
        length = len(orig_file)
        for mix_count in range(times_to_mix):
            for entry in orig_file:
                index = file.index(entry)
                print(f"{mix_count+1:2}/{times_to_mix}{entry[0]:4}/{length}: {entry}", end="\r")
                index += entry[1]
                index = index % (length-1)
                file.remove(entry)
                file.insert(index, entry)
        print()

        sum = 0
        index = list(map(lambda x: x[1], file)).index(0)
        for _ in range(3):
            index += 1000
            index %= length
            sum += file[index][1]
        return sum

    def solve_b(self, input: list[str]):
        return self.decrypt(input, 811589153, 10)


example_input1 = """"""

example_input2 = """"""

if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test()\
        .solve()\
        .submit()
