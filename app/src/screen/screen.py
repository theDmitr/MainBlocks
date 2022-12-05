import pygame as pg
from src.screen.properties import WIDTH, HEIGHT, TITLE

pg.init()

class Screen:
    pg.display.set_caption(TITLE)
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    sceneControl = None
    def setSceneControl(scene):
        Screen.sceneControl = scene
    def playScene():
        Screen.sceneControl.playCurrentScene(Screen.screen)
    def getScreenSize():
        return (Screen.screen.get_width(), Screen.screen.get_height())
    def getScreenRect():
        return Screen.screen.get_rect()