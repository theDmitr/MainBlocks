import pygame as pg
from pygame.time import Clock
from src.screen.properties import WIDTH, HEIGHT
from src.scene.scenes.gui.Inventory import Inventory
from src.objects.landscape.Landscape import Landscape
from src.objects.camera.Camera import Camera
from src.objects.entity.creature.Player import Player
from src.objects.blocks.Block import Block, Block_bedrock, Block_air
from src.objects.landscape.MapLoader import MapLoader
pg.init()

FPS = 60
clock = Clock()
edges = (WIDTH // Block.WIDTH // 2, HEIGHT // Block.HEIGHT // 2)

try:
    landscape = MapLoader.getMapFromFile("map")
except:
    landscape = Landscape(100)
    landscape.preGenerate(edges[0], edges[0])

player = Player(landscape.columns[edges[0]].x, landscape.columns[edges[0]].y - Player.HEIGHT)
camera = Camera(player.rect)

class Game:
    def play(surface):
        global leftHalf, rightHalf
        if not Inventory.active:
            leftHalf = (player.rect.x - landscape.leftEdge) // Block.WIDTH - edges[0]
            if leftHalf < 0: leftHalf = 0
            rightHalf = (player.rect.right - landscape.leftEdge) // Block.WIDTH + edges[0] + 1
            Game.eventListener()
        
        Game.renderer(surface)

        if Inventory.active: 
            invItm = Inventory.play(surface)
            if invItm: player.handItem = None if invItm == 1 else invItm
    
    def eventListener():
        events = pg.event.get()
        keys = pg.key.get_pressed()
        mouseClick, mouseButton = None, None

        for event in events:
            if event.type == pg.QUIT:
                MapLoader.saveMapToFile("map", landscape)
                quit()
            elif event.type == pg.MOUSEBUTTONDOWN: 
                mouseClick = event.pos
                mouseButton = event.button
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_e: Inventory.active = True
                elif event.key == pg.K_r: print(f"{landscape.yLower} {player.rect.y} {landscape.yHigher}")
        
        if keys[pg.K_a]: player.moveX = -player.speed
        elif keys[pg.K_d]: player.moveX = player.speed
        else: player.moveX = 0

        if keys[pg.K_w]: player.moveY = -player.speed
        elif keys[pg.K_s]: player.moveY = player.speed
        else: player.moveY = 0
        
        for indexColumn, column in enumerate(landscape.columns[leftHalf : rightHalf]):
            for indexBlock, block in enumerate(column.blocks[:]):
                if mouseClick:
                    if block.cursor:
                        if mouseButton == 1 and block.rect.collidepoint((mouseClick[0] + camera.xOffset, mouseClick[1] + camera.yOffset)) and not isinstance(block, Block_bedrock) and not isinstance(block, Block_air): 
                            column.blocks[indexBlock] = Block_air(block.rect.x, block.rect.y)
                            continue
                        if mouseButton == 3 and player.handItem and isinstance(block, Block_air) and block.rect.collidepoint((mouseClick[0] + camera.xOffset, mouseClick[1] + camera.yOffset)) and not block.rect.colliderect(player):
                            column.blocks[indexBlock] = player.handItem(block.rect.x, block.rect.y)
                
                if block.rect.collidepoint((pg.mouse.get_pos()[0] + camera.xOffset, pg.mouse.get_pos()[1] + camera.yOffset)): block.cursor = True
                else: block.cursor = False

                if isinstance(block, Block_air): continue

                if player.moveX != 0:
                    if player.moveX > 0: r = range(player.moveX, -1, -1)
                    else: r = range(player.moveX, 1)
                    for i in r:
                        if not block.rect.colliderect(pg.Rect(player.rect.x + i, player.rect.y, player.rect.w, player.rect.h)):
                            player.moveX = i
                            break
                if player.moveY != 0:
                    if player.moveY > 0: r = range(player.moveY, -1, -1)
                    else: r = range(player.moveY, 1)
                    for i in r:
                        if not block.rect.colliderect(pg.Rect(player.rect.x + player.moveX, player.rect.y + i, player.rect.w, player.rect.h)):
                            player.moveY = i
                            break
                        
        player.rect.x += player.moveX
        player.rect.y += player.moveY
        camera.xOffset += player.moveX
        camera.yOffset += player.moveY

        if player.rect.x - landscape.leftEdge < WIDTH // 2:
            landscape.addColumn(landscape.columns[0].y, right = False)
        elif landscape.rightEdge - player.rect.right < WIDTH // 2:
            landscape.addColumn(landscape.columns[-1].y, right = True)

    def renderer(surface):
        clock.tick(FPS)
        surface.fill((0, 191, 255))
        
        for column in landscape.columns[leftHalf : rightHalf]:
            for block in column.blocks[:]:
                block.draw(surface, -camera.xOffset, -camera.yOffset)
        player.draw(surface, -camera.xOffset, -camera.yOffset)