from character import Character
from weapon import Weapon


class Enemy(Character):
    def __init__(self, max_health: int,
                 default_weapon: Weapon, movement_speed: int, height: int, jump_height: int, ducking_height: int,
                 sliding_height: int):
        super().__init__(max_health, default_weapon, None, movement_speed,height, jump_height, ducking_height, sliding_height)
        print("I am an enemy! I'm going to defeat you!")

    def attack(self):
        print("Attack")

    def jump(self):
        print("Jump")
