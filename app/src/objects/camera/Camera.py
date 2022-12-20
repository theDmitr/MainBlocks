from src.screen.properties import WIDTH, HEIGHT

class Camera:
    xOffset, yOffset = 0, 0
    def __init__(self, obj):
        self.obj = obj
        self.xOffset, self.yOffset = obj.rect.centerx - WIDTH // 2, obj.rect.centery - HEIGHT // 2
    def update(self):
        self.xOffset += self.obj.moveX
        self.yOffset += self.obj.moveY