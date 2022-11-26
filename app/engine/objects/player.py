import pygame as pg
from engine.objects.blocks.block import Block

class Player:
    WIDTH = Block.WIDTH
    HEIGHT = Block.HEIGHT * 2
    def __init__(self, x, y):
        self.rect = pg.Rect(x, y, Player.WIDTH, Player.HEIGHT)
        self.speed = 3
        self.moveX, self.moveY = 0, 0
    def draw(self, surface, x, y):
        pg.draw.rect(surface, (0, 255, 0), pg.Rect(self.rect.x + x, self.rect.y + y, self.rect.w, self.rect.h), 2)