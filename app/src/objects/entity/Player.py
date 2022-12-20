import pygame as pg
from src.objects.blocks.Block import Block

class Player(pg.sprite.Sprite):
    WIDTH, HEIGHT = Block.WIDTH // 1.1, Block.HEIGHT * 1.9
    blockBreakLenght = 4
    handItem = None
    speed = 3
    def __init__(self, x, y):
        super().__init__()
        self.moveX, self.moveY = 0.0, 0.0
        self.image = None
        self.rect = pg.Rect(x, y, Player.WIDTH, Player.HEIGHT)
    def update(self):
        self.rect.x += self.moveX
        self.rect.y += self.moveY
    def draw(self, surface, x, y):
        pg.draw.rect(surface, (0, 255, 0), pg.Rect(self.rect.x + x, self.rect.y + y, self.rect.w, self.rect.h), 2)
        if self.handItem != None:
            self.handItem(self.rect.x + Block.WIDTH // 2, self.rect.y + Block.HEIGHT // 2).draw(surface, x, y)