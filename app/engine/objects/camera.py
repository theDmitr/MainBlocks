from engine.SETTINGS import WIDTH, HEIGHT

class Camera:
    xOffset, yOffset = 0, 0
    speed = 3       
    def __init__(self, obj):
        self.obj = obj
        self.xOffset, self.yOffset = obj.centerx - WIDTH // 2, obj.centery - HEIGHT // 2