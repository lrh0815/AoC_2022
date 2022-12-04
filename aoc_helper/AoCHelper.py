from aocd.models import Puzzle
from colorama import Fore
from abc import ABC, abstractmethod


class PuzzleSolver(ABC):
    def __init__(self, year: int, day: int, example_answer_a, example_answer_b, do_submit: bool):
        self.year = year
        self.day = day
        self.example_answers = {'a': example_answer_a, 'b': example_answer_b}
        self.solvers = {'a': self.solve_a, 'b': self.solve_b}
        self.do_submit = do_submit

    @abstractmethod
    def solve_a(self, input: list[str]):
        pass

    @abstractmethod
    def solve_b(self, input: list[str]):
        pass


class AoCHelper(object):

    def __init__(self, puzzle_solver: PuzzleSolver):
        self.puzzle = Puzzle(puzzle_solver.year, puzzle_solver.day)
        self.puzzle_solver = puzzle_solver
        self.test_results = {'a': None, 'b': None}
        self.solutions = {'a': None, 'b': None}
        self.submitters = {'a': self.__submit_a, 'b': self.__submit_b}

    def with_expected_a(self, expected_answer):
        self.expected_answers['a'] = expected_answer
        return self

    def with_expected_b(self, expected_answer):
        self.expected_answers['b'] = expected_answer
        return self

    def print_input(self):
        print(self.puzzle.input_data)
        return self

    def print_example_input(self):
        print(self.puzzle.example_data)
        return self

    def __get_parts(self, part):
        if part == None:
            parts = ['a', 'b']
        else:
            parts = [part]
        return parts

    def test(self, part=None):
        print()
        for part in self.__get_parts(part):
            self.test_results[part] = self.__test_for_part(part)
        return self

    def __test_for_part(self, part):
        print(f'Test {part}: ', end='')
        return self.__test(self.puzzle_solver.solvers[part], self.puzzle_solver.example_answers[part])

    def __test(self, solver, expected_answer):
        if solver != None and expected_answer != None:
            answer = solver(self.puzzle.example_data.splitlines())
            if answer == expected_answer:
                print(Fore.GREEN + 'PASSED' + Fore.RESET)
                return True
            else:
                print(Fore.RED + 'FAILED' + Fore.RESET +
                      f' (expected {expected_answer} but was {answer})')
                return False
        else:
            print(Fore.YELLOW + 'IGNORED' + Fore.RESET)
            return None

    def solve(self, part=None):
        print()
        for part in self.__get_parts(part):
            self.solutions[part] = self.__solve_for_part(part)
        return self

    def __solve_for_part(self, part):
        print(f'Solve {part}: ', end='')
        return self.__solve(self.test_results[part], self.puzzle_solver.solvers[part])

    def __solve(self, test_result: bool, solver):
        if test_result == False:
            print(Fore.RED + 'test failed' + Fore.RESET)
        elif test_result == None:
            print(Fore.YELLOW + 'not tested' + Fore.RESET)
        elif solver == None:
            print(Fore.YELLOW + 'no solver' + Fore.RESET)
        else:
            answer = solver(self.puzzle.input_data.splitlines())
            print(f'{answer}')
            return answer
        return None

    def submit(self, part=None):
        print()
        for part in self.__get_parts(part):
            self.__submit_for_part(part)
        return self

    def __submit_for_part(self, part):
        print(f'Submit {part}: ', end='')
        self.__submit(self.solutions[part], self.submitters[part])

    def __submit(self, solution, submitter):
        if solution == None:
            print(Fore.RED + 'not solved')
        elif self.puzzle_solver.do_submit == True:
            print(solution)
            submitter(solution)
        else:
            print(f'{solution} ' + Fore.CYAN + 'not submitted')

    def __submit_a(self, solution):
        self.puzzle.answer_a = solution

    def __submit_b(self, solution):
        self.puzzle.answer_b = solution
