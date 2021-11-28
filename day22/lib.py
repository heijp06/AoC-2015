from game import Game


def part1():
    games = {Game()}
    min_mana = None
    while games:
        new_games = set()
        for game in games:
            min_mana = play(
                game.cast_magic_missile(), min_mana, new_games)
            min_mana = play(game.cast_drain(), min_mana, new_games)
            min_mana = play(game.cast_shield(), min_mana, new_games)
            min_mana = play(game.cast_poison(), min_mana, new_games)
            min_mana = play(game.cast_recharge(), min_mana, new_games)
        games = new_games
        new_games = set()
        for game in games:
            min_mana = play(game.boss_play(), min_mana, new_games)
        games = new_games
    return min_mana


def play(new_game: Game, min_mana: int, new_games: set[Game]) -> int:
    if new_game.boss_loses():
        return new_game.mana_spent if not min_mana or new_game.mana_spent < min_mana else min_mana
    if not new_game.player_loses() and (not min_mana or new_game.mana_spent < min_mana):
        new_games.add(new_game)
    return min_mana


def part2(rows):
    pass
