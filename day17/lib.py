from collections import defaultdict
import copy


def part1(sizes):
    return solve1(150, sizes)


def part2(sizes):
    return solve2(150, sizes)


def solve1(liters, sizes):
    total_sizes = defaultdict(int, {0: 1})
    for size in sizes:
        temp = total_sizes.copy()
        for total, count in total_sizes.items():
            if total + size <= liters:
                temp[total + size] += count
        total_sizes = temp
    return total_sizes[liters]


def solve2(liters, sizes):
    total_sizes = defaultdict(list, {0: [0]})
    for size in sizes:
        temp = copy.deepcopy(total_sizes)
        for total, counts in total_sizes.items():
            if total + size <= liters:
                temp[total + size] += [count + 1 for count in counts]
        total_sizes = temp
    return sum(size == min(total_sizes[liters]) for size in total_sizes[liters])
