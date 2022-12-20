from src.screen.screen import Screen
from src.scenes.Game import Game

Screen.setScene(Game)

while True: 
    Screen.playScene()