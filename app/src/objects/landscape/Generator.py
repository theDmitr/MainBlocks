from random import randint
from src.objects.blocks.Block import Block, Block_dirt, Block_grass, Block_stone, Block_bedrock, Block_air
from src.objects.landscape.Column import Column

class Generator:
    def __init__(self, yLower, yHigher):
        self.yLower = yLower
        self.yHigher = yHigher
        self.limits = (yLower // 4, yHigher // 4)
    def generateColumn(self, x, y, offset = True): 
        if offset:
            r = randint(1, 5)
            if r == 1 and y > self.limits[0]: y -= Block.HEIGHT
            elif r == 2 and y < self.limits[1]: y += Block.HEIGHT

        column = []

        for i in range(self.yLower // Block.HEIGHT, y // Block.HEIGHT): # y // Block.HEIGHT
            column.append(Block_air(x, i * Block.HEIGHT))

        column.append(Block_grass(x, y))
        for i in range(1, 4):
            column.append(Block_dirt(x, y + Block.HEIGHT * i))
        
        while column[-1].rect.bottom < self.yHigher - Block.HEIGHT:
            column.append(Block_stone(x, column[-1].rect.y + Block.HEIGHT))

        column.append(Block_bedrock(x, column[-1].rect.y + Block.HEIGHT))
        return Column(x, y, column)