from itertools import permutations

WEAPONS = [
    ("Dagger", 8, 4, 0),
    ("Shortsword", 10, 5, 0),
    ("Warhammer", 25, 6, 0),
    ("Longsword", 40, 7, 0),
    ("Greataxe", 74, 8, 0)
]

ARMOR = [
    ("Leather", 13, 0, 1),
    ("Chainmail", 31, 0, 2),
    ("Splintmail", 53, 0, 3),
    ("Bandedmail", 75, 0, 4),
    ("Platemail", 102, 0, 5)
]

RINGS = [
    ("Damage +1", 25, 1, 0),
    ("Damage +2", 50, 2, 0),
    ("Damage +3", 100, 3, 0),
    ("Defense +1", 20, 0, 1),
    ("Defense +2", 40, 0, 2),
    ("Defense +3", 80, 0, 3)
]


def part1():
    boss_damage = 8
    boss_armor = 2
    lowest_cost = None
    for items in iterate_items():
        name = ""
        cost = 0
        my_damage = 0
        my_armor = 0
        for item in items:
            name += " " + item[0]
            cost += item[1]
            my_damage += item[2]
            my_armor += item[3]
        name = name[1:]
        boss_deals = max(1, boss_damage - my_armor)
        i_deal = max(1, my_damage - boss_armor)
        if ((100 + boss_deals - 1) // boss_deals >= (100 + i_deal - 1) // i_deal
                and (not lowest_cost or cost < lowest_cost)):
            print(f"{name}, cost = {cost}, damage = {my_damage}, armor = {my_armor}")
            lowest_cost = cost
    return lowest_cost


def iterate_items():
    for weapon in WEAPONS:
        for count_armor in (0, 1):
            for armor in permutations(ARMOR, count_armor):
                for count_rings in (0, 1, 2):
                    for rings in permutations(RINGS, count_rings):
                        yield [weapon] + list(armor) + list(rings)


def part2(rows):
    pass
