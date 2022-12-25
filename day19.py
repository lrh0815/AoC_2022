from aoc_helper.AoCHelper import *
import re
from dataclasses import dataclass


def sub(t1, t2):
    return tuple(x-y for x, y in zip(t1, t2))


def add(t1, t2):
    return tuple(x+y for x, y in zip(t1, t2))


@dataclass
class Resources(object):
    ore: Optional[int] = 0
    clay: Optional[int] = 0
    obsidian: Optional[int] = 0

    def __add__(self, other: "Resources"):
        return Resources(self.ore + other.ore, self.clay + other.clay, self.obsidian + other.obsidian)

    def __sub__(self, other: "Resources"):
        return Resources(self.ore - other.ore, self.clay - other.clay, self.obsidian - other.obsidian)

    def __mul__(self, other: int):
        return Resources(self.ore * other, self.clay * other, self.obsidian * other)

    def __lt__(self, other: int):
        return self.ore < other or self.clay < other or self.obsidian < other

    def __floordiv__(self, other: "Resources"):
        max(self.ore // other.ore, self.clay // other.clay, self.obsidian // other.obsidian)


@dataclass
class Blueprint(object):
    id: int
    ore_bot_costs: Resources
    clay_bot_costs: Resources
    obsidian_bot_costs: Resources
    geode_bot_costs: Resources

    def __post_init__(self):
        self.max_ore_cost = max(self.ore_bot_costs.ore, self.clay_bot_costs.ore, self.obsidian_bot_costs.ore, self.geode_bot_costs.ore)
        self.max_clay_cost = max(self.ore_bot_costs.clay, self.clay_bot_costs.clay, self.obsidian_bot_costs.clay, self.geode_bot_costs.clay)
        self.max_obsidian_cost = max(self.ore_bot_costs.obsidian, self.clay_bot_costs.obsidian, self.obsidian_bot_costs.obsidian, self.geode_bot_costs.obsidian)


@dataclass
class State(object):
    robots: Resources
    resources: Resources
    total_minutes: int
    minutes_used: int
    geodes: int
    geode_bots: Optional[int] = 0

    @property
    def minutes_left(self):
        return self.total_minutes - self.minutes_used

    def after_minutes(self, minutes: int):
        return State(self.robots * 1, self.resources + self.robots * minutes, self.total_minutes, self.minutes_used + minutes, self.geodes, self.geode_bots)

    def build_ore_bot(self, blueprint: Blueprint):
        self.robots.ore += 1
        self.resources -= blueprint.ore_bot_costs
        return self

    def build_clay_bot(self, blueprint: Blueprint):
        self.robots.clay += 1
        self.resources -= blueprint.clay_bot_costs
        return self

    def build_obsidian_bot(self, blueprint: Blueprint):
        self.robots.obsidian += 1
        self.resources -= blueprint.obsidian_bot_costs
        return self

    def build_geode_bot(self, blueprint: Blueprint):
        self.geode_bots += 1
        self.geodes += self.minutes_left
        self.resources -= blueprint.geode_bot_costs
        return self


class DaySolver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 19, None, None, True)

    def solve_a(self, input: list[str]):
        blueprints = [self.__read_blueprint(line) for line in input]

        qualitiy_levels = []
        for blueprint in blueprints:
            print(f"{blueprint.id:3}/{len(blueprints)}")
            num_geodes = self.__simulate_blueprint(blueprint, 24)
            quality_level = blueprint.id * num_geodes
            qualitiy_levels.append(quality_level)

        answer = sum(qualitiy_levels)
        return answer

    def __simulate_blueprint(self, blueprint: Blueprint, total_minutes: int) -> int:

        initial_state = State(Resources(1, 0, 0), Resources(0, 0, 0), total_minutes, 0, 0)
        queue = [initial_state]

        max_geode_state = initial_state
        while len(queue) > 0:
            state = queue.pop(0)
            if max_geode_state.geodes < state.geodes:
                max_geode_state = state
            print(f"{len(queue):5}: {state} {max_geode_state.geodes} ", end="\r")
            if state.geodes + (state.minutes_left * (state.minutes_left - 1) / 2) < max_geode_state.geodes:
                continue
            if state.minutes_left > 2:
                if state.robots.ore >= blueprint.geode_bot_costs.ore and state.robots.obsidian >= blueprint.geode_bot_costs.obsidian:
                    next_state = state.after_minutes(0)
                    while next_state.minutes_left > 0:
                        next_state = next_state.after_minutes(1).build_geode_bot(blueprint)
                    queue.append(next_state)
                else:
                    if state.robots.obsidian > 0:
                        next_state = state.after_minutes(0)
                        while next_state.resources - blueprint.geode_bot_costs < 0 and next_state.minutes_left > 1:
                            next_state = next_state.after_minutes(1)
                        next_state = next_state.after_minutes(1).build_geode_bot(blueprint)
                        queue.append(next_state)
                    if state.robots.obsidian < blueprint.max_obsidian_cost and state.robots.clay > 0:
                        next_state = state.after_minutes(0)
                        while next_state.resources - blueprint.obsidian_bot_costs < 0 and next_state.minutes_left > 1:
                            next_state = next_state.after_minutes(1)
                        next_state = next_state.after_minutes(1).build_obsidian_bot(blueprint)
                        queue.append(next_state)
                    if state.robots.clay < blueprint.max_clay_cost:
                        next_state = state.after_minutes(0)
                        while next_state.resources - blueprint.clay_bot_costs < 0 and next_state.minutes_left > 1:
                            next_state = next_state.after_minutes(1)
                        next_state = next_state.after_minutes(1).build_clay_bot(blueprint)
                        queue.append(next_state)
                    if state.robots.ore < blueprint.max_ore_cost:
                        next_state = state.after_minutes(0)
                        while next_state.resources - blueprint.ore_bot_costs < 0 and next_state.minutes_left > 1:
                            next_state = next_state.after_minutes(1)
                        next_state = next_state.after_minutes(1).build_ore_bot(blueprint)
                        queue.append(next_state)
            queue.sort(key=self.__key, reverse=True)
            queue = queue[:2000]
        print()
        print(max_geode_state)
        return max_geode_state.geodes

    def __key(self, state: State):
        return state.geodes * 10000 + state.resources.obsidian * 1000 + state.resources.clay * 100 + state.resources.ore + state.minutes_left

    def __read_blueprint(self, line: str):
        id, ore_bot_ores, clay_bot_ores, obsidian_bot_ores, obsidian_bot_clay, geode_bot_ores, geode_bot_obsidian = map(int, re.findall(r"\d+", line))
        ore_bot_costs = Resources(ore_bot_ores)
        clay_bot_costs = Resources(clay_bot_ores)
        obsidian_bot_costs = Resources(obsidian_bot_ores, clay=obsidian_bot_clay)
        geode_bot_costs = Resources(geode_bot_ores, obsidian=geode_bot_obsidian)
        return Blueprint(id, ore_bot_costs, clay_bot_costs, obsidian_bot_costs, geode_bot_costs)

    def solve_b(self, input: list[str]):
        blueprints = [self.__read_blueprint(line) for line in input]

        answer = 1
        for blueprint in blueprints[:3]:
            print(f"{blueprint.id:3}/{len(blueprints)}")
            num_geodes = self.__simulate_blueprint(blueprint, 32)
            answer *= num_geodes
        return answer


example_input = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""

if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test_with('a', example_input.splitlines(), 33)\
        .test_with('b', example_input.splitlines(), 55 * 61)\
        .solve().submit()
