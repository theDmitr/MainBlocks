import pygame as pg

pg.init()

class Screen:
    screen = None
    sceneControl = None
    def createScreen(w, h, t, s):
        pg.display.set_caption(t)
        Screen.screen = pg.display.set_mode((w, h))
        Screen.sceneControl = s
    def playScene():
        Screen.sceneControl.playCurrentScene(Screen.screen)
    def getScreenSize():
        return (Screen.screen.get_width(), Screen.screen.get_height())