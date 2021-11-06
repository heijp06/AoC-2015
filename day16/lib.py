import re
import operator


def part1(rows):
    for i in range(len(rows)):
        if all(
                int(m.group(2)) == ticker_tape[m.group(1)][0]
                for m
                in re.finditer("([a-z]+): (\d+)", rows[i])
            ):
            return i+1


def part2(rows):
    for i in range(len(rows)):
        if all(
                ticker_tape[m.group(1)][1](int(m.group(2)), ticker_tape[m.group(1)][0])
                for m
                in re.finditer("([a-z]+): (\d+)", rows[i])
            ):
            return i+1


ticker_tape = {
    "children": (3, operator.eq),
    "cats": (7, operator.gt),
    "samoyeds": (2, operator.eq),
    "pomeranians": (3, operator.lt),
    "akitas": (0, operator.eq),
    "vizslas": (0, operator.eq),
    "goldfish": (5, operator.lt),
    "trees": (3, operator.gt),
    "cars": (2, operator.eq),
    "perfumes": (1, operator.eq)
}
