from engine.scene.scene import Scene
from engine.scene.scenes.game import Game
from engine.screen import Screen

Screen.setSceneControl(Scene)
Scene.setCurrentScene(Game)

while True: 
    Screen.playScene()