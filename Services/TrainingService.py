from keras.layers import Dense,Input
from keras.models import Sequential 

import numpy as np 

class TrainingService:
    def __init__(self,points):
        self.points = points 

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