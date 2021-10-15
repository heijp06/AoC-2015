import pyperclip
from lib import part1, part2


def read_rows():
    with open('data.txt', newline='') as csv_file:
        return csv_file.read().rstrip()


def clip(text):
    if not text:
        return
    pyperclip.copy(text)


code = read_rows()
result = part1(code)
print(f"Part 1: {result}")
clip(result)

code = read_rows()
result = part2(code)
print(f"Part 2: {result}")
clip(result)
