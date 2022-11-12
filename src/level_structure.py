import pygame.sprite
import pygame.draw


class LevelStructure(pygame.sprite.Sprite):
    origin: (int, int) # upper left corner
    is_moving_horizontal = False
    is_moving_vertical = False
    is_walkthrough = False  # looks like background but can jump on top of
    is_rotating = False
    rotate_direction = False  # False = left, True = right
    causes_damage = False
    is_slippery = False

    def __init__(self, shape_type: pygame.draw, origin: (int, int), struct_type: str):
        super().__init__()
        self.shape_type = shape_type
        self.origin = origin
        self.struct_type = struct_type

