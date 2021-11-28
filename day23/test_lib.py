import pytest
from lib import part1, part2
from computer import Computer


def test_lib():
    computer = Computer([
        "inc a",
        "jio a, +2",
        "tpl a",
        "inc a"
    ])
    computer.run()

    assert computer.registers["a"] == 2
    assert computer.registers["b"] == 0


def test_negative_jump():
    computer = Computer([
        "inc a",
        "jio a, -1"
    ])
    computer.run()

    assert computer.registers["a"] == 2
    assert computer.registers["b"] == 0
