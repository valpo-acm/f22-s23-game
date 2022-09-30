#!/usr/bin/python3

import time
import pygame
from pygame.locals import *


WINDOW_HEIGHT = 800
WINDOW_WIDTH = 600


class Character:
    def __init__(self, name: str):
        print("Hello, my name is ", name)


def game():
    print("Starting Game")

    continue_game = True

    while continue_game:

        character = Character("Jordan")

        for event in pygame.event.get():
            if event.type == QUIT:
                continue_game = False



def welcome():
    print("Welcome to the game!")

    # if we had a custom crosshair image, we could use that instead
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)


def load_config():
    print("Loading config...")


def initialize():
    print("Initializing...")
    load_config()

    pygame.init()   
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)


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
