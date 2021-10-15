from itertools import count
import hashlib


def part1(code):
    return find(code, 5)


def part2(code):
    return find(code, 6)


def find(code, zeros):
    for i in count():
        s = code + str(i)
        md5 = hash(s)
        if md5.startswith("0" * zeros):
            return i


def hash(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()
