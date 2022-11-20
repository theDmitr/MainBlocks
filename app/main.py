from engine.scene import Scene
from engine.scenes.menu import Menu
from engine.screen import Screen

TITLE = "MineBlocks"
WIDTH = 400
HEIGHT = 400

Screen.createScreen(WIDTH, HEIGHT, TITLE, Scene)
Scene.setCurrentScene(Menu)

while True: Screen.playScene()