import numpy as np
# from p5 import *
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense

class ImageBird:
    def __init__(self):
        self.x = 25
        self.y = height / 2
        self.radius = 40

        self.velocity = 0
        self.gravity = 0.8
        self.lift = -12

        self.score = 0
        self.fitness = 0

        self.brain = self.createBrain()

    def show(self):
        no_stroke()
        fill(255)
        circle((self.x, self.y), self.radius)

    def update(self):
        self.velocity += self.gravity
        self.velocity *= 0.9
        self.y += self.velocity

    def up(self):
        self.velocity += self.lift

    def think(self, screen):
        pass

    def createBrain(self):
        model = Sequential()
        model.add(Conv2D(32, (3, 3), input_shape=(300, 450, 3)))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(32, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(64, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
        model.add(Dense(64))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        model.add(Dense(1))
        model.add(Activation('sigmoid'))

        # model.compile(loss='binary_crossentropy',
        #             optimizer='rmsprop',
        #             metrics=['accuracy'])

        return model