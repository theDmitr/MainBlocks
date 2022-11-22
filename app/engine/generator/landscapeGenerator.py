from engine.objects.blocks.block import Block_grass, Block_dirt, Block_stone
from random import randint
def generateLandscape(xOffSet, yOffSet, count, startX = 0, startY = 200):
    blocks = []
    for i in range(count):
        column = []
        if randint(0, 5) == 1: yOffSet -= Block_grass.HEIGHT
        elif randint(0, 5) == 1: yOffSet += Block_grass.HEIGHT
        column.append(Block_grass(startX + xOffSet * i, startY + yOffSet))
        for j in range(1, randint(2, 5)):
            column.append(Block_dirt(startX + xOffSet * i, startY + yOffSet + Block_grass.HEIGHT * j))
        while column[-1].getPos()[1] < 600: 
            column.append(Block_stone(startX + xOffSet * i, column[-1].getPos()[1] + Block_grass.HEIGHT))
        blocks.append(column)
    return blocks