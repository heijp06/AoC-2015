import re
import json


def part1(data):
    return sum(int(n) for n in re.findall(r"-?\d+", data))


def part2(data):
    obj = json.loads(data)
    return total(obj)


def total(obj):
    if isinstance(obj, int):
        return obj
    if isinstance(obj, str):
        return 0
    if isinstance(obj, dict):
        if "red" in obj.values():
            return 0
        return sum(total(value) for value in obj.values())
    if isinstance(obj, list):
        return sum(total(value) for value in obj)
    raise NotImplementedError(f"Objects of type '{type(obj)}.")
