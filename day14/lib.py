import re


def part1(rows, seconds=2503):
    herd = Herd(rows)
    herd.race(seconds)
    return herd.max_position()


def part2(rows, seconds=2503):
    herd = Herd(rows)
    herd.race(seconds)
    return herd.max_points()


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


class Herd:
    def __init__(self, rows):
        self.reindeer = [Reindeer(row) for row in rows]

    def move(self):
        for reindeer in self.reindeer:
            reindeer.move()
        for reindeer in self.reindeer:
            if reindeer.position == self.max_position():
                reindeer.points += 1

    def max_position(self):
        return max(reindeer.position for reindeer in self.reindeer)

    def max_points(self):
        return max(reindeer.points for reindeer in self.reindeer)

    def race(self, seconds):
        for _ in range(seconds):
            self.move()
