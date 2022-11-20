from pygame.time import Clock
from pygame import display
FPS = 60
clock = Clock()
class Scene:
    currentScene = None
    def setCurrentScene(scene): # setter current`s scene
        Scene.currentScene = scene
    def playCurrentScene(surface): # player current`s scene
        clock.tick(FPS) # tick frames per second
        Scene.currentScene.play(surface) # call method `play` from current scene
        display.update() # update screen