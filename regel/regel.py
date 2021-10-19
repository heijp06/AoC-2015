import re
from collections import namedtuple
from parsec import ParseError, digit, generate, letter, many, many1, none_of, regex, string


def regel(typename, pattern):
    try:
        regex, fields = _regel.parse_strict(pattern)
        cls = type(typename, (namedtuple(typename, fields),), {})
        cls.regex = re.compile(regex)
        cls.parse = parse
        return cls
    except ParseError as err:
        raise ValueError(err)


@classmethod
def parse(cls, value):
    match = cls.regex.match(value)
    return cls(*match.groups())


@generate
def _regel():
    head = yield _text
    tail = yield many(_field + _text)
    regex = "(.*)".join([head, *[re.escape(t) for _, t in tail]])
    fields = [f for f, _ in tail]
    return regex, fields


@generate
def _text():
    chars = yield many(none_of("{"))
    return "".join(chars)


@generate
def _field():
    return (yield string("{") >> _identifier << string("}"))


@generate
def _identifier():
    head = yield (string("_") | letter())
    tail = yield many(string("_") | letter() | digit())
    return head + "".join(tail)
