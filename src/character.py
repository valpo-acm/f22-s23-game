from movement import Movement
class Character:
    health: int
    current_weapon = None
    shield_hand = None
    powerups = []

    def __init__(self, id: int, movement: Movement, max_health: int, default_weapon, special_ability, height:int):
        print("Hello! I am a character!")
        self.id = id
        self.movement = movement
        self.max_health = max_health
        self.default_weapon = default_weapon
        self.special_ability = special_ability
        
