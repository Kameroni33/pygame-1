import pygame as pg

from objects.racer import Racer
from objects.track import Track


# constants
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

# setup track sprites
track = pg.sprite.Group()
racers = pg.sprite.Group()
track1 = (
    # row 1
    (TRACK_TURN_SE,      (80,  80)),
    (TRACK_HORIZONTAL,   (240, 80)),
    (TRACK_TURN_SW,      (400, 80)),
    (TRACK_BACKGROUND,   (560, 80)),
    (TRACK_BACKGROUND,   (720, 80)),
    # row 2
    (TRACK_VERTICAL,     (80,  240)),
    (TRACK_BACKGROUND,   (240, 240)),
    (TRACK_VERTICAL,     (400, 240)),
    (TRACK_BACKGROUND,   (560, 240)),
    (TRACK_BACKGROUND,   (720, 240)),
    # row 3
    (TRACK_TURN_NE,      (80,  400)),
    (TRACK_HORIZONTAL,   (240, 400)),
    (TRACK_INTERSECTION, (400, 400)),
    (TRACK_HORIZONTAL,   (560, 400)),
    (TRACK_TURN_SW,      (720, 400)),
    # row 4
    (TRACK_BACKGROUND,   (80,  560)),
    (TRACK_BACKGROUND,   (240, 560)),
    (TRACK_VERTICAL,     (400, 560)),
    (TRACK_BACKGROUND,   (560, 560)),
    (TRACK_VERTICAL,     (720, 560)),
    # row 5
    (TRACK_BACKGROUND,   (80,  720)),
    (TRACK_BACKGROUND,   (240, 720)),
    (TRACK_TURN_NE,      (400, 720)),
    (TRACK_HORIZONTAL,   (560, 720)),
    (TRACK_TURN_NW,      (720, 720)),
)
for tile in track1:
    new_tile = Track(tile[0], tile[1])
    track.add(new_tile)

# setup racer sprites
racer = Racer(RACER1, (screen.get_width() / 2, screen.get_height() / 2))
racers.add(racer)


# main game loop
while running:
    # poll for events
    for event in pg.event.get():
        if event.type == pg.QUIT:  # pg.QUIT means window closed (ie. 'x' button)
            running = False

    # call `update` function for all sprites in the group(s)
    track.update(dt)
    racers.update(dt)

    # clears the screen by writing SURFACE_COLOR
    screen.fill(SURFACE_COLOR)

    # draw all items in the group(s)
    track.draw(screen)
    racers.draw(screen)

    # use `flip` to actually display all drawn elements to the screen
    pg.display.flip()

    # limit game to 60 FPS and get delta time
    dt = clock.tick(60) / 1000

# end of game
pg.quit()
