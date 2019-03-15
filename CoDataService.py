import models.coordinate as cModel


def getPoints(xDim,yDim):

    points = []
    for x in range(xDim):
        for y in range(yDim):
            c = cModel.Coordinate(x,y)
            points.append(c)

    return points
