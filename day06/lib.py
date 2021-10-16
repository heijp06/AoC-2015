from functools import partial
from parsec import ParseError, digit, generate, many1, string


def part1(rows):
    grid = [[0] * 1000 for _ in range(1000)]
    for row in rows:
        f = parse(row)
        f(grid)
    return sum(sum(row) for row in grid)


def part2(rows):
    pass


def parse(row):
    try:
        return rule.parse_strict(row)
    except ParseError as err:
        raise ValueError(err)


@generate
def rule():
    return (yield turn_on ^ turn_off ^ toggle)


@generate
def turn_on():
    rect = yield string("turn on ") >> rectangle
    return partial(set, rect, 1)


@generate
def turn_off():
    rect = yield string("turn off ") >> rectangle
    return partial(set, rect, 0)


@generate
def toggle():
    rect = yield string("toggle ") >> rectangle
    return partial(invert, rect)


@generate
def rectangle():
    p1 = yield point
    yield string(" through ")
    p2 = yield point
    return (p1, p2)


@generate
def point():
    n1 = yield number
    yield string(",")
    n2 = yield number
    return (int(n1), int(n2))


@generate
def number():
    digits = yield many1(digit())
    return int("".join(digits))


def set(rect, value, grid):
    ((x0, y0), (x1, y1)) = rect
    for x in range(x0, x1+1):
        for y in range(y0, y1+1):
            grid[x][y] = value

def invert(rect, grid):
    ((x0, y0), (x1, y1)) = rect
    for x in range(x0, x1+1):
        for y in range(y0, y1+1):
            grid[x][y] = 1 - grid[x][y]
