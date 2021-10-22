import pytest
from regel import eq, ne, regel, split


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
    obj = regel("Obj", "{dict:lambda x:: {{x:: 5}}}")._parse("five")
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


def test_do_not_use_str_for_no_conversion():
    # Initially str() was used as a no-op string conversion.
    # Which has the below potential problem.
    str = int
    obj = regel("Obj", "{field1}")._parse("42")
    assert obj.field1 == "42"


def test_duplicate_field():
    with pytest.raises(ValueError):
        regel("Obj", "{field} {field}")


def test_split_default_separator():
    obj = regel("Obj", "{fields:split()}.")._parse("one two three.")
    assert obj.fields == ["one", "two", "three"]


def test_split_no_match():
    obj = regel("Obj", "{fields:split(',')}.")._parse("one two three.")
    assert obj.fields == ["one two three"]


def test_split_multiple_delimiters():
    obj = regel("Obj", "{fields:split(', ', ' and ')}.")._parse(
        "one, two and three.")
    assert obj.fields == ["one", "two", "three"]


def test_list_to_int():
    obj = regel("Obj", "{fields:split():int}")._parse("1 2 3")
    assert obj.fields == [1, 2, 3]


def test_list_to_int_to_bool():
    obj = regel("Obj", "{fields:split():int:eq(2)}")._parse("1 2 3")
    assert obj.fields == [False, True, False]


def test_colon_in_text():
    obj = regel("Obj", "The value is: {field}")._parse("The value is: 42")
    assert obj.field == "42"


# 2020 day 4, passport, dictionary
# 2020 day 7, shiny gold bag, list, object
