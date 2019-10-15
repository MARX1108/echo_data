from __future__ import absolute_import, division, print_function
import sys
import tensorflow as tf
import os
import cv2 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from PIL import Image
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

from cnn import load_data
IMG_SIZE_X = 437
IMG_SIZE_Y = 308

x, y = load_data("mic0", IMG_SIZE_X, IMG_SIZE_Y)
x_train = x[5:3000]
y_train = y[5:3000]
x_test = x[3000::]
y_test = y[3000::]


#print(x_train.shape)
#plt.imshow(x_train[0])
#print(y_train[8])

#y_train = tf.keras.utils.to_categorical(y_train)
#y_test = tf.keras.utils.to_categorical(y_test)


model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE_X, IMG_SIZE_Y, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.5));
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.5));
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(4, activation='softmax'))

model.compile(optimizer='adam',
              loss='mean_absolute_error',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=200,  batch_size=50)
model.evaluate(x_test, y_test, batch_size=36)
model.save("100.h5")
predictions = model.predict(x_test,verbose=1)
print(predictions)


