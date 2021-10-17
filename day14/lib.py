import re


def part1(rows, seconds=2503):
    herd = [Reindeer(row) for row in rows]
    for _ in range(seconds):
        for reindeer in herd:
            reindeer.move()
    return max(reindeer.position for reindeer in herd)


def part2(rows, seconds=2503):
    herd = [Reindeer(row) for row in rows]
    for _ in range(seconds):
        for reindeer in herd:
            reindeer.move()
        lead = max(reindeer.position for reindeer in herd)
        for reindeer in herd:
            if reindeer.position == lead:
                reindeer.points += 1
    return max(reindeer.points for reindeer in herd)


class Reindeer:
    FLYING = 0
    RESTING = 1

    def __init__(self, row):
        match = re.match(
            r"(.*) can fly (.*) km/s for (.*) seconds, but then must rest for (.*) seconds.",
            row
        )
        name, speed, fly_time, rest_time = match.groups()
        self.name = name
        self.speed = int(speed)
        self.fly_time = int(fly_time)
        self.rest_time = int(rest_time)
        self.state = Reindeer.FLYING
        self.timer = self.fly_time
        self.position = 0
        self.points = 0

    def move(self):
        self.timer -= 1
        if self.state == Reindeer.FLYING:
            self.position += self.speed
            if self.timer == 0:
                self.state = Reindeer.RESTING
                self.timer = self.rest_time
        elif self.timer == 0:
            self.state = Reindeer.FLYING
            self.timer = self.fly_time
