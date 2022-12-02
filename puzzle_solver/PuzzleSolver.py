from aocd.models import Puzzle
from colorama import Fore

class PuzzleSolver(object):

    def __init__(self, day, expected_answer_a = None, solver_a = None, expected_answer_b = None, solver_b = None):
        self.puzzle = Puzzle(2022, day)
        self.solvers = { 'a' : solver_a, 'b' : solver_b }
        self.expected_answers = {'a' : expected_answer_a, 'b' : expected_answer_b }

    def print_input(self):
        print(self.puzzle.input_data)

    def print_example_input(self):
        print(self.puzzle.example_data)

    def solve(self, part = None, do_submit = False):
        for part in self._get_parts(part):
            if self._test(part):
                self._solve(part, do_submit)
            print()
        return self

    def _get_parts(self, part):
        if part == None:
            parts = {'a', 'b'}
        else:
            parts = {'a'}
        return parts

    def _solve(self, part, do_submit):
        solver = self.solvers[part]
        if solver != None:
            answer = solver(self.puzzle.input_data)
            print(f'Answer {part}: {answer}')
            if do_submit == True and answer != None:
                self.puzzle.answer_b = answer
            else:
                print(Fore.CYAN + 'Not submitted' + Fore.RESET)


    def test(self, part = None):
        for part in self._get_parts(part):
            self._test(part)
            print()
        return self

    def _test(self, part):
        print(f'Solver {part}: ', end='')
        solver = self.solvers[part]
        expected_answer = self.expected_answers[part]
        if solver != None and expected_answer != None:
            answer = solver(self.puzzle.example_data)
            if answer == expected_answer:
                print(Fore.GREEN + 'PASSED' + Fore.RESET)
                return True
            else:
                print(Fore.RED + 'FAILED' + Fore.RESET + f'(expected {expected_answer} but was {answer})')
                return False
        else:
            print(Fore.YELLOW + 'IGNORED' + Fore.RESET)
            return False

            
