import pygame as pg
from pygame.time import Clock
from engine.generator.landscape import Landscape
from engine.objects.player import Player
from engine.camera import Camera
from engine.SETTINGS import WIDTH, HEIGHT

pg.init()
FPS = 60
clock = Clock()

player = Player(WIDTH // 2, Player.HEIGHT)
camera = Camera(player.rect)
map = Landscape(player.rect)

class testScene:
    def play(surface):
        testScene.eventListener()
        testScene.renderer(surface)
    def eventListener():
        events = pg.event.get()
        keys = pg.key.get_pressed()
        if keys[pg.K_d]: player.moveX = 3
        elif keys[pg.K_a]: player.moveX = -3
        else: player.moveX = 0
        if keys[pg.K_w]: player.moveY = -3
        elif keys[pg.K_s]: player.moveY = 3
        else: player.moveY = 0

        for event in events:
            if event.type == pg.QUIT:
                quit() 
            elif event.type == pg.KEYDOWN or event.type == pg.KEYUP:
                if keys[pg.K_r]:
                    map.addColumnn()

        for column in map.columns:
            for block in column.blocks:
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
                for event in events:
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if block.rect.collidepoint((event.pos[0] - camera.xOffSet, event.pos[1] - camera.yOffSet)):
                            column.blocks.remove(block)
                            continue
                    elif event.type == pg.MOUSEMOTION:
                        block.cursor = True if block.rect.collidepoint((event.pos[0] - camera.xOffSet, event.pos[1] - camera.yOffSet)) else False

        player.rect.x += player.moveX
        camera.xOffSet += player.moveX
        player.rect.y += player.moveY
        camera.yOffSet += player.moveY
        camera.update()

    def renderer(surface):
        clock.tick(FPS)
        surface.fill((255, 255, 255))
        surface.blit(map.getSurface(), (camera.xOffSet, camera.yOffSet))
        player.draw(surface, camera.xOffSet, camera.yOffSet)