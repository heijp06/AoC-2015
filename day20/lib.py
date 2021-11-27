SIZE = 1000000


def part1(presents, size=SIZE):
    sieve = [0] * size
    for elf in range(1, size):
        present = 10 * elf
        for house in range(elf, size, elf):
            sieve[house] += present
    for elf in range(1, size):
        if sieve[elf] >= presents:
            return elf
    return -1


def part2(presents, size=SIZE):
    sieve = [0] * size
    for elf in range(1, size):
        present = 11 * elf
        for house in range(elf, min(size, 50 * elf), elf):
            sieve[house] += present
    for elf in range(1, size):
        if sieve[elf] >= presents:
            return elf
    return -1
