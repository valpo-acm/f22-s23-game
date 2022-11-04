import pygame.sprite


class LevelStructure(pygame.sprite.Sprite):
    length: int
    height: int
    origin: (int, int)
    is_moving_horizontal = False
    is_moving_vertical = False
    is_walkthrough = False  # looks like background but can jump on top of
    is_rotating = False
    rotate_direction = False  # False = left, True = right
    causes_damage = False
    is_slippery = False

    def __init__(self, length: int, height: int, origin: (int, int), struct_type: str):
        super().__init__()
        self.length = length
        self.height = height
        self.origin = origin
        self.struct_type = struct_type

    def change_length(self, new_length):
        self.length = new_length

    def change_height(self, new_height):
        self.height = new_height


class RoundStructure(LevelStructure):
    radius: int

    def __init__(self, length: int, height: int, origin: (int, int), type: str):
        super().__init__(length, height, origin, type)
        print("This is a round structure (i.e. circle/ellipse)")


class SlopedStructure(LevelStructure):
    def __init__(self, length: int, height: int, origin: (int, int), type: str):
        super().__init__(length, height, origin, type)
        print("This is a sloped structure (i.e. triangle)")


class FlatStructure(LevelStructure):

    def __init__(self, length: int, height: int, origin: (int, int), type: str):
        super().__init__(length, height, origin, type)
        print("I am a flat structure (i.e. rectangle/square)")
