#!/usr/bin/python3

import pygame
import yaml
from pygame.constants import QUIT
from level_structure import LevelStructure
from pathlib import Path
#from pygame.locals import *

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 600

# Absolute path of the folder that contains this file.
PATH = str(Path(__file__).parent.absolute()) + "/"

config: dict
data: dict

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)


def game():
    print("Starting Game")

    continue_game = True

    while continue_game:

        for event in pygame.event.get():
            if event.type == QUIT:
                continue_game = False


def welcome():
    print("Welcome to the game!")

    # if we had a custom crosshair image, we could use that instead
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)


def load_config():
    print("Loading config...")

    global config

    # Open and close the config file safely.
    with open(PATH + 'config.yaml', 'r') as file:
        config = yaml.safe_load(file)


def initialize():
    print("Initializing...")
    load_config()

    pygame.init()
    pygame.display.set_caption("Blob Warrior")
    display_surface.fill((194,63,16))
    pygame.display.update()


def close():
    print("Closing...")
    pygame.quit()


def main():
    initialize()
    welcome()
    game()
    close()


if __name__ == "__main__":
    main()
