import pygame as pg


class Player(pg.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, image, pos):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect(center=pos)

    def update(self, dt):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -= 300 * dt
        if keys[pg.K_s]:
            self.rect.y += 300 * dt
        if keys[pg.K_a]:
            self.rect.x -= 300 * dt
        if keys[pg.K_d]:
            self.rect.x += 300 * dt
