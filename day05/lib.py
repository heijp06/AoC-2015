import re


def part1(rows):
    return sum(1 for s in rows if nice(s))


def part2(rows):
    return sum(1 for s in rows if new_nice(s))


def nice(word):
    if any(s in word for s in ["ab", "cd", "pq", "xy"]):
        return False

    if sum(s in "aeiou" for s in word) < 3:
        return False

    return re.search(r"(.)\1", word)


def new_nice(word):
    return re.search(r"(..).*\1", word) and re.search(r"(.).\1", word)
