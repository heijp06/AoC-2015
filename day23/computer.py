import re


class Computer:
    def __init__(self, statements: list[str]) -> None:
        self.statements = statements
        self.program_counter = 0
        self.registers = {"a": 0, "b": 0}
        self.instructions = {
            "hlf": self.half,
            "tpl": self.triple,
            "inc": self.inc,
            "jmp": self.jump,
            "jie": self.jump_if_even,
            "jio": self.jump_if_one
        }

    def __repr__(self) -> str:
        if self.can_execute():
            statement = self.statements[self.program_counter]
        else:
            statement = "..."
        return f"a={self.registers['a']} b={self.registers['b']} " + \
            f"pc={self.program_counter} ins={statement}"

    def run(self) -> None:
        while self.can_execute():
            statement = self.statements[self.program_counter]
            self.execute(statement)

    def can_execute(self) -> bool:
        return self.program_counter >= 0 and self.program_counter < len(self.statements)

    def execute(self, statement: str) -> None:
        args = re.split(r"[, ]+", statement)
        self.instructions[args[0]](*args[1:])

    def half(self, register) -> None:
        self.registers[register] //= 2
        self.program_counter += 1

    def triple(self, register) -> None:
        self.registers[register] *= 3
        self.program_counter += 1

    def inc(self, register) -> None:
        self.registers[register] += 1
        self.program_counter += 1

    def jump(self, offset) -> None:
        self.program_counter += int(offset)

    def jump_if_even(self, register, offset) -> None:
        self.program_counter += int(
            offset) if not self.registers[register] % 2 else 1

    def jump_if_one(self, register, offset) -> None:
        self.program_counter += int(
            offset) if self.registers[register] == 1 else 1
