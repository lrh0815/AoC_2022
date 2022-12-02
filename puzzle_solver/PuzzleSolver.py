from aocd.models import Puzzle
from colorama import Fore, Back, Style

class PuzzleSolver(object):

    def __init__(self, day, solver_a = None, solver_b = None):
        self.puzzle = Puzzle(2022, day)
        self.solver_a = solver_a
        self.solver_b = solver_b

    def print_input(self):
        print(self.puzzle.input_data)

    def print_example_input(self):
        print(self.puzzle.example_data)

    def solve(self, do_submit = False):
        self._solve('a', self.solver_a, do_submit)
        self._solve('b', self.solver_b, do_submit)

    def _solve(self, part, solver, do_submit):
        if solver != None:
            answer = solver(self.puzzle.input_data)
            print(f'Answer {part}: {answer}')
            if do_submit == True and answer != None:
                self.puzzle.answer_b = answer


    def test(self, expected_answer_a = None, expected_answer_b = None):
        self._test('a', self.solver_a, expected_answer_a)
        self._test('b', self.solver_b, expected_answer_b)

    def _test(self, part, solver, expected_answer):
        if solver != None and expected_answer != None:
            answer = solver(self.puzzle.example_data)
            if answer == expected_answer:
                print(f'Solver {part} ' + Fore.GREEN + 'PASSED' + Fore.RESET)
            else:
                print(f'Solver {part} ' + Fore.RED + 'FAILED' + Fore.RESET + f': Expected {expected_answer} but was {answer}')

            
