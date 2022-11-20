import pygame as pg
pg.init()
class Button:
    def __init__(self, x, y, w, h, c1, c2, txt, f):
        self.rect1 = pg.Rect(x, y, w, h)
        self.rect2 = pg.Rect(x + 5, y + 5, w, h)
        self.colorBg = c1
        self.text = f.render(txt, True, c2)
        self.textRect = self.text.get_rect(center = (self.rect1.centerx, self.rect1.centery))
    def draw(self, s):
        pg.draw.rect(s, self.colorBg, self.rect1)
        pg.draw.rect(s, self.colorBg, self.rect2, 2)
        s.blit(self.text, self.textRect)