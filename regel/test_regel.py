from regel import regel


def test_string_field():
    obj = regel("Obj", "{field}").parse("value")
    assert obj.field == "value"


def test_string_field_begin():
    obj = regel("Obj", "{field}xxx").parse("valuexxx")
    assert obj.field == "value"


def test_string_field_middle():
    obj = regel("Obj", "xxx{field}xxx").parse("xxxvaluexxx")
    assert obj.field == "value"


def test_string_field_end():
    obj = regel("Obj", "xxx{field}").parse("xxxvalue")
    assert obj.field == "value"


def test_group_in_pattern():
    obj = regel("Obj", "{field} (abc)").parse("value (abc)")
    assert obj.field == "value"


def test_day13_seating():
    Seating = regel(
        "Seating",
        "{guest1} would {gain:lambda x: x == 'gain'} {happiness:int} happiness units by sitting next to {guest2}."
    )
    seating = Seating.parse(
        "Alice would gain 54 happiness units by sitting next to Bob.")
    assert seating.guest1 == "Alice"
    assert seating.gain == True
    assert seating.happiness == 54
    assert seating.guest2 == "Bob"


def test_module_name():
    Obj = regel("Obj", "{field} (abc)")
    assert Obj.__module__ == __name__
