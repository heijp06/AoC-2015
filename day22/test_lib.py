import pytest
from lib import part1, part2
from game import EFFECT_POISON, EFFECT_SHIELD, Game, EFFECT_RECHARGE


def test_game():
    game = Game()

    assert game.player_hitpoints == 50
    assert game.player_armor == 0
    assert game.boss_hitpoints == 55
    assert game.mana == 500
    assert game.effects == {}
    assert game.mana_spent == 0
    assert game.invalid_cast == False

    game = game.cast_recharge()

    assert game.player_hitpoints == 50
    assert game.player_armor == 0
    assert game.boss_hitpoints == 55
    assert game.mana == 271
    assert game.effects == {EFFECT_RECHARGE: 5}
    assert game.mana_spent == 229
    assert game.invalid_cast == False

    game = game.boss_play()

    assert game.player_hitpoints == 42
    assert game.player_armor == 0
    assert game.boss_hitpoints == 55
    assert game.mana == 372
    assert game.effects == {EFFECT_RECHARGE: 4}
    assert game.mana_spent == 229
    assert game.invalid_cast == False

    game = game.cast_drain()

    assert game.player_hitpoints == 44
    assert game.player_armor == 0
    assert game.boss_hitpoints == 53
    assert game.mana == 400
    assert game.effects == {EFFECT_RECHARGE: 3}
    assert game.mana_spent == 302
    assert game.invalid_cast == False

    game = game.boss_play()

    assert game.player_hitpoints == 36
    assert game.player_armor == 0
    assert game.boss_hitpoints == 53
    assert game.mana == 501
    assert game.effects == {EFFECT_RECHARGE: 2}
    assert game.mana_spent == 302
    assert game.invalid_cast == False

    game = game.cast_shield()

    assert game.player_hitpoints == 36
    assert game.player_armor == 0
    assert game.boss_hitpoints == 53
    assert game.mana == 489
    assert game.effects == {EFFECT_RECHARGE: 1, EFFECT_SHIELD: 6}
    assert game.mana_spent == 415
    assert game.invalid_cast == False

    game = game.boss_play()

    assert game.player_hitpoints == 35
    assert game.player_armor == 7
    assert game.boss_hitpoints == 53
    assert game.mana == 590
    assert game.effects == {EFFECT_SHIELD: 5}
    assert game.mana_spent == 415
    assert game.invalid_cast == False

    game = game.cast_magic_missile()

    assert game.player_hitpoints == 35
    assert game.player_armor == 7
    assert game.boss_hitpoints == 49
    assert game.mana == 537
    assert game.effects == {EFFECT_SHIELD: 4}
    assert game.mana_spent == 468
    assert game.invalid_cast == False

    game = game.boss_play()

    assert game.player_hitpoints == 34
    assert game.player_armor == 7
    assert game.boss_hitpoints == 49
    assert game.mana == 537
    assert game.effects == {EFFECT_SHIELD: 3}
    assert game.mana_spent == 468
    assert game.invalid_cast == False

    game = game.cast_magic_missile()

    assert game.player_hitpoints == 34
    assert game.player_armor == 7
    assert game.boss_hitpoints == 45
    assert game.mana == 484
    assert game.effects == {EFFECT_SHIELD: 2}
    assert game.mana_spent == 521
    assert game.invalid_cast == False

    game = game.boss_play()

    assert game.player_hitpoints == 33
    assert game.player_armor == 7
    assert game.boss_hitpoints == 45
    assert game.mana == 484
    assert game.effects == {EFFECT_SHIELD: 1}
    assert game.mana_spent == 521
    assert game.invalid_cast == False

    game = game.cast_magic_missile()

    assert game.player_hitpoints == 33
    assert game.player_armor == 7
    assert game.boss_hitpoints == 41
    assert game.mana == 431
    assert game.effects == {}
    assert game.mana_spent == 574
    assert game.invalid_cast == False

    game = game.boss_play()

    assert game.player_hitpoints == 25
    assert game.player_armor == 0
    assert game.boss_hitpoints == 41
    assert game.mana == 431
    assert game.effects == {}
    assert game.mana_spent == 574
    assert game.invalid_cast == False

    game = game.cast_poison()

    assert game.player_hitpoints == 25
    assert game.player_armor == 0
    assert game.boss_hitpoints == 41
    assert game.mana == 258
    assert game.effects == {EFFECT_POISON: 6}
    assert game.mana_spent == 747
    assert game.invalid_cast == False

    game = game.boss_play()

    assert game.player_hitpoints == 17
    assert game.player_armor == 0
    assert game.boss_hitpoints == 38
    assert game.mana == 258
    assert game.effects == {EFFECT_POISON: 5}
    assert game.mana_spent == 747
    assert game.invalid_cast == False
