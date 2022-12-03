from aocd.models import Puzzle
from colorama import Fore


class PuzzleSolver(object):

    def __init__(self, year: int, day: int, solver_a, solver_b, debug: bool = False):
        self.debug = debug
        self.puzzle = Puzzle(year, day)
        self.solvers = {'a': solver_a, 'b': solver_b}
        self.expected_answers = {'a': None, 'b': None}
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
        return self.__test(self.solvers[part], self.expected_answers[part])

    def __test(self, solver, expected_answer):
        if solver != None and expected_answer != None:
            answer = solver(self.puzzle.example_data)
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
        return self.__solve(self.test_results[part], self.solvers[part])

    def __solve(self, test_result: bool, solver):
        if test_result == False:
            print(Fore.RED + 'test failed' + Fore.RESET)
        elif test_result == None:
            print(Fore.YELLOW + 'not tested' + Fore.RESET)
        elif solver == None:
            print(Fore.YELLOW + 'no solver' + Fore.RESET)
        else:
            answer = solver(self.puzzle.input_data)
            print(f'{answer}')
            return answer
        return None

    def submit(self, part=None, do_submit: bool = False):
        print()
        for part in self.__get_parts(part):
            self.__submit_for_part(part, do_submit)
        return self

    def __submit_for_part(self, part, do_submit: bool):
        print(f'Submit {part}: ', end='')
        self.__submit(do_submit, self.solutions[part], self.submitters[part])

    def __submit(self, do_submit: bool, solution, submitter):
        if solution == None:
            print(Fore.RED + 'not solved')
        elif do_submit == True:
            print(solution)
            submitter(solution)
        else:
            print(f'{solution} ' + Fore.CYAN + 'not submitted')

    def __submit_a(self, solution):
        if self.debug:
            print(Fore.MAGENTA + f'_submit_a {solution}' + Fore.RESET)
        else:
            self.puzzle.answer_a = solution

    def __submit_b(self, solution):
        if self.debug:
            print(Fore.MAGENTA + f'_submit_b {solution}' + Fore.RESET)
        else:
            self.puzzle.answer_b = solution
