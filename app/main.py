from engine.scene import Scene
from engine.scenes.menu import Menu
from engine.scenes.testScene import testScene
from engine.screen import Screen

Screen.setSceneControl(Scene)
Scene.setCurrentScene(testScene)

while True: 
    Screen.playScene()