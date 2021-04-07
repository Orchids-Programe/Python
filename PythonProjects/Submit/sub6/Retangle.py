class Retangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
    def getArea(self):
        return self.height * self.width

r1 = Retangle(10,5)
r2 = Retangle(20,11)
print('r1.width = ', r1.width)
print('r1.height = ', r1.height)
print(r1.getWidth())
print(r1.getHeight())
print(r1.getArea())