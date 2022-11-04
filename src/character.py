import uuid
import pygame.sprite
from weapon import Weapon


class Character(pygame.sprite.Sprite):
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

class Movement:

    x_loc: int = 0
    y_loc: int = 0 # should be located at the feed
    is_ducking = False
    is_sliding = False #can remove this later but just an idea
    is_jumping = False

    def __init__(self, movement_speed: int, height: int, jump_height: int, ducking_height: int,
                 sliding_height: int):
        print("Hello, I am a thing that can move!")
        self.movement_speed = movement_speed
        self.height = height
        self.jump_height = jump_height
        self.ducking_height = ducking_height
        self.sliding_height = sliding_height

    def modify_speed(self, new_speed):
        self.movement_speed = new_speed

    def slide_start(self):
        self.is_sliding = True

    def slide_end(self):
        # IF THERE IS A BLOCK ABOVE
            # KEEP SLIDING
        # ELSE
        self.is_sliding = False

    def get_current_height(self):
        if self.is_sliding:
            return self.sliding_height
        elif self.is_ducking:
            return self.ducking_height
        else:
            return self.height
