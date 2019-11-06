from keras.models import *
from keras.layers import *
from keras import regularizers
#from tensorflow.python.keras.applications import ResNet50
import keras

class RegressionModel:

    def __init__(self):
        self.model = Sequential()


    def Create(self):
        
        #Simple Model
        
        '''
        #self.model.add(LocallyConnected2D(16, kernel_size=4, activation='relu', input_shape=(20, 20, 3)))
        #self.model.add(Dropout(0.5))
        #self.model.add(Conv2D(4, kernel_size=4, activation='relu', input_shape=(20, 20, 3)))
        #self.model.add(Flatten())
        #self.model.add(Dense(50, activation='tanh')) #, kernel_regularizer=keras.regularizers.l2(0.01)
        #self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Flatten())
        self.model.add(Dense(400, activation='relu'))
        self.model.add(Dense(500, activation='tanh'))
        self.model.add(Dropout(0.4))
        self.model.add(Dense(20, activation='sigmoid'))
        #self.model.add(Dense(10, activation='tanh'))
        self.model.add(Dense(1, activation='sigmoid'))'''

        '''#Complexe Model
        #self.model.add(SeparableConv2D(1, kernel_size=2, activation='relu', input_shape=(20, 20, 1),))
        self.model.add(Conv2D(1, kernel_size=12, padding='same', activation='relu', #input_shape=(20, 20, 1),
                              use_bias=True, bias_initializer='Zeros', bias_regularizer=keras.regularizers.l2(0.01)
                              ))
        #self.model.add(Dropout(0.1))
        #self.model.add(MaxPooling2D(pool_size=(10, 10)))
        #self.model.add(Conv2D(64, kernel_size=5, activation='tanh'))
        #self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Flatten())
        self.model.add(Dense(5, activation='sigmoid'))
        #self.model.add(Dropout(0.5))
        self.model.add(Dense(1, activation='sigmoid'))'''
        
        #ResNet
        for i in range(0, 10):
            self.model.add(Conv2D(4, kernel_size=2, padding='same', activation='relu',
                                kernel_regularizer=keras.regularizers.l2(0.0001)
                                ))
        self.model.add(BatchNormalization())
        self.model.add(Flatten())
        self.model.add(Dense(120, activation='relu'))
        self.model.add(BatchNormalization())
        self.model.add(Dense(90, activation='tanh'))
        self.model.add(BatchNormalization())
        self.model.add(Dense(1, activation='sigmoid'))


    def Train(self, set, optimizer, epochs, verbose = 0):
        #Compile
        if optimizer == 'sgd':
            self.model.compile(loss='mean_squared_error',
                  optimizer=keras.optimizers.SGD(learning_rate=0.01, momentum=0.7, nesterov=False),
                  metrics=['mae'])
        if optimizer == 'adam':
            self.model.compile(loss='mean_squared_error',
              optimizer='adam', #adadelta
              metrics=['mae'])
        data = set[0]
        #print(data.shape)
        labels = set[1]
        #print(labels.shape)
        history = self.model.fit(data, labels, batch_size=16, epochs=epochs, verbose=verbose)
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