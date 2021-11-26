from __future__ import annotations
from typing import Any, Iterable


class Group:
    @staticmethod
    def parse_molecule(molecule: str) -> Group:
        groups, _ = Group._do_parse(molecule, 0)
        return Group(groups)

    @staticmethod
    def _do_parse(molecule: str, pos: int) -> tuple[list[Any], int]:
        groups: list[Any] = []
        while True:
            rn = molecule.find("Rn", pos)
            ar = molecule.find("Ar", pos)
            if rn == -1 and ar == -1:
                if pos < len(molecule):
                    groups.append(molecule[pos:])
                return groups, len(molecule)
            if rn == -1 or rn > ar:
                if pos < ar:
                    groups.append(molecule[pos:ar])
                return groups, ar + 2
            if pos < rn:
                groups.append(molecule[pos:rn])
            nested_groups, pos = Group._do_parse(molecule, rn + 2)
            groups.append(Group(nested_groups))

    @staticmethod
    def _do_reduction(string: str, replacements: list[tuple[str, str]], terminals: set[str]) -> tuple[str, int]:
        print(f"string  = {string}")
        strings = {string}
        reductions = 0
        while all(s not in terminals for s in strings):
            print(len(strings))
            strings = {
                replaced
                for s in strings
                for replaced in Group._replace_all(s, replacements)
            }
            reductions += 1
        reduced = next(string for string in strings if string in terminals)
        print(f"reduced = {reduced}")
        return reduced, reductions

    @staticmethod
    def _replace_all(molecule: str, replacements: list[tuple[str, str]]) -> set[str]:
        max_pos = molecule.find("Ar")
        if max_pos == -1:
            max_pos = len(molecule)
        new_molecules = set()
        for pattern, replacement in replacements:
            start = 0
            pos = molecule.find(pattern, start)
            while pos >= 0 and pos < max_pos:
                new_molecule = molecule[:pos] + \
                    replacement + molecule[pos + len(pattern):]
                new_molecules.add(new_molecule)
                start = pos + len(pattern)
                pos = molecule.find(pattern, start)
        return new_molecules
    
    _terminals = {
        "Al",
        "F",
        "FYF",
        "FYFYF",
        "FYMg",
        "Mg",
        "MgYF"
    }

    def __init__(self, groups: Iterable[Any]) -> None:
        self.reductions = 0
        self.groups = list(groups)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Group) and self.groups == other.groups

    def __repr__(self) -> str:
        return f"Group({', '.join(repr(group) for group in self.groups)})"

    def reduce(self, replacements: list[tuple[str, str]], terminals: set[str] = None) -> None:
        terminals = terminals or Group._terminals
        result = ""

        for group in self.groups:
            if isinstance(group, str):
                result += group
            else:
                group.reduce(replacements)
                result += "".join(["Rn", group.groups[0], "Ar"])
                self.reductions += group.reductions

        reduced, reductions = Group._do_reduction(
            result, replacements, terminals)

        self.groups.clear()
        self.groups.append(reduced)
        self.reductions += reductions
