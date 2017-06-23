from random import randint

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self, other):
        a = (self.x - other.x) ** 2
        b = (self.y - other.y) ** 2
        return (a + b) ** (1/2)

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    @staticmethod
    def createRandom():
        return Point(randint(1,100),randint(1,100))


a = Point(1,2)
b = Point(4,6)

print(a.distance(b))
