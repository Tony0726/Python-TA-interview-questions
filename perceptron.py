## This is course material for Introduction to Modern Artificial Intelligence
## Class 10 Example code: perceptron.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

# Please make sure to conda install -c conda-forge keras
import keras
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt
from keras.activations import sigmoid

linearSeparableFlag = True
x_bias = 10

def toy_2D_samples(x_bias ,linearSeparableFlag):
    if linearSeparableFlag:

        samples1 = np.random.multivariate_normal([5+x_bias, 0], [[1, 0],[0, 1]], 100)
    
        labels1 = np.zeros(100)

        samples2 = np.random.multivariate_normal([-5+x_bias, 0], [[1, 0],[0, 1]], 100)
        labels2 = np.ones(100)

        samples = np.concatenate((samples1, samples2 ), axis =0)
        labels = np.concatenate((labels1, labels2 ), axis =0)
    
        # Plot the data
        plt.plot(samples1[:, 0], samples1[:, 1], 'bo')
        plt.plot(samples2[:, 0], samples2[:, 1], 'rx')
        plt.show()

    else:
        samples1 = np.random.multivariate_normal([5+x_bias, 5], [[1, 0],[0, 1]], 50)
        samples2 = np.random.multivariate_normal([-5+x_bias, -5], [[1, 0],[0, 1]], 50)
        samples3 = np.random.multivariate_normal([-5+x_bias, 5], [[1, 0],[0, 1]], 50)
        samples4 = np.random.multivariate_normal([5+x_bias, -5], [[1, 0],[0, 1]], 50)

        samples = np.concatenate((samples1, samples2, samples3, samples4 ), axis =0)

        labels1 = np.zeros(100)
        labels2 = np.ones(100)
        labels = np.concatenate((labels1, labels2 ), axis =0)
    
        # Plot the data
        plt.plot(samples1[:, 0], samples1[:, 1], 'bo')
        plt.plot(samples2[:, 0], samples2[:, 1], 'bo')
        plt.plot(samples3[:, 0], samples3[:, 1], 'rx')
        plt.plot(samples4[:, 0], samples4[:, 1], 'rx')
        plt.show()

    return samples, labels

samples, labels = toy_2D_samples(x_bias ,linearSeparableFlag)

# Split training and testing set

randomOrder = np.random.permutation(200)
trainingX = samples[randomOrder[0:100],:]
trainingY = labels[randomOrder[0:100]]
testingX = samples[randomOrder[100:200],:]
testingY = labels[randomOrder[100:200]]

model = Sequential()
model.add(Dense(1, input_shape=(2,), activation='sigmoid', use_bias=True))
model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['binary_accuracy'])
model.fit(trainingX, trainingY, epochs=100, batch_size=10, verbose=1, validation_split=0.2)
score = model.evaluate(testingX, testingY, verbose=0)

print('Test loss:', score[0])
print('Test accuracy:', score[1])