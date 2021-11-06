import re
from math import prod


def part1(rows):
    ingredients = [[int(s) for s in re.findall("-?\d+", row)][:-1]
                   for row in rows]
    properties = list(map(list, zip(*ingredients)))
    result = 0

    for amounts in choices(len(ingredients), 100):
        product = 1
        for property in properties:
            score = max(0, sum(amount * ingredient for amount, ingredient in zip(amounts, property)))
            product *= score
        if product > result:
            result = product

    return result


def choices(length, maximum):
    items = [[]]

    for index in range(length):
        current = []
        for item in items:
            if index == length - 1:
                yield item + [maximum - sum(item)]
            else:
                for to_add in range(maximum - sum(item) + 1):
                    current.append(item + [to_add])
        items = current


def part2(rows):
    pass
