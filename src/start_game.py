#!/usr/bin/python3

import pygame
import pygame_menu
from pygame.constants import QUIT

from background import Background

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)


def game():
    print("Starting Game")
    menu = pygame_menu.Menu("TestMenu", 400, 400)
    menu.add.button("Test", test_button)
    continue_game = True
    background = Background()

    while continue_game:

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                continue_game = False

        if menu.is_enabled():
            menu.update(events)
            menu.draw(display_surface)

        pygame.display.update()

        background.render(display_surface, WINDOW_WIDTH, WINDOW_HEIGHT)


def test_button():
    print("Pressed Test Button")


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
    pygame.display.set_caption("Blob Warrior")
    display_surface.fill((194, 63, 16))
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
