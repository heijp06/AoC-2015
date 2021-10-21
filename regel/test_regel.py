import pytest
from regel import eq, ne, regel


def test_string_field():
    obj = regel("Obj", "{field}")._parse("value")
    assert obj.field == "value"


def test_string_field_begin():
    obj = regel("Obj", "{field}xxx")._parse("valuexxx")
    assert obj.field == "value"


def test_string_field_middle():
    obj = regel("Obj", "xxx{field}xxx")._parse("xxxvaluexxx")
    assert obj.field == "value"


def test_string_field_end():
    obj = regel("Obj", "xxx{field}")._parse("xxxvalue")
    assert obj.field == "value"


def test_group_in_pattern():
    obj = regel("Obj", "{field} (abc)")._parse("value (abc)")
    assert obj.field == "value"


def test_day13_seating():
    Seating = regel(
        "Seating",
        "{guest1} would {gain:eq('gain')} {happiness:int} happiness units by sitting next to {guest2}."
    )
    seating = Seating._parse(
        "Alice would gain 54 happiness units by sitting next to Bob.")
    assert seating.guest1 == "Alice"
    assert seating.gain == True
    assert seating.happiness == 54
    assert seating.guest2 == "Bob"


def test_local_function():
    def f(x):
        return 1 + int(x)
    obj = regel("Obj", "The number is {number:f}.")._parse("The number is 5.")
    assert obj.number == 6


def test_dictionary():
    obj = regel("Obj", "{dict:lambda x: {{x: 5}}}")._parse("five")
    assert "five" in obj.dict
    assert obj.dict["five"] == 5


def test_braces_in_text():
    obj = regel("Obj", "{{not_a_field:int}} {a_field:int}")._parse(
        "{not_a_field:int} 42")
    assert obj.a_field == 42


def test_module_name():
    Obj = regel("Obj", "{field} (abc)")
    assert Obj.__module__ == __name__


def test_constructor():
    Obj = regel("Obj", "{field1:int} {field2:int}")
    obj = Obj("42 43")
    assert obj.field1 == 42
    assert obj.field2 == 43


def test_field_cannot_start_with_underscore():
    with pytest.raises(ValueError):
        regel("Obj", "{_field}")
