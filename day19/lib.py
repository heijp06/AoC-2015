import re


def part1(rows):
    medicine = rows[-1]
    replacements = get_replacements(rows)
    molecules = replace_all(medicine, replacements)
    return len(molecules)


def part2(rows):
    medicine = rows[-1]
    replacements = [(b, a) for a, b in get_replacements(rows)]
    return reduce(medicine, replacements)


def reduce(string: str, replacements: list[tuple[str, str]]) -> int:
    reductions = 0
    while string != "e":
        for pattern, replacement in replacements:
            pos = string.find(pattern)
            if pos != -1:
                string = string[:pos] + replacement + \
                    string[pos + len(pattern):]
                reductions += 1
                break
    return reductions


def get_replacements(rows):
    replacements = []
    for row in rows:
        match = re.match("(\w+) => (\w+)", row)
        if match:
            replacements.append((match.group(1), match.group(2)))
    replacements.sort(
        key=lambda x: len([c for c in x[1] if c.isupper()]), reverse=True
    )

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
