from aoc_helper.AoCHelper import *
import re
from dataclasses import dataclass
from icecream import ic
from collections import deque
from rich import print
from rich.progress import track
from rich.status import Status


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

        minutes_left = 30
        total_flow = 0
        visited = {}
        queue = deque()

        queue.append(("AA", 30, 0, frozenset()))

        status = Status(f"Queue {len(queue)}")
        status.start()
        while len(queue) > 0:
            status.update(f"Queue {len(queue)}")
            current_valve, minutes_left, total_flow, open_valves = queue.pop()
            for next_valve in [v for v in flow_valves if v not in open_valves]:
                next_minutes_left = minutes_left - distances[current_valve][next_valve] - 1
                if next_minutes_left <= 0:
                    continue
                next_open_valves = open_valves.union([next_valve])
                next_total_flow = total_flow + flow_valves[next_valve].flow_rate * next_minutes_left
                if visited.get(next_open_valves, 0) < next_total_flow:
                    visited[next_open_valves] = next_total_flow
                    queue.append((next_valve, next_minutes_left, next_total_flow, next_open_valves))
        status.stop()
        answer = max(visited.values())
        return answer

    def solve_b(self, input: list[str]):
        return None


if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test()\
        .solve().submit()
