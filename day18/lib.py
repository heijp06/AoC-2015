def part1(rows):
    grid = set()
    for y in range(100):
        for x in range(100):
            if rows[y][x] == '#':
                grid.add((x, y))
    for _ in range(100):
        new_grid = set()
        for y in range(100):
            for x in range(100):
                neighbours = sum(
                    (x+dx, y+dy) in grid for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx, dy) != (0, 0))
                if ((x, y) in grid and neighbours in [2, 3]) or ((x, y) not in grid and neighbours == 3):
                    new_grid.add((x, y))
        grid = new_grid
    return len(grid)


def part2(rows):
    grid = set()
    for y in range(100):
        for x in range(100):
            if rows[y][x] == '#':
                grid.add((x, y))
    grid.add((0, 0))
    grid.add((99, 0))
    grid.add((0, 99))
    grid.add((99, 99))
    for _ in range(100):
        new_grid = set()
        for y in range(100):
            for x in range(100):
                if (x in [0, 99] and y in [0, 99]): continue
                neighbours = sum(
                    (x+dx, y+dy) in grid for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx, dy) != (0, 0))
                if ((x, y) in grid and neighbours in [2, 3]) or ((x, y) not in grid and neighbours == 3):
                    new_grid.add((x, y))
        grid = new_grid
        grid.add((0, 0))
        grid.add((99, 0))
        grid.add((0, 99))
        grid.add((99, 99))
    return len(grid)
