import pygame as pg
from src.screen.properties import WIDTH, HEIGHT
from src.objects.blocks.Block import Block, Block_grass, Block_dirt, Block_stone, Block_bedrock

xOffSet, yOffSet = WIDTH // 4, WIDTH // 4
window = pg.Rect(xOffSet, yOffSet, WIDTH // 2, HEIGHT // 2)
items = [Block_grass, Block_dirt, Block_stone, Block_bedrock]
startX = (window.w - len(items) * Block.WIDTH - len(items) * 5) // 2
for i in range(len(items)):
    items[i] = items[i](startX + xOffSet + 5 + Block.WIDTH * i + 5 * i, yOffSet + 5)
clear = pg.Rect(window.w + xOffSet - 5 - Block.WIDTH, window.h + yOffSet - 5 - Block.HEIGHT, Block.WIDTH, Block.HEIGHT)

class Inventory:
    active = False
    item = None
    def play(surface):
        Inventory.item = None
        Inventory.eventListener()
        Inventory.draw(surface)
        return Inventory.item
    def eventListener():
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT: quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_e or event.key == pg.K_ESCAPE: Inventory.active = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                for i in items:
                    if i.rect.collidepoint(event.pos):
                        Inventory.item = i.__class__
                if clear.collidepoint(event.pos):
                    Inventory.item = 1
    def draw(surface):
        pg.draw.rect(surface, (36, 30, 30), window)
        for i in items:
            i.draw(surface, 0, 0)
        pg.draw.rect(surface, (200, 10, 10), clear)