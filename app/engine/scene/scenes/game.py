import pygame as pg
from pygame.time import Clock
from engine.SETTINGS import WIDTH, HEIGHT
from engine.objects.landscape.landscape import Landscape
from engine.objects.camera import Camera
from engine.objects.player import Player
from engine.objects.blocks.block import Block, Block_bedrock
pg.init()

edges = (WIDTH // Block.WIDTH // 2, HEIGHT // Block.HEIGHT // 2)
FPS = 60
clock = Clock()

landscape = Landscape(100)
landscape.addColumn(0, offset = False)
for i in range(edges[0]):
    landscape.addColumn(landscape.columns[-1].y, right = False)
    landscape.addColumn(landscape.columns[-1].y, right = True)

player = Player(landscape.columns[edges[0]].x, landscape.columns[edges[0]].y - Player.HEIGHT)
camera = Camera(player.rect)

class Game:
    def play(surface):
        global leftHalf, rightHalf
        leftHalf = (player.rect.x - landscape.leftEdge) // Block.WIDTH - edges[0]
        rightHalf = (player.rect.right - landscape.leftEdge) // Block.WIDTH + edges[0] + 1

        Game.eventListener()
        Game.renderer(surface)
    
    def eventListener():
        events = pg.event.get()
        keys = pg.key.get_pressed()
        mouseClick, mouseMove = None, None

        for event in events:
            if event.type == pg.QUIT: quit()
            elif event.type == pg.MOUSEBUTTONDOWN: mouseClick = event.pos
            elif event.type == pg.MOUSEMOTION: mouseMove = event.pos

        if keys[pg.K_a]: player.moveX = -player.speed
        elif keys[pg.K_d]: player.moveX = player.speed
        else: player.moveX = 0

        if keys[pg.K_w]: player.moveY = -player.speed
        elif keys[pg.K_s]: player.moveY = player.speed
        else: player.moveY = 0
        
        for column in landscape.columns[leftHalf : rightHalf]:
            for block in column.blocks[0 : (player.rect.bottom - column.y) // Block.WIDTH + edges[1] + 1]:
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
                
                if mouseClick:
                    if block.cursor and block.rect.collidepoint((mouseClick[0] + camera.xOffset, mouseClick[1] + camera.yOffset)) and not isinstance(block, Block_bedrock): 
                        column.blocks.remove(block)
                        continue
                if mouseMove:
                    if block.rect.collidepoint((mouseMove[0] + camera.xOffset, mouseMove[1] + camera.yOffset)) and abs(block.rect.center[0] - player.rect.center[0]) < player.blockBreakLenght * Block.WIDTH and abs(block.rect.center[1] - player.rect.center[1]) < player.blockBreakLenght * Block.HEIGHT:
                        block.cursor = True
                    else: block.cursor = False
                        
        player.rect.x += player.moveX
        player.rect.y += player.moveY
        camera.xOffset += player.moveX
        camera.yOffset += player.moveY

        if player.rect.x - landscape.leftEdge < WIDTH // 2:
            landscape.addColumn(landscape.columns[-1].y, right = False)
        elif landscape.rightEdge - player.rect.right < WIDTH // 2:
            landscape.addColumn(landscape.columns[-1].y, right = True)

    def renderer(surface):
        clock.tick(FPS)
        surface.fill((0, 191, 255))

        leftHalf = (player.rect.x - landscape.leftEdge) // Block.WIDTH - edges[0]
        if leftHalf < 0: leftHalf = 0
        rightHalf = (player.rect.right - landscape.leftEdge) // Block.WIDTH + edges[0] + 1

        for column in landscape.columns[leftHalf : rightHalf]:
            for block in column.blocks[0 : (player.rect.bottom - column.y) // Block.WIDTH + edges[1] + 1]:
                block.draw(surface, -camera.xOffset, -camera.yOffset)
                if block.cursor: pg.draw.line(surface, Block.cursorColor, (player.rect.center[0] - camera.xOffset, player.rect.center[1] - camera.yOffset),(block.rect.center[0] - camera.xOffset, block.rect.center[1] - camera.yOffset), 1)
        
        player.draw(surface, -camera.xOffset, -camera.yOffset)