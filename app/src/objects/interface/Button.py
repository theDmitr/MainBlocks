import pygame as pg
pg.init()
class Button:
    animation = False
    time = 0
    def __init__(self, x, y, w, h, c1, c2, txt, textFontSize):
        self.rect1 = pg.Rect(x, y, w, h)
        self.rect2 = pg.Rect(x + 5, y + 5, w, h)
        self.colorBg = c1
        self.colorText = c2
        self.text = txt
        self.textFontSize = textFontSize
    def animateIn(self):
        if self.rect2.x > self.rect1.x - 5 and pg.time.get_ticks() - self.time > 30:
            self.rect2.x -= 1
            self.textFontSize += 0.3
            self.colorText = self.colorText[0] - 5, self.colorText[1] - 5, self.colorText[2] - 5
            self.timer = pg.time.get_ticks()
    def animateOut(self):
        if self.rect2.x < self.rect1.x + 5 and pg.time.get_ticks() - self.time > 30:
            self.rect2.x += 1
            self.textFontSize -= 0.3
            self.colorText = self.colorText[0] + 5, self.colorText[1] + 5, self.colorText[2] + 5
            self.timer = pg.time.get_ticks()
    def animationUpdate(self):
        self.animateIn() if self.animation else self.animateOut()
    def draw(self, s):
        pg.draw.rect(s, self.colorBg, self.rect1)
        pg.draw.rect(s, self.colorBg, self.rect2, 2)
        label = pg.font.Font(None, int(self.textFontSize)).render(self.text, True, self.colorText)
        s.blit(label, label.get_rect(center = (self.rect1.centerx, self.rect1.centery)))
    def getCollision(self, pos):
        return self.rect1.collidepoint(pos)