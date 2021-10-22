import re
from itertools import pairwise, permutations
import sys
sys.path.append("../regel")
from regel import regel, eq


def part1(rows):
    seating = Seating(rows)
    return seating.optimal()


def part2(rows):
    seating = Seating(rows, "me")
    return seating.optimal()


class Seating:
    def __init__(self, guest_list, me=None):
        Parser = regel(
            "Parser",
            "{guest1} would {gain:eq('gain')} {happiness:int} happiness units by sitting next to {guest2}."
        )
        self.guests = set()
        self.happiness = {}
        self.first_guest = me
        for row in guest_list:
            result = Parser._parse(row)
            if self.first_guest != result.guest1:
                if not self.first_guest:
                    self.first_guest = result.guest1
                else:
                    self.guests.add(result.guest1)
            self.happiness[result.guest1,
                           result.guest2] = result.happiness if result.gain else -result.happiness
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
                in pairwise(arrangement)
            )
            for arrangement in self.arrangements()
        )

    def arrangements(self):
        for permutation in permutations(self.guests):
            yield [self.first_guest, *permutation, self.first_guest]
