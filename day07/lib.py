from functools import cache
import operator
from parsec import digit, letter, generate, many1, space, string


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
        if a is not None and op == "b":
            return a
        f, args = self._gates[op]
        return f(*(self.value(arg, a) for arg in args))


binary_operators = {
    "AND": operator.and_,
    "OR": operator.or_,
    "LSHIFT": operator.lshift,
    "RSHIFT": operator.rshift,
}


@generate
def gate():
    f, args = (
        yield binary_gate
        ^ not_gate
        ^ const_gate
    )
    yield string(" -> ")
    n = yield identifier
    return n, (f, args)


@generate
def const_gate():
    op = yield operand
    return int, [op]


@generate
def binary_gate():
    op1 = yield operand
    yield space()
    func = (yield string("AND") ^ string("OR") ^ string("RSHIFT") ^ string("LSHIFT"))
    yield space()
    op2 = yield operand
    return binary_operators[func], [op1, op2]


@generate
def not_gate():
    yield string("NOT ")
    op = yield operand
    return operator.sub, [65535, op]


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
