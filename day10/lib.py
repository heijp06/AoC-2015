from itertools import groupby


def part1(string):
    return length(string, 40)


def part2(string):
    return length(string, 50)


def length(string, times):
    for _ in range(times):
        string = transform(string)
    return len(string)


def transform(string):
    return "".join(
        str(len(list(group))) + char
        for char, group
        in groupby(string)
    )
