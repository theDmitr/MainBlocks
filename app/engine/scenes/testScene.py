import pygame as pg
from pygame.time import Clock
from engine.generator.landscapeGenerator import Landscape
from engine.objects.blocks.block import Block
from engine.objects.player import Player
from engine.camera import Camera
from engine.SETTINGS import WIDTH, HEIGHT

def getCollisionByTwoRects(r1, r2):
    if r1.right < r2.x or r1.x > r2.right: return False
    if r1.bottom < r2.y or r2.y > r1.bottom: return False
    return True

pg.init()
FPS = 60
clock = Clock()

map = Landscape(20)
player = Player(WIDTH // 2, map.columns[0].y - Player.HEIGHT)
camera = Camera(player.rect)

class testScene:
    def play(surface):
        testScene.eventListener()
        testScene.renderer(surface)
    def eventListener():
        keys = pg.key.get_pressed()
        if keys[pg.K_d]: player.moveX = 3
        elif keys[pg.K_a]: player.moveX = -3
        else: player.moveX = 0
        if keys[pg.K_w]: player.moveY = -3
        elif keys[pg.K_s]: player.moveY = 3
        else: player.moveY = 0

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit() 
            elif event.type == pg.KEYDOWN or event.type == pg.KEYUP:
                if keys[pg.K_r]: map.regenerate()

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
                        if not block.rect.colliderect(pg.Rect(player.rect.x, player.rect.y + i, player.rect.w, player.rect.h)):
                            player.moveY = i
                            break
                for event in pg.event.get():
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if block.rect.collidepoint(event.pos):
                            column.blocks.remove(block)
                            continue
                    elif event.type == pg.MOUSEMOTION:
                        block.cursor = True if block.rect.collidepoint(event.pos) else False

        player.rect.x += player.moveX
        player.rect.y += player.moveY

    def renderer(surface):
        clock.tick(FPS)
        surface.fill((255, 255, 255))
        surface.blit(map.getSurface(), (0, 0))
        player.draw(surface)