from character import Character
from movement import Movement
from weapon import Weapon

class Enemy(Character):
    def __init__(self, char_id: int, movement: Movement, max_health: int,
                 default_weapon: Weapon, height:int):
        super().__init__(char_id, movement, max_health, default_weapon, None, height)
        print("I am an enemy! I'm going to defeat you!")

    def enemy_attack(self):
        print("Attack")

    def enemy_jump(self):
        print("Jump")
