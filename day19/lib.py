import re
from collections import defaultdict
from group import Group


def part1(rows):
    medicine = rows[-1]
    replacements = get_replacements(rows)
    molecules = replace_all(medicine, replacements)
    return len(molecules)


# Once created, Ar, C, Rn, Th and Y can never be destroyed.
def part2(rows):
    medicine = rows[-1]
    replacements = [(b, a) for a, b in get_replacements(rows)]
    # return reduce(medicine, replacements)
    molecule = Group.parse_molecule(medicine)
    molecule.reduce(replacements, {"e"})
    return molecule


def get_replacements(rows):
    replacements = []
    for row in rows:
        match = re.match("(\w+) => (\w+)", row)
        if match:
            replacements.append((match.group(1), match.group(2)))
    return replacements


def replace_all(molecule, replacements):
    new_molecules = set()
    for pattern, replacement in replacements:
        start = 0
        pos = molecule.find(pattern, start)
        while pos >= 0:
            new_molecule = molecule[:pos] + \
                replacement + molecule[pos + len(pattern):]
            new_molecules.add(new_molecule)
            start = pos + len(pattern)
            pos = molecule.find(pattern, start)
    return new_molecules


def reduce(string: str, replacements: list[tuple[str, str]]) -> int:
    strings = {string: 0}
    reductions = 0
    while "e" not in strings:
        print(len(strings))
        new_strings = {}
        for string, start_pos in strings.items():
            for replaced, pos in replace_all2(string, start_pos, replacements).items():
                if replaced not in new_strings or new_strings[replaced] < pos:
                    new_strings[replaced] = pos
        reductions += 1
        strings = new_strings
    return reductions


def replace_all2(molecule, start_pos, replacements):
    new_molecules = {}
    max_pos = molecule.find("Ar")
    if max_pos == -1:
        max_pos = len(molecule)
    for pattern, replacement in replacements:
        start = max(0, start_pos - len(pattern) + 1)
        pos = molecule.find(pattern, start)
        while pos >= 0 and pos < max_pos:
            new_molecule = molecule[:pos] + \
                replacement + molecule[pos + len(pattern):]
            if new_molecule not in new_molecules or new_molecules[new_molecule] < pos:
                new_molecules[new_molecule] = pos
            start = pos + 1
            pos = molecule.find(pattern, start)
    return new_molecules
