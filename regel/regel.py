import re
import sys
from collections import namedtuple
from parsec import digit, generate, letter, many, none_of, string

_MODULE = "module"


def regel(typename, pattern, **kwargs):
    regex, fields, funcs = _regel.parse_strict(pattern)
    _set_module(kwargs)
    cls = type(typename, (namedtuple(typename, fields, **kwargs),), {})
    cls.__module__ = kwargs[_MODULE]
    cls.regex = re.compile(regex)
    cls.funcs = funcs
    cls.parse = parse
    return cls


def _set_module(kwargs):
    if _MODULE in kwargs and kwargs[_MODULE]:
        return
    try:
        kwargs[_MODULE] = sys._getframe(
            2).f_globals.get('__name__', '__main__')
    except (AttributeError, ValueError):
        pass


@classmethod
def parse(cls, value):
    match = cls.regex.match(value)
    strings = match.groups()
    values = [
        eval(f"({func})('{string}')")
        for func, string
        in zip(cls.funcs, strings)
    ]
    return cls(*values)


@generate
def _regel():
    head = yield _text
    tail = yield many((_field_with_func ^ _field) + _text)
    regex = "(.*)".join([head, *[re.escape(t) for _, t in tail]])
    fields = [f[0] for f, _ in tail]
    funcs = [f[1] for f, _ in tail]
    return regex, fields, funcs


@generate
def _text():
    chars = yield many(none_of("{}"))
    return "".join(chars)


@generate
def _field_with_func():
    yield string("{")
    identifier = yield _identifier
    yield string(":")
    func = yield _text
    yield string("}")
    return identifier, func


@generate
def _field():
    identifier = yield string("{") >> _identifier << string("}")
    return identifier, "str"


@generate
def _identifier():
    head = yield (string("_") | letter())
    tail = yield many(string("_") | letter() | digit())
    return head + "".join(tail)
