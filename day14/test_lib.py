import pytest
from lib import Reindeer, part1, part2


def test_parse():
    reindeer = Reindeer(example[0])
    assert reindeer.name == "Comet"
    assert reindeer.speed == 14
    assert reindeer.fly_time == 10
    assert reindeer.rest_time == 127

def test_position_1_second():
    comet = Reindeer(example[0])
    assert comet.position(1) == 14

def test_position_1000_second():
    comet = Reindeer(example[0])
    assert comet.position(1000) == 1120

def test_part1():
    assert part1(example, 1000) == 1120


example = [
    "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
    "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
]