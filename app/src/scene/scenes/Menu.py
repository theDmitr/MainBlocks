import pygame as pg
from pygame.time import Clock
from src.screen.screen import Screen
from src.objects.interface.Button import Button
pg.init()

FPS = 60
clock = Clock()

CENTERX = Screen.getScreenRect().centerx
CENTERY = Screen.getScreenRect().centery

class Menu:
    button = Button(CENTERX - 150 // 2, CENTERY - 50 // 2, 150, 50, (0, 255, 0), (255, 255, 255), "Click me!", 24)
    def play(surface):
        Menu.eventListener()
        Menu.renderer(surface)
    def eventListener():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            elif event.type == pg.MOUSEMOTION:
                if Menu.button.getCollision(event.pos): Menu.button.animation = True
                else: Menu.button.animation = False
        Menu.button.animationUpdate()
    def renderer(surface):
        clock.tick(FPS)
        surface.fill((255, 255, 255))
        Menu.button.draw(surface)