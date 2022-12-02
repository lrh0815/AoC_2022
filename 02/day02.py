from aocd.models import Puzzle

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

def get_own_shape_a(shapes):
    own_shape_dict = {
        "X" : "A",
        "Y" : "B",
        "Z" : "C"
    }
    return own_shape_dict[shapes[1]]

def get_own_shape_b(shapes):
    own_shape_dict = {
        "X" : { "A" : "C", "B" : "A", "C" : "B" },
        "Y" : { "A" : "A", "B" : "B", "C" : "C" },
        "Z" : { "A" : "B", "B" : "C", "C" : "A" }
    }
    return own_shape_dict[shapes[1]][shapes[0]]


def calculate_score(round, own_shape_getter):
    shapes = round.split(" ")

    opponent_shape = shapes[0]
    own_shape = own_shape_getter(shapes)

    shape_score = shape_scores[own_shape]
    result_score = result_scores[f"{opponent_shape} {own_shape}"]

    return shape_score + result_score


def solve(puzzle : Puzzle, own_shape_getter):
    total_score = 0
    for round in puzzle.input_data.splitlines():
        score = calculate_score(round, own_shape_getter)
        total_score += score
    
    return total_score


def solve_a(puzzle : Puzzle):
    return solve(puzzle, get_own_shape_a)


def solve_b(puzzle : Puzzle):
    return solve(puzzle, get_own_shape_b)

if __name__ == "__main__":
    submit_answers = False

    puzzle = Puzzle(year=2022, day=2)

    answer_a = solve_a(puzzle)
    answer_b = solve_b(puzzle)

    print()
    if submit_answers:
        print("Submitting answers...")
        if answer_a != "?":
            puzzle.answer_a = answer_a

        if answer_b != "?":
            puzzle.answer_b = answer_b
    else:
        print("Answers not submitted:")
        print(answer_a)
        print(answer_b)

