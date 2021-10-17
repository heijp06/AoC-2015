import re
from itertools import permutations


def part1(rows):
    seating = Seating(rows)
    return seating.optimal()


def part2(rows):
    seating = Seating(rows, "me")
    return seating.optimal()


class Seating:
    def __init__(self, guest_list, me=None):
        self.guests = set()
        self.happiness = {}
        self.first_guest = me
        for row in guest_list:
            match = re.match(
                r"(.*) would (.*) (.*) happiness units by sitting next to (.*)\.",
                row)
            guest1, sign, units, guest2 = match.groups()
            if self.first_guest != guest1:
                if not self.first_guest:
                    self.first_guest = guest1
                else:
                    self.guests.add(guest1)
            self.happiness[guest1, guest2] = int(
                units) if sign == "gain" else -int(units)
        self.add_me(me)

    def add_me(self, me):
        if not me:
            return
        for guest in self.guests:
            self.happiness[me, guest] = 0
            self.happiness[guest, me] = 0

    def optimal(self):
        return max(
            sum(
                self.happiness[a, b] + self.happiness[b, a]
                for a, b
                in zip(arrangement, arrangement[1:])
            )
            for arrangement in self.arrangements()
        )

    def arrangements(self):
        for permutation in permutations(self.guests):
            yield [self.first_guest, *permutation, self.first_guest]
