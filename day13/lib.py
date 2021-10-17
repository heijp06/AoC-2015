import re
def part1(rows):
    pass


def part2(rows):
    pass

class Seating:
    def __init__(self, guest_list):
        self.guests = set()
        self.happiness = {}
        for row in guest_list:
            match = re.match(
                r"(.*) would (.*) (.*) happiness units by sitting next to (.*)\.",
                row)
            guest1, sign, units, guest2 = match.groups()
            self.guests.add(guest1)
            self.happiness[guest1, guest2] = int(units) if sign == "gain" else -int(units)
            