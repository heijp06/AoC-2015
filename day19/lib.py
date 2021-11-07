import re
from collections import defaultdict

def part1(rows):
    molecule = rows[-1]
    molecules = set()
    for row in rows:
        match = re.match("(\w+) => (\w+)", row)
        if match:
            pattern = match.group(1)
            replacement = match.group(2)
            start = 0
            pos = molecule.find(pattern, start)
            while pos >= 0:
                new_molecule = molecule[:pos] + replacement + molecule[pos + len(pattern):]
                molecules.add(new_molecule)
                start = pos + 1
                pos = molecule.find(pattern, start)
    return len(molecules)



def part2(rows):
    pass
