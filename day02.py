from puzzle_solver.PuzzleSolver import PuzzleSolver

shape_scores = {
    "A" : 1,
    "B" : 2,
    "C" : 3
}

result_scores = {
    "A A" : 3,
    "B B" : 3,
    "C C" : 3,
    "A B" : 6,
    "B C" : 6,
    "C A" : 6,
    "A C" : 0,
    "B A" : 0,
    "C B" : 0,
}

def get_own_shape_a(round):
    own_shape_dict = {
        "X" : "A",
        "Y" : "B",
        "Z" : "C"
    }
    return own_shape_dict[round[1]]

def get_own_shape_b(round):
    own_shape_dict = {
        "X" : { "A" : "C", "B" : "A", "C" : "B" },
        "Y" : { "A" : "A", "B" : "B", "C" : "C" },
        "Z" : { "A" : "B", "B" : "C", "C" : "A" }
    }
    return own_shape_dict[round[1]][round[0]]


def calculate_score(round, own_shape_getter):
    opponent_shape = round[0]
    own_shape = own_shape_getter(round)

    shape_score = shape_scores[own_shape]
    result_score = result_scores[f"{opponent_shape} {own_shape}"]

    return shape_score + result_score


def solve(input, own_shape_getter):
    total_score = 0
    for line in input.splitlines():
        score = calculate_score(line.split(), own_shape_getter)
        total_score += score
    
    return total_score


def solve_a(input):
    return solve(input, get_own_shape_a)


def solve_b(input):
    return solve(input, get_own_shape_b)


if __name__ == "__main__":
    ps = PuzzleSolver(2, solve_a, solve_b)
    ps.test(15, 12)
    ps.solve()
