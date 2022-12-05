from aoc_helper.AoCHelper import PuzzleSolver, AoCHelper


class Day(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 5, "CMZ", "MCD", True)

    def __decode_input(self, input):
        split_input = list(map(lambda line: line.replace("    ", " [_] ").split(), input))
        num_stacks = len(split_input[0])
        moves = []
        stacks = list(map(lambda x: [], range(0, num_stacks)))
        for line in split_input:
            if len(line) == 0 or line[0] == "1":
                continue
            if line[0] == "move":
                moves.append((int(line[1]), int(line[3])-1, int(line[5])-1))
            else:
                self.__add_to_stacks(stacks, line)
        return moves,stacks

    def __add_to_stacks(self, stacks, line):
        for i in range(0, len(line)):
            if line[i][1] != "_":
                stacks[i].append(line[i][1])

    def __perform_moves(self, stacks, moves, move_operation):
        for move in moves:
            move_operation(move[0], stacks[move[1]], stacks[move[2]])
    
    def solve_a(self, input: list[str]):
        moves, stacks = self.__decode_input(input)
        self.__perform_moves(stacks, moves, self.__move_one_create_at_a_time)
        answer = "".join(map(lambda x: x[0], stacks))
        return answer

    def __move_one_create_at_a_time(self, num: int, source_stack: list, target_stack: list):
            for i in range(0, num):
                element = source_stack[0]
                source_stack.remove(element)
                target_stack.insert(0, element)

    def solve_b(self, input: list[str]):
        moves, stacks = self.__decode_input(input)
        self.__perform_moves(stacks, moves, self.__move_all_crates_together)
        answer = "".join(map(lambda x: x[0], stacks))
        return answer

    def __move_all_crates_together(self, num: int, source_stack: list, target_stack: list):
        elements = source_stack[:num].copy()
        for element in elements:
            source_stack.remove(element)
        elements.reverse()
        for element in elements:
            target_stack.insert(0, element)


if __name__ == "__main__":
    AoCHelper(Day()).test().solve().submit()
