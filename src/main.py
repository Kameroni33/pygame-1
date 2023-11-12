# Example file showing a circle moving on screen
import pygame as pg
import random as rd

from objects.racer import Racer
from objects.track import Track


# Constants
SURFACE_COLOR = "black"
WIDTH = 800
HEIGHT = 800

# global variables
running = True
dt = 0

# pygame setup
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

# load assets
RACER1 = pg.image.load("assets/images/racer1-001.png").convert_alpha()
RACER2 = pg.image.load("assets/images/racer2-001.png").convert_alpha()
TRACK_BACKGROUND = pg.image.load("assets/images/track-background.png").convert_alpha()
TRACK_VERTICAL = pg.image.load("assets/images/track-straight-001.png").convert_alpha()
TRACK_HORIZONTAL = pg.image.load("assets/images/track-straight-002.png").convert_alpha()
TRACK_INTERSECTION = pg.image.load("assets/images/track-intersection-001.png").convert_alpha()
TRACK_TURN_SE = pg.image.load("assets/images/track-turn-001.png").convert_alpha()
TRACK_TURN_SW = pg.image.load("assets/images/track-turn-002.png").convert_alpha()
TRACK_TURN_NW = pg.image.load("assets/images/track-turn-003.png").convert_alpha()
TRACK_TURN_NE = pg.image.load("assets/images/track-turn-004.png").convert_alpha()

# setup sprites
track = pg.sprite.Group()
racers = pg.sprite.Group()
track1 = (
    (TRACK_TURN_SE, (80, 80)),
    (TRACK_HORIZONTAL, (240, 80)),
    (TRACK_TURN_SW, (400, 80)),
    (TRACK_BACKGROUND, (560, 80)),
    (TRACK_BACKGROUND, (720, 80)),
)
for tile in track1:
    new_tile = Track(tile[0], tile[1])
    track.add(new_tile)
racer = Racer(RACER1, (screen.get_width() / 2, screen.get_height() / 2))



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
