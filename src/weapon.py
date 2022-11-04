from enum import Enum

class Weapon_Type(Enum):
    PISTOL = 0 # standard/starter weapon
    SHOTGUN = 1 #high damage/medium fire rate
    AR = 2 #high fire rate/standard damage
    SNIPER = 3 #low fire rate/high damage
    SMG = 4 #high fire rate/low damage
    RPG = 5 #low fire rate/high damage/area damage

class Weapon:
    ammo: int

    def __init__(self, damage: int, max_ammo: int, fire_rate: int, spread: float,
                 area_damage: bool, area_damage_radius: int, weapon_type: Weapon_Type):
        self.damage = damage
        self.max_ammo = max_ammo
        self.fire_rate = fire_rate
        self.spread = spread
        self.area_damage = area_damage
        self.area_damage_radius = area_damage_radius
        self.weapon_type = weapon_type
