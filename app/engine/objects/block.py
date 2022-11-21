import pygame as pg
pg.init()
class Block:
    WIDTH, HEIGHT = 40, 40
    def __init__(self, x, y, texture):
        self.rect = pg.Rect(x, y, Block.WIDTH, Block.HEIGHT)
        self.texture1 = pg.transform.scale(pg.image.load(rf"app/assets/textures/blocks/{texture}.png"), (self.WIDTH, self.HEIGHT))
    def getPos(self):
        return (self.rect.x, self.rect.y)
    def move(self, x, y):
        self.rect.x, self.rect.y = x, y
    def draw(self, surface):
        surface.blit(self.texture1, self.rect)