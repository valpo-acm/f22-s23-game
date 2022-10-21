from character import Character
from movement import Movement
from weapon import Weapon

class Boss(Character):
    def __init__(self, char_id: int, movement: Movement, max_health: int,
                 default_weapon: Weapon, special_ability, height:int):
        super().__init__(char_id, movement, max_health, default_weapon, special_ability, height)
        print("I am a boss enemy! Prepare for a real challenge!")

    def boss_attack(self):
        print("Attack")

    def boss_jump(self):
        print("Jump")
