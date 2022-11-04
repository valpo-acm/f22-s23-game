from character import Character
from weapon import Weapon


class Boss(Character):
    def __init__(self, max_health: int, default_weapon: Weapon,
                 special_ability, height: int, movement_speed: int, jump_height: int, ducking_height: int,
                 sliding_height: int):
        super().__init__(max_health, default_weapon, special_ability, height, movement_speed, jump_height,
                         ducking_height, sliding_height)
        print("I am a boss enemy! Prepare for a real challenge!")

    def boss_attack(self):
        print("Attack")

    def boss_jump(self):
        print("Jump")
