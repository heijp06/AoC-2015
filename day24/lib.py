from itertools import permutations
from math import prod


def part1(rows):
    return go(rows, 508, 6)


def part2(rows):
    return go(rows, 381, 5)


def go(rows, weight, group_size):
    qe = None
    for group in permutations(rows, group_size):
        if sum(group) == weight and (not qe or prod(group) < qe):
            qe = prod(group)
    return qe
