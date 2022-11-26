from engine.objects.blocks.block import Block_grass, Block_dirt, Block_stone, Block
from engine.SETTINGS import WIDTH, HEIGHT
from pygame import Surface
from random import randint

class Landscape:
    columns = []
    xLimitLeft, xLimitRight, yLimitDown, yLimitUp = 0, 0, 0, 0
    def __init__(self, obj):
        self.obj = obj
        self.gen = Generator(20 + obj.h * 2)
        self.columns.append(self.gen.generateColumn(obj.x, obj.y + obj.h, first = True))
        self.surface = Surface((self.columns[-1].xLimitRight, self.gen.yLower))
    def addColumnn(self):
        self.columns.append(self.gen.generateColumn(self.columns[-1].xLimitRight, self.columns[-1].blocks[0].rect.y))
        del self.surface
        self.surface = Surface((self.columns[-1].xLimitRight, self.gen.yLower))

    def getSurface(self):
        self.surface.fill((255, 255, 255))
        for column in self.columns:
            if self.obj.right + WIDTH / 2 > column.xLimitLeft and self.obj.x - WIDTH / 2 < column.xLimitRight:
                for block in column.blocks:
                    if self.obj.bottom + HEIGHT / 2 > block.rect.y and self.obj.top - HEIGHT / 2 < block.rect.bottom:
                        block.draw(self.surface)
        return self.surface

class Column:
    blocks = []
    def __init__(self, x, y, blocks):
        self.blocks = blocks
        self.xLimitRight = blocks[0].rect.right
        self.xLimitLeft = blocks[0].rect.x

class Generator:
    def __init__(self, yBlocksLimit):
        self.yLower = yBlocksLimit * Block.HEIGHT
    def generateColumn(self, x, y, first = False):
        if not first:
            r = randint(1, 5)
            if r == 1: y -= Block.HEIGHT
            elif r == 2: y += Block.HEIGHT
        blocks = []
        blocks.append(Block_grass(x, y))
        for i in range(1, randint(3, 4)):
            blocks.append(Block_dirt(x, y + Block.HEIGHT * i))
        while len(blocks) < 20:
            blocks.append(Block_stone(x, blocks[-1].rect.y + Block.HEIGHT))
        return Column(blocks[0].rect.x, blocks[0].rect.y, blocks)