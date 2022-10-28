
import uuid
from movement import Movement
from weapon import Weapon

class Character(Movement):

    health: int
    current_weapon = None
    shield_hand = None
    powerups = []
    direction_facing = False # False = Left; True = Right

    def __init__(self, max_health: int,
                 default_weapon: Weapon, special_ability, movement_speed: int, height: int, jump_height: int, ducking_height: int,
                 sliding_height: int):
        print("Hello! I am a character!")

        super().__init__(movement_speed, height, jump_height, ducking_height, sliding_height)

        self.char_id = uuid.uuid4()
        self.max_health = max_health
        self.default_weapon = default_weapon
        self.special_ability = special_ability

