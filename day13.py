from aoc_helper.AoCHelper import *
from functools import cmp_to_key


def compare(left_list: list, right_list: list):
    for i in range(len(left_list)):
        if i >= len(right_list):
            return 1

        left = left_list[i]
        right = right_list[i]

        left_is_int = type(left) is int
        right_is_int = type(right) is int

        if left_is_int and right_is_int:
            if left < right:
                return -1
            if left > right:
                return 1
        else:
            if left_is_int:
                result = compare([left], right)
            elif right_is_int:
                result = compare(left, [right])
            else:
                result = compare(left, right)
            if result != 0:
                return result

    if len(left_list) < len(right_list):
        return -1
    else:
        return 0


class DaySolver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 13, 13, 140, True)

    def solve_a(self, input: list[str]):
        packet_pairs = [(eval(x[0]), eval(x[1])) for x in chunk_input(input, 3)]

        answer = 0
        for index, packet_pair in enumerate(packet_pairs):
            if compare(packet_pair[0], packet_pair[1]) == -1:
                answer += (index + 1)
        return answer

    def solve_b(self, input: list[str]):
        packets = []
        for line in input:
            if line.strip() != "":
                packets.append(eval(line))

        divider_packet_1 = [[2]]
        divider_packet_2 = [[6]]
        packets.append(divider_packet_1)
        packets.append(divider_packet_2)

        packets.sort(key=cmp_to_key(compare))
        divider_packet_1_index = packets.index(divider_packet_1) + 1
        divider_packet_2_index = packets.index(divider_packet_2) + 1
        return divider_packet_1_index * divider_packet_2_index


example_input1 = """"""

example_input2 = """"""

if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test().solve()
