import re
from math import prod


def part1(rows):
    return calculate(rows)


def part2(rows):
    return calculate(rows, 500)


def calculate(rows, calories=None):
    ingredients = [[int(s) for s in re.findall("-?\d+", row)]
                   for row in rows]
    properties = list(map(list, zip(*ingredients)))
    result = 0

    for amounts in choices(len(ingredients), 100):
        product = 1
        for property in properties[:-1]:
            product *= score(amounts, property)
        if product > result and (not calories or calories == score(amounts, properties[-1])):
            result = product

    return result


def score(amounts, property):
    return max(0, sum(amount * ingredient for amount, ingredient in zip(amounts, property)))


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
