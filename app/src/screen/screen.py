import pygame as pg
from src.screen.properties import WIDTH, HEIGHT, TITLE

pg.init()

class Screen:
    pg.display.set_caption(TITLE)
    screen = pg.display.set_mode((WIDTH, HEIGHT), vsync = 1)
    scene = None
    def setScene(scene): 
        Screen.scene = scene
    def playScene(): 
        Screen.scene.play(surface = Screen.screen)