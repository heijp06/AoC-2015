import pytest
from lib import code_len, part1, part2, value_len


def test_code_len():
    assert code_len(example) == 23

def test_value_len():
    assert value_len(example) == 11

def test_part1():
    assert part1(example) == 12

def test_part2():
    assert part2(example) == 19


example = [
    r'""',
    r'"abc"',
    r'"aaa\"aaa"',
    r'"\x27"'
]
