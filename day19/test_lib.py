import pytest
from lib import part1, part2
from group import Group


def test_molecule_h_f():
    assert Group.parse_molecule("HF") == Group(["HF", ])


def test_molecule_c_rn_al_ar_f():
    assert Group.parse_molecule("CRnAlArF") == Group(["C", Group(["Al"]), "F"])


def test_molecule_c_rn_al_ar():
    assert Group.parse_molecule("CRnAlAr") == Group(["C", Group(["Al"])])


def test_molecule_rn_al_ar_f():
    assert Group.parse_molecule("RnAlArF") == Group([Group(["Al"]), "F"])


def test_molecule_rn_rn_ar_ar():
    assert Group.parse_molecule("RnRnArAr") == Group([Group([Group([])])])


def test_reduce_rn_b_p_ti_mg_ar():
    group = Group.parse_molecule("BPTiMg")

    assert len(group.groups) == 1
    assert group.groups[0] == "BPTiMg"

    group.reduce(replacements)

    assert group.reductions == 3
    assert len(group.groups) == 1


def test_reduce_h_si_rn_mg_ar():
    group = Group.parse_molecule("HSiRnMgAr")

    assert len(group.groups) == 2
    assert group.groups[0] == "HSi"
    assert group.groups[1] == Group(["Mg"])

    group.reduce(replacements, {"H"})

    assert group.reductions == 2
    assert len(group.groups) == 1
    assert group.groups[0] == "H"

def test_reduce_c_rn_f_y_f_ar():
    group = Group.parse_molecule("CRnFYFAr")

    assert len(group.groups) == 2
    assert group.groups[0] == "C"
    assert group.groups[1] == Group(["FYF"])

    group.reduce(replacements, {"O"})

    assert group.reductions == 1
    assert len(group.groups) == 1
    assert group.groups[0] == "O"

def test_reduce_c_rn_f_ar_th_rn_f_ar():
    group = Group.parse_molecule("CRnFArThRnFAr")

    assert len(group.groups) == 4
    assert group.groups[0] == "C"
    assert group.groups[1] == Group(["F"])
    assert group.groups[2] == "Th"
    assert group.groups[3] == Group(["F"])

    group.reduce(replacements, {"e"})

    assert group.reductions == 3
    assert len(group.groups) == 1
    assert group.groups[0] == "e"


def test_group_replace_all():
    assert Group._replace_all("BPTiMg", replacements) == {
        "TiTiMg", "BPMg"}


replacements = [
    ("ThF", "Al"),
    ("ThRnFAr", "Al"),
    ("BCa", "B"),
    ("TiB", "B"),
    ("TiRnFAr", "B"),
    ("CaCa", "Ca"),
    ("PB", "Ca"),
    ("PRnFAr", "Ca"),
    ("SiRnFYFAr", "Ca"),
    ("SiRnMgAr", "Ca"),
    ("SiTh", "Ca"),
    ("CaF", "F"),
    ("PMg", "F"),
    ("SiAl", "F"),
    ("CRnAlAr", "H"),
    ("CRnFYFYFAr", "H"),
    ("CRnFYMgAr", "H"),
    ("CRnMgYFAr", "H"),
    ("HCa", "H"),
    ("NRnFYFAr", "H"),
    ("NRnMgAr", "H"),
    ("NTh", "H"),
    ("OB", "H"),
    ("ORnFAr", "H"),
    ("BF", "Mg"),
    ("TiMg", "Mg"),
    ("CRnFAr", "N"),
    ("HSi", "N"),
    ("CRnFYFAr", "O"),
    ("CRnMgAr", "O"),
    ("HP", "O"),
    ("NRnFAr", "O"),
    ("OTi", "O"),
    ("CaP", "P"),
    ("PTi", "P"),
    ("SiRnFAr", "P"),
    ("CaSi", "Si"),
    ("ThCa", "Th"),
    ("BP", "Ti"),
    ("TiTi", "Ti"),
    ("HF", "e"),
    ("NAl", "e"),
    ("OMg", "e")
]

terminals = {
    "Al",
    "B",
    "Ca",
    "F",
    "H",
    "Mg",
    "N",
    "O",
    "P",
    "Si",
    "Th",
    "Ti",
    "e"
}
