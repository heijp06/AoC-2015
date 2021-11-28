import pytest
from lib import part1, part2, get_number

testdata = [
    (1, 1, 1),
    (3, 1, 4),
    (4, 2, 12),
    (1, 5, 15)
]

@pytest.mark.parametrize("row,column,number", testdata)
def test_get_number(row, column, number):
    assert get_number(row, column) == number
