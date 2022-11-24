import pygame as pg
from engine.objects.blocks.block import Block

class Player:
    WIDTH = Block.WIDTH
    HEIGHT = Block.HEIGHT * 2
    def __init__(self, x, y):
        self.rect = pg.Rect(x, y, Player.WIDTH, Player.HEIGHT)
        self.speed = 3
        self.moveX, self.moveY = 0, 0
    def draw(self, surface):
        pg.draw.rect(surface, (0, 255, 0), self.rect, 2)