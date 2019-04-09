import models.coordinate as cModel
import random


def getPoints(xDim,yDim):

    points = []
    for x in range(xDim):
        for y in range(yDim):
            c = cModel.Coordinate(x,y,xDim,yDim)
            points.append(c)

    return points

def setSouthEastNeighbours(points):
    
    for i in range(len(points)):
        coordinate = points[i]
 
        neighbourSouth = findPoint(points,coordinate.x,coordinate.y -1)

        if neighbourSouth != None:
            coordinate.neighbours.append(neighbourSouth)

        neighbourEast = findPoint(points,coordinate.x+1,coordinate.y)

        if neighbourEast != None:
            coordinate.neighbours.append(neighbourEast)

def findPoint(points,x,y):
    
    for i in range(len(points)):
        coordinate = points[i]  
        if coordinate.x == x  and coordinate.y == y:
            return coordinate
    return None

def setRandomPredictionPoints(points,xDim,yDim):
    for i in range(len(points)):
        coordinate = points[i]
        coordinate.xPrediction = random.uniform(0,xDim-1)
        coordinate.yPrediction = random.uniform(0,yDim-1)







