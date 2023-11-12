import pygame as pg


class Track(pg.sprite.Sprite):

    def __init__(self, image, pos):
        super().__init__()  # call pg.sprite.Sprite constructor

        self.image = image
        self.rect = self.image.get_rect(center=pos)

    def update(self, dt):
        pass
