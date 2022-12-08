from aoc_helper.AoCHelper import PuzzleSolver, AoCHelper


class Day8Solver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 8, 21, 8, True)

    def solve_a(self, input: list[str]):
        self.grid = list(map(lambda y: list(map(lambda x: int(x), y)), input))

        num_visible = 0
        for i in range(0, len(self.grid[0])):
            for j in range(0, len(self.grid)):
                if self.__is_visible(i, j):
                    num_visible += 1
        return num_visible

    def __is_visible(self, i, j):
        max_height = self.grid[j][i]
        visible = True
        for k in range(0, len(self.grid[0])):
            if k > i:
                if self.grid[j][k] >= max_height:
                    visible = False
                    break
        if not visible:
            visible = True
            for k in range(len(self.grid[0]), 0, -1):
                if k - 1 < i:
                    if self.grid[j][k-1] >= max_height:
                        visible = False
                        break
        if not visible:
            visible = True
            for k in range(0, len(self.grid)):
                if k > j:
                    if self.grid[k][i] >= max_height:
                        visible = False
                        break
        if not visible:
            visible = True
            for k in range(len(self.grid), 0, -1):
                if k - 1 < j:
                    if self.grid[k-1][i] >= max_height:
                        visible = False
                        break
        return visible

    def solve_b(self, input: list[str]):
        self.grid = list(map(lambda y: list(map(lambda x: int(x), y)), input))

        max_score = 0
        for i in range(0, len(self.grid[0])):
            for j in range(0, len(self.grid)):
                score = self.__get_score(i, j)
                if score > max_score:
                    max_score = score
        return max_score

    def __get_score(self, i, j):
        max_height = self.grid[j][i]
        score1 = 0
        for k in range(0, len(self.grid[0])):
            if k > i:
                score1 += 1
                if self.grid[j][k] >= max_height:
                    break
        score2 = 0
        for k in range(len(self.grid[0]), 0, -1):
            if k - 1 < i:
                score2 += 1
                if self.grid[j][k-1] >= max_height:
                    break
        score3 = 0
        for k in range(0, len(self.grid)):
            if k > j:
                score3 += 1
                if self.grid[k][i] >= max_height:
                    break
        score4 = 0
        for k in range(len(self.grid), 0, -1):
            if k - 1 < j:
                score4 += 1
                if self.grid[k-1][i] >= max_height:
                    break
        return score1 * score2 * score3 * score4


if __name__ == "__main__":
    AoCHelper(Day8Solver())\
        .test().solve().submit()
