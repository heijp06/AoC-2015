import pytest
from lib import Circuit


def test_d():
    circuit = Circuit(gates)
    assert circuit.value("d") == 72

def test_e():
    circuit = Circuit(gates)
    assert circuit.value("e") == 507

def test_f():
    circuit = Circuit(gates)
    assert circuit.value("f") == 492

def test_g():
    circuit = Circuit(gates)
    assert circuit.value("g") == 114

def test_h():
    circuit = Circuit(gates)
    assert circuit.value("h") == 65412

def test_i():
    circuit = Circuit(gates)
    assert circuit.value("i") == 65079

def test_x():
    circuit = Circuit(gates)
    assert circuit.value("x") == 123

def test_y():
    circuit = Circuit(gates)
    assert circuit.value("y") == 456

gates = [
    "123 -> x",
    "456 -> y",
    "x AND y -> d",
    "x OR y -> e",
    "x LSHIFT 2 -> f",
    "y RSHIFT 2 -> g",
    "NOT x -> h",
    "NOT y -> i",
]