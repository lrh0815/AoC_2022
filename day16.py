from aoc_helper.AoCHelper import *
import re
from dataclasses import dataclass
from icecream import ic
from collections import deque
from rich import print
from rich.progress import track
from rich.status import Status
from itertools import chain, combinations


@dataclass(frozen=True)
class Valve(object):
    name: str
    flow_rate: int
    neighbors: list[str]


class DaySolver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 16, 1651, 1707, True)

    def __read_input(self, input: list[str]) -> dict[str, Valve]:
        valves = {}
        pattern = re.compile(r"Valve (..) has flow rate=(.+); tunnels? leads? to valves? (.+)")

        for line in input:
            valve_name, flow_rate, neighbors = pattern.findall(line)[0]
            valves[valve_name] = Valve(valve_name, int(flow_rate), neighbors.split(", "))

        return valves

    def __get_min_distances(self, valves: dict[str, Valve]) -> dict[str, dict[str, int]]:
        distances = {x: {y: 1 if y in valves[x].neighbors else float("inf") for y in valves} for x in valves}

        for k in distances:
            for i in distances:
                for j in distances:
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

        return distances

    def solve_a(self, input: list[str]):
        all_valves = self.__read_input(input)
        distances = self.__get_min_distances(all_valves)
        flow_valves = {valve.name: valve for valve in all_valves.values() if valve.flow_rate > 0}

        answer = self.__find_max_released_pressure(30, distances, flow_valves, flow_valves.keys())
        return answer

    def __find_max_released_pressure(self, remaining_minutes, distances, flow_valves: dict[str, Valve], valve_subset):
        visited = {}
        queue = deque([("AA", remaining_minutes, 0, frozenset())])

        while len(queue) > 0:
            current_valve, minutes_left, released_pressure, open_valves = queue.pop()
            for next_valve in [v for v in valve_subset if v not in open_valves]:
                next_minutes_left = minutes_left - distances[current_valve][next_valve] - 1
                if next_minutes_left <= 0:
                    continue
                next_open_valves = open_valves.union([next_valve])
                next_released_pressure = released_pressure + flow_valves[next_valve].flow_rate * next_minutes_left
                if visited.get(next_open_valves, 0) < next_released_pressure:
                    visited[next_open_valves] = next_released_pressure
                    queue.append((next_valve, next_minutes_left, next_released_pressure, next_open_valves))
        answer = max(visited.values())
        return answer

    def solve_b(self, input: list[str]):
        all_valves = self.__read_input(input)
        distances = self.__get_min_distances(all_valves)
        flow_valves = {valve.name: valve for valve in all_valves.values() if valve.flow_rate > 0}

        all_flow_valves = set(flow_valves.keys())

        subsets = list(chain.from_iterable(combinations(flow_valves, r) for r in range(1, len(flow_valves) + 1)))
        num_subsets = len(subsets)

        status = Status(f"Find released pressure per subset")
        status.start()

        released_pressures = {}
        for i, subset in enumerate(subsets):
            status.update(f"Find released pressure per subset {i+1}/{num_subsets}")
            if len(subset) == len(all_flow_valves):
                continue
            max_release_pressure = self.__find_max_released_pressure(26, distances, flow_valves, subset)
            key = "".join(sorted(subset))
            released_pressures[key] = max_release_pressure

        max_combined_released_pressure = 0
        for i, subset in enumerate(subsets):
            status.update(f"Find max released pressure per combination {i+1}/{num_subsets}")
            if len(subset) == len(all_flow_valves):
                continue
            complement_key = "".join(sorted(all_flow_valves.difference(subset)))
            subset_key = "".join(sorted(subset))
            combined_released_pressure = released_pressures[subset_key] + released_pressures[complement_key]
            if max_combined_released_pressure < combined_released_pressure:
                max_combined_released_pressure = combined_released_pressure
        status.stop()

        return max_combined_released_pressure


if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test()\
        .solve().submit()
