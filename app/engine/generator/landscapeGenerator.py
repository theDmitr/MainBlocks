from engine.objects.blocks.block import Block_grass, Block_dirt, Block_stone, Block
from pygame import Surface
from random import randint
from engine.screen import Screen
class Landscape:
    columns = []
    def __init__(self, lenght):
        self.generate(lenght)
    def regenerate(self):
        self.generate(self.lenght)
    def generate(self, lenght, startY = 100):
        gen = Generator()
        columns = [gen.generateColumn(x, startY) for x in range(lenght)]
        self.xLimitLeft, self.xLimitRight = columns[0].x * Block.WIDTH, columns[-1].x * Block.WIDTH + Block.WIDTH
        self.yLimitDown = columns[0].y + len(columns[0].blocks) * Block.HEIGHT
        self.columns = columns
        self.lenght = lenght
        self.surface = Surface((self.xLimitRight, self.yLimitDown))
    def getSurface(self):
        self.surface.fill((255, 255, 255))
        self.draw(self.surface)
        return self.surface
    def draw(self, surface):
        for column in self.columns:
            for block in column.blocks: block.draw(surface)

class Column:
    blocks = []
    def __init__(self, blocks, x, y):
        self.blocks = blocks
        self.x, self.y = x, y

class Generator:
    yOffSet = 0
    def __init__(self):
        pass
    def generateColumn(self, x, y):
        column = []
        r = randint(0, 10)
        if r == 2: self.yOffSet += 1
        elif r == 3: self.yOffSet -= 1
        column.append(Block_grass(x * Block.WIDTH, y + Block.HEIGHT * self.yOffSet))
        for j in range(1, randint(2, 5)):
            column.append(Block_dirt(x * Block.WIDTH, y + Block.HEIGHT * self.yOffSet + Block.HEIGHT * j))
        while column[-1].getPos()[1] < 600: 
            column.append(Block_stone(x * Block.WIDTH, column[-1].getPos()[1] + Block.HEIGHT))
        return Column(column, x, y)