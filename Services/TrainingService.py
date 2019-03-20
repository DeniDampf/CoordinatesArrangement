from keras.layers import Dense,Input
from keras.models import Sequential 

import numpy as np 

class TrainingService:
    def __init__(self,points,xDim,yDim):
        self.points = points 
        self.createCoordsModel()

        self.xDim = xDim
        self.yDim = yDim

        self.Eingangswerte = np.array([[0,0],[0,1],[1,0],[1,1]])
        self.Ausgangswerte = np.array([[0],[1],[1],[0]]) 

    def createModel(self):
        #pass
        model = Sequential()
        model.add(Dense(32, input_dim=2, activation='relu'))
        model.add(Dense(1, activation='sigmoid')) 


        model.compile(loss='mean_squared_error',optimizer='rmsprop',metrics=['accuracy']) 

        for i in range(10):

            model.fit(x=self.Eingangswerte,y=self.Ausgangswerte,epochs=150,verbose=0)

            print('- - - - - - - -  - - - - - -  - -- -  - - - -' + str(i))
            print(model.predict(self.Eingangswerte))

    def createCoordsModel(self):
        #pass
        self.coordsModel = Sequential()
        self.coordsModel.add(Dense(32, input_dim=2, activation='relu'))
        self.coordsModel.add(Dense(2, activation='sigmoid'))
        
        self.coordsModel.compile(loss='mean_squared_error',optimizer='rmsprop',metrics=['accuracy'])  

    def trainCoordsModel(self):
        #self.coordsModel.fit(x=self.Eingangswerte,y=self.Ausgangswerte,epochs=30,verbose=0)
        
        inputArray = np.zeros((len(self.points),2))
        outputArray = np.zeros((len(self.points),2))

       
        for idx in range(len(self.points)):
            tmpArray = np.zeros((2))
            tmpOArray = np.zeros((2))

            tmpArray[0] =self.points[idx].xNormalized
            tmpArray[1] =self.points[idx].yNormalized

            tmpOArray[0] =self.points[idx].xNormalized
            tmpOArray[1] =self.points[idx].yNormalized

            inputArray[idx] = tmpArray
            outputArray[idx] = tmpOArray

        #print('InputArray: ')
        #print(inputArray)           
            
        self.coordsModel.fit(x=inputArray,y=outputArray,epochs=5,verbose=0)

    


    def predictCoordsModel(self): 

        for coordinate in self.points:
            print(str(self.coordsModel.predict( np.array([[coordinate.xNormalized,coordinate.yNormalized]]))) + '  -  ' + str(coordinate.x) + ' / ' + str( coordinate.y))
