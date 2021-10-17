import string
import re


def part1(row):
    password_generator = PasswordGenerator(row)
    password_generator.generate()
    while not password_generator.valid():
        password_generator.generate()
    return password_generator.password


def part2(row):
    return part1(part1(row))


class PasswordGenerator:
    letters = re.sub(r"[iol]", "", string.ascii_lowercase)
    digits = string.digits + string.ascii_lowercase[:13]
    toNumber = str.maketrans(letters, digits)
    toPassword = str.maketrans(digits, letters)
    triples = [
        "".join(triple)
        for triple
        in zip(
            string.ascii_lowercase,
            string.ascii_lowercase[1:],
            string.ascii_lowercase[2:])
        if not any(char in triple for char in "iol")
    ]

    def __init__(self, password):
        self.password = password
        self.password_to_number()

    def password_to_number(self):
        base_23_number = self.password.translate(PasswordGenerator.toNumber)
        self.number = int(base_23_number, 23)

    def valid(self):
        return self.has_straight() and self.has_pairs()

    def has_straight(self):
        return any(triple in self.password for triple in PasswordGenerator.triples)

    def has_pairs(self):
        matches = re.findall(r"(.)\1", self.password)
        return len(matches) >= 2

    def generate(self):
        self.number += 1
        self.password = self.base23().translate(PasswordGenerator.toPassword)

    def base23(self):
        base_23_number = ""
        number = self.number
        while number > 0:
            number, index = divmod(number, 23)
            base_23_number = PasswordGenerator.digits[index] + base_23_number
        return base_23_number
