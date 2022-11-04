from level_structure import LevelStructure


class RoundStructure(LevelStructure):
    radius: int

    def __init__(self, length: int, height: int, origin: (int, int), type: str):
        super().__init__(length, height, origin, type)
        print("This is a round structure (i.e. circle/ellipse)")
