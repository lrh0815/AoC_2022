from aoc_helper.AoCHelper import PuzzleSolver, AoCHelper


class Day(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 5, "CMZ", "MCD", True)

    def solve_a(self, input: list[str]):
        split_input = list(map(lambda line: line.replace("    ", " [_] ").split(), input))
        num_stacks = len(split_input[0])
        moves = []
        stacks = list(map(lambda x: [], range(0, num_stacks)))
        for line in split_input:
            if len(line) == 0:
                continue
            if line[0] == "1":
                continue
            if line[0] == "move":
                moves.append((int(line[1]), int(line[3])-1, int(line[5])-1))
            else:
                self.__add_to_stacks(stacks, line)
        
        self.__perform_moves(stacks, moves)
        answer = "".join(map(lambda x: x[0], stacks))
        return answer

    def __add_to_stacks(self, stacks, line):
        for i in range(0, len(line)):
            if line[i][1] != "_":
                stacks[i].append(line[i][1])

    def __perform_moves(self, stacks, moves):
        for move in moves:
            for i in range(0, move[0]):
                self.__move(stacks[move[1]], stacks[move[2]])

    def __move(self, source_stack: list, target_stack: list):
        element = source_stack[0]
        source_stack.remove(element)
        target_stack.insert(0, element)

    def solve_b(self, input: list[str]):
        split_input = list(map(lambda line: line.replace("    ", " [_] ").split(), input))
        num_stacks = len(split_input[0])
        moves = []
        stacks = list(map(lambda x: [], range(0, num_stacks)))
        for line in split_input:
            if len(line) == 0:
                continue
            if line[0] == "1":
                continue
            if line[0] == "move":
                moves.append((int(line[1]), int(line[3])-1, int(line[5])-1))
            else:
                self.__add_to_stacks(stacks, line)
        
        self.__perform_moves_b(stacks, moves)
        answer = "".join(map(lambda x: x[0], stacks))
        return answer

    def __perform_moves_b(self, stacks, moves):
        for move in moves:
            self.__move_b(move[0], stacks[move[1]], stacks[move[2]])

    def __move_b(self, num: int, source_stack: list, target_stack: list):
        elements = source_stack[:num].copy()
        for element in elements:
            source_stack.remove(element)
        elements.reverse()
        for element in elements:
            target_stack.insert(0, element)


if __name__ == "__main__":
    AoCHelper(Day()).test().solve().submit()
