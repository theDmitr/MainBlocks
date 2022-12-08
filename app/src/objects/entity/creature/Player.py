import pygame as pg
from src.objects.blocks.Block import Block

class Player:
    WIDTH = Block.WIDTH // 1.1
    HEIGHT = Block.HEIGHT * 1.9
    blockBreakLenght = 4
    handItem = None
    def __init__(self, x, y):
        self.rect = pg.Rect(x, y, Player.WIDTH, Player.HEIGHT)
        self.speed = 3
        self.moveX, self.moveY = 0, 0
    def draw(self, surface, x, y):
        pg.draw.rect(surface, (0, 255, 0), pg.Rect(self.rect.x + x, self.rect.y + y, self.rect.w, self.rect.h), 2)
        if self.handItem:
            self.handItem(self.rect.x + Block.WIDTH // 2, self.rect.y + Block.HEIGHT // 2).draw(surface, x, y)