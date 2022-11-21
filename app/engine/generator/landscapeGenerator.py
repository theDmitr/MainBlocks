from engine.objects.block import Block
from random import randint
def generateLandscape(xOffSet, yOffSet, count, startX = 0, startY = 200):
    blocks = []
    for i in range(count):
        if randint(0, 5) == 1: yOffSet -= Block.HEIGHT
        elif randint(0, 5) == 1: yOffSet += Block.HEIGHT
        blocks.append(Block(startX + xOffSet * i, startY + yOffSet, "grass"))
        for j in range(1, randint(2, 5)):
            blocks.append(Block(startX + xOffSet * i, startY + yOffSet + Block.HEIGHT * j, "dirt"))
        while blocks[-1].getPos()[1] < 600: 
            blocks.append(Block(startX + xOffSet * i, blocks[-1].getPos()[1] + Block.HEIGHT, "stone"))
    return blocks