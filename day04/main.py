import csv
from lib import part1, part2
import pyperclip


def read_rows(**kwargs):
    with open('data.txt', newline='') as csv_file:
        # return list(csv.reader(csv_file, **kwargs))
        return csv_file.read().rstrip()


def clip(x):
    if not x:
        return
    pyperclip.copy(x)


code = read_rows()
x = part1(code)
print(f"Part 1: {x}")

code = read_rows()
x = part2(code)
print(f"Part 2: {x}")

clip(x)
