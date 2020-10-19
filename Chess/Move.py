class Move():
    def __init__(self, x, y, length):
        self.length = length
        self.x = x
        self.y = y

    def getLength(self):
        return self.length

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setLength(self, l):
        self.length = l

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def __str__(self):
        return "x: {x} - y: {y} - length: {l}".format(x=self.x, y=self.y, l=self.length)
