import pygame as pg


class Racer(pg.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()  # call pg.sprite.Sprite constructor

        self.image = image
        self.rect = self.image.get_rect(center=pos)

        self.original_image = image

    def update(self, dt):
        """
        Update position of racer based on the keys that are pressed
        """
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -= 300 * dt
            self.image = pg.transform.rotate(self.original_image, 0)
        if keys[pg.K_s]:
            self.rect.y += 300 * dt
            self.image = pg.transform.rotate(self.original_image, 180)
        if keys[pg.K_a]:
            self.rect.x -= 300 * dt
            self.image = pg.transform.rotate(self.original_image, 90)
        if keys[pg.K_d]:
            self.rect.x += 300 * dt
            self.image = pg.transform.rotate(self.original_image, 270)
