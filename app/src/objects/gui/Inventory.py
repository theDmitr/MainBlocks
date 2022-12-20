import pygame as pg
from math import ceil
from src.screen.properties import WIDTH, HEIGHT
from src.objects.blocks.Block import Block, blocks, special_blocks

gray_1 = (140, 140, 140)
gray_2 = (80, 80, 80)
gray_3 = (100, 100, 100)

cellW, cellH = Block.WIDTH + 6, Block.HEIGHT + 6

class Scrollbar:
    def __init__(self, x, y, width, height):
        self.rect_1 = pg.Rect(x, y, width, height)
        self.rect_2 = pg.Rect(x, y, width, height // 4)
    def handler(self, x, y, h):
        pos = pg.mouse.get_pos()
        if pg.mouse.get_pressed()[0] and self.rect_2.collidepoint(pos[0] - x, pos[1] - y):
            self.rect_2.y += pg.mouse.get_rel()[1]
            if self.rect_2.y < 0: self.rect_2.y = 0
            elif self.rect_2.bottom > h: self.rect_2.bottom = h
        pg.mouse.get_rel()
    def draw(self, surface):
        pg.draw.rect(surface, gray_3, self.rect_1)
        pg.draw.rect(surface, gray_2, self.rect_2)

class Grid:
    def __init__(self, rows):
        self.rows, self.columns = max(6, rows), 5
        self.content = [None for _ in range(self.columns) for _ in range(self.rows)]
        self.width, self.height = 5 * cellW + 50, 3 * cellH + 25
        self.x, self.y = (WIDTH - self.width) // 2, (HEIGHT - self.height) // 2
        self.surface = pg.Surface((self.width, self.height))
        self.items = [pg.Rect(self.surface.get_rect().x + 5 + (5 + cellW) * j, self.surface.get_rect().y + 5 + (5 + cellH) * i, cellW, cellH) for i in range(self.rows) for j in range(self.columns)]
        self.scrollbar = Scrollbar(self.width - 20, 0, 20, self.height)
    def handler(self):
        self.scrollbar.handler(self.x, self.y, self.height)
    def draw(self, surface):
        pos = pg.mouse.get_pos()
        self.surface.fill(gray_1)
        for i in range(len(self.items)):
            pg.draw.rect(self.surface, gray_2, self.items[i])
            if self.items[i].collidepoint(pos[0] - self.x, pos[1] - self.y): pg.draw.rect(self.surface, (0, 0, 0), self.items[i], 2)
            if self.content[i]: self.content[i].draw(self.surface, self.items[i].x + 3, self.items[i].y + 3)
        self.scrollbar.draw(self.surface)
        surface.blit(self.surface, (self.x, self.y))

class Inventory:
    active = False
    grid = Grid(ceil(len(blocks) / 5))
    for i in range(len(blocks)): grid.content[i] = blocks[i](0, 0)
    def handler(mouseClick, mouseButton, creature):
        if mouseButton == 1:
            for i in range(len(Inventory.grid.items)):
                if Inventory.grid.items[i].collidepoint(mouseClick[0] - Inventory.grid.x, mouseClick[1] - Inventory.grid.y) and Inventory.grid.content[i] != None:
                    creature.handItem = Inventory.grid.content[i].__class__
        Inventory.grid.handler()
    def renderer(surface):
        Inventory.grid.draw(surface)