from computer import Computer


def part1(rows):
    computer = Computer(rows)
    computer.run()
    return computer.registers["b"]


def part2(rows):
    computer = Computer(rows)
    computer.registers["a"] = 1
    computer.run()
    return computer.registers["b"]
