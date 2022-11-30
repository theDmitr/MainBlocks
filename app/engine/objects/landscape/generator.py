from engine.objects.blocks.block import Block, Block_dirt, Block_grass, Block_stone
from engine.objects.landscape.column import Column
from random import randint

class Generator:
    def __init__(self, yHigher):
        self.yHigher = yHigher
    def generateColumn(self, x, y, offset = True):
        if offset:
            r = randint(1, 5)
            if r == 1: y -= Block.HEIGHT
            elif r == 2: y += Block.HEIGHT
        column = []
        column.append(Block_grass(x, y))
        for i in range(1, 4):
            column.append(Block_dirt(x, y + Block.HEIGHT * i))
        while column[-1].rect.bottom < self.yHigher:
            column.append(Block_stone(x, column[-1].rect.y + Block.HEIGHT))
        return Column(x, y, column)