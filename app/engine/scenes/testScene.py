import pygame as pg
from pygame.time import Clock
from engine.screen import Screen
from engine.generator.landscapeGenerator import Landscape
from engine.SETTINGS import WIDTH
pg.init()
FPS = 60
clock = Clock()

map = Landscape(20)

class Camera:
    moveTop, moveDown, moveRight, moveLeft = False, False, False, False
    speed = 2
    xOffSet, yOffSet = 0, 0

class testScene:
    def play(surface):
        testScene.eventListener()
        testScene.renderer(surface)
    def eventListener():
        keys = pg.key.get_pressed()
        if keys[pg.K_a]: Camera.moveLeft = True
        else: Camera.moveLeft = False
        if keys[pg.K_d]: Camera.moveRight = True
        else: Camera.moveRight = False
        if keys[pg.K_w]: Camera.moveTop = True
        else: Camera.moveTop = False
        if keys[pg.K_s]: Camera.moveDown = True
        else: Camera.moveDown = False
        if Camera.moveLeft and -Camera.xOffSet > map.xLimitLeft: Camera.xOffSet += Camera.speed
        elif Camera.moveRight and -Camera.xOffSet + WIDTH < map.xLimitRight: Camera.xOffSet -= Camera.speed
        if Camera.moveTop: Camera.yOffSet += Camera.speed
        elif Camera.moveDown: Camera.yOffSet -= Camera.speed

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            elif event.type == pg.KEYDOWN or event.type == pg.KEYUP:
                if keys[pg.K_r]: map.regenerate()

            for column in map.columns:
                for block in column.blocks:
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if block.getCollisionByPoint((event.pos[0] - Camera.xOffSet, event.pos[1] - Camera.yOffSet)): 
                            column.blocks.remove(block)
                            continue
                    try:
                        if block.getCollisionByPoint((event.pos[0] - Camera.xOffSet, event.pos[1] - Camera.yOffSet)): block.cursor = True
                        else: block.cursor = False
                    except: pass

    def renderer(surface):
        clock.tick(FPS)
        surface.fill((255, 255, 255))
        surface.blit(map.getSurface(), (Camera.xOffSet, Camera.yOffSet))