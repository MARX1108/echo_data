from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
import os
import cv2 
import numpy as np
import matplotlib.pyplot as plt

IMG_SIZE_X = 656//2
IMG_SIZE_Y = 875//2

def load_data(micName, IMG_SIZE_X, IMG_SIZE_Y):
    this_path = os.getcwd()
    #print(this_path)

    filePath =  this_path + "/Fig/" + micName
    folderList = os.listdir(filePath)
    #print(fileList)
    

    images_array = np.empty((1082+974,IMG_SIZE_X,IMG_SIZE_Y,3), dtype=float, order='C')
    labels_array = np.empty((1082+974,1), dtype=float, order='C')
    labels_array[0:1081] = 4
    labels_array[1082:1082+974] = 5
    #print(images_array)
    #print(labels_array)
    i = 0

    for folder in folderList:
        folderPath = filePath + "/" + folder
        picList = os.listdir(folderPath)
        picList = [k for k in picList if '.jpg' in k]
        #print(picList)
        
        for pic in picList:
            temp_array = cv2.imread(folderPath+"/"+pic)
            #print(folderPath+"/"+pic);
            #print(i);
            #print(pic);
            #print(temp_array);
            #if (temp_array != None):
            if (check_array(temp_array)):
              temp_array = cv2.resize(temp_array, (IMG_SIZE_Y, IMG_SIZE_X))
              img_array = np.array(temp_array)
              images_array[i] = img_array
              i = i + 1

    return images_array[1:2056], labels_array[1:2056], images_array[0:2056:2], labels_array[0:2056:2]


def check_array(x):
    try:
        x.shape
        return True
    except:
        return False

x_train, y_train, x_test, y_test = load_data("mic0", IMG_SIZE_X, IMG_SIZE_Y)
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(IMG_SIZE_X, IMG_SIZE_Y, 3)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)


print("program finished")
