from level_structure import LevelStructure

class FlatStructure(LevelStructure):

    def __init__(self, length: int, height: int, origin: (int, int), type: str):
        super().__init__(length, height, origin, type)
        print("I am a flat structure (i.e. rectangle/square)")
