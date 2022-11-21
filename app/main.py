from engine.scene import Scene
from engine.scenes.menu import Menu
from engine.screen import Screen
from engine.SETTINGS import WIDTH, HEIGHT, TITLE

Screen.setSceneControl(Scene)
Scene.setCurrentScene(Menu)

while True: Screen.playScene()