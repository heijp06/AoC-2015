import pytest
from lib import part1, part2, solve1, solve2


def test_solve1_example():
    assert solve1(25, [20, 15, 10, 5, 5]) == 4


def test_solve2_example():
    assert solve2(25, [20, 15, 10, 5, 5]) == 3


def test_solve2_1_1_liters_2():
    assert solve2(2, [1, 1]) == 1
