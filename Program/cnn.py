from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
import os
import cv2 
import numpy as np

def load_data(micName):

    this_path = os.getcwd()
    #print(this_path)

    filePath =  this_path + "/Fig/" + micName;
    folderList = os.listdir(filePath)
    #print(fileList)
    

    images_array = np.empty((5,656,875,3))
    #print(images_array)

    for folder in folderList:
        folderPath = filePath + "/" + folder
        picList = os.listdir(folderPath);
        picList = [k for k in picList if '.jpg' in k];
        #print(picList)

        for pic in picList[0:2]:
            temp_array = cv2.imread(folderPath+"/"+pic)
            img_array = np.array(temp_array)
            #print(img_array)
            np.append(images_array, img_array)
            print(img_array.shape)
            #new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    
    


    return 0;



(x_train, y_train), (x_test, y_test) = load_data("mic0")
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)

load_data("mic0")
print("program finished")
