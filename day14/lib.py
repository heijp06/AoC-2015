import re


def part1(rows, seconds=2503):
    return max(Reindeer(row).position(seconds) for row in rows)



def part2(rows):
    pass


class Reindeer:
    def __init__(self, row):
        self.parse(row)

    def parse(self, row):
        match = re.match(
            r"(.*) can fly (.*) km/s for (.*) seconds, but then must rest for (.*) seconds.",
            row
        )
        name, speed, fly_time, rest_time = match.groups()
        self.name = name
        self.speed = int(speed)
        self.fly_time = int(fly_time)
        self.rest_time = int(rest_time)
    
    def position(self, seconds):
        quotient, remainder = divmod(seconds, self.fly_time + self.rest_time)
        return (quotient * self.fly_time + min(self.fly_time, remainder)) * self.speed
