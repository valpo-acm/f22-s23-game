from character import Character
from weapon import Weapon


class Player(Character):

    def __init__(self, max_health: int,
                 default_weapon: Weapon, special_ability, movement_speed: int, height: int, jump_height: int, ducking_height: int, sliding_height: int):
        super().__init__(max_health, default_weapon, special_ability, movement_speed, height, jump_height, ducking_height, sliding_height)

        self.height = height
        print("Hello World")

    def attack(self):
        print("Attack")

    def jump(self):
        print("Jump")
