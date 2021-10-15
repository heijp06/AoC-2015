from itertools import count
import hashlib


def part1(code):
    for i in count():
        s = code + str(i)
        md5 = hash(s)
        if md5.startswith("00000"):
            return i


def hash(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def part2(code):
    for i in count():
        s = code + str(i)
        md5 = hash(s)
        if md5.startswith("000000"):
            return i
