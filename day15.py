from aoc_helper.AoCHelper import *
import re

class DaySolver(PuzzleSolver):
    def __init__(self):
        PuzzleSolver.__init__(self, 2022, 15, 26, 56000011, True)

    def __read_input(self, input: list[str]):
        self.grid = Grid(".")
        self.sensors = []
        for line in input:
            match = re.search("Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)
            sensor = Point(int(match.group(1)), int(match.group(2)))
            beacon = Point(int(match.group(3)), int(match.group(4)))
            delta_x = abs(beacon.x - sensor.x)
            delta_y = abs(beacon.y - sensor.y)
            radius = delta_x + delta_y
            self.sensors.append((sensor, radius))
            # for point in self.__sensor_edge(self.sensors[-1]):
            #     self.grid.set(point, "*")
            self.grid.set(sensor, "S")
            self.grid.set(beacon, "B")

    def solve_a(self, input: list[str]):
        self.__read_input(input)
        y = 10 if self.grid.max_y() < 100 else 2000000
        print()
        cov = {x for sensor_index in range(len(self.sensors)) for x in self.__sensor_line_coverage(sensor_index, y) if self.grid.get(Point(x, y)) != "B"}
        return len(cov)

    def __sensor_line_coverage(self, sensor_index: int, line: int):
        print(f"{sensor_index}/{len(self.sensors)}")
        sensor, radius = self.sensors[sensor_index]
        line_delta = abs(line - sensor.y)
        if line_delta > radius:
            return []
        return [x for x in range(sensor.x - (radius - line_delta), sensor.x + (radius - line_delta) + 1)]

    def solve_b(self, input: list[str]):
        self.__read_input(input)
        max = 20 if self.grid.max_y() < 100 else 4000000
        print()
        for i in range(len(self.sensors)):
            print(f"{i}/{len(self.sensors)}")
            distress_beacon = self.__check_sensor(max, i)
            if distress_beacon != None:
                break
        print(distress_beacon)
        tuning_freq = distress_beacon.x * 4000000 + distress_beacon.y
        return tuning_freq

    def __check_sensor(self, max: int, sensor_index: int):
        for point in self.__sensor_edge(self.sensors[sensor_index]):
            if point.x < 0 or point.y < 0 or point.x > max or point.y > max:
                continue
            if self.__not_covered(point, sensor_index):
                return point
        return None

    def __sensor_edge(self, sensor_info):
        sensor = sensor_info[0]
        radius = sensor_info[1] + 1

        for delta_y in range(0, radius + 1):
            delta_x = radius - delta_y
            yield Point(sensor.x - delta_x, sensor.y - delta_y)
            yield Point(sensor.x + delta_x, sensor.y - delta_y)
            yield Point(sensor.x - delta_x, sensor.y + delta_y)
            yield Point(sensor.x + delta_x, sensor.y + delta_y)

    def __not_covered(self, point, sensor_index):
        for i in range(len(self.sensors)):
            if i == sensor_index:
                continue
            sensor, radius = self.sensors[i]
            delta_x = abs(sensor.x - point.x)
            delta_y = abs(sensor.y - point.y)
            if delta_x + delta_y <= radius:
                return False
        return True


example_input1 = """"""

example_input2 = """"""

if __name__ == "__main__":
    AoCHelper(DaySolver())\
        .test().solve().submit()
