from functools import cache
from parsec import digit, letter, generate, many1, string


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
    def value(self, op, a=None):
        if isinstance(op, int):
            return op
        if a and op == "b":
            return a
        f, args = self._gates[op]
        return f(*(self.value(arg, a) for arg in args))


@generate
def gate():
    f, args = (
        yield and_gate
        ^ or_gate
        ^ lshift_gate
        ^ rshift_gate
        ^ not_gate
        ^ const_gate
    )
    yield string(" -> ")
    n = yield identifier
    return n, (f, args)


@generate
def const_gate():
    op = yield operand
    return lambda a: a, [op]


@generate
def and_gate():
    op1 = yield operand
    yield string(" AND ")
    op2 = yield operand
    return lambda a, b: a & b, [op1, op2]


@generate
def or_gate():
    op1 = yield operand
    yield string(" OR ")
    op2 = yield operand
    return lambda a, b: a | b, [op1, op2]


@generate
def lshift_gate():
    op1 = yield operand
    yield string(" LSHIFT ")
    op2 = yield operand
    return lambda a, b: a << b, [op1, op2]


@generate
def rshift_gate():
    op1 = yield operand
    yield string(" RSHIFT ")
    op2 = yield operand
    return lambda a, b: a >> b, [op1, op2]


@generate
def not_gate():
    yield string("NOT ")
    op = yield operand
    return lambda a: 65535 - a, [op]


@generate
def operand():
    return (yield number ^ identifier)


@generate
def number():
    digits = yield many1(digit())
    return int("".join(digits))


@generate
def identifier():
    letters = yield many1(letter())
    return "".join(letters)
