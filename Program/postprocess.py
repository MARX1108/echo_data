from __future__ import absolute_import, division, print_function
import sys
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from cnn import load_data

IMG_SIZE_X = 437
IMG_SIZE_Y = 308

model = models.load_model("ep-1_bs-12.h5")
x_train, y_train, x_test, y_test = load_data("mic0", IMG_SIZE_X, IMG_SIZE_Y)
predictions = model.predict(x_test)
print(predictions)