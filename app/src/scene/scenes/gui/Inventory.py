import pygame as pg
from src.screen.properties import WIDTH, HEIGHT
from src.objects.blocks.Block import Block, special_blocks

xOffSet, yOffSet = WIDTH // 4, WIDTH // 4
window = pg.Rect(xOffSet, yOffSet, WIDTH // 2, HEIGHT // 2)

items = []
_items = [block for block in Block.__subclasses__() if not block in special_blocks]
step = window.w // (Block.WIDTH + 10)
for i in range(0, len(_items), step): items.append(_items[i : i + step])
for i in range(len(items)):
    for j in range(len(items[i])):
        startX = (window.w - len(items[i]) * Block.WIDTH - len(items[i]) * 5) // 2
        items[i][j] = items[i][j](startX + xOffSet + 5 + Block.WIDTH * j + 5 * j, (Block.HEIGHT + 5) * i + yOffSet + 5)
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
                    for j in i:
                        if j.rect.collidepoint(event.pos):
                            Inventory.item = j.__class__
                if clear.collidepoint(event.pos):
                    Inventory.item = 1
    def draw(surface):
        pg.draw.rect(surface, (36, 30, 30), window)
        for i in items:
            for j in i: j.draw(surface, 0, 0)
        pg.draw.rect(surface, (200, 10, 10), clear)