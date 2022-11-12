from abc import abstractmethod
from boss import Boss
from player import Player
from enum import Enum


class Difficulty(Enum):
    EASY = 0
    MEDIUM = 1
    HARD = 2
    EXPERT = 3
    ROSASCO = 4 # CS-250 MIDTERM MODE


class Level:
    name: str
    starting_point: (int, int)
    background: str # file path to image
    player: Player
    boss: Boss
    enemies = []
    structures = [] # if we need moving structures, so they can be accessed
    difficulty: Difficulty
    timer: int = None # if None, there is no timer
    current_score: int
    high_score: int

    def __init__(self):
       pass

    def generate_structures(self):
        pass

    def level_prepare(self):
        self.generate_structures()

        self.level_start()

    @abstractmethod
    def level_start(self):
        pass

    def defeat_boss(self):
        pass
        # make end door available

    def end_game(self):
        print("Level ", self.name, " is over!")

        # return to main screen
