from pygame import display
class Scene:
    currentScene = None
    def setCurrentScene(scene): # setter current`s scene
        Scene.currentScene = scene
    def playCurrentScene(surface): # player current`s scene
        Scene.currentScene.play(surface) # call method `play` from current scene
        display.update() # update screen