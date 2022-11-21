import pygame as pg
from pygame.time import Clock
from engine.objects.block import Block
from engine.screen import Screen
from engine.generator.landscapeGenerator import generateLandscape
pg.init()
FPS = 60
clock = Clock()
CENTERX = Screen.getScreenRect().centerx
CENTERY = Screen.getScreenRect().centery
class testScene:
    blocks = generateLandscape(Block.WIDTH, Block.HEIGHT, Screen.getScreenSize()[0] // Block.WIDTH + 1, startY = 100)
    def play(surface):
        testScene.eventListener()
        testScene.renderer(surface)
    def eventListener():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                testScene.blocks = generateLandscape(Block.WIDTH, Block.HEIGHT, Screen.getScreenSize()[0] // Block.WIDTH + 1, startY = 100)
    def renderer(surface):
        clock.tick(FPS)
        surface.fill((255, 255, 255))
        for i in testScene.blocks:
            i.draw(surface)