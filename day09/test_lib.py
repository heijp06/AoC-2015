import pytest
from lib import Travel, part1, part2


def test_parse_row():
    travel = Travel([example[0]])
    assert len(travel.destinations) == 2
    assert "London" in travel.destinations
    assert "Dublin" in travel.destinations
    assert len(travel.distances) == 2
    assert ("London", "Dublin") in travel.distances
    assert ("Dublin", "London") in travel.distances
    assert travel.distances["London", "Dublin"] == 464
    assert travel.distances["Dublin", "London"] == 464


def test_shortest_route():
    travel = Travel(example)
    assert travel.route() == 605


example = [
    "London to Dublin = 464",
    "London to Belfast = 518",
    "Dublin to Belfast = 141",
]
