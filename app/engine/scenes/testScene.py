import pygame as pg
from pygame.time import Clock
from engine.objects.block import Block
pg.init()
FPS = 60
clock = Clock()
class testScene:
    block_1 = Block(50, 250, "grass")
    block_2 = Block(50, 290, "dirt")
    block_3 = Block(50, 330, "stone")
    def play(surface):
        testScene.eventListener()
        testScene.renderer(surface)
    def eventListener():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
    def renderer(surface):
        clock.tick(FPS)
        surface.fill((255, 255, 255))
        testScene.block_1.draw(surface)
        testScene.block_2.draw(surface)
        testScene.block_3.draw(surface)