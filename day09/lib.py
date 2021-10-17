from itertools import permutations
import re


def part1(rows):
    travel = Travel(rows)
    return travel.route()


def part2(rows):
    travel = Travel(rows)
    return travel.route(max)


class Travel:
    def __init__(self, rows):
        self.destinations = set()
        self.distances = {}
        for row in rows:
            self.parse_row(row)

    def parse_row(self, row):
        match = re.match(r"(.*) to (.*) = (.*)", row)
        start, end, distance = match.groups()
        self.destinations.add(start)
        self.destinations.add(end)
        self.distances[start, end] = int(distance)
        self.distances[end, start] = int(distance)

    def route(self, optimum=min):
        return optimum(
            sum(self.distances[hop]
                for hop in zip(permutation, permutation[1:]))
            for permutation in permutations(self.destinations)
        )
