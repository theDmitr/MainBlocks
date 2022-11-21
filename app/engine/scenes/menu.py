import pygame as pg
from pygame.time import Clock
from engine.objects.button import Button
from engine.screen import Screen
pg.init()
FPS = 60
clock = Clock()
class Menu:
    font = pg.font.Font(None, 24)
    button = Button(0, 0, 100, 40, (0, 255, 0), (255, 255, 255), "Click me!", font)
    def play(surface):
        WIDTH, HEIGHT = Screen.getScreenSize()
        Menu.eventListener()
        Menu.renderer(surface)
    def eventListener():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
    def renderer(surface):
        clock.tick(FPS)
        surface.fill((255, 255, 255))
        Menu.button.draw(surface)