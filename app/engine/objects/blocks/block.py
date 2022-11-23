import pygame as pg
pg.init()
class Block:
    WIDTH, HEIGHT = 40, 40
    cursor = False
    def __init__(self, x, y, texture):
        self.rect = pg.Rect(x, y, Block.WIDTH, Block.HEIGHT)
        self.texture1 = pg.transform.scale(pg.image.load(rf"app\assets\textures\blocks\{texture}.png"), (self.WIDTH, self.HEIGHT))
    def getPos(self):
        return (self.rect.x, self.rect.y)
    def move(self, x, y):
        self.rect.x, self.rect.y = x, y
    def afterBreak(self):
        return
    def getCollisionByPoint(self, pos):
        return self.rect.collidepoint(pos)
    def draw(self, surface):
        surface.blit(self.texture1, self.rect)
        if self.cursor: pg.draw.rect(surface, (50, 50, 50), self.rect, 1)

class Block_grass(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "grass")

class Block_dirt(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "dirt")

class Block_stone(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "stone")