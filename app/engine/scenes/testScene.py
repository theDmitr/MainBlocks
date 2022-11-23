import pygame as pg
from pygame.time import Clock
from engine.screen import Screen
from engine.generator.landscapeGenerator import Landscape
pg.init()
FPS = 60
clock = Clock()

CENTERX = Screen.getScreenRect().centerx
CENTERY = Screen.getScreenRect().centery

map = Landscape(20)

class testScene:
    def play(surface):
        testScene.eventListener()
        testScene.renderer(surface)
    def eventListener():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            elif event.type == pg.KEYDOWN:
                map.regenerate()
            for column in map.columns:
                for block in column.blocks:
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if block.getCollisionByPoint(event.pos): 
                            column.blocks.remove(block)
                    elif event.type == pg.MOUSEMOTION:
                        if block.getCollisionByPoint(event.pos): block.cursor = True
                        else: block.cursor = False
    def renderer(surface):
        clock.tick(FPS)
        surface.fill((255, 255, 255))
        for column in map.columns:
            for block in column.blocks: block.draw(surface)