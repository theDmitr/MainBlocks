class Camera:
    xOffSet, yOffSet = 0, 0
    def __init__(self, obj):
        self.bindObject = obj
    def update(self):
        self.xOffSet, self.yOffSet = 0 - self.bindObject.x, 0 - self.bindObject.y