import re
import sys
from collections import namedtuple
from parsec import ParseError, digit, generate, letter, many, none_of, string
import operator
from functools import partial

_MODULE = "module"


def regel(typename, pattern, **kwargs):
    def _init(self, text):
        values = bla(self, text)
        for field, value in zip(fields, values):
            setattr(self, field, value)
    try:
        regex, fields, funcs = _regel.parse_strict(pattern)
    except ParseError as err:
        raise ValueError(
            f"Error parsing pattern '{pattern}' at position {err.loc()}.")
    caller = sys._getframe(1)
    _set_module(caller, kwargs)
    cls = type(typename, (), {})
    cls._caller = caller
    cls.__module__ = kwargs[_MODULE]
    cls.__init__ = _init
    cls.regex = re.compile(regex)
    cls.fields = fields
    cls.funcs = funcs
    cls.parse = parse
    cls.pattern = pattern
    return cls


def eq(value):
    return partial(operator.eq, value)


def ne(value):
    return partial(operator.ne, value)


def _set_module(caller, kwargs):
    if _MODULE in kwargs and kwargs[_MODULE]:
        return
    try:
        kwargs[_MODULE] = caller.f_globals.get('__name__', '__main__')
    except (AttributeError, ValueError):
        pass

def bla(cls, text):
    match = cls.regex.match(text)
    if not match:
        raise ValueError(f"Text '{text}' does not match pattern '{cls.pattern}'")
    strings = match.groups()
    return [
        eval(f"({func})('{string}')",
             cls._caller.f_globals, cls._caller.f_locals)
        for func, string
        in zip(cls.funcs, strings)
    ]

@classmethod
def parse(cls, text):
    # values = bla(cls, text)
    # return cls(*values)
    return cls(text)


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
    chars = yield many(_open_brace ^ _close_brace ^ none_of("{}"))
    return "".join(chars)


@generate
def _open_brace():
    yield string("{{")
    return "{"


@generate
def _close_brace():
    yield string("}}")
    return "}"


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
