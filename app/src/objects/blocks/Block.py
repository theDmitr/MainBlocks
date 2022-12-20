import pygame as pg
pg.init()
class Block:
    WIDTH, HEIGHT = 40, 40
    cursorColor = (50, 50, 50)
    cursor = False
    def __init__(self, x, y, texture):
        self.rect = pg.Rect(x, y, Block.WIDTH, Block.HEIGHT)
        self.texture1 = pg.transform.scale(pg.image.load(rf"assets\textures\blocks\{texture}.png"), (self.WIDTH, self.HEIGHT))
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

class Block_podzol(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "podzol")

class Block_stone(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "stone")

class Block_cobblestone(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "cobblestone")

class Block_oak_planks(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "oak_planks")

class Block_acacia_planks(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "acacia_planks")

class Block_birch_planks(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "birch_planks")

class Block_dark_oak_planks(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "dark_oak_planks")

class Block_jungle_planks(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "jungle_planks")

class Block_spruce_planks(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "spruce_planks")

class Block_sand(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "sand")

class Block_sandstone(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "sandstone")

class Block_red_sand(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "red_sand")

class Block_red_sandstone(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "red_sandstone")

class Block_glass(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "glass")

class Block_lapis_ore(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "lapis_ore")

class Block_bedrock(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "bedrock")

class Block_air(Block):
    def __init__(self, x, y):
        self.rect = pg.Rect(x, y, Block.WIDTH, Block.HEIGHT)
    def draw(self, surface, xOffset, yOffSet):
        if self.cursor: pg.draw.rect(surface, Block.cursorColor, (self.rect.x + xOffset, self.rect.y + yOffSet, self.rect.w, self.rect.h), 1)

special_blocks = [Block_air, Block_bedrock]
blocks = [i for i in Block.__subclasses__() if not i in special_blocks]