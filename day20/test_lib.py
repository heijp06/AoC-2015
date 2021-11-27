import pytest
from lib import part1, part2


def test_at_least_100():
    assert part1(100, 10) == 6

def test_at_least_150():
    assert part1(150, 10) == 8
