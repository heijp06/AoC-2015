import pytest
from regel import regel

def test_string_field():
    obj = regel("Obj", "{field}").parse("value")
    assert obj.field == "value"

def test_group_in_pattern():
    obj = regel("Obj", "{field} (abc)").parse("value (abc)")
    assert obj.field == "value"

def test_day13_seating():
    Seating = regel(
        "Seating",
        "{guest1} would {sign} {units} happiness units by sitting next to {guest2}."
    )
    seating = Seating.parse("Alice would gain 54 happiness units by sitting next to Bob.")
    assert seating.guest1 == "Alice"
    assert seating.sign == "gain"
    assert seating.units == "54"
    assert seating.guest2 == "Bob"
    pytest.fail("Implement data types for sign and units.")

# TODO: module name of class.