import pytest
from lib import choices, part1, part2


def test_choices():
    actual = list(choices(3, 3))
    expected = [
        [0, 0, 3],
        [0, 1, 2],
        [0, 2, 1],
        [0, 3, 0],
        [1, 0, 2],
        [1, 1, 1],
        [1, 2, 0],
        [2, 0, 1],
        [2, 1, 0],
        [3, 0, 0]
    ]

    assert expected == actual


def test_example():
    assert part1(example) == 62842880


example = [
"Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
"Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"
]
