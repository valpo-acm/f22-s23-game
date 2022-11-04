from level_structure import LevelStructure


class SlopedStructure(LevelStructure):
    def __init__(self, length: int, height: int, origin: (int, int), type: str):
        super().__init__(length, height, origin, type)
        print("This is a sloped structure (i.e. triangle)")
