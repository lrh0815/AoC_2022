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

    def test_with(self, part, input: list[str], expected_answer):
        print()
        self.__test_for_part(part, input, expected_answer)
        return self

    def test(self, part=None):
        print()
        input = self.puzzle.example_data.splitlines()
        for part in self.__get_parts(part):
            self.__test_for_part(part, input, self.puzzle_solver.example_answers[part])
        return self

    def __test_for_part(self, part, input, expected_answer):
        print(f'Test {part}: ', end='')
        result = self.__test(self.puzzle_solver.solvers[part], input, expected_answer)
        if self.test_results[part] == None:
            self.test_results[part] = result
        else:
            self.test_results[part] = self.test_results[part] and result

    def __test(self, solver, input, expected_answer):
        if solver != None and expected_answer != None:
            answer = solver(input)
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
