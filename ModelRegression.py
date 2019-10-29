from keras.models import *
from keras.layers import *
from keras import regularizers
import keras

class ModelRegression:

    def __init__(self):
        self.model = Sequential()


    def Create(self):
        #Model
        self.model.add(Conv2D(32, kernel_size=4, activation='relu', input_shape=(20, 20, 3)))
        self.model.add(Flatten())
        self.model.add(Dense(40, activation='tanh'))
        self.model.add(Dense(1, activation='sigmoid'))

        
    def Train(self, set, optimizer, epochs, verbose = 0):
        #Compile
        self.model.compile(loss='mean_squared_error',
              optimizer=optimizer,
              metrics=['mae'])
        data = set[0]
        #print(data.shape)
        labels = set[1]
        #print(labels.shape)
        history = self.model.fit(data, labels, epochs=epochs, verbose=verbose)
        return history
        
        #Train
        #self.model.train_on_batch(labels, datalabels, batch_size=1)


    def Evaluate(self, set) :
        #Evaluate
        data = set[0]
        labels = set[1]
        score = self.model.evaluate(data, labels, verbose=0, use_multiprocessing=False)
        return score


    def Predict(self, x):
        return self.model.predict(x)
