SIZE = 1000000

def part1(presents, size = SIZE):
    target = presents // 10
    sieve = [0] * size
    for elf in range(1, size):
        for house in range(elf, size, elf):
            sieve[house] += elf
    for elf in range(1, size):
        if sieve[elf] >= target:
            return elf
    return -1

def part2(rows):
    pass
