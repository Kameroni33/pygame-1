# Example file showing a circle moving on screen
import pygame as pg
import random as rd

from utils.constants import SURFACE_COLOR, WIDTH, HEIGHT
from objects.player import Player
from objects.item import Item

# pg setup
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
running = True
dt = 0

# load assets
PLAYER_1 = pg.image.load("assets/images/player1.png").convert_alpha()
ITEM_1 = pg.image.load("assets/images/item1.png").convert_alpha()

# setup sprites
group1 = pg.sprite.Group()

center = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player1 = Player(PLAYER_1, center)

group1.add(player1)

# initialize random number generator
rd.seed()


def generate_item():
    if rd.random() > 0.99:
        new_item = Item(ITEM_1, (rd.randint(0, WIDTH), rd.randint(0, HEIGHT)))
        group1.add(new_item)


while running:
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # call all `update` function for all sprites in the group
    group1.update(dt)
    # clears the screen by writing SURFACE_COLOR
    screen.fill(SURFACE_COLOR)
    # draw every item in group1
    group1.draw(screen)

    # use `flip` to actually display all drawn elements to the screen
    pg.display.flip()

    # randomly generate a new item at a random position
    generate_item()

    dt = clock.tick(60) / 1000

pg.quit()
