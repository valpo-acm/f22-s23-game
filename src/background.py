import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bgimage = pygame.image.load("Background.jpg")
        self.rectBGimg = self.bgimage.get_rect()
        self.bgY = 0
        self.bgX = 0

    def render(self, displaysurface=None, xsize=0, ysize=0):
        picture = self.bgimage
        picture = pygame.transform.scale(picture, (xsize, ysize))
        displaysurface.blit(picture, (self.bgX, self.bgY))
