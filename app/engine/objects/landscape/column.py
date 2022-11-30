class Column:
    def __init__(self, x, y, blocks):
        self.blocks = blocks
        self.x, self.y = blocks[0].rect.x, blocks[0].rect.y