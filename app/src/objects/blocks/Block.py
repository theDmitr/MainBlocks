import pygame as pg
pg.init()
class Block:
    WIDTH, HEIGHT = 40, 40
    cursorColor = (50, 50, 50)
    cursor = False
    def __init__(self, x, y, texture):
        self.rect = pg.Rect(x, y, Block.WIDTH, Block.HEIGHT)
        self.texture1 = pg.transform.scale(pg.image.load(rf"app\assets\textures\blocks\{texture}.png"), (self.WIDTH, self.HEIGHT))
    def afterBreak(self):
        return
    def draw(self, surface, xOffset, yOffSet):
        surface.blit(self.texture1, (self.rect.x + xOffset, self.rect.y + yOffSet, self.rect.w, self.rect.h))
        if self.cursor: pg.draw.rect(surface, Block.cursorColor, (self.rect.x + xOffset, self.rect.y + yOffSet, self.rect.w, self.rect.h), 1)

class Block_grass(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "grass")

class Block_dirt(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "dirt")

class Block_stone(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "stone")

class Block_bedrock(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "bedrock")

class Block_air(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "glass")