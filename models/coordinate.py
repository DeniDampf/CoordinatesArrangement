class Coordinate:
    def __init__(self,x,y,xDim,yDim):
        self.x = x
        self.y = y

        self.xDim = xDim
        self.yDim = yDim

        self.xNormalized = x / (xDim - 1)
        self.yNormalized = y / (yDim - 1)

        self.xPredNormalized = 0
        self.yPredNormalized = 0 

        self.xPredDenormalized = self.xPredNormalized * (xDim -1)
        self.yPredDenormalized = self.yPredNormalized * (yDim -1)

        self.neighbours = []

    def printCoordinate(self):
        print('-----COORDINATE------')
        print('Coordinate: ' + str(self.x)+' / ' + str(self.y)) 
        print('Normalized: ' + str(self.xNormalized) + ' / ' + str(self.yNormalized)) 
     
