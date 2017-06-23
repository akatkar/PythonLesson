from random import randint
from Point import Point

def createPoints(n):
    result = []
    for i in range(n):
        result.append(Point.createRandom())
    return result

#Create Points
points = createPoints(100);

#print the point list
for p in points:
    print(p)

# Get a new point
here = createPoints(1)[0]
print(here)

#find the nearest point
np = points[0]
for p in points:
    if here.distance(p) < here.distance(np):
        np = p

print("The nearest one to ", here, " is ", np)
