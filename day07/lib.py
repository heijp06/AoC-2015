from functools import cache
from parsec import ParseError, digit, letter, generate, many, many1, none_of, regex, string


def part1(rows):
    circuit = Circuit(rows)
    return circuit.value("a")


def part2(rows):
    circuit = Circuit(rows)
    a = circuit.value("a")
    return circuit.value("a", a)

class Circuit:
    def __init__(self, rows):
        self._gates = dict(
            gate.parse_strict(row)
            for row
            in rows
        )

    @cache
    def value(self, name, a = None):
        if a and name == "b":
            return a
        f, args = self._gates[name]
        return f(*(self.value(arg, a) for arg in args))


@generate
def gate():
    f, args = (
        yield and_gate
        ^ or_gate
        ^ lshift_gate
        ^ rshift_gate
        ^ not_gate
        ^ odd_gate
        ^ copy_gate
        ^ const_gate
    )
    yield string(" -> ")
    n = yield identifier
    return n, (f, args)


@generate
def const_gate():
    value = yield number
    return lambda: value, []


@generate
def and_gate():
    op1 = yield identifier
    yield string(" AND ")
    op2 = yield identifier
    return lambda a, b: a & b, [op1, op2]


@generate
def or_gate():
    op1 = yield identifier
    yield string(" OR ")
    op2 = yield identifier
    return lambda a, b: a | b, [op1, op2]


@generate
def lshift_gate():
    op = yield identifier
    yield string(" LSHIFT ")
    value = yield number
    return lambda a: a << value, [op]


@generate
def rshift_gate():
    op = yield identifier
    yield string(" RSHIFT ")
    value = yield number
    return lambda a: a >> value, [op]


@generate
def not_gate():
    yield string("NOT ")
    op = yield identifier
    return lambda a: 65535 - a, [op]


@generate
def odd_gate():
    yield string("1 AND ")
    op = yield identifier
    return lambda a: 1 & a, [op]


@generate
def copy_gate():
    op = yield identifier
    return lambda a: a, [op]


@generate
def number():
    digits = yield many1(digit())
    return int("".join(digits))


@generate
def identifier():
    letters = yield many1(letter())
    return "".join(letters)