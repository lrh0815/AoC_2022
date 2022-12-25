from aoc_helper.AoCHelper import *

sanfu_to_int_value = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
int_to_snafu_value = {0: "0", 1: "1", 2: "2", 3: "=", 4: "-"}


class DaySolver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 25, "2=-1=0", None, True)

    def solve_a(self, input: list[str]):
        decimal_sum = 0
        for snafu in input:
            decimal = self.__from_snafu(snafu)
            decimal_sum += decimal

        snafu_sum = self.__to_snafu(decimal_sum)
        return snafu_sum

    def __from_snafu(self, snafu: str) -> int:
        decimal = 0
        for i, digit in enumerate(snafu[::-1]):
            digit_value = (5 ** i) * sanfu_to_int_value[digit]
            decimal += digit_value
        return decimal

    def __to_snafu(self, decimal: int) -> str:
        digits = []
        while decimal > 0:
            remainder = decimal % 5
            digits.insert(0, int_to_snafu_value[remainder])
            decimal //= 5
            if remainder > 2:
                decimal += 1

        return "".join(digits)

    def solve_b(self, input: list[str]):
        return None


if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test()\
        .solve().submit()
