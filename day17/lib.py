from collections import defaultdict


def part1(sizes):
    return solve1(150, sizes)


def part2(sizes):
    pass


def solve1(liters, sizes):
    total_sizes = defaultdict(int, {0: 1})
    for size in sizes:
        next = defaultdict(int, total_sizes)
        for total, count in total_sizes.items():
            if total + size <= liters:
                next[total + size] += count
        total_sizes = next
    return total_sizes[liters]