from keras.layers import Dense,Input,Dropout
from keras.models import Sequential 
from keras.initializers import RandomUniform

import numpy as np 

class TrainingService:
    def __init__(self,points,xDim,yDim):
        self.points = points 
        self.createCoordsModel()

        self.xDim = xDim
        self.yDim = yDim

    def createCoordsModel(self):
  
        self.coordsModel = Sequential()
        
        #First Layer
        # self.coordsModel.add(Dense(24, input_dim=2, activation='relu',kernel_initializer=RandomUniform(minval=-0.9, maxval=0.9, seed=None)))
        self.coordsModel.add(Dense(24, input_dim=2, activation='relu'))
        self.coordsModel.add(Dropout(0.2))

        #Second Layer
        # self.coordsModel.add(Dense(4, input_dim=2, activation='sigmoid',kernel_initializer=RandomUniform(minval=-0.9, maxval=0.9, seed=None)))
        # self.coordsModel.add(Dropout(0.4))
        
        self.coordsModel.add(Dense(2, activation='sigmoid'))

        self.coordsModel.compile(loss='mean_squared_error',optimizer='rmsprop',metrics=['accuracy'])  

        print(self.coordsModel.summary())

    def trainCoordsModel(self):

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
            
        self.coordsModel.fit(x=inputArray,y=outputArray,epochs=2,verbose=0)

    def predictCoordsModel(self): 

        for coordinate in self.points:
            prediction = self.coordsModel.predict( np.array([[coordinate.xNormalized,coordinate.yNormalized]]))
            
            coordinate.xPredNormalized = prediction[0,0]
            coordinate.yPredNormalized = prediction[0,1]
