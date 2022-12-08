import pygame as pg
from pygame.time import Clock
from src.screen.properties import WIDTH, HEIGHT
from src.objects.landscape.MapLoader import MapLoader
from src.objects.landscape.Landscape import Landscape
from src.objects.landscape.Column import Column
from src.objects.blocks.Block import *
pg.init()

FPS = 60
clock = Clock()
edges = (WIDTH // Block.WIDTH // 2, HEIGHT // Block.HEIGHT // 2)

landscape = MapLoader.getMapFromFile("new_map")

#landscape = Landscape(20)
#landscape.preGenerate(edges[0], edges[1])
#MapLoader.saveMapToFile("new_map", landscape)

class Game:
    def play(surface):
        Game.eventListener()
        Game.renderer(surface)
    
    def eventListener():
        for event in pg.event.get(): 
            if event.type == pg.QUIT: quit()
    def renderer(surface):
        clock.tick(FPS)
        surface.fill((0, 191, 255))
        
        for column in landscape.columns:
            for block in column.blocks[:]: 
                block.draw(surface, 0, 0)