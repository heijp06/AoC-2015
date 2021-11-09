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
    molecule = Group.parse_molecule(medicine)



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
