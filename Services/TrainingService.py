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

        #Compeliert das Model, damit es spaeter verwendet werden kann
        model.compile(loss='mean_squared_error',optimizer='adam',metrics=['accuracy']) 

        #Trainiert das Model mit den Eingangs- und den entsprechenden Ausgangswerten fuer 500 Epochen
        model.fit(x=self.Eingangswerte,y=self.Ausgangswerte,epochs=500,verbose=0)
        #Testet die Eingangsdaten und schreibt die Ergebnisse in die Console
        print(model.predict(self.Eingangswerte)) 