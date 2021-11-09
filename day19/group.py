from __future__ import annotations
from typing import Any, Iterable

class Group:
    @staticmethod
    def parse_molecule(molecule: str) -> list[Group]:
        groups, _ = Group._do_parse(molecule, 0)
        return groups
    
    @staticmethod
    def _do_parse(molecule: str, pos: int) -> list[list[Group], int]:
        groups = []
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


    def __init__(self, groups: Iterable[Any]) -> Group:
        self.groups = list(groups)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Group) and self.groups == other.groups
    
    def __repr__(self) -> str:
        return f"Group({', '.join(repr(group) for group in self.groups)})"
