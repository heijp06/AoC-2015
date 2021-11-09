import pytest
from lib import part1, part2
from group import Group


def test_molecule_h_f():
    assert Group.parse_molecule("HF") == ["HF",]


def test_molecule_c_rn_al_ar_f():
    assert Group.parse_molecule("CRnAlArF") == ["C", Group(["Al"]), "F"]


def test_molecule_c_rn_al_ar():
    assert Group.parse_molecule("CRnAlAr") == ["C", Group(["Al"])]


def test_molecule_rn_al_ar_f():
    assert Group.parse_molecule("RnAlArF") == [Group(["Al"]), "F"]


def test_molecule_rn_rn_ar_ar():
    assert Group.parse_molecule("RnRnArAr") == [Group([Group([])])]
