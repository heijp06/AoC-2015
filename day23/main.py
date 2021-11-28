import csv
import pyperclip
from lib import part1, part2


def read_rows(**kwargs):
    with open('data.txt', newline='') as csv_file:
        # return list(csv.reader(csv_file, **kwargs))
        # return csv_file.read().strip()
        return csv_file.read().splitlines()


def clip(x):
    if not x:
        return
    pyperclip.copy(x)


rows = read_rows()
x = part1(rows)
print(f"Part 1: {x}")
clip(x)

rows = read_rows()
x = part2(rows)
print(f"Part 2: {x}")
clip(x)
