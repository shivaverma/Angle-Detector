import os
import json
import numpy as np
from matplotlib import pyplot as plt
from keras.models import Sequential, load_model
from keras.layers import Conv2D, Flatten, Dense, Activation, MaxPooling2D, Dropout, Input, BatchNormalization


def get_model():

    model = Sequential()

    model.add(Conv2D(50, kernel_size=5, padding='same', strides=2, activation='relu', input_shape=(128,128,3)))
    model.add(Dropout(0.3))

    model.add(Conv2D(100, padding='same', kernel_size=3, strides=1, activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=2))

    model.add(Conv2D(150, kernel_size=3, strides=2, activation='relu'))
    model.add(Dropout(0.3))

    model.add(Conv2D(200, kernel_size=3, strides=2, activation='relu'))
    model.add(Dropout(0.3))

    model.add(Conv2D(200, kernel_size=3, strides=2, activation='relu'))
    model.add(Dropout(0.3))

    model.add(Flatten())

    model.add(Dense(100, activation='relu'))
    model.add(Dropout(0.4))
    model.add(Dense(200, activation='relu'))
    model.add(Dropout(0.4))
    model.add(Dense(1, activation='linear'))

    return model