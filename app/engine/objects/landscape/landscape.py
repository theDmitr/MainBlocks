from engine.objects.blocks.block import Block
from engine.objects.landscape.generator import Generator

class Landscape:
    columns = []
    def __init__(self, maxYBlocks):
        self.yHigher, self.yLower = maxYBlocks * Block.HEIGHT, 0
        self.leftEdge, self.rightEdge = 0, 0
        self.gen = Generator(self.yHigher)

    def addColumn(self, y, offset = True, right = True):
        if right:
            self.columns.append(self.gen.generateColumn(self.rightEdge, y, offset = offset))
            self.rightEdge += Block.WIDTH
        else:
            self.columns.insert(0, self.gen.generateColumn(self.leftEdge - Block.WIDTH, y, offset = offset))
            self.leftEdge -= Block.WIDTH