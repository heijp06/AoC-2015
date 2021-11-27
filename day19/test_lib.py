from lib import reduce


def test_reduce():
    assert reduce("CRnFArThRnFAr", replacements) == 3


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
