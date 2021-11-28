from __future__ import annotations
import copy

BOSS_DAMAGE = 8

EFFECT_SHIELD = 1
EFFECT_POISON = 2
EFFECT_RECHARGE = 3


class Game:
    def __init__(self, hard=False):
        self.player_hitpoints: int = 50
        self.player_armor: int = 0
        self.boss_hitpoints: int = 55
        self.mana: int = 500
        self.effects: dict[int, int] = {}
        self.mana_spent: int = 0
        self.invalid_cast: bool = False
        self.hard = hard

    def __repr__(self) -> str:
        return f"p_hp: {self.player_hitpoints}, b_hp: {self.boss_hitpoints}, mana: {self.mana}, spent: {self.mana_spent}"

    def _key(self) -> tuple[int, int, int, int, int, bool, bool, int]:
        effects = 0
        if EFFECT_SHIELD in self.effects:
            effects += self.effects[EFFECT_SHIELD]
        if EFFECT_POISON in self.effects:
            effects += self.effects[EFFECT_POISON] * 10
        if EFFECT_RECHARGE in self.effects:
            effects += self.effects[EFFECT_RECHARGE] * 100
        return (
            self.player_hitpoints,
            self.player_armor,
            self.boss_hitpoints,
            self.mana,
            self.mana_spent,
            self.invalid_cast,
            self.hard,
            effects
        )

    def __hash__(self) -> int:
        return hash(self._key())

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Game):
            return False
        return self._key() == other._key()

    def player_loses(self) -> bool:
        return self.invalid_cast or self.mana < 0 or self.player_hitpoints <= 0

    def boss_loses(self) -> bool:
        return self.boss_hitpoints <= 0

    def boss_play(self) -> Game:
        game = self._next_turn(player_turn=False)
        if game.boss_loses():
            return game
        damage = max(1, BOSS_DAMAGE - game.player_armor)
        game.player_hitpoints -= damage
        return game

    def cast_magic_missile(self) -> Game:
        game = self._next_turn()
        if game.player_loses() or game.boss_loses():
            return game
        game._spend(53)
        if game.player_loses():
            return game
        game.boss_hitpoints -= 4
        return game

    def cast_drain(self) -> Game:
        game = self._next_turn()
        if game.player_loses() or game.boss_loses():
            return game
        game._spend(73)
        if game.player_loses():
            return game
        game.boss_hitpoints -= 2
        game.player_hitpoints += 2
        return game

    def cast_shield(self) -> Game:
        return self._cast_effect(EFFECT_SHIELD, 113, 6)

    def cast_poison(self) -> Game:
        return self._cast_effect(EFFECT_POISON, 173, 6)

    def cast_recharge(self) -> Game:
        return self._cast_effect(EFFECT_RECHARGE, 229, 5)

    def _cast_effect(self, effect, mana, duration) -> Game:
        game = self._next_turn()
        if game.player_loses() or game.boss_loses():
            return game
        game.invalid_cast = effect in game.effects
        game._spend(mana)
        if game.player_loses():
            return game
        game.effects[effect] = duration
        return game

    def _spend(self, mana) -> None:
        self.mana -= mana
        self.mana_spent += mana

    def _next_turn(self, player_turn: bool = True) -> Game:
        game = copy.deepcopy(self)
        if player_turn and game.hard:
            game.player_hitpoints -= 1
            if game.player_loses():
                return game
        game._handle_effects()
        return game

    def _handle_effects(self) -> None:
        self.player_armor = 7 if EFFECT_SHIELD in self.effects else 0
        if EFFECT_POISON in self.effects:
            self.boss_hitpoints -= 3
        if EFFECT_RECHARGE in self.effects:
            self.mana += 101
        self._decrease_effects()

    def _decrease_effects(self) -> None:
        for effect, duration in list(self.effects.items()):
            duration -= 1
            if duration:
                self.effects[effect] = duration
            else:
                del self.effects[effect]
