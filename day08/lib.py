import re


def part1(rows):
    return code_len(rows) - value_len(rows)


def part2(rows):
    return sum(inc(row) for row in rows)


def code_len(rows):
    return sum(len(row) for row in rows)


def value_len(rows):
    return sum(len(clean(row)) for row in rows)


def clean(row):
    row = row[1:-1]
    row = str.replace(row, r'\"', '"')
    row = str.replace(row, r'\\', '-')
    row = re.sub(r'\\x..', '-', row)
    return row


def inc(row):
    return 2 + sum(x in r'\"' for x in row)
