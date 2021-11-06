import re


def part1(rows):
    for i in range(len(rows)):
        if all(ticker_tape[m.group(1)] == m.group(2) for m in re.finditer("([a-z]+): (\d+)", rows[i])):
            return i+1


def part2(rows):
    pass


ticker_tape = {
    "children": "3",
    "cats": "7",
    "samoyeds": "2",
    "pomeranians": "3",
    "akitas": "0",
    "vizslas": "0",
    "goldfish": "5",
    "trees": "3",
    "cars": "2",
    "perfumes": "1"
}
