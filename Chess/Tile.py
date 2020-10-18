class Tile:
    def __init__(self, color, xy):
        self.color = color
        self.x, self.y = xy

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setXy(self, xy):
        self.x, self.y = xy

    def getXy(self):
        return self.x, self.y
