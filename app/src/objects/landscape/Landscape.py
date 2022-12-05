from src.objects.blocks.Block import Block
from src.objects.landscape.Generator import Generator

class Landscape:
    columns = []
    def __init__(self, maxYBlocks):
        self.yHigher, self.yLower = maxYBlocks * Block.HEIGHT // 2, -maxYBlocks * Block.HEIGHT // 2
        self.leftEdge, self.rightEdge = 0, 0
        self.gen = Generator(self.yLower, self.yHigher)
        self.ySize = self.yHigher + abs(self.yLower)
        self.addColumn(0, offset = False)

    def addColumn(self, y, offset = True, right = True):
        if right:
            self.columns.append(self.gen.generateColumn(self.rightEdge, y, offset = offset))
            self.rightEdge += Block.WIDTH
        else:
            self.columns.insert(0, self.gen.generateColumn(self.leftEdge - Block.WIDTH, y, offset = offset))
            self.leftEdge -= Block.WIDTH

    def preGenerate(self, countLeft, countRight):
        for i in range(countLeft):
            self.addColumn(self.columns[-1].y, right = False)
        for i in range(countRight):
            self.addColumn(self.columns[-1].y, right = True)