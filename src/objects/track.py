import pygame as pg


class Track(pg.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, image, pos):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect(center=pos)

    def update(self, dt):
        pass
