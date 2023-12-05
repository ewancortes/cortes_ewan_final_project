import pygame as pg
import os


SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pg.display.set_caption("Chrome Dino Runner")

Ico = pg.image.load("Assets/DinoWallpaper.png")
pg.display.set_icon(Ico)

RUNNING = [
    pg.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
    pg.image.load(os.path.join("Assets/Dino", "DinoRun2.png")),
]
JUMPING = pg.image.load(os.path.join("Assets/Dino", "DinoJump.png"))
DUCKING = [
    pg.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
    pg.image.load(os.path.join("Assets/Dino", "DinoDuck2.png")),
]

SMALL_CACTUS = [
    pg.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
    pg.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
    pg.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png")),
]
LARGE_CACTUS = [
    pg.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
    pg.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
    pg.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png")),
]

BIRD = [
    pg.image.load(os.path.join("Assets/Bird", "Bird1.png")),
    pg.image.load(os.path.join("Assets/Bird", "Bird2.png")),
]

CLOUD = pg.image.load(os.path.join("Assets/Other", "Cloud.png"))

BG = pg.image.load(os.path.join("Assets/Other", "Track.png"))

FONT_COLOR=(0,0,0)