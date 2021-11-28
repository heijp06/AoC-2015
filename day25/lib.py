def part1() -> int:
    row = 2978
    column = 3083
    number = get_number(row, column)
    code = 20151125
    for _ in range(1, number):
        code *= 252533
        code %= 33554393
    return code


def part2(rows):
    pass


def get_number(row: int, column: int) -> int:
    diagonal = row + column - 1
    return diagonal * (diagonal - 1) // 2 + column
