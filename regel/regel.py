import re
import sys
from collections import namedtuple
from parsec import ParseError, digit, generate, letter, many, none_of, string
import operator
from functools import partial

_MODULE = "module"


def regel(typename, pattern):
    def _init(self, text):
        match = self._regex.match(text)
        if not match:
            raise ValueError(
                f"Text '{text}' does not match pattern '{self._pattern}'")
        strings = match.groups()
        values = [
            eval(f"({func})('{string}')",
                 self._f_globals, self._f_locals) if func else string
            for func, string
            in zip(self._funcs, strings)
        ]
        for field, value in zip(self._fields, values):
            setattr(self, field, value)

    try:
        regex, fields, funcs = _regel.parse_strict(pattern)
    except ParseError as err:
        raise ValueError(
            f"Error parsing pattern '{pattern}' at position {err.loc()}.")

    seen = set()
    for field in fields:
        if field in seen:
            raise ValueError(f"Duplicate field '{field}'.")
        seen.add(field)

    try:
        caller = sys._getframe(1)
        f_globals = caller.f_globals
        f_locals = caller.f_locals
        module = f_globals.get('__name__', '__main__')
    except (AttributeError, ValueError):
        f_globals = {}
        f_locals = {}
        module = __name__

    namespace = {
        "__module__": module,
        "__init__": _init,
        "_regex": re.compile(regex),
        "_fields": fields,
        "_funcs": funcs,
        "_parse": _parse,
        "_pattern": pattern,
        "_f_globals": f_globals,
        "_f_locals": f_locals,
    }

    return type(typename, (), namespace)


def eq(value):
    return partial(operator.eq, value)


def ne(value):
    return partial(operator.ne, value)


@classmethod
def _parse(cls, text):
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
    return identifier, None


@generate
def _identifier():
    head = yield letter()
    tail = yield many(string("_") | letter() | digit())
    return head + "".join(tail)
