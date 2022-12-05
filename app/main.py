from src.scene.scene import Scene
from src.scene.scenes.Game import Game
from src.screen.screen import Screen

Screen.setSceneControl(Scene)
Scene.setCurrentScene(Game)

while True: 
    Screen.playScene()