import pytest
from lib import part1, part2, solve1


def test_solve_example():
    assert solve1(25, [20, 15, 10, 5, 5]) == 4
