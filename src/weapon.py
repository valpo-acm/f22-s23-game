from enum import Enum

class Weapon_Type(Enum):
    PISTOL = 0
    SHOTGUN = 1
    AR = 2
    SNIPER = 3
    SMG = 4
    RPG = 5

class Weapon:
    ammo: int

    def __init__(self, id: int, damage: int, max_ammo: int, fire_rate: int, spread: float,
                 area_damage: bool, area_damage_radius: int, weapon_type: Weapon_Type):
        self.id = id
        self.damage = damage
        self.max_ammo = max_ammo
        self.fire_rate = fire_rate
        self.spread = spread
        self.area_damage = area_damage
        self.area_damage_radius = area_damage_radius
        self.weapon_type = weapon_type
